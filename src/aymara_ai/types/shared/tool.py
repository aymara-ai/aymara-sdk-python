# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from ..._models import BaseModel

__all__ = ["Tool"]


class Tool(BaseModel):
    """Tools the agent has access to."""

    content: Union[str, object, None] = None

    name: str
