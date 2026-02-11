from __future__ import annotations

from typing import Any

from nansen._pagination import AsyncPage, SyncPage
from nansen._response import APIResponse
from nansen._types import NOT_GIVEN, NotGiven
from nansen.resources._base import AsyncAPIResource, SyncAPIResource
from nansen.types.profiler import (
    AddressLabelItem,
    CounterpartyItem,
    HistoricalBalanceItem,
    ProfilerBalanceItem,
    RelatedWalletItem,
    TransactionItem,
)


class Address(SyncAPIResource):
    def current_balance(
        self,
        *,
        chain: str,
        address: str | NotGiven = NOT_GIVEN,
        entity_name: str | NotGiven = NOT_GIVEN,
        hide_spam_token: bool | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[ProfilerBalanceItem]:
        return self._post_page(
            "/profiler/address/current-balance",
            body={
                "chain": chain,
                "address": address,
                "entity_name": entity_name,
                "hide_spam_token": hide_spam_token,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=ProfilerBalanceItem,
        )

    def historical_balances(
        self,
        *,
        chain: str,
        date: dict[str, str],
        address: str | NotGiven = NOT_GIVEN,
        entity_name: str | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[HistoricalBalanceItem]:
        return self._post_page(
            "/profiler/address/historical-balances",
            body={
                "chain": chain,
                "date": date,
                "address": address,
                "entity_name": entity_name,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=HistoricalBalanceItem,
        )

    def transactions(
        self,
        *,
        address: str,
        chain: str,
        date: dict[str, str],
        hide_spam_token: bool | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[TransactionItem]:
        return self._post_page(
            "/profiler/address/transactions",
            body={
                "address": address,
                "chain": chain,
                "date": date,
                "hide_spam_token": hide_spam_token,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=TransactionItem,
        )

    def counterparties(
        self,
        *,
        chain: str,
        date: dict[str, str],
        address: str | NotGiven = NOT_GIVEN,
        entity_name: str | NotGiven = NOT_GIVEN,
        source_input: str | NotGiven = NOT_GIVEN,
        group_by: str | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[CounterpartyItem]:
        return self._post_page(
            "/profiler/address/counterparties",
            body={
                "chain": chain,
                "date": date,
                "address": address,
                "entity_name": entity_name,
                "source_input": source_input,
                "group_by": group_by,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=CounterpartyItem,
        )

    def related_wallets(
        self,
        *,
        address: str,
        chain: str,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> SyncPage[RelatedWalletItem]:
        return self._post_page(
            "/profiler/address/related-wallets",
            body={
                "address": address,
                "chain": chain,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=RelatedWalletItem,
        )

    def labels(
        self,
        *,
        chain: str,
        address: str,
        entity: str | NotGiven = NOT_GIVEN,
        label: str | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
    ) -> APIResponse[list[AddressLabelItem]]:
        """Fetch address labels (beta endpoint).

        Note: This endpoint uses ``/api/beta/`` and has a different
        request structure than standard v1 endpoints.
        """

        parameters: dict[str, Any] = {"chain": chain, "address": address}
        if not isinstance(entity, NotGiven):
            parameters["entity"] = entity
        if not isinstance(label, NotGiven):
            parameters["label"] = label

        body: dict[str, Any] = {"parameters": parameters}
        if not isinstance(pagination, NotGiven):
            body["pagination"] = pagination

        # Beta endpoint uses a different base path

        from pydantic import TypeAdapter

        response = self._client._request(
            "POST",
            "/profiler/address/labels",
            body=body,
            base_url=self._client.base_url.replace("/api/v1", "/api/beta"),
        )
        items = TypeAdapter(list[AddressLabelItem]).validate_python(response.json())
        from nansen._response import APIResponse

        return APIResponse(data=items, http_response=response)


class AsyncAddress(AsyncAPIResource):
    async def current_balance(
        self,
        *,
        chain: str,
        address: str | NotGiven = NOT_GIVEN,
        entity_name: str | NotGiven = NOT_GIVEN,
        hide_spam_token: bool | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[ProfilerBalanceItem]:
        return await self._post_page(
            "/profiler/address/current-balance",
            body={
                "chain": chain,
                "address": address,
                "entity_name": entity_name,
                "hide_spam_token": hide_spam_token,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=ProfilerBalanceItem,
        )

    async def historical_balances(
        self,
        *,
        chain: str,
        date: dict[str, str],
        address: str | NotGiven = NOT_GIVEN,
        entity_name: str | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[HistoricalBalanceItem]:
        return await self._post_page(
            "/profiler/address/historical-balances",
            body={
                "chain": chain,
                "date": date,
                "address": address,
                "entity_name": entity_name,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=HistoricalBalanceItem,
        )

    async def transactions(
        self,
        *,
        address: str,
        chain: str,
        date: dict[str, str],
        hide_spam_token: bool | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[TransactionItem]:
        return await self._post_page(
            "/profiler/address/transactions",
            body={
                "address": address,
                "chain": chain,
                "date": date,
                "hide_spam_token": hide_spam_token,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=TransactionItem,
        )

    async def counterparties(
        self,
        *,
        chain: str,
        date: dict[str, str],
        address: str | NotGiven = NOT_GIVEN,
        entity_name: str | NotGiven = NOT_GIVEN,
        source_input: str | NotGiven = NOT_GIVEN,
        group_by: str | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[CounterpartyItem]:
        return await self._post_page(
            "/profiler/address/counterparties",
            body={
                "chain": chain,
                "date": date,
                "address": address,
                "entity_name": entity_name,
                "source_input": source_input,
                "group_by": group_by,
                "filters": filters,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=CounterpartyItem,
        )

    async def related_wallets(
        self,
        *,
        address: str,
        chain: str,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
        order_by: list[dict[str, str]] | NotGiven = NOT_GIVEN,
    ) -> AsyncPage[RelatedWalletItem]:
        return await self._post_page(
            "/profiler/address/related-wallets",
            body={
                "address": address,
                "chain": chain,
                "pagination": pagination,
                "order_by": order_by,
            },
            model=RelatedWalletItem,
        )

    async def labels(
        self,
        *,
        chain: str,
        address: str,
        entity: str | NotGiven = NOT_GIVEN,
        label: str | NotGiven = NOT_GIVEN,
        pagination: dict[str, Any] | NotGiven = NOT_GIVEN,
    ) -> APIResponse[list[AddressLabelItem]]:

        parameters: dict[str, Any] = {"chain": chain, "address": address}
        if not isinstance(entity, NotGiven):
            parameters["entity"] = entity
        if not isinstance(label, NotGiven):
            parameters["label"] = label

        body: dict[str, Any] = {"parameters": parameters}
        if not isinstance(pagination, NotGiven):
            body["pagination"] = pagination

        from pydantic import TypeAdapter

        response = await self._client._request(
            "POST",
            "/profiler/address/labels",
            body=body,
            base_url=self._client.base_url.replace("/api/v1", "/api/beta"),
        )
        items = TypeAdapter(list[AddressLabelItem]).validate_python(response.json())
        from nansen._response import APIResponse

        return APIResponse(data=items, http_response=response)
