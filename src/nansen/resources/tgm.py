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
    """Token God Mode resource for token-level analytics."""

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
        """Screen tokens across one or more chains.

        Args:
            chains: List of chain identifiers to screen (e.g. ``["ethereum"]``).
            timeframe: Timeframe for the screener data (e.g. ``"24h"``).
            date: Date range filter with ``"from"`` and ``"to"`` keys.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives (e.g. ``[{"field": "volume", "direction": "desc"}]``).
        """
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
        """Get detailed information for a specific token.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            token_address: Contract address of the token.
            timeframe: Timeframe for the data (e.g. ``"24h"``).
        """
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
        """Get flow intelligence data for a token.

        Shows smart money and notable wallet flows into and out of a token.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            token_address: Contract address of the token.
            timeframe: Timeframe for the data (e.g. ``"24h"``).
            filters: Field-level filters to narrow results.
        """
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
        """Get holder data for a token.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            token_address: Contract address of the token.
            label_type: Filter holders by label type.
            aggregate_by_entity: If ``True``, aggregate holdings by entity.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get token flow data within a date range.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            token_address: Contract address of the token.
            date: Date range with ``"from"`` and ``"to"`` keys.
            label: Filter flows by wallet label.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get buy/sell activity for a token.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            token_address: Contract address of the token.
            date: Date range with ``"from"`` and ``"to"`` keys.
            buy_or_sell: Filter by ``"buy"`` or ``"sell"`` side.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get DEX trade history for a token.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            token_address: Contract address of the token.
            date: Date range with ``"from"`` and ``"to"`` keys.
            only_smart_money: If ``True``, only return trades from smart money wallets.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get transfer history for a token.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            token_address: Contract address of the token.
            date: Date range with ``"from"`` and ``"to"`` keys.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get Jupiter DCA orders for a token (Solana only).

        Args:
            token_address: Token mint address.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
        """
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
        """Get the PnL leaderboard for a token.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            token_address: Contract address of the token.
            date: Date range with ``"from"`` and ``"to"`` keys.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Screen perpetual futures contracts.

        Args:
            date: Date range with ``"from"`` and ``"to"`` keys.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get the perpetual futures PnL leaderboard for a token.

        Args:
            token_symbol: Token ticker symbol (e.g. ``"BTC"``).
            date: Date range with ``"from"`` and ``"to"`` keys.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get open perpetual futures positions for a token.

        Args:
            token_symbol: Token ticker symbol (e.g. ``"BTC"``).
            label_type: Filter positions by wallet label type.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get perpetual futures trade history for a token.

        Args:
            token_symbol: Token ticker symbol (e.g. ``"BTC"``).
            date: Date range with ``"from"`` and ``"to"`` keys.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
    """Token God Mode resource for token-level analytics (async)."""

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
        """Screen tokens across one or more chains.

        Args:
            chains: List of chain identifiers to screen (e.g. ``["ethereum"]``).
            timeframe: Timeframe for the screener data (e.g. ``"24h"``).
            date: Date range filter with ``"from"`` and ``"to"`` keys.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives (e.g. ``[{"field": "volume", "direction": "desc"}]``).
        """
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
        """Get detailed information for a specific token.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            token_address: Contract address of the token.
            timeframe: Timeframe for the data (e.g. ``"24h"``).
        """
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
        """Get flow intelligence data for a token.

        Shows smart money and notable wallet flows into and out of a token.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            token_address: Contract address of the token.
            timeframe: Timeframe for the data (e.g. ``"24h"``).
            filters: Field-level filters to narrow results.
        """
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
        """Get holder data for a token.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            token_address: Contract address of the token.
            label_type: Filter holders by label type.
            aggregate_by_entity: If ``True``, aggregate holdings by entity.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get token flow data within a date range.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            token_address: Contract address of the token.
            date: Date range with ``"from"`` and ``"to"`` keys.
            label: Filter flows by wallet label.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get buy/sell activity for a token.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            token_address: Contract address of the token.
            date: Date range with ``"from"`` and ``"to"`` keys.
            buy_or_sell: Filter by ``"buy"`` or ``"sell"`` side.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get DEX trade history for a token.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            token_address: Contract address of the token.
            date: Date range with ``"from"`` and ``"to"`` keys.
            only_smart_money: If ``True``, only return trades from smart money wallets.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get transfer history for a token.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            token_address: Contract address of the token.
            date: Date range with ``"from"`` and ``"to"`` keys.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get Jupiter DCA orders for a token (Solana only).

        Args:
            token_address: Token mint address.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
        """
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
        """Get the PnL leaderboard for a token.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            token_address: Contract address of the token.
            date: Date range with ``"from"`` and ``"to"`` keys.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Screen perpetual futures contracts.

        Args:
            date: Date range with ``"from"`` and ``"to"`` keys.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get the perpetual futures PnL leaderboard for a token.

        Args:
            token_symbol: Token ticker symbol (e.g. ``"BTC"``).
            date: Date range with ``"from"`` and ``"to"`` keys.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get open perpetual futures positions for a token.

        Args:
            token_symbol: Token ticker symbol (e.g. ``"BTC"``).
            label_type: Filter positions by wallet label type.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get perpetual futures trade history for a token.

        Args:
            token_symbol: Token ticker symbol (e.g. ``"BTC"``).
            date: Date range with ``"from"`` and ``"to"`` keys.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
