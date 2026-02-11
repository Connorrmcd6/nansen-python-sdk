# Nansen Python SDK - Implementation Plan

## Context

Build an open-source Python SDK for the Nansen blockchain analytics API. The SDK follows patterns from best-in-class SDKs (OpenAI, Anthropic, Stripe): dual sync/async clients, typed responses, auto-pagination, retry with backoff, and a clean resource-based API surface.

**API Facts:**
- Base URL: `https://api.nansen.ai/api/v1` (except Points: `https://app.nansen.ai`)
- Auth: `apikey` header (lowercase)
- All endpoints POST with JSON body (except Points: GET, no auth)
- Pagination: `{"page": N, "per_page": N}` in body, response has `is_last_page`
- Rate limits: 20 req/sec, 300 req/min
- ~40 endpoints across 5 resource groups

---

## Project Structure

```
nansen-python-sdk/
├── pyproject.toml
├── README.md
├── LICENSE
├── src/
│   └── nansen/
│       ├── __init__.py              # Public exports
│       ├── _version.py              # __version__ = "0.1.0"
│       ├── _constants.py            # URLs, timeouts, defaults
│       ├── _types.py                # NotGiven sentinel, Chain/Label literals
│       ├── _exceptions.py           # NansenError → APIError → per-status errors
│       ├── _models.py               # BaseModel with extra="allow"
│       ├── _response.py             # APIResponse wrapper, RateLimitInfo
│       ├── _pagination.py           # SyncPage/AsyncPage with auto-iteration
│       ├── _base_client.py          # SyncAPIClient/AsyncAPIClient (httpx, retry)
│       ├── _client.py               # Nansen/AsyncNansen (public entry points)
│       ├── _utils/
│       │   ├── __init__.py
│       │   └── _retry.py            # Backoff calculation
│       ├── resources/
│       │   ├── __init__.py
│       │   ├── _base.py             # SyncAPIResource/AsyncAPIResource
│       │   ├── smart_money.py       # 6 endpoints (netflow, dex_trades, perp_trades, dcas, holdings, historical_holdings)
│       │   ├── profiler/
│       │   │   ├── __init__.py
│       │   │   ├── profiler.py      # pnl_summary, pnl, perp_positions, perp_trades, entity_search, perp_leaderboard
│       │   │   └── address.py       # current_balance, historical_balances, transactions, counterparties, related_wallets, labels
│       │   ├── tgm.py               # 15 endpoints (token_screener, token_information, flow_intel, holders, flows, who_bought_sold, dex_trades, transfers, dcas, pnl_leaderboard, perp_screener, perp_pnl_leaderboard, perp_positions, perp_trades)
│       │   ├── portfolio.py         # defi_holdings
│       │   └── points.py            # leaderboard (GET, no auth, different base URL)
│       ├── types/
│       │   ├── __init__.py
│       │   ├── _shared.py           # DateRange, SortOrder, NumericRangeFilter
│       │   ├── _pagination.py       # PaginationParam TypedDict
│       │   ├── smart_money.py       # Response models
│       │   ├── profiler.py          # Response models
│       │   ├── tgm.py               # Response models (TokenScreenerResponse etc.)
│       │   ├── portfolio.py         # Response models
│       │   └── points.py            # Response models
│       └── py.typed
├── tests/
│   ├── conftest.py
│   ├── test_client.py
│   ├── test_exceptions.py
│   ├── test_pagination.py
│   ├── test_retry.py
│   └── test_resources/
│       ├── test_smart_money.py
│       ├── test_profiler.py
│       ├── test_tgm.py
│       ├── test_portfolio.py
│       └── test_points.py
└── examples/
    ├── basic_usage.py
    ├── async_usage.py
    └── error_handling.py
```

---

## Implementation Phases

### Phase 1: Foundation
Files: `_version.py`, `_constants.py`, `_types.py`, `_exceptions.py`, `_models.py`

- **`_constants.py`**: `DEFAULT_BASE_URL`, `POINTS_BASE_URL`, `DEFAULT_TIMEOUT=60.0`, `DEFAULT_MAX_RETRIES=2`, `INITIAL_RETRY_DELAY=0.5`, `MAX_RETRY_DELAY=8.0`, `API_KEY_ENV_VAR="NANSEN_API_KEY"`
- **`_types.py`**: `NOT_GIVEN` sentinel (distinguishes "not provided" from `None`), `Chain` Literal type (26 chains), `SmartMoneyLabel` Literal, `SortDirection` Literal
- **`_exceptions.py`**: `NansenError` base → `APIError(status_code, message, response, body)` → `BadRequestError(400)`, `AuthenticationError(401)`, `PermissionDeniedError(403)`, `NotFoundError(404)`, `UnprocessableEntityError(422)`, `RateLimitError(429, retry_after)`, `InternalServerError(500)`, `GatewayTimeoutError(504)`. Plus `APIConnectionError` and `APITimeoutError` for network errors.
- **`_models.py`**: Extended Pydantic `BaseModel` with `extra="allow"` (forward-compatible with new API fields)

