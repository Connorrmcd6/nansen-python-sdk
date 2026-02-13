# CLAUDE.md

This is the Nansen Python SDK — a typed Python client for the [Nansen](https://docs.nansen.ai/) blockchain analytics API.

## Project Structure

```
src/nansen/
  _base_client.py   — Sync/async HTTP clients (httpx), retry logic, response parsing
  _client.py        — Nansen / AsyncNansen top-level client classes
  _types.py         — NOT_GIVEN sentinel, type aliases (Chain, Timeframe, etc.)
  _pagination.py    — SyncPage / AsyncPage with auto-pagination
  _exceptions.py    — Exception hierarchy (NansenError -> APIError -> specific errors)
  _response.py      — APIResponse wrapper with rate limit info
  _models.py        — BaseModel (pydantic v2)
  resources/        — API resource classes (one file per resource group)
    _base.py        — SyncAPIResource / AsyncAPIResource with _strip_not_given()
    tgm.py          — Token God Mode endpoints (token_screener, holders, flows, etc.)
    smart_money.py  — Smart Money endpoints (netflow, holdings, dex_trades, etc.)
    portfolio.py    — Portfolio endpoints (defi_holdings)
    points.py       — Points leaderboard (public, no auth)
    profiler/       — Profiler endpoints (pnl, perp, address sub-resource)
  types/            — Pydantic response models (one file per resource group)
examples/           — Runnable scripts for every endpoint (try_*.py)
tests/              — pytest test suite with respx mocks
```

## Key Patterns

- **NOT_GIVEN sentinel**: Optional params default to `NOT_GIVEN` (not `None`). `_strip_not_given()` in `resources/_base.py` removes these before sending, so `None` can be a valid user-supplied value.
- **Sync/async mirroring**: Every resource has both a sync class (`TGM`) and an async class (`AsyncTGM`) with identical method signatures. Both must be updated together.
- **Pagination**: Paginated endpoints return `SyncPage[T]` / `AsyncPage[T]`. These support `__iter__` / `__aiter__` for auto-pagination across pages.
- **Response models**: All response models live in `src/nansen/types/` and extend `BaseModel` (pydantic v2). Every field is `Optional` with `None` default.

## Commands

```bash
poetry install              # Install dependencies
poetry run pytest           # Run all tests
poetry run ruff check .     # Lint
poetry run mypy src/        # Type check
```

## Adding a New Endpoint

1. Add the response model in `src/nansen/types/<resource>.py`
2. Add the method to both sync and async classes in `src/nansen/resources/<resource>.py`
3. Export new types from `src/nansen/__init__.py` if public
4. Add a test in `tests/test_resources/` using `respx` mocks
5. Add a `try_*.py` example in `examples/`

## Examples

The `examples/` directory has a runnable `try_*.py` script for every SDK endpoint. Each requires `NANSEN_API_KEY` set as an env var (except `try_points.py`):

```bash
export NANSEN_API_KEY="your-key"
poetry run python examples/try_token_screener.py
```

## Conventions

- Python 3.10+ compatibility (no `X | Y` unions in runtime code — use `from __future__ import annotations`)
- Ruff for linting/formatting (line length 100)
- Strict mypy with pydantic plugin
- Use `timezone.utc` for UTC datetimes (not deprecated `datetime.utcnow()`)

## Versioning

Follow [semantic versioning](https://semver.org/): **MAJOR.MINOR.PATCH**

Version is managed in `pyproject.toml` (line 3). When making changes that warrant a version bump:

1. **Suggest the appropriate version bump** based on the changes made
2. **Ask for user approval** before updating `pyproject.toml`

### Version Bump Rules

- **MAJOR (x.0.0)**: Breaking changes
  - Removed or renamed public methods/parameters
  - Changed method signatures (removed parameters, changed parameter order)
  - Dropped Python version support
  - Changed response model fields (removed/renamed)

- **MINOR (0.x.0)**: New features (backward compatible)
  - New endpoints/methods added
  - New optional parameters added
  - New response model types added
  - New convenience features

- **PATCH (0.0.x)**: Bug fixes and non-breaking changes
  - Bug fixes
  - Documentation improvements
  - Internal refactoring (no public API changes)
  - Dependency updates (non-breaking)

**Note**: While in `0.x.x`, the API is considered unstable and breaking changes may occur in MINOR versions.
