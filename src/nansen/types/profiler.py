from __future__ import annotations

from nansen._models import BaseModel

# --- Address Current Balance ---


class ProfilerBalanceItem(BaseModel):
    chain: str | None = None
    address: str | None = None
    token_address: str | None = None
    token_symbol: str | None = None
    token_name: str | None = None
    token_amount: float | None = None
    price_usd: float | None = None
    value_usd: float | None = None


# --- Address Historical Balances ---


class HistoricalBalanceItem(BaseModel):
    block_timestamp: str | None = None
    token_address: str | None = None
    chain: str | None = None
    token_symbol: str | None = None
    token_amount: float | None = None
    value_usd: float | None = None


# --- Address Transactions ---


class TokenTransfer(BaseModel):
    token_symbol: str | None = None
    token_amount: float | None = None
    price_usd: float | None = None
    value_usd: float | None = None
    token_address: str | None = None
    chain: str | None = None
    from_address: str | None = None
    to_address: str | None = None
    from_address_label: str | None = None
    to_address_label: str | None = None


class TransactionItem(BaseModel):
    chain: str | None = None
    method: str | None = None
    tokens_sent: list[TokenTransfer] | None = None
    tokens_received: list[TokenTransfer] | None = None
    volume_usd: float | None = None
    block_timestamp: str | None = None
    transaction_hash: str | None = None
    source_type: str | None = None


# --- Address Counterparties ---


class CounterpartyTokenInfo(BaseModel):
    token_address: str | None = None
    token_symbol: str | None = None
    token_name: str | None = None
    num_transfer: str | None = None


class CounterpartyItem(BaseModel):
    counterparty_address: str | None = None
    counterparty_address_label: list[str] | None = None
    interaction_count: int | None = None
    total_volume_usd: float | None = None
    volume_in_usd: float | None = None
    volume_out_usd: float | None = None
    tokens_info: list[CounterpartyTokenInfo] | None = None


# --- Address Related Wallets ---


class RelatedWalletItem(BaseModel):
    address: str | None = None
    address_label: str | None = None
    relation: str | None = None
    transaction_hash: str | None = None
    block_timestamp: str | None = None
    order: int | None = None
    chain: str | None = None


# --- Address Labels ---


class AddressLabelItem(BaseModel):
    label: str | None = None
    category: str | None = None
    definition: str | None = None
    smEarnedDate: str | None = None
    fullname: str | None = None


# --- PnL Summary ---


class PnlSummaryTokenItem(BaseModel):
    realized_pnl: float | None = None
    realized_roi: float | None = None
    token_address: str | None = None
    token_symbol: str | None = None
    chain: str | None = None


class PnlSummaryResponse(BaseModel):
    top5_tokens: list[PnlSummaryTokenItem] | None = None
    traded_token_count: int | None = None
    traded_times: int | None = None
    realized_pnl_usd: float | None = None
    realized_pnl_percent: float | None = None
    win_rate: float | None = None


# --- PnL (Detailed) ---


class PnlItem(BaseModel):
    token_address: str | None = None
    token_symbol: str | None = None
    token_price: float | None = None
    roi_percent_realised: float | None = None
    pnl_usd_realised: float | None = None
    pnl_usd_unrealised: float | None = None
    roi_percent_unrealised: float | None = None
    bought_amount: float | None = None
    bought_usd: float | None = None
    cost_basis_usd: float | None = None
    sold_amount: float | None = None
    sold_usd: float | None = None
    avg_sold_price_usd: float | None = None
    holding_amount: float | None = None
    holding_usd: float | None = None
    nof_buys: str | None = None
    nof_sells: str | None = None
    max_balance_held: float | None = None
    max_balance_held_usd: float | None = None


# --- Perp Positions ---


class PerpPositionDetail(BaseModel):
    token_symbol: str | None = None
    size: str | None = None
    position_value_usd: str | None = None
    entry_price_usd: str | None = None
    liquidation_price_usd: str | None = None
    leverage_value: int | None = None
    leverage_type: str | None = None
    leverage_raw_usd: str | None = None
    margin_used_usd: str | None = None
    max_leverage_value: int | None = None
    return_on_equity: str | None = None
    unrealized_pnl_usd: str | None = None
    cumulative_funding_all_time_usd: str | None = None
    cumulative_funding_since_change_usd: str | None = None
    cumulative_funding_since_open_usd: str | None = None


class AssetPosition(BaseModel):
    position: PerpPositionDetail | None = None
    position_type: str | None = None


class PerpPositionsData(BaseModel):
    assetPositions: list[AssetPosition] | None = None
    crossMaintenanceMarginUsed: str | None = None
    cross_margin_summary_account_value_usd: str | None = None
    cross_margin_summary_total_margin_used_usd: str | None = None
    cross_margin_summary_total_net_liquidation_position_on_usd: str | None = None
    cross_margin_summary_total_raw_usd: str | None = None
    margin_summary_account_value_usd: str | None = None
    margin_summary_total_margin_used_usd: str | None = None
    margin_summary_total_net_liquidation_position_usd: str | None = None
    margin_summary_total_raw_usd: str | None = None
    time: int | None = None
    withdrawable: str | None = None


class PerpPositionsResponse(BaseModel):
    data: PerpPositionsData | None = None


# --- Perp Trades ---


class ProfilerPerpTradeItem(BaseModel):
    timestamp: str | None = None
    side: str | None = None
    action: str | None = None
    block_number: int | None = None
    token_symbol: str | None = None
    price: float | None = None
    size: float | None = None
    value_usd: float | None = None
    start_position: float | None = None
    closed_pnl: float | None = None
    crossed: bool | None = None
    fee_usd: float | None = None
    fee_token_symbol: str | None = None
    transaction_hash: str | None = None
    user: str | None = None
    oid: int | None = None


# --- Entity Search ---


class EntitySearchItem(BaseModel):
    entity_name: str | None = None


# --- Perp Leaderboard ---


class PerpLeaderboardItem(BaseModel):
    trader_address: str | None = None
    trader_address_label: str | None = None
    total_pnl: float | None = None
    roi: float | None = None
    account_value: float | None = None
