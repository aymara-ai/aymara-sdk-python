# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolString"]


class ToolString(TypedDict, total=False):
    """Container for string-based tool instructions"""

    value: Required[str]

    type: Literal["string"]
