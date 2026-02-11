from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

import httpx

T = TypeVar("T")


@dataclass(frozen=True)
class RateLimitInfo:
    """Parsed rate-limit information from response headers."""

    credits_used: int | None = None
    credits_remaining: int | None = None
    limit: int | None = None
    remaining: int | None = None
    reset: float | None = None
    limit_second: int | None = None
    remaining_second: int | None = None
    limit_minute: int | None = None
    remaining_minute: int | None = None

    @classmethod
    def from_headers(cls, headers: httpx.Headers) -> RateLimitInfo:
        def _int(key: str) -> int | None:
            val = headers.get(key)
            if val is None:
                return None
            try:
                return int(val)
            except (ValueError, TypeError):
                return None

        def _float(key: str) -> float | None:
            val = headers.get(key)
            if val is None:
                return None
            try:
                return float(val)
            except (ValueError, TypeError):
                return None

        return cls(
            credits_used=_int("x-nansen-credits-used"),
            credits_remaining=_int("x-nansen-credits-remaining"),
            limit=_int("ratelimit-limit"),
            remaining=_int("ratelimit-remaining"),
            reset=_float("ratelimit-reset"),
            limit_second=_int("x-ratelimit-limit-second"),
            remaining_second=_int("x-ratelimit-remaining-second"),
            limit_minute=_int("x-ratelimit-limit-minute"),
            remaining_minute=_int("x-ratelimit-remaining-minute"),
        )


class APIResponse(Generic[T]):
    """Wrapper around an API response that exposes parsed data and metadata."""

    _data: T
    http_response: httpx.Response

    def __init__(self, *, data: T, http_response: httpx.Response) -> None:
        self._data = data
        self.http_response = http_response

    @property
    def data(self) -> T:
        return self._data

    @property
    def headers(self) -> httpx.Headers:
        return self.http_response.headers

    @property
    def status_code(self) -> int:
        return self.http_response.status_code

    @property
    def rate_limit(self) -> RateLimitInfo:
        return RateLimitInfo.from_headers(self.http_response.headers)
