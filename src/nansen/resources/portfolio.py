from __future__ import annotations

from nansen._response import APIResponse
from nansen.resources._base import AsyncAPIResource, SyncAPIResource
from nansen.types.portfolio import DefiHoldingsResponse


class Portfolio(SyncAPIResource):
    """Portfolio resource for wallet-level analytics."""

    def defi_holdings(
        self,
        *,
        wallet_address: str,
    ) -> APIResponse[DefiHoldingsResponse]:
        """Get DeFi holdings for a wallet address.

        Args:
            wallet_address: The wallet address to look up.
        """
        return self._post(
            "/portfolio/defi-holdings",
            body={"wallet_address": wallet_address},
            model=DefiHoldingsResponse,
        )


class AsyncPortfolio(AsyncAPIResource):
    """Portfolio resource for wallet-level analytics (async)."""

    async def defi_holdings(
        self,
        *,
        wallet_address: str,
    ) -> APIResponse[DefiHoldingsResponse]:
        """Get DeFi holdings for a wallet address.

        Args:
            wallet_address: The wallet address to look up.
        """
        return await self._post(
            "/portfolio/defi-holdings",
            body={"wallet_address": wallet_address},
            model=DefiHoldingsResponse,
        )
