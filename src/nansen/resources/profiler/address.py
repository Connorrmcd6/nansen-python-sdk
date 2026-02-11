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
    """Address sub-resource for wallet-level profiler endpoints."""

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
        """Get current token balances for an address or entity.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            address: Wallet address to look up.
            entity_name: Entity name to look up (alternative to ``address``).
            hide_spam_token: If ``True``, exclude tokens flagged as spam.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get historical token balances for an address or entity.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            date: Date range with ``"from"`` and ``"to"`` keys.
            address: Wallet address to look up.
            entity_name: Entity name to look up (alternative to ``address``).
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get transaction history for an address.

        Args:
            address: Wallet address to look up.
            chain: Chain identifier (e.g. ``"ethereum"``).
            date: Date range with ``"from"`` and ``"to"`` keys.
            hide_spam_token: If ``True``, exclude transactions involving spam tokens.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get counterparty data for an address or entity.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            date: Date range with ``"from"`` and ``"to"`` keys.
            address: Wallet address to look up.
            entity_name: Entity name to look up (alternative to ``address``).
            source_input: Source input type for the query.
            group_by: Field to group counterparties by.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get wallets related to an address.

        Args:
            address: Wallet address to look up.
            chain: Chain identifier (e.g. ``"ethereum"``).
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get labels for an address (beta endpoint).

        This endpoint uses the ``/api/beta/`` base path and has a different
        request structure than standard v1 endpoints.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            address: Wallet address to look up.
            entity: Filter by entity name.
            label: Filter by label name.
            pagination: Pagination options (``page``, ``per_page``).
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
    """Address sub-resource for wallet-level profiler endpoints (async)."""

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
        """Get current token balances for an address or entity.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            address: Wallet address to look up.
            entity_name: Entity name to look up (alternative to ``address``).
            hide_spam_token: If ``True``, exclude tokens flagged as spam.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get historical token balances for an address or entity.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            date: Date range with ``"from"`` and ``"to"`` keys.
            address: Wallet address to look up.
            entity_name: Entity name to look up (alternative to ``address``).
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get transaction history for an address.

        Args:
            address: Wallet address to look up.
            chain: Chain identifier (e.g. ``"ethereum"``).
            date: Date range with ``"from"`` and ``"to"`` keys.
            hide_spam_token: If ``True``, exclude transactions involving spam tokens.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get counterparty data for an address or entity.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            date: Date range with ``"from"`` and ``"to"`` keys.
            address: Wallet address to look up.
            entity_name: Entity name to look up (alternative to ``address``).
            source_input: Source input type for the query.
            group_by: Field to group counterparties by.
            filters: Field-level filters to narrow results.
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get wallets related to an address.

        Args:
            address: Wallet address to look up.
            chain: Chain identifier (e.g. ``"ethereum"``).
            pagination: Pagination options (``page``, ``per_page``).
            order_by: List of ordering directives.
        """
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
        """Get labels for an address (beta endpoint).

        This endpoint uses the ``/api/beta/`` base path and has a different
        request structure than standard v1 endpoints.

        Args:
            chain: Chain identifier (e.g. ``"ethereum"``).
            address: Wallet address to look up.
            entity: Filter by entity name.
            label: Filter by label name.
            pagination: Pagination options (``page``, ``per_page``).
        """

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
