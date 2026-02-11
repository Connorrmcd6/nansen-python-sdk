from __future__ import annotations

from typing_extensions import TypedDict


class PaginationParam(TypedDict, total=False):
    page: int
    per_page: int
