from __future__ import annotations

from nansen._models import BaseModel

# --- Token Screener ---


class TokenScreenerItem(BaseModel):
    chain: str | None = None
    token_address: str | None = None
    token_symbol: str | None = None
    token_name: str | None = None
    market_cap_usd: float | None = None
    price_usd: float | None = None
    price_change: float | None = None
    volume: float | None = None
    buy_volume: float | None = None
    sell_volume: float | None = None
    unique_buyers: int | None = None
    unique_sellers: int | None = None
    total_buys: int | None = None
    total_sells: int | None = None
    netflow: float | None = None
    smart_money_netflow: float | None = None
    smart_money_inflow: float | None = None
    smart_money_outflow: float | None = None
    smart_money_buy_volume: float | None = None
    smart_money_sell_volume: float | None = None
    total_holders: int | None = None
    token_age_days: int | None = None
    liquidity_usd: float | None = None
    fdv_usd: float | None = None


# --- Token Information ---


class TokenDetails(BaseModel):
    token_deployment_date: str | None = None
    website: str | None = None
    x: str | None = None
    telegram: str | None = None
    market_cap_usd: float | None = None
    fdv_usd: float | None = None
    circulating_supply: float | None = None
    total_supply: float | None = None


class SpotMetrics(BaseModel):
    volume_total_usd: float | None = None
    buy_volume_usd: float | None = None
    sell_volume_usd: float | None = None
    total_buys: int | None = None
    total_sells: int | None = None
    unique_buyers: int | None = None
    unique_sellers: int | None = None
    liquidity_usd: float | None = None
    total_holders: int | None = None


class TokenInformationData(BaseModel):
    name: str | None = None
    symbol: str | None = None
    contract_address: str | None = None
    logo: str | None = None
    token_details: TokenDetails | None = None
    spot_metrics: SpotMetrics | None = None


class TokenInformationResponse(BaseModel):
    data: TokenInformationData | None = None


# --- Flow Intel ---


class FlowIntelItem(BaseModel):
    public_figure_net_flow_usd: float | None = None
    public_figure_avg_flow_usd: float | None = None
    public_figure_wallet_count: int | None = None
    top_pnl_net_flow_usd: float | None = None
    top_pnl_avg_flow_usd: float | None = None
    top_pnl_wallet_count: int | None = None
    whale_net_flow_usd: float | None = None
    whale_avg_flow_usd: float | None = None
    whale_wallet_count: int | None = None
    smart_trader_net_flow_usd: float | None = None
    smart_trader_avg_flow_usd: float | None = None
    smart_trader_wallet_count: int | None = None
    exchange_net_flow_usd: float | None = None
    exchange_avg_flow_usd: float | None = None
    exchange_wallet_count: int | None = None
    fresh_wallets_net_flow_usd: float | None = None
    fresh_wallets_avg_flow_usd: float | None = None
    fresh_wallets_wallet_count: int | None = None


# --- Holders ---


class HolderItem(BaseModel):
    address: str | None = None
    address_label: str | None = None
    token_amount: float | None = None
    total_outflow: float | None = None
    total_inflow: float | None = None
    balance_change_24h: float | None = None
    balance_change_7d: float | None = None
    balance_change_30d: float | None = None
    ownership_percentage: float | None = None
    value_usd: float | None = None


# --- Flows ---


class FlowItem(BaseModel):
    date: str | None = None
    price_usd: float | None = None
    token_amount: float | None = None
    value_usd: float | None = None
    holders_count: int | None = None
    total_inflows_count: float | None = None
    total_outflows_count: float | None = None


# --- Who Bought/Sold ---


class WhoBoughtSoldItem(BaseModel):
    address: str | None = None
    address_label: str | None = None
    bought_token_volume: float | None = None
    sold_token_volume: float | None = None
    token_trade_volume: float | None = None
    bought_volume_usd: float | None = None
    sold_volume_usd: float | None = None
    trade_volume_usd: float | None = None


# --- DEX Trades ---


class TgmDexTradeItem(BaseModel):
    block_timestamp: str | None = None
    transaction_hash: str | None = None
    trader_address: str | None = None
    trader_address_label: str | None = None
    action: str | None = None
    token_address: str | None = None
    token_name: str | None = None
    token_amount: float | None = None
    traded_token_address: str | None = None
    traded_token_name: str | None = None
    traded_token_amount: float | None = None
    estimated_swap_price_usd: float | None = None
    estimated_value_usd: float | None = None


