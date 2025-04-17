# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PromptExampleParam"]


class PromptExampleParam(TypedDict, total=False):
    content: Required[str]

    example_uuid: Optional[str]

    explanation: Optional[str]

    type: Literal["good", "bad"]
