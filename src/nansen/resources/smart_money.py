from __future__ import annotations

from typing import Any

from nansen._pagination import AsyncPage, SyncPage
from nansen._types import NOT_GIVEN, NotGiven
from nansen.resources._base import AsyncAPIResource, SyncAPIResource
from nansen.types.smart_money import (
    SmartMoneyDcaItem,
    SmartMoneyDexTradeItem,
    SmartMoneyHistoricalHoldingItem,
    SmartMoneyHoldingItem,
    SmartMoneyNetflowItem,
    SmartMoneyPerpTradeItem,
)


class SmartMoney(SyncAPIResource):
    """Smart Money resource for tracking labeled smart money wallets."""

    def netflow(
        self,
        *,
        chains: list[str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[SmartMoneyNetflowItem]:
        """Get smart money netflow data across chains.

        Args:
            chains: List of chain identifiers (e.g. ``["ethereum"]``).
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
        return self._post_page(
            "/smart-money/netflow",
            body={
                "chains": chains,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=SmartMoneyNetflowItem,
        )

    def dex_trades(
        self,
        *,
        chains: list[str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[SmartMoneyDexTradeItem]:
        """Get smart money DEX trades across chains.

        Args:
            chains: List of chain identifiers (e.g. ``["ethereum"]``).
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
        return self._post_page(
            "/smart-money/dex-trades",
            body={
                "chains": chains,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=SmartMoneyDexTradeItem,
        )

    def perp_trades(
        self,
        *,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        only_new_positions: bool | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[SmartMoneyPerpTradeItem]:
        """Get smart money perpetual futures trades.

        Args:
            filters: Field-level filters to narrow results.
            only_new_positions: If ``True``, only return trades that open new positions.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
        return self._post_page(
            "/smart-money/perp-trades",
            body={
                "filters": filters,
                "only_new_positions": only_new_positions,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=SmartMoneyPerpTradeItem,
        )

    def dcas(
        self,
        *,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[SmartMoneyDcaItem]:
        """Get smart money DCA orders.

        Args:
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
        return self._post_page(
            "/smart-money/dcas",
            body={
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=SmartMoneyDcaItem,
        )

    def holdings(
        self,
        *,
        chains: list[str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[SmartMoneyHoldingItem]:
        """Get current smart money holdings across chains.

        Args:
            chains: List of chain identifiers (e.g. ``["ethereum"]``).
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
        return self._post_page(
            "/smart-money/holdings",
            body={
                "chains": chains,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=SmartMoneyHoldingItem,
        )

    def historical_holdings(
        self,
        *,
        date_range: dict[str, str],
        chains: list[str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[SmartMoneyHistoricalHoldingItem]:
        """Get historical smart money holdings across chains.

        Args:
            date_range: Date range with ``"from"`` and ``"to"`` keys.
            chains: List of chain identifiers (e.g. ``["ethereum"]``).
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
        return self._post_page(
            "/smart-money/historical-holdings",
            body={
                "date_range": date_range,
                "chains": chains,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=SmartMoneyHistoricalHoldingItem,
        )


class AsyncSmartMoney(AsyncAPIResource):
    """Smart Money resource for tracking labeled smart money wallets (async)."""

    async def netflow(
        self,
        *,
        chains: list[str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[SmartMoneyNetflowItem]:
        """Get smart money netflow data across chains.

        Args:
            chains: List of chain identifiers (e.g. ``["ethereum"]``).
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
        return await self._post_page(
            "/smart-money/netflow",
            body={
                "chains": chains,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=SmartMoneyNetflowItem,
        )

    async def dex_trades(
        self,
        *,
        chains: list[str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[SmartMoneyDexTradeItem]:
        """Get smart money DEX trades across chains.

        Args:
            chains: List of chain identifiers (e.g. ``["ethereum"]``).
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
        return await self._post_page(
            "/smart-money/dex-trades",
            body={
                "chains": chains,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=SmartMoneyDexTradeItem,
        )

    async def perp_trades(
        self,
        *,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        only_new_positions: bool | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[SmartMoneyPerpTradeItem]:
        """Get smart money perpetual futures trades.

        Args:
            filters: Field-level filters to narrow results.
            only_new_positions: If ``True``, only return trades that open new positions.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
        return await self._post_page(
            "/smart-money/perp-trades",
            body={
                "filters": filters,
                "only_new_positions": only_new_positions,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=SmartMoneyPerpTradeItem,
        )

    async def dcas(
        self,
        *,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[SmartMoneyDcaItem]:
        """Get smart money DCA orders.

        Args:
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
        return await self._post_page(
            "/smart-money/dcas",
            body={
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=SmartMoneyDcaItem,
        )

    async def holdings(
        self,
        *,
        chains: list[str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[SmartMoneyHoldingItem]:
        """Get current smart money holdings across chains.

        Args:
            chains: List of chain identifiers (e.g. ``["ethereum"]``).
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
        return await self._post_page(
            "/smart-money/holdings",
            body={
                "chains": chains,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=SmartMoneyHoldingItem,
        )

    async def historical_holdings(
        self,
        *,
        date_range: dict[str, str],
        chains: list[str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[SmartMoneyHistoricalHoldingItem]:
        """Get historical smart money holdings across chains.

        Args:
            date_range: Date range with ``"from"`` and ``"to"`` keys.
            chains: List of chain identifiers (e.g. ``["ethereum"]``).
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
        return await self._post_page(
            "/smart-money/historical-holdings",
            body={
                "date_range": date_range,
                "chains": chains,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=SmartMoneyHistoricalHoldingItem,
        )
