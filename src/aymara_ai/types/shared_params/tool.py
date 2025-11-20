# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = ["Tool"]


class Tool(TypedDict, total=False):
    content: Required[Union[str, object, None]]

    name: Required[str]
