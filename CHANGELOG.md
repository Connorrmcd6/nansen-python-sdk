# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1] - 2026-02-13

### Added
- Comprehensive docstrings for all public methods

### Changed
- Migrated from Poetry to uv for dependency management and project tooling
- Switched build backend from poetry-core to hatchling (PEP 621)
- Replaced pre-commit with prek as the hook runner
- Expanded pre-commit hooks: added codespell, yamllint, yamlfmt, trailing-whitespace, end-of-file-fixer, check-merge-conflict, check-toml, check-yaml, check-added-large-files
- Added `"B"` (flake8-bugbear) to ruff lint rules
- Restructured CI from single workflow to reusable workflow pattern (on-pr, on-merge, job-prek, job-test)
- CI now uses `astral-sh/setup-uv@v5` instead of `snok/install-poetry@v1`
- Improved documentation formatting for `order_by` parameters

## [0.1.0] - 2024-02-09

### Added
- Initial release of Nansen Python SDK
- Support for all major Nansen API endpoints:
  - Token God Mode (TGM): token screener, holders, flows, transfers, DCAs, perp screener
  - Smart Money: netflow, holdings, historical holdings, DEX trades, perp trades, DCAs
  - Profiler: PnL summary/detailed, perp positions/trades, address balances/transactions/counterparties/labels, entity search, perp leaderboard
  - Portfolio: DeFi holdings
  - Points: leaderboard (public, no auth required)
- Full sync and async support with identical APIs
- Auto-pagination for all paginated endpoints via `SyncPage`/`AsyncPage`
- Automatic retry logic with exponential backoff for 429/5xx errors
- Comprehensive error handling with typed exceptions
- Rate limit information in all responses
- Type-safe request/response models using Pydantic v2
- 35+ runnable example scripts demonstrating all endpoints
- Full test coverage using pytest and respx mocks
- CI/CD pipeline with automated testing
- Pre-commit hooks for code quality
- Python 3.10+ support

### Development
- Ruff for linting and formatting
- Strict mypy type checking
- uv for dependency management
- httpx for HTTP client (sync + async)

[Unreleased]: https://github.com/nansen-ai/nansen-python-sdk/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/nansen-ai/nansen-python-sdk/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/nansen-ai/nansen-python-sdk/releases/tag/v0.1.0
