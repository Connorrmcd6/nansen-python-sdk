from __future__ import annotations

from functools import cached_property
from typing import Any

from nansen._pagination import AsyncPage, SyncPage
from nansen._response import APIResponse
from nansen._types import NOT_GIVEN, NotGiven
from nansen.resources._base import AsyncAPIResource, SyncAPIResource
from nansen.resources.profiler.address import Address, AsyncAddress
from nansen.types.profiler import (
    EntitySearchItem,
    PerpLeaderboardItem,
    PerpPositionsResponse,
    PnlItem,
    PnlSummaryResponse,
    ProfilerPerpTradeItem,
)


class Profiler(SyncAPIResource):
    @cached_property
    def address(self) -> Address:
        return Address(self._client)

    def pnl_summary(
        self,
        *,
        chain: str,
        date: dict[str, str],
        address: str | NotGiven = NOT_GIVEN,
        entity_name: str | NotGiven = NOT_GIVEN,
    ) -> APIResponse[PnlSummaryResponse]:
        return self._post(
            "/profiler/address/pnl-summary",
            body={
                "chain": chain,
                "date": date,
                "address": address,
                "entity_name": entity_name,
            },
            model=PnlSummaryResponse,
        )

    def pnl(
        self,
        *,
        chain: str,
        address: str | NotGiven = NOT_GIVEN,
        entity_name: str | NotGiven = NOT_GIVEN,
        date: dict[str, str] | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[PnlItem]:
        return self._post_page(
            "/profiler/address/pnl",
            body={
                "chain": chain,
                "address": address,
                "entity_name": entity_name,
                "date": date,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=PnlItem,
        )

    def perp_positions(
        self,
        *,
        address: str,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> APIResponse[PerpPositionsResponse]:
        return self._post(
            "/profiler/perp-positions",
            body={
                "address": address,
                "filters": filters,
                "order_by": order_by,
            },
            model=PerpPositionsResponse,
        )

    def perp_trades(
        self,
        *,
        address: str,
        date: dict[str, str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[ProfilerPerpTradeItem]:
        return self._post_page(
            "/profiler/perp-trades",
            body={
                "address": address,
                "date": date,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=ProfilerPerpTradeItem,
        )

    def entity_search(
        self,
        *,
        search_query: str,
    ) -> APIResponse[list[EntitySearchItem]]:

        from pydantic import TypeAdapter

        response = self._client._request(
            "POST",
            "/search/entity-name",
            body={"search_query": search_query},
        )
        body = response.json()
        raw_data = body.get("data", [])
        items = TypeAdapter(list[EntitySearchItem]).validate_python(raw_data)
        from nansen._response import APIResponse

        return APIResponse(data=items, http_response=response)

    def perp_leaderboard(
        self,
        *,
        date: dict[str, str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[PerpLeaderboardItem]:
        return self._post_page(
            "/perp-leaderboard",
            body={
                "date": date,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=PerpLeaderboardItem,
        )


class AsyncProfiler(AsyncAPIResource):
    @cached_property
    def address(self) -> AsyncAddress:
        return AsyncAddress(self._client)

    async def pnl_summary(
        self,
        *,
        chain: str,
        date: dict[str, str],
        address: str | NotGiven = NOT_GIVEN,
        entity_name: str | NotGiven = NOT_GIVEN,
    ) -> APIResponse[PnlSummaryResponse]:
        return await self._post(
            "/profiler/address/pnl-summary",
            body={
                "chain": chain,
                "date": date,
                "address": address,
                "entity_name": entity_name,
            },
            model=PnlSummaryResponse,
        )

    async def pnl(
        self,
        *,
        chain: str,
        address: str | NotGiven = NOT_GIVEN,
        entity_name: str | NotGiven = NOT_GIVEN,
        date: dict[str, str] | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[PnlItem]:
        return await self._post_page(
            "/profiler/address/pnl",
            body={
                "chain": chain,
                "address": address,
                "entity_name": entity_name,
                "date": date,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=PnlItem,
        )

    async def perp_positions(
        self,
        *,
        address: str,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> APIResponse[PerpPositionsResponse]:
        return await self._post(
            "/profiler/perp-positions",
            body={
                "address": address,
                "filters": filters,
                "order_by": order_by,
            },
            model=PerpPositionsResponse,
        )

    async def perp_trades(
        self,
        *,
        address: str,
        date: dict[str, str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[ProfilerPerpTradeItem]:
        return await self._post_page(
            "/profiler/perp-trades",
            body={
                "address": address,
                "date": date,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=ProfilerPerpTradeItem,
        )

    async def entity_search(
        self,
        *,
        search_query: str,
    ) -> APIResponse[list[EntitySearchItem]]:

        from pydantic import TypeAdapter

        response = await self._client._request(
            "POST",
            "/search/entity-name",
            body={"search_query": search_query},
        )
        body = response.json()
        raw_data = body.get("data", [])
        items = TypeAdapter(list[EntitySearchItem]).validate_python(raw_data)
        from nansen._response import APIResponse

        return APIResponse(data=items, http_response=response)

    async def perp_leaderboard(
        self,
        *,
        date: dict[str, str],
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[PerpLeaderboardItem]:
        return await self._post_page(
            "/perp-leaderboard",
            body={
                "date": date,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=PerpLeaderboardItem,
        )
