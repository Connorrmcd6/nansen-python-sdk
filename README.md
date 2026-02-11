# Nansen Python SDK

Python SDK for the [Nansen](https://docs.nansen.ai/) blockchain analytics API.

## Installation

```bash
poetry add nansen
```

Or with pip:

```bash
pip install nansen
```

### Development

```bash
git clone https://github.com/nansen-ai/nansen-python-sdk.git
cd nansen-python-sdk
poetry install
```

## Quick Start

```python
from nansen import Nansen

client = Nansen(api_key="your-api-key")  # or set NANSEN_API_KEY env var

# Smart Money holdings with auto-pagination
for item in client.smart_money.holdings(chains=["ethereum"]):
    print(f"{item.token_symbol}: ${item.value_usd:,.2f}")

client.close()
```

## Async Support

```python
import asyncio
from nansen import AsyncNansen

async def main():
    async with AsyncNansen() as client:
        page = await client.smart_money.holdings(chains=["ethereum"])
        async for item in page:
            print(item.token_symbol)

asyncio.run(main())
```

## Pagination

All paginated endpoints return `SyncPage` / `AsyncPage` objects that auto-iterate across pages:

```python
# Iterate all items across all pages
for item in client.smart_money.holdings(chains=["ethereum"]):
    print(item.token_symbol)

# Or work with individual pages
page = client.smart_money.holdings(chains=["ethereum"])
print(page.data)          # Current page items
print(page.has_next_page) # Check if more pages exist

for p in page.iter_pages():
    print(f"Page {p.pagination.page}: {len(p.data)} items")
```

## Error Handling

```python
from nansen import Nansen, RateLimitError, AuthenticationError, NansenError

try:
    page = client.smart_money.holdings(chains=["ethereum"])
except AuthenticationError:
    print("Invalid API key")
except RateLimitError as e:
    print(f"Rate limited, retry after {e.retry_after}s")
except NansenError as e:
    print(f"API error: {e}")
```

Exception hierarchy:
- `NansenError` — base
  - `APIError` — HTTP errors (has `.status_code`, `.message`, `.body`)
    - `BadRequestError` (400)
    - `AuthenticationError` (401)
    - `PermissionDeniedError` (403)
    - `NotFoundError` (404)
    - `UnprocessableEntityError` (422)
    - `RateLimitError` (429) — has `.retry_after`
    - `InternalServerError` (500)
    - `GatewayTimeoutError` (504)
  - `APIConnectionError` — network errors
    - `APITimeoutError`

## Credits & Rate Limits

Every response includes rate limit and credit info:

```python
resp = client.portfolio.defi_holdings(wallet_address="0x...")
print(resp.rate_limit.credits_used)
print(resp.rate_limit.credits_remaining)
print(resp.rate_limit.remaining_second)
print(resp.rate_limit.remaining_minute)
```

The SDK automatically retries on 429/5xx errors with exponential backoff (configurable):

```python
client = Nansen(api_key="...", max_retries=3, timeout=30.0)
```

## API Reference

### Smart Money (`client.smart_money`)

| Method | Description |
|--------|-------------|
| `.netflow(chains=...)` | Net capital flows |
| `.dex_trades(chains=...)` | DEX trading activity |
| `.perp_trades()` | Perpetual trades (Hyperliquid) |
| `.dcas()` | DCA patterns (Jupiter/Solana) |
| `.holdings(chains=...)` | Current holdings |
| `.historical_holdings(date_range=..., chains=...)` | Historical holdings |

### Profiler (`client.profiler`)

| Method | Description |
|--------|-------------|
| `.address.current_balance(chain=..., address=...)` | Token balances |
| `.address.historical_balances(chain=..., date=...)` | Historical balances |
| `.address.transactions(address=..., chain=..., date=...)` | Transaction history |
| `.address.counterparties(chain=..., date=...)` | Top counterparties |
| `.address.related_wallets(address=..., chain=...)` | Related wallets |
| `.address.labels(chain=..., address=...)` | Address labels (beta) |
| `.pnl_summary(chain=..., date=...)` | PnL summary |
| `.pnl(chain=...)` | Detailed PnL per token |
| `.perp_positions(address=...)` | Open perp positions |
| `.perp_trades(address=..., date=...)` | Perp trade history |
| `.entity_search(search_query=...)` | Search entity names |
| `.perp_leaderboard(date=...)` | Perp leaderboard |

### Token God Mode (`client.tgm`)

| Method | Description |
|--------|-------------|
| `.token_screener(chains=...)` | Token screener |
| `.token_information(chain=..., token_address=..., timeframe=...)` | Token details |
| `.flow_intel(chain=..., token_address=...)` | Flow intelligence |
| `.holders(chain=..., token_address=...)` | Token holders |
| `.flows(chain=..., token_address=..., date=...)` | Token flows |
| `.who_bought_sold(chain=..., token_address=..., date=...)` | Buyer/seller analysis |
| `.dex_trades(chain=..., token_address=..., date=...)` | DEX trades for token |
| `.transfers(chain=..., token_address=..., date=...)` | Token transfers |
| `.dcas(token_address=...)` | Jupiter DCAs |
| `.pnl_leaderboard(chain=..., token_address=..., date=...)` | PnL leaderboard |
| `.perp_screener(date=...)` | Perp screener |
| `.perp_pnl_leaderboard(token_symbol=..., date=...)` | Perp PnL leaderboard |
| `.perp_positions(token_symbol=...)` | Perp positions |
| `.perp_trades(token_symbol=..., date=...)` | Perp trades |

### Portfolio (`client.portfolio`)

| Method | Description |
|--------|-------------|
| `.defi_holdings(wallet_address=...)` | DeFi holdings |

### Points (`client.points`)

| Method | Description |
|--------|-------------|
| `.leaderboard(tier=...)` | Points leaderboard (public, no auth) |

## Examples

The `examples/` directory contains runnable scripts for every SDK endpoint. Each `try_*.py` script demonstrates a single endpoint with sample output formatting.

```bash
export NANSEN_API_KEY="your-key"
poetry run python examples/try_token_screener.py
poetry run python examples/try_smart_money_netflow.py
poetry run python examples/try_address_balance.py
# ... etc
```

| Script | Endpoint |
|--------|----------|
| `try_token_screener.py` | Token screener |
| `try_token_information.py` | Token details |
| `try_flow_intel.py` | Flow intelligence |
| `try_holders.py` | Token holders |
| `try_flows.py` | Token flows |
| `try_who_bought_sold.py` | Buyer/seller analysis |
| `try_tgm_dex_trades.py` | DEX trades (token) |
| `try_transfers.py` | Token transfers |
| `try_tgm_dcas.py` | Jupiter DCAs |
| `try_pnl_leaderboard.py` | PnL leaderboard |
| `try_perp_screener.py` | Perp screener |
| `try_perp_pnl_leaderboard.py` | Perp PnL leaderboard |
| `try_tgm_perp_positions.py` | Perp positions (token) |
| `try_tgm_perp_trades.py` | Perp trades (token) |
| `try_smart_money.py` | Smart Money holdings |
| `try_smart_money_netflow.py` | Smart Money netflow |
| `try_smart_money_dex_trades.py` | Smart Money DEX trades |
| `try_smart_money_perp_trades.py` | Smart Money perp trades |
| `try_smart_money_dcas.py` | Smart Money DCAs |
| `try_smart_money_historical_holdings.py` | Smart Money historical holdings |
| `try_portfolio.py` | DeFi holdings |
| `try_entity_search.py` | Entity search |
| `try_profiler_pnl.py` | PnL summary + detailed |
| `try_profiler_perp.py` | Perp positions + trades (profiler) |
| `try_perp_leaderboard.py` | Perp leaderboard |
| `try_address_balance.py` | Address current balance |
| `try_address_historical_balances.py` | Address historical balances |
| `try_address_transactions.py` | Address transactions |
| `try_address_counterparties.py` | Address counterparties |
| `try_address_related_wallets.py` | Address related wallets |
| `try_address_labels.py` | Address labels (beta) |
| `try_points.py` | Points leaderboard (no auth) |

See also `basic_usage.py`, `async_usage.py`, and `error_handling.py` for general SDK usage patterns.

## Requirements

- Python 3.9+
- httpx
- pydantic v2
- anyio
