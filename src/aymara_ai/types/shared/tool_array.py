# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .tool import Tool
from ..._models import BaseModel

__all__ = ["ToolArray"]


class ToolArray(BaseModel):
    """Container for an array of tools"""

    value: List[Tool]

    type: Optional[Literal["array"]] = None