### Phase 2: HTTP Layer
Files: `_utils/_retry.py`, `_response.py`, `_pagination.py`, `_base_client.py`

- **`_retry.py`**: `calculate_retry_delay(attempt, retry_after_header)` → exponential backoff with jitter. `RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}`
- **`_response.py`**: `RateLimitInfo` dataclass parsed from response headers (`X-Nansen-Credits-Used`, `X-Nansen-Credits-Remaining`, `RateLimit-*`, `X-RateLimit-*`). `APIResponse[T]` wrapper exposing `.data`, `.headers`, `.status_code`, `.rate_limit`
- **`_pagination.py`**: `SyncPage[T]` / `AsyncPage[T]` storing `data: list[T]`, `pagination: PaginationInfo`, plus reference to client/path/body for fetching next pages. `__iter__` auto-paginates across all pages. `iter_pages()` yields page objects. `has_next_page` checks `is_last_page`.
- **`_base_client.py`**: `BaseClient` with shared logic (header building, error mapping, retry decisions). `SyncAPIClient(httpx.Client)` with `_request()` retry loop using `time.sleep`. `AsyncAPIClient(httpx.AsyncClient)` with `_request()` using `asyncio.sleep`. Both support context managers. Both have `_request_page()` that returns `SyncPage`/`AsyncPage`.

### Phase 3: Type Definitions
Files: `types/_shared.py`, `types/_pagination.py`, `types/smart_money.py`, `types/profiler.py`, `types/tgm.py`, `types/portfolio.py`, `types/points.py`

All response models use our `_models.BaseModel` with `extra="allow"` and `Optional` fields defaulting to `None` (forward-compatible). Key models include:
- `HoldingsItem`: chain, token_address, token_symbol, value_usd, holders_count, balance_24h_percent_change
- `TokenScreenerItem`: chain, token_address, token_symbol, market_cap_usd, price_usd, price_change, volume, netflow, etc.
- `DefiHoldingsResponse`: summary (total_value_usd, etc.) + protocols list with token breakdowns
- `PointsLeaderboardEntry`: rank, evm_address, solana_address, points, tier, is_eligible

### Phase 4: Resource Classes
Files: `resources/_base.py`, `resources/smart_money.py`, `resources/profiler/`, `resources/tgm.py`, `resources/portfolio.py`, `resources/points.py`

- **`_base.py`**: `SyncAPIResource` / `AsyncAPIResource` with `_post()`, `_post_page()`, `_get()` helpers
- Each resource class has sync + async variant. Method signatures use keyword-only args with `NOT_GIVEN` defaults.
- Pattern: `client.smart_money.holdings(chains=["ethereum"])` → `SyncPage[HoldingsItem]`
- Pattern: `client.profiler.address.current_balance(address="0x...", chain="ethereum")` → `CurrentBalanceResponse`
- Points is special: `client.points.leaderboard(tier="green")` uses GET, different base URL, no auth

### Phase 5: Client Assembly
Files: `_client.py`, `__init__.py`

- **`_client.py`**: `Nansen(SyncAPIClient)` and `AsyncNansen(AsyncAPIClient)`. API key from param or `NANSEN_API_KEY` env var. Resources via `@cached_property`. `with_raw_response` proxy for accessing headers/credits.
- **`__init__.py`**: Clean public API: `Nansen`, `AsyncNansen`, all exception classes, `SyncPage`, `AsyncPage`, `types` submodule

### Phase 6: Quality & Polish
Files: `pyproject.toml`, `py.typed`, tests, `README.md`, examples

- **pyproject.toml**: hatchling build, Python >=3.9, deps: `httpx>=0.23,<1`, `pydantic>=2,<3`, `typing-extensions>=4.7`, `anyio>=3.5,<5`. Dev deps: pytest, pytest-asyncio, respx, ruff, mypy.
- **Tests**: Use `respx` to mock httpx. Test client init, auth, retry logic (429/5xx retried, 400/401 not), pagination auto-iteration, exception mapping, all resource methods.
- **README**: Install, quick start, sync/async examples, pagination, error handling, credits/rate-limits, full API reference table

---

## Key Design Decisions

1. **`extra="allow"` on all response models** - SDK won't break when API adds new fields
2. **`NOT_GIVEN` sentinel** - Distinguishes "not provided" from explicit `None` (matches OpenAI/Anthropic pattern)
3. **httpx for HTTP** - Native sync+async in one library
4. **Resource hierarchy** - `client.profiler.address.labels()` mirrors API structure
5. **Page-based auto-pagination** - `for item in client.smart_money.holdings(...)` iterates all pages automatically
6. **Retry with jitter** - Exponential backoff (0.5s, 1s, 2s, 4s, 8s cap) with 50-100% jitter, respects Retry-After header

---

## Verification

1. **Unit tests**: `pytest tests/` - all resource methods mocked with respx, retry logic tested with controlled responses
2. **Type checking**: `mypy src/nansen --strict` and `pyright src/nansen`
3. **Lint**: `ruff check src/ tests/`
4. **Manual smoke test** (with real API key): Run `examples/basic_usage.py` against the live API
5. **Package build**: `pip install -e .` and verify imports work
