from __future__ import annotations

from typing import Any

import httpx


class NansenError(Exception):
    """Base exception for all Nansen SDK errors."""


class APIError(NansenError):
    """Error returned by the Nansen API."""

    status_code: int
    message: str
    response: httpx.Response
    body: Any

    def __init__(
        self,
        message: str,
        *,
        response: httpx.Response,
        body: Any,
    ) -> None:
        self.status_code = response.status_code
        self.message = message
        self.response = response
        self.body = body
        super().__init__(f"{response.status_code} {message}")


class BadRequestError(APIError):
    """400 Bad Request."""

    status_code: int = 400


class AuthenticationError(APIError):
    """401 Unauthorized."""

    status_code: int = 401


class PermissionDeniedError(APIError):
    """403 Forbidden."""

    status_code: int = 403


class NotFoundError(APIError):
    """404 Not Found."""

    status_code: int = 404


class UnprocessableEntityError(APIError):
    """422 Unprocessable Entity."""

    status_code: int = 422


class RateLimitError(APIError):
    """429 Too Many Requests."""

    status_code: int = 429
    retry_after: float | None

    def __init__(
        self,
        message: str,
        *,
        response: httpx.Response,
        body: Any,
    ) -> None:
        super().__init__(message, response=response, body=body)
        retry_after_raw = response.headers.get("retry-after")
        self.retry_after = float(retry_after_raw) if retry_after_raw else None


class InternalServerError(APIError):
    """500 Internal Server Error."""

    status_code: int = 500


class GatewayTimeoutError(APIError):
    """504 Gateway Timeout."""

    status_code: int = 504


class APIConnectionError(NansenError):
    """Raised when the SDK cannot connect to the API."""

    def __init__(self, *, message: str = "Connection error.") -> None:
        self.message = message
        super().__init__(message)


class APITimeoutError(APIConnectionError):
    """Raised when a request times out."""

    def __init__(self, *, message: str = "Request timed out.") -> None:
        super().__init__(message=message)


_STATUS_CODE_TO_EXCEPTION: dict[int, type[APIError]] = {
    400: BadRequestError,
    401: AuthenticationError,
    403: PermissionDeniedError,
    404: NotFoundError,
    422: UnprocessableEntityError,
    429: RateLimitError,
    500: InternalServerError,
    504: GatewayTimeoutError,
}


def _make_api_error(*, response: httpx.Response, body: Any) -> APIError:
    """Create the appropriate APIError subclass for a given response."""
    message = ""
    if isinstance(body, dict):
        error = body.get("error")
        if isinstance(error, dict):
            message = error.get("message", "")
        elif "detail" in body:
            message = str(body["detail"])
    if not message:
        message = response.reason_phrase or "Unknown error"

    exc_class = _STATUS_CODE_TO_EXCEPTION.get(response.status_code, APIError)
    return exc_class(message, response=response, body=body)
