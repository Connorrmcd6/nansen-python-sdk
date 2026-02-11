from __future__ import annotations

from typing import Union

from typing_extensions import Literal


class _NotGiven:
    """Sentinel class to distinguish 'not provided' from None."""

    _instance: _NotGiven | None = None

    def __new__(cls) -> _NotGiven:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __repr__(self) -> str:
        return "NOT_GIVEN"

    def __bool__(self) -> bool:
        return False


NOT_GIVEN = _NotGiven()
NotGiven = _NotGiven

# fmt: off
Chain = Literal[
    "arbitrum", "avalanche", "base", "bitcoin", "bnb", "ethereum",
    "hyperevm", "iotaevm", "linea", "mantle", "monad", "near",
    "optimism", "plasma", "polygon", "ronin", "scroll", "sei",
    "solana", "sonic", "starknet", "sui", "ton", "tron",
]
# fmt: on

SmartMoneyLabel = Literal[
    "smart_money",
    "fund",
    "whale",
    "institutional",
]

SortDirection = Literal["asc", "desc"]

Timeframe = Literal["5m", "10m", "1h", "6h", "24h", "7d", "30d"]

HeaderTypes = dict[str, str]
QueryTypes = dict[str, Union[str, int, float, bool, None]]
BodyTypes = dict[str, object]
