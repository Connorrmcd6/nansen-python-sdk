from __future__ import annotations

from nansen._models import BaseModel


class PointsLeaderboardEntry(BaseModel):
    rank: int | None = None
    evm_address: str | None = None
    solana_address: str | None = None
    points: int | None = None
    tier: str | None = None
    is_eligible: bool | None = None


class PointsLeaderboardResponse(BaseModel):
    data: list[PointsLeaderboardEntry] | None = None
