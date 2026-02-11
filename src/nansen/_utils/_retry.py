from __future__ import annotations

import random

from nansen._constants import INITIAL_RETRY_DELAY, MAX_RETRY_DELAY

RETRYABLE_STATUS_CODES: frozenset[int] = frozenset({429, 500, 502, 503, 504})


def calculate_retry_delay(
    attempt: int,
    retry_after_header: str | None = None,
) -> float:
    """Return the delay in seconds before the next retry.

    Uses exponential backoff with jitter.  If the server sent a
    ``Retry-After`` header its value is used as a *minimum*.
    """
    # Exponential backoff: 0.5, 1, 2, 4, 8 ...
    delay: float = INITIAL_RETRY_DELAY * (2**attempt)
    delay = min(delay, MAX_RETRY_DELAY)

    # Add jitter: random value in [delay * 0.5, delay]
    delay = delay * (0.5 + random.random() * 0.5)  # noqa: S311

    # Respect Retry-After header if present
    if retry_after_header is not None:
        try:
            retry_after = float(retry_after_header)
            delay = max(delay, retry_after)
        except (ValueError, TypeError):
            pass

    return delay
