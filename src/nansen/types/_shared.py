from __future__ import annotations

from typing_extensions import TypedDict

from nansen._models import BaseModel


class DateRange(TypedDict, total=False):
    start: str
    end: str


class NumericRangeFilter(TypedDict, total=False):
    min: float
    max: float


class OrderBy(TypedDict, total=False):
    field: str
    direction: str  # "ASC" | "DESC"


class PaginationResponse(BaseModel):
    page: int = 1
    per_page: int = 10
    is_last_page: bool = True
