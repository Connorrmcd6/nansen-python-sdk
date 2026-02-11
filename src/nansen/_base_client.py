from __future__ import annotations

import time
from typing import Any, TypeVar

import anyio
import httpx
from pydantic import TypeAdapter

from nansen._constants import DEFAULT_BASE_URL, DEFAULT_MAX_RETRIES, DEFAULT_TIMEOUT
from nansen._exceptions import (
    APIConnectionError,
    APITimeoutError,
    _make_api_error,
)
from nansen._models import BaseModel
from nansen._pagination import AsyncPage, PaginationInfo, SyncPage
from nansen._response import APIResponse
from nansen._utils._retry import RETRYABLE_STATUS_CODES, calculate_retry_delay
from nansen._version import __version__

T = TypeVar("T", bound=BaseModel)


class _BaseClient:
    """Shared logic for both sync and async clients."""

    base_url: str
    api_key: str
    timeout: float
    max_retries: int

    def __init__(
        self,
        *,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
    ) -> None:
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries

    def _build_headers(self) -> dict[str, str]:
        return {
            "apikey": self.api_key,
            "content-type": "application/json",
            "user-agent": f"nansen-python/{__version__}",
        }

    def _build_url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    def _should_retry(self, response: httpx.Response) -> bool:
        return response.status_code in RETRYABLE_STATUS_CODES

    def _parse_response(
        self,
        response: httpx.Response,
        model: type[T],
    ) -> APIResponse[T]:
        body = response.json()
        data = TypeAdapter(model).validate_python(body)
        return APIResponse(data=data, http_response=response)

    def _parse_page_response(
        self,
        response: httpx.Response,
        model: type[T],
    ) -> tuple[list[T], PaginationInfo]:
        body = response.json()
        raw_data = body.get("data", [])
        items = TypeAdapter(list[model]).validate_python(raw_data)  # type: ignore[valid-type]
        raw_pagination = body.get("pagination", {})
        pagination = PaginationInfo.model_validate(raw_pagination)
        return items, pagination

    @staticmethod
    def _raise_for_response(response: httpx.Response) -> None:
        if response.is_success:
            return
        try:
            body = response.json()
        except Exception:
            body = None
        raise _make_api_error(response=response, body=body)


class SyncAPIClient(_BaseClient):
    """Synchronous HTTP client backed by ``httpx.Client``."""

    _client: httpx.Client

    def __init__(
        self,
        *,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        http_client: httpx.Client | None = None,
    ) -> None:
        super().__init__(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
        )
        self._client = http_client or httpx.Client(timeout=timeout)

    def __enter__(self) -> SyncAPIClient:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    def close(self) -> None:
        self._client.close()

    def _request(
        self,
        method: str,
        path: str,
        *,
        body: dict[str, object] | None = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        base_url: str | None = None,
    ) -> httpx.Response:
        url = f"{base_url or self.base_url}{path}"
        request_headers = self._build_headers()
        if headers:
            request_headers.update(headers)

        last_exc: Exception | None = None
        for attempt in range(self.max_retries + 1):
            try:
                response = self._client.request(
                    method,
                    url,
                    json=body,
                    params=params,
                    headers=request_headers,
                )
            except httpx.TimeoutException as exc:
                last_exc = APITimeoutError()
                if attempt >= self.max_retries:
                    raise last_exc from exc
                delay = calculate_retry_delay(attempt)
                time.sleep(delay)
                continue
            except httpx.ConnectError as exc:
                last_exc = APIConnectionError(message=str(exc))
                if attempt >= self.max_retries:
                    raise last_exc from exc
                delay = calculate_retry_delay(attempt)
                time.sleep(delay)
                continue

            if self._should_retry(response) and attempt < self.max_retries:
                delay = calculate_retry_delay(
                    attempt,
                    response.headers.get("retry-after"),
                )
                time.sleep(delay)
                continue

            self._raise_for_response(response)
            return response

        # Should not be reached, but satisfy type checker
        raise last_exc or APIConnectionError(message="Max retries exceeded")

    def _post(
        self,
        path: str,
        *,
        body: dict[str, object],
        model: type[T],
    ) -> APIResponse[T]:
        response = self._request("POST", path, body=body)
        return self._parse_response(response, model)

    def _get(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        model: type[T],
        headers: dict[str, str] | None = None,
        base_url: str | None = None,
    ) -> APIResponse[T]:
        response = self._request(
            "GET",
            path,
            params=params,
            headers=headers,
            base_url=base_url,
        )
        return self._parse_response(response, model)

    def _request_page(
        self,
        *,
        path: str,
        body: dict[str, object],
        model: type[T],
    ) -> SyncPage[T]:
        response = self._request("POST", path, body=body)
        items, pagination = self._parse_page_response(response, model)
        return SyncPage(
            data=items,
            pagination=pagination,
            client=self,
            path=path,
            body=body,
            model=model,
        )


class AsyncAPIClient(_BaseClient):
    """Asynchronous HTTP client backed by ``httpx.AsyncClient``."""

    _client: httpx.AsyncClient

    def __init__(
        self,
        *,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        super().__init__(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
        )
        self._client = http_client or httpx.AsyncClient(timeout=timeout)

    async def __aenter__(self) -> AsyncAPIClient:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()

    async def close(self) -> None:
        await self._client.aclose()

    async def _request(
        self,
        method: str,
        path: str,
        *,
        body: dict[str, object] | None = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        base_url: str | None = None,
    ) -> httpx.Response:
        url = f"{base_url or self.base_url}{path}"
        request_headers = self._build_headers()
        if headers:
            request_headers.update(headers)

        last_exc: Exception | None = None
        for attempt in range(self.max_retries + 1):
            try:
                response = await self._client.request(
                    method,
                    url,
                    json=body,
                    params=params,
                    headers=request_headers,
                )
            except httpx.TimeoutException as exc:
                last_exc = APITimeoutError()
                if attempt >= self.max_retries:
                    raise last_exc from exc
                delay = calculate_retry_delay(attempt)
                await anyio.sleep(delay)
                continue
            except httpx.ConnectError as exc:
                last_exc = APIConnectionError(message=str(exc))
                if attempt >= self.max_retries:
                    raise last_exc from exc
                delay = calculate_retry_delay(attempt)
                await anyio.sleep(delay)
                continue

            if self._should_retry(response) and attempt < self.max_retries:
                delay = calculate_retry_delay(
                    attempt,
                    response.headers.get("retry-after"),
                )
                await anyio.sleep(delay)
                continue

            self._raise_for_response(response)
            return response

        raise last_exc or APIConnectionError(message="Max retries exceeded")

    async def _post(
        self,
        path: str,
        *,
        body: dict[str, object],
        model: type[T],
    ) -> APIResponse[T]:
        response = await self._request("POST", path, body=body)
        return self._parse_response(response, model)

    async def _get(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        model: type[T],
        headers: dict[str, str] | None = None,
        base_url: str | None = None,
    ) -> APIResponse[T]:
        response = await self._request(
            "GET",
            path,
            params=params,
            headers=headers,
            base_url=base_url,
        )
        return self._parse_response(response, model)

    async def _request_page(
        self,
        *,
        path: str,
        body: dict[str, object],
        model: type[T],
    ) -> AsyncPage[T]:
        response = await self._request("POST", path, body=body)
        items, pagination = self._parse_page_response(response, model)
        return AsyncPage(
            data=items,
            pagination=pagination,
            client=self,
            path=path,
            body=body,
            model=model,
        )
