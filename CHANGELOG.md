# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive docstrings for all public methods

### Changed
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
- Poetry for dependency management
- httpx for HTTP client (sync + async)

[Unreleased]: https://github.com/nansen-ai/nansen-python-sdk/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/nansen-ai/nansen-python-sdk/releases/tag/v0.1.0
