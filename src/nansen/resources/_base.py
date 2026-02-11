from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeVar

from nansen._models import BaseModel
from nansen._pagination import AsyncPage, SyncPage
from nansen._response import APIResponse
from nansen._types import _NotGiven

if TYPE_CHECKING:
    from nansen._base_client import AsyncAPIClient, SyncAPIClient

T = TypeVar("T", bound=BaseModel)


def _strip_not_given(body: dict[str, Any]) -> dict[str, Any]:
    """Remove keys whose values are NOT_GIVEN from a dict."""
    return {k: v for k, v in body.items() if not isinstance(v, _NotGiven)}


class SyncAPIResource:
    _client: SyncAPIClient

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def _post(
        self,
        path: str,
        *,
        body: dict[str, Any],
        model: type[T],
    ) -> APIResponse[T]:
        return self._client._post(path, body=_strip_not_given(body), model=model)

    def _post_page(
        self,
        path: str,
        *,
        body: dict[str, Any],
        model: type[T],
    ) -> SyncPage[T]:
        return self._client._request_page(
            path=path,
            body=_strip_not_given(body),
            model=model,
        )

    def _get(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        model: type[T],
        headers: dict[str, str] | None = None,
        base_url: str | None = None,
    ) -> APIResponse[T]:
        cleaned = _strip_not_given(params) if params else params
        return self._client._get(
            path,
            params=cleaned,
            model=model,
            headers=headers,
            base_url=base_url,
        )


class AsyncAPIResource:
    _client: AsyncAPIClient

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def _post(
        self,
        path: str,
        *,
        body: dict[str, Any],
        model: type[T],
    ) -> APIResponse[T]:
        return await self._client._post(path, body=_strip_not_given(body), model=model)

    async def _post_page(
        self,
        path: str,
        *,
        body: dict[str, Any],
        model: type[T],
    ) -> AsyncPage[T]:
        return await self._client._request_page(
            path=path,
            body=_strip_not_given(body),
            model=model,
        )

    async def _get(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        model: type[T],
        headers: dict[str, str] | None = None,
        base_url: str | None = None,
    ) -> APIResponse[T]:
        cleaned = _strip_not_given(params) if params else params
        return await self._client._get(
            path,
            params=cleaned,
            model=model,
            headers=headers,
            base_url=base_url,
        )