# --- Transfers ---


class TransferItem(BaseModel):
    block_timestamp: str | None = None
    transaction_hash: str | None = None
    from_address: str | None = None
    to_address: str | None = None
    from_address_label: str | None = None
    to_address_label: str | None = None
    transaction_type: str | None = None
    transfer_amount: float | None = None
    transfer_value_usd: float | None = None


# --- DCAs (Jupiter) ---


class TgmDcaItem(BaseModel):
    since_timestamp: str | None = None
    last_timestamp: str | None = None
    trader_address: str | None = None
    creation_hash: str | None = None
    trader_label: str | None = None
    dca_vault_address: str | None = None
    input_mint_address: str | None = None
    output_mint_address: str | None = None
    deposit_amount: float | None = None
    deposit_spent: float | None = None
    other_token_redeemed: float | None = None
    status: str | None = None
    token_input: str | None = None
    token_output: str | None = None
    deposit_usd_value: float | None = None


# --- PnL Leaderboard ---


class PnlLeaderboardItem(BaseModel):
    trader_address: str | None = None
    trader_address_label: str | None = None
    price_usd: float | None = None
    pnl_usd_realised: float | None = None
    pnl_usd_unrealised: float | None = None
    pnl_usd_total: float | None = None
    holding_amount: float | None = None
    holding_usd: float | None = None
    max_balance_held: float | None = None
    max_balance_held_usd: float | None = None
    still_holding_balance_ratio: float | None = None
    netflow_amount_usd: float | None = None
    netflow_amount: float | None = None
    roi_percent_total: float | None = None
    roi_percent_realised: float | None = None
    roi_percent_unrealised: float | None = None
    nof_trades: int | None = None


# --- Perp Screener ---


class PerpScreenerItem(BaseModel):
    token_symbol: str | None = None
    volume: float | None = None
    buy_volume: float | None = None
    sell_volume: float | None = None
    buy_sell_pressure: float | None = None
    trader_count: int | None = None
    mark_price: float | None = None
    funding: float | None = None
    open_interest: float | None = None
    previous_price_usd: float | None = None
    # Smart money fields (present when only_smart_money=true)
    smart_money_volume: float | None = None
    smart_money_buy_volume: float | None = None
    smart_money_sell_volume: float | None = None
    net_position_change: float | None = None
    current_smart_money_position_longs_usd: float | None = None
    current_smart_money_position_shorts_usd: float | None = None
    smart_money_longs_count: int | None = None
    smart_money_shorts_count: int | None = None


# --- Perp PnL Leaderboard ---


class PerpPnlLeaderboardItem(BaseModel):
    trader_address: str | None = None
    trader_address_label: str | None = None
    price_usd: float | None = None
    pnl_usd_realised: float | None = None
    pnl_usd_unrealised: float | None = None
    pnl_usd_total: float | None = None
    holding_amount: float | None = None
    position_value_usd: float | None = None
    max_balance_held: float | None = None
    max_balance_held_usd: float | None = None
    still_holding_balance_ratio: float | None = None
    netflow_amount_usd: float | None = None
    netflow_amount: float | None = None
    roi_percent_total: float | None = None
    roi_percent_realised: float | None = None
    roi_percent_unrealised: float | None = None
    nof_trades: int | None = None


# --- Perp Positions ---


class TgmPerpPositionItem(BaseModel):
    address: str | None = None
    address_label: str | None = None
    side: str | None = None
    position_value_usd: float | None = None
    position_size: float | None = None
    leverage: str | None = None
    leverage_type: str | None = None
    entry_price: float | None = None
    mark_price: float | None = None
    liquidation_price: float | None = None
    funding_usd: float | None = None
    upnl_usd: float | None = None


# --- Perp Trades ---


class TgmPerpTradeItem(BaseModel):
    trader_address: str | None = None
    trader_address_label: str | None = None
    token_symbol: str | None = None
    side: str | None = None
    action: str | None = None
    token_amount: float | None = None
    price_usd: float | None = None
    value_usd: float | None = None
    type: str | None = None
    block_timestamp: str | None = None
    transaction_hash: str | None = None
