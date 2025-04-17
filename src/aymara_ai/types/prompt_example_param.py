# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .example_type import ExampleType

__all__ = ["PromptExampleParam"]


class PromptExampleParam(TypedDict, total=False):
    content: Required[str]

    example_uuid: Optional[str]

    explanation: Optional[str]

    type: ExampleType
