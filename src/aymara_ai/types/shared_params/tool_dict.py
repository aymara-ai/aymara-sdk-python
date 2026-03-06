# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolDict"]


class ToolDict(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Container for a tool dictionary"""

    value: Required[object]

    type: Literal["dict"]
