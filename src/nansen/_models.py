from __future__ import annotations

from pydantic import BaseModel as _PydanticBaseModel
from pydantic import ConfigDict


class BaseModel(_PydanticBaseModel):
    """Base model for all Nansen response types.

    Uses ``extra="allow"`` so that new fields added by the API
    won't break existing SDK versions.
    """

    model_config = ConfigDict(extra="allow")
