from __future__ import annotations

from nansen._models import BaseModel

# --- Netflow ---


class SmartMoneyNetflowItem(BaseModel):
    token_address: str | None = None
    token_symbol: str | None = None
    net_flow_1h_usd: float | None = None
    net_flow_24h_usd: float | None = None
    net_flow_7d_usd: float | None = None
    net_flow_30d_usd: float | None = None
    chain: str | None = None
    token_sectors: list[str] | None = None
    trader_count: int | None = None
    token_age_days: int | None = None
    market_cap_usd: float | None = None


# --- DEX Trades ---


class SmartMoneyDexTradeItem(BaseModel):
    chain: str | None = None
    block_timestamp: str | None = None
    transaction_hash: str | None = None
    trader_address: str | None = None
    trader_address_label: str | None = None
    token_bought_address: str | None = None
    token_sold_address: str | None = None
    token_bought_amount: float | None = None
    token_sold_amount: float | None = None
    token_bought_symbol: str | None = None
    token_sold_symbol: str | None = None
    token_bought_age_days: int | None = None
    token_sold_age_days: int | None = None
    token_bought_market_cap: float | None = None
    token_sold_market_cap: float | None = None
    trade_value_usd: float | None = None


# --- Perp Trades ---


class SmartMoneyPerpTradeItem(BaseModel):
    trader_address_label: str | None = None
    trader_address: str | None = None
    token_symbol: str | None = None
    side: str | None = None
    action: str | None = None
    token_amount: float | None = None
    price_usd: float | None = None
    value_usd: float | None = None
    type: str | None = None
    block_timestamp: str | None = None
    transaction_hash: str | None = None


# --- DCAs ---


class SmartMoneyDcaItem(BaseModel):
    dca_created_at: str | None = None
    dca_updated_at: str | None = None
    trader_address: str | None = None
    transaction_hash: str | None = None
    trader_address_label: str | None = None
    dca_vault_address: str | None = None
    input_token_address: str | None = None
    output_token_address: str | None = None
    deposit_token_amount: float | None = None
    token_spent_amount: float | None = None
    output_token_redeemed_amount: float | None = None
    dca_status: str | None = None
    input_token_symbol: str | None = None
    output_token_symbol: str | None = None
    deposit_value_usd: float | None = None


# --- Holdings ---


class SmartMoneyHoldingItem(BaseModel):
    chain: str | None = None
    token_address: str | None = None
    token_symbol: str | None = None
    token_sectors: list[str] | None = None
    value_usd: float | None = None
    balance_24h_percent_change: float | None = None
    holders_count: int | None = None
    share_of_holdings_percent: float | None = None
    token_age_days: int | None = None
    market_cap_usd: float | None = None


# --- Historical Holdings ---


class SmartMoneyHistoricalHoldingItem(BaseModel):
    date: str | None = None
    chain: str | None = None
    token_address: str | None = None
    token_symbol: str | None = None
    token_sectors: list[str] | None = None
    smart_money_labels: list[str] | None = None
    balance: float | None = None
    value_usd: float | None = None
    balance_24h_percent_change: float | None = None
    holders_count: int | None = None
    share_of_holdings_percent: float | None = None
    token_age_days: int | None = None
    market_cap_usd: float | None = None
