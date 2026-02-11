from __future__ import annotations

from typing import Any

from nansen._pagination import AsyncPage, SyncPage
from nansen._response import APIResponse
from nansen._types import NOT_GIVEN, NotGiven
from nansen.resources._base import AsyncAPIResource, SyncAPIResource
from nansen.types.tgm import (
    FlowIntelItem,
    FlowItem,
    HolderItem,
    PerpPnlLeaderboardItem,
    PerpScreenerItem,
    PnlLeaderboardItem,
    TgmDcaItem,
    TgmDexTradeItem,
    TgmPerpPositionItem,
    TgmPerpTradeItem,
    TokenInformationResponse,
    TokenScreenerItem,
    TransferItem,
    WhoBoughtSoldItem,
)


class TGM(SyncAPIResource):
    def token_screener(
        self,
        *,
        chains: list[str],
        timeframe: str | NotGiven = NOT_GIVEN,
        date: dict[str, str] | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[TokenScreenerItem]:
        return self._post_page(
            "/token-screener",
            body={
                "chains": chains,
                "timeframe": timeframe,
                "date": date,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=TokenScreenerItem,
        )

    def token_information(
        self,
        *,
        chain: str,
        token_address: str,
        timeframe: str,
    ) -> APIResponse[TokenInformationResponse]:
        return self._post(
            "/tgm/token-information",
            body={
                "chain": chain,
                "token_address": token_address,
                "timeframe": timeframe,
            },
            model=TokenInformationResponse,
        )

    def flow_intel(
        self,
        *,
        chain: str,
        token_address: str,
        timeframe: str | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[FlowIntelItem]:
        return self._post_page(
            "/tgm/flow-intelligence",
            body={
                "chain": chain,
                "token_address": token_address,
                "timeframe": timeframe,
                "filters": filters,
            },
            model=FlowIntelItem,
        )

    def holders(
        self,
        *,
        chain: str,
        token_address: str,
        label_type: str | NotGiven = NOT_GIVEN,
        aggregate_by_entity: bool | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[HolderItem]:
        return self._post_page(
            "/tgm/holders",
            body={
                "chain": chain,
                "token_address": token_address,
                "label_type": label_type,
                "aggregate_by_entity": aggregate_by_entity,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=HolderItem,
        )

    def flows(
        self,
        *,
        chain: str,
        token_address: str,
        date: dict[str, str],
        label: str | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[FlowItem]:
        return self._post_page(
            "/tgm/flows",
            body={
                "chain": chain,
                "token_address": token_address,
                "date": date,
                "label": label,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=FlowItem,
        )

    def who_bought_sold(
        self,
        *,
        chain: str,
        token_address: str,
        date: dict[str, str],
        buy_or_sell: str | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[WhoBoughtSoldItem]:
        return self._post_page(
            "/tgm/who-bought-sold",
            body={
                "chain": chain,
                "token_address": token_address,
                "date": date,
                "buy_or_sell": buy_or_sell,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=WhoBoughtSoldItem,
        )

    def dex_trades(
        self,
        *,
        chain: str,
        token_address: str,
        date: dict[str, str],
        only_smart_money: bool | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[TgmDexTradeItem]:
        return self._post_page(
            "/tgm/dex-trades",
            body={
                "chain": chain,
                "token_address": token_address,
                "date": date,
                "only_smart_money": only_smart_money,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=TgmDexTradeItem,
        )

    def transfers(
        self,
        *,
        chain: str,
        token_address: str,
        date: dict[str, str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[TransferItem]:
        return self._post_page(
            "/tgm/transfers",
            body={
                "chain": chain,
                "token_address": token_address,
                "date": date,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=TransferItem,
        )

    def dcas(
        self,
        *,
        token_address: str,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[TgmDcaItem]:
        return self._post_page(
            "/tgm/jup-dca",
            body={
                "token_address": token_address,
                "filters": filters,
                "pagination": pagination,
            },
            model=TgmDcaItem,
        )

    def pnl_leaderboard(
        self,
        *,
        chain: str,
        token_address: str,
        date: dict[str, str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[PnlLeaderboardItem]:
        return self._post_page(
            "/tgm/pnl-leaderboard",
            body={
                "chain": chain,
                "token_address": token_address,
                "date": date,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=PnlLeaderboardItem,
        )

    def perp_screener(
        self,
        *,
        date: dict[str, str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[PerpScreenerItem]:
        return self._post_page(
            "/perp-screener",
            body={
                "date": date,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=PerpScreenerItem,
        )

    def perp_pnl_leaderboard(
        self,
        *,
        token_symbol: str,
        date: dict[str, str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[PerpPnlLeaderboardItem]:
        return self._post_page(
            "/tgm/perp-pnl-leaderboard",
            body={
                "token_symbol": token_symbol,
                "date": date,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=PerpPnlLeaderboardItem,
        )

    def perp_positions(
        self,
        *,
        token_symbol: str,
        label_type: str | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[TgmPerpPositionItem]:
        return self._post_page(
            "/tgm/perp-positions",
            body={
                "token_symbol": token_symbol,
                "label_type": label_type,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=TgmPerpPositionItem,
        )

    def perp_trades(
        self,
        *,
        token_symbol: str,
        date: dict[str, str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[TgmPerpTradeItem]:
        return self._post_page(
            "/tgm/perp-trades",
            body={
                "token_symbol": token_symbol,
                "date": date,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=TgmPerpTradeItem,
        )


class AsyncTGM(AsyncAPIResource):
    async def token_screener(
        self,
        *,
        chains: list[str],
        timeframe: str | NotGiven = NOT_GIVEN,
        date: dict[str, str] | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[TokenScreenerItem]:
        return await self._post_page(
            "/token-screener",
            body={
                "chains": chains,
                "timeframe": timeframe,
                "date": date,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=TokenScreenerItem,
        )

    async def token_information(
        self,
        *,
        chain: str,
        token_address: str,
        timeframe: str,
    ) -> APIResponse[TokenInformationResponse]:
        return await self._post(
            "/tgm/token-information",
            body={
                "chain": chain,
                "token_address": token_address,
                "timeframe": timeframe,
            },
            model=TokenInformationResponse,
        )

    async def flow_intel(
        self,
        *,
        chain: str,
        token_address: str,
        timeframe: str | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[FlowIntelItem]:
        return await self._post_page(
            "/tgm/flow-intelligence",
            body={
                "chain": chain,
                "token_address": token_address,
                "timeframe": timeframe,
                "filters": filters,
            },
            model=FlowIntelItem,
        )

    async def holders(
        self,
        *,
        chain: str,
        token_address: str,
        label_type: str | NotGiven = NOT_GIVEN,
        aggregate_by_entity: bool | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[HolderItem]:
        return await self._post_page(
            "/tgm/holders",
            body={
                "chain": chain,
                "token_address": token_address,
                "label_type": label_type,
                "aggregate_by_entity": aggregate_by_entity,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=HolderItem,
        )

    async def flows(
        self,
        *,
        chain: str,
        token_address: str,
        date: dict[str, str],
        label: str | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[FlowItem]:
        return await self._post_page(
            "/tgm/flows",
            body={
                "chain": chain,
                "token_address": token_address,
                "date": date,
                "label": label,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=FlowItem,
        )

    async def who_bought_sold(
        self,
        *,
        chain: str,
        token_address: str,
        date: dict[str, str],
        buy_or_sell: str | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[WhoBoughtSoldItem]:
        return await self._post_page(
            "/tgm/who-bought-sold",
            body={
                "chain": chain,
                "token_address": token_address,
                "date": date,
                "buy_or_sell": buy_or_sell,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=WhoBoughtSoldItem,
        )

    async def dex_trades(
        self,
        *,
        chain: str,
        token_address: str,
        date: dict[str, str],
        only_smart_money: bool | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[TgmDexTradeItem]:
        return await self._post_page(
            "/tgm/dex-trades",
            body={
                "chain": chain,
                "token_address": token_address,
                "date": date,
                "only_smart_money": only_smart_money,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=TgmDexTradeItem,
        )

    async def transfers(
        self,
        *,
        chain: str,
        token_address: str,
        date: dict[str, str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[TransferItem]:
        return await self._post_page(
            "/tgm/transfers",
            body={
                "chain": chain,
                "token_address": token_address,
                "date": date,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=TransferItem,
        )

    async def dcas(
        self,
        *,
        token_address: str,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[TgmDcaItem]:
        return await self._post_page(
            "/tgm/jup-dca",
            body={
                "token_address": token_address,
                "filters": filters,
                "pagination": pagination,
            },
            model=TgmDcaItem,
        )

    async def pnl_leaderboard(
        self,
        *,
        chain: str,
        token_address: str,
        date: dict[str, str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[PnlLeaderboardItem]:
        return await self._post_page(
            "/tgm/pnl-leaderboard",
            body={
                "chain": chain,
                "token_address": token_address,
                "date": date,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=PnlLeaderboardItem,
        )

    async def perp_screener(
        self,
        *,
        date: dict[str, str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[PerpScreenerItem]:
        return await self._post_page(
            "/perp-screener",
            body={
                "date": date,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=PerpScreenerItem,
        )

    async def perp_pnl_leaderboard(
        self,
        *,
        token_symbol: str,
        date: dict[str, str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[PerpPnlLeaderboardItem]:
        return await self._post_page(
            "/tgm/perp-pnl-leaderboard",
            body={
                "token_symbol": token_symbol,
                "date": date,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=PerpPnlLeaderboardItem,
        )

    async def perp_positions(
        self,
        *,
        token_symbol: str,
        label_type: str | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[TgmPerpPositionItem]:
        return await self._post_page(
            "/tgm/perp-positions",
            body={
                "token_symbol": token_symbol,
                "label_type": label_type,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=TgmPerpPositionItem,
        )

    async def perp_trades(
        self,
        *,
        token_symbol: str,
        date: dict[str, str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[TgmPerpTradeItem]:
        return await self._post_page(
            "/tgm/perp-trades",
            body={
                "token_symbol": token_symbol,
                "date": date,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=TgmPerpTradeItem,
        )
