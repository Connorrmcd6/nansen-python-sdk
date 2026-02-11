from __future__ import annotations

from nansen._response import APIResponse
from nansen.resources._base import AsyncAPIResource, SyncAPIResource
from nansen.types.portfolio import DefiHoldingsResponse


class Portfolio(SyncAPIResource):
    def defi_holdings(
        self,
        *,
        wallet_address: str,
    ) -> APIResponse[DefiHoldingsResponse]:
        return self._post(
            "/portfolio/defi-holdings",
            body={"wallet_address": wallet_address},
            model=DefiHoldingsResponse,
        )


class AsyncPortfolio(AsyncAPIResource):
    async def defi_holdings(
        self,
        *,
        wallet_address: str,
    ) -> APIResponse[DefiHoldingsResponse]:
        return await self._post(
            "/portfolio/defi-holdings",
            body={"wallet_address": wallet_address},
            model=DefiHoldingsResponse,
        )
