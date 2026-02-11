from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import TYPE_CHECKING, Generic, TypeVar

from nansen._models import BaseModel

if TYPE_CHECKING:
    from nansen._base_client import AsyncAPIClient, SyncAPIClient

T = TypeVar("T", bound=BaseModel)


class PaginationInfo(BaseModel):
    page: int = 1
    per_page: int = 10
    is_last_page: bool = True


class SyncPage(Generic[T]):
    """A single page of results with auto-pagination support."""

    data: list[T]
    pagination: PaginationInfo

    _client: SyncAPIClient
    _path: str
    _body: dict[str, object]
    _model: type[T]

    def __init__(
        self,
        *,
        data: list[T],
        pagination: PaginationInfo,
        client: SyncAPIClient,
        path: str,
        body: dict[str, object],
        model: type[T],
    ) -> None:
        self.data = data
        self.pagination = pagination
        self._client = client
        self._path = path
        self._body = body
        self._model = model

    @property
    def has_next_page(self) -> bool:
        return not self.pagination.is_last_page

    def next_page(self) -> SyncPage[T]:
        """Fetch the next page of results."""
        if not self.has_next_page:
            raise StopIteration("No more pages")
        body = {**self._body}
        pagination = body.get("pagination", {})
        if not isinstance(pagination, dict):
            pagination = {}
        pagination["page"] = self.pagination.page + 1
        body["pagination"] = pagination
        return self._client._request_page(
            path=self._path,
            body=body,
            model=self._model,
        )

    def iter_pages(self) -> Iterator[SyncPage[T]]:
        """Iterate over all pages starting from this one."""
        page = self
        while True:
            yield page
            if not page.has_next_page:
                break
            page = page.next_page()

    def __iter__(self) -> Iterator[T]:
        """Iterate over all items across all pages."""
        for page in self.iter_pages():
            yield from page.data

    def __len__(self) -> int:
        return len(self.data)


class AsyncPage(Generic[T]):
    """A single page of results with async auto-pagination support."""

    data: list[T]
    pagination: PaginationInfo

    _client: AsyncAPIClient
    _path: str
    _body: dict[str, object]
    _model: type[T]

    def __init__(
        self,
        *,
        data: list[T],
        pagination: PaginationInfo,
        client: AsyncAPIClient,
        path: str,
        body: dict[str, object],
        model: type[T],
    ) -> None:
        self.data = data
        self.pagination = pagination
        self._client = client
        self._path = path
        self._body = body
        self._model = model

    @property
    def has_next_page(self) -> bool:
        return not self.pagination.is_last_page

    async def next_page(self) -> AsyncPage[T]:
        """Fetch the next page of results."""
        if not self.has_next_page:
            raise StopAsyncIteration("No more pages")
        body = {**self._body}
        pagination = body.get("pagination", {})
        if not isinstance(pagination, dict):
            pagination = {}
        pagination["page"] = self.pagination.page + 1
        body["pagination"] = pagination
        return await self._client._request_page(
            path=self._path,
            body=body,
            model=self._model,
        )

    async def iter_pages(self) -> AsyncIterator[AsyncPage[T]]:
        """Iterate over all pages starting from this one."""
        page = self
        while True:
            yield page
            if not page.has_next_page:
                break
            page = await page.next_page()

    async def __aiter__(self) -> AsyncIterator[T]:
        """Iterate over all items across all pages."""
        async for page in self.iter_pages():
            for item in page.data:
                yield item

    def __len__(self) -> int:
        return len(self.data)
