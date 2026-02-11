"""Basic usage of the Nansen Python SDK."""

from nansen import Nansen

# API key from param or NANSEN_API_KEY env var
# client = Nansen(api_key="your-api-key")
client = Nansen()

# Smart Money holdings — auto-paginates across all pages
for item in client.smart_money.holdings(chains=["ethereum"]):
    print(f"{item.token_symbol}: ${item.value_usd:,.2f} ({item.holders_count} holders)")

# Token screener with filters
page = client.tgm.token_screener(
    chains=["ethereum", "base"],
    timeframe="24h",
    filters={"market_cap_usd": {"min": 1_000_000}},
    pagination={"page": 1, "per_page": 20},
)
for token in page.data:
    print(f"{token.token_symbol} on {token.chain}: ${token.price_usd}")

# Profiler — address balance
balances = client.profiler.address.current_balance(
    chain="ethereum",
    address="0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
)
for bal in balances.data:
    print(f"{bal.token_symbol}: ${bal.value_usd}")

# Portfolio — DeFi holdings
resp = client.portfolio.defi_holdings(
    wallet_address="0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
)
print(f"Total DeFi value: ${resp.data.summary.total_value_usd:,.2f}")
for protocol in resp.data.protocols:
    print(f"  {protocol.protocol_name}: ${protocol.total_value_usd:,.2f}")

# Check credits remaining
print(f"Credits remaining: {resp.rate_limit.credits_remaining}")

client.close()
