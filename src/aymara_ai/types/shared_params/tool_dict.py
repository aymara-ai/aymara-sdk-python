# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ToolDict"]


class ToolDictTyped(TypedDict, total=False):
    value: Required[object]

    type: Literal["dict"]


ToolDict: TypeAlias = Union[ToolDictTyped, Dict[str, object]]
