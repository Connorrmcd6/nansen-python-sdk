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
    def netflow(
        self,
        *,
        chains: list[str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[SmartMoneyNetflowItem]:
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
    async def netflow(
        self,
        *,
        chains: list[str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[SmartMoneyNetflowItem]:
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
