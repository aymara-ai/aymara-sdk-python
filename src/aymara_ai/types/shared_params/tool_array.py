# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .tool import Tool

__all__ = ["ToolArray"]


class ToolArray(TypedDict, total=False):
    """Container for an array of tools"""

    value: Required[Iterable[Tool]]

    type: Literal["array"]
