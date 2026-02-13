# Contributing to Nansen Python SDK

Thank you for considering contributing to the Nansen Python SDK! This document provides guidelines and instructions for contributing.

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/nansen-ai/nansen-python-sdk.git
   cd nansen-python-sdk
   ```

2. **Install dependencies**
   ```bash
   poetry install
   ```

3. **Set up pre-commit hooks**
   ```bash
   poetry run pre-commit install
   ```

## Running Tests

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=src/nansen

# Run specific test file
poetry run pytest tests/test_resources/test_tgm.py
```

## Code Quality

Before submitting a PR, ensure your code passes all checks:

```bash
# Lint with Ruff
poetry run ruff check .

# Format with Ruff
poetry run ruff format .

# Type check with mypy
poetry run mypy src/
```

Pre-commit hooks will automatically run these checks, but you can run them manually as well.

## Code Style

- **Python 3.10+ compatibility**: Use `from __future__ import annotations` instead of `X | Y` unions in runtime code
- **Line length**: 100 characters (enforced by Ruff)
- **Type hints**: All public methods must have type hints
- **Docstrings**: Use Google-style docstrings for public methods
- **Imports**: Sorted by Ruff (use `ruff check --fix` to auto-sort)

## Project Conventions

- **NOT_GIVEN sentinel**: Optional params default to `NOT_GIVEN` (not `None`)
- **Sync/async mirroring**: Every resource has both sync and async classes with identical signatures
- **Response models**: All response models extend `BaseModel` (pydantic v2) with `Optional` fields
- **Pagination**: Use `SyncPage[T]` / `AsyncPage[T]` for paginated endpoints

## Adding a New Endpoint

1. **Add response model** in `src/nansen/types/<resource>.py`
2. **Add method** to both sync and async classes in `src/nansen/resources/<resource>.py`
3. **Export types** from `src/nansen/__init__.py` if public
4. **Add test** in `tests/test_resources/` using `respx` mocks
5. **Add example** as `examples/try_*.py` script
6. **Update CHANGELOG.md** under `[Unreleased]`

## Pull Request Process

1. **Create a branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the code style guidelines

3. **Add tests** for any new functionality

4. **Update documentation**:
   - Add docstrings to new methods
   - Update README.md if adding user-facing features
   - Add entry to CHANGELOG.md under `[Unreleased]`

5. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add support for X endpoint"
   ```

   Use conventional commit prefixes:
   - `feat:` — new feature
   - `fix:` — bug fix
   - `docs:` — documentation changes
   - `test:` — test additions/changes
   - `refactor:` — code refactoring
   - `chore:` — maintenance tasks

6. **Push and create PR**:
   ```bash
   git push -u origin feature/your-feature-name
   ```

   Then open a pull request on GitHub with:
   - Clear description of changes
   - Reference any related issues
   - Screenshots/examples if applicable

7. **Respond to feedback**: Address any review comments

## Testing Your Changes

If you've added a new endpoint, test it manually:

```bash
export NANSEN_API_KEY="your-key"
poetry run python examples/try_your_endpoint.py
```

## Questions?

- Check existing [issues](https://github.com/nansen-ai/nansen-python-sdk/issues)
- Open a new issue for bugs or feature requests
- Reach out to maintainers for guidance

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
