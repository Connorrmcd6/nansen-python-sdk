from __future__ import annotations

from nansen._models import BaseModel


class ProtocolToken(BaseModel):
    address: str | None = None
    symbol: str | None = None
    amount: float | None = None
    value_usd: float | None = None
    position_type: str | None = None


class ProtocolHolding(BaseModel):
    protocol_name: str | None = None
    chain: str | None = None
    total_value_usd: float | None = None
    total_assets_usd: float | None = None
    total_debts_usd: float | None = None
    total_rewards_usd: float | None = None
    tokens: list[ProtocolToken] | None = None


class HoldingsSummary(BaseModel):
    total_value_usd: float | None = None
    total_assets_usd: float | None = None
    total_debts_usd: float | None = None
    total_rewards_usd: float | None = None
    token_count: int | None = None
    protocol_count: int | None = None


class DefiHoldingsResponse(BaseModel):
    summary: HoldingsSummary | None = None
    protocols: list[ProtocolHolding] | None = None
