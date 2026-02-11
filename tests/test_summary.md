# Test Coverage Summary

## Overview

The test suite covers **core SDK infrastructure** comprehensively and **33 out of 36 endpoint methods** across all resource groups. All tests use `respx` mocks (no live API calls) and exercise the sync client paths.

## Core Infrastructure

| File | What it covers |
|---|---|
| `test_client.py` | Client init (API key from param, env, missing), header building, resource access, cached properties |
| `test_exceptions.py` | All 8 HTTP error types (400, 401, 403, 404, 422, 429, 500, 504), error body parsing |
| `test_pagination.py` | Auto-pagination across pages, `iter_pages()`, `has_next_page` |
| `test_retry.py` | Exponential backoff, jitter, max delay cap, retry-after header, retry on 429/500, no retry on 400 |

## Endpoint Coverage by Resource

### TGM — 14/14 tested

`token_screener`, `token_information`, `flow_intel`, `holders`, `flows`, `who_bought_sold`, `dex_trades`, `transfers`, `dcas`, `pnl_leaderboard`, `perp_screener`, `perp_pnl_leaderboard`, `perp_positions`, `perp_trades`

### SmartMoney — 6/6 tested

`netflow`, `dex_trades`, `perp_trades`, `dcas`, `holdings`, `historical_holdings`

### Portfolio — 1/1 tested

`defi_holdings`

### Points — 1/1 tested

`leaderboard`

### Profiler — 4/6 tested

| Method | Tested | Notes |
|---|---|---|
| `pnl_summary` | Yes | |
| `pnl` | Yes | |
| `entity_search` | Yes | |
| `perp_leaderboard` | Yes | |
| `perp_positions` | **No** | Standard `_post` call; low risk but untested |
| `perp_trades` | **No** | Standard `_post_page` call; low risk but untested |

### Profiler > Address — 5/6 tested

| Method | Tested | Notes |
|---|---|---|
| `current_balance` | Yes | |
| `historical_balances` | Yes | |
| `transactions` | Yes | |
| `counterparties` | Yes | |
| `related_wallets` | Yes | |
| `labels` | **No** | Beta endpoint — uses `/api/beta` base path, wraps params in a `"parameters"` key, and manually calls `TypeAdapter` instead of going through the standard `_post` helper. Structurally different from every other method. |

## Why the 3 Endpoints Are Untested

### `Profiler.perp_positions` and `Profiler.perp_trades`

These two methods follow the same `_post` / `_post_page` patterns already exercised by the other Profiler tests (`pnl_summary`, `pnl`, etc.). They were likely skipped because they don't introduce any new code paths — the underlying HTTP call, `NOT_GIVEN` stripping, and response parsing are identical to what's already covered. Adding tests would improve completeness but wouldn't exercise new logic.

### `Address.labels`

This is the most meaningful gap. Unlike every other endpoint, `labels`:

- Hits `/api/beta` instead of `/api/v1`
- Manually constructs a `base_url` override (`self._client.base_url.replace("/api/v1", "/api/beta")`)
- Wraps parameters inside a `"parameters"` key in the request body
- Bypasses the standard `_post` helper and calls `self._client._request` directly
- Uses `TypeAdapter(list[AddressLabelItem])` to parse the response instead of the normal model-based flow

Because it deviates from the standard patterns, it's the one untested method that carries real risk of silently breaking. A test here would catch regressions in the beta base-path logic and the manual response parsing.
