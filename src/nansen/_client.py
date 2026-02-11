from __future__ import annotations

import os
from functools import cached_property

import httpx

from nansen._base_client import AsyncAPIClient, SyncAPIClient
from nansen._constants import (
    API_KEY_ENV_VAR,
    DEFAULT_BASE_URL,
    DEFAULT_MAX_RETRIES,
    DEFAULT_TIMEOUT,
)
from nansen.resources.points import AsyncPoints, Points
from nansen.resources.portfolio import AsyncPortfolio, Portfolio
from nansen.resources.profiler.profiler import AsyncProfiler, Profiler
from nansen.resources.smart_money import AsyncSmartMoney, SmartMoney
from nansen.resources.tgm import TGM, AsyncTGM


class Nansen(SyncAPIClient):
    """Synchronous Nansen API client.

    Usage::

        client = Nansen(api_key="nansen-...")
        page = client.smart_money.holdings(chains=["ethereum"])
        for item in page:
            print(item.token_symbol, item.value_usd)
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        http_client: httpx.Client | None = None,
    ) -> None:
        resolved_key = api_key or os.environ.get(API_KEY_ENV_VAR)
        if not resolved_key:
            raise ValueError(
                f"API key must be provided via the api_key parameter "
                f"or the {API_KEY_ENV_VAR} environment variable."
            )
        super().__init__(
            api_key=resolved_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            http_client=http_client,
        )

    @cached_property
    def smart_money(self) -> SmartMoney:
        return SmartMoney(self)

    @cached_property
    def profiler(self) -> Profiler:
        return Profiler(self)

    @cached_property
    def tgm(self) -> TGM:
        return TGM(self)

    @cached_property
    def portfolio(self) -> Portfolio:
        return Portfolio(self)

    @cached_property
    def points(self) -> Points:
        return Points(self)


class AsyncNansen(AsyncAPIClient):
    """Asynchronous Nansen API client.

    Usage::

        async with AsyncNansen(api_key="nansen-...") as client:
            page = await client.smart_money.holdings(chains=["ethereum"])
            async for item in page:
                print(item.token_symbol, item.value_usd)
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        resolved_key = api_key or os.environ.get(API_KEY_ENV_VAR)
        if not resolved_key:
            raise ValueError(
                f"API key must be provided via the api_key parameter "
                f"or the {API_KEY_ENV_VAR} environment variable."
            )
        super().__init__(
            api_key=resolved_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            http_client=http_client,
        )

    @cached_property
    def smart_money(self) -> AsyncSmartMoney:
        return AsyncSmartMoney(self)

    @cached_property
    def profiler(self) -> AsyncProfiler:
        return AsyncProfiler(self)

    @cached_property
    def tgm(self) -> AsyncTGM:
        return AsyncTGM(self)

    @cached_property
    def portfolio(self) -> AsyncPortfolio:
        return AsyncPortfolio(self)

    @cached_property
    def points(self) -> AsyncPoints:
        return AsyncPoints(self)
