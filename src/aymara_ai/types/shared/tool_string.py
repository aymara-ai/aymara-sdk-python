# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ToolString"]


class ToolString(BaseModel):
    value: str

    type: Optional[Literal["string"]] = None
