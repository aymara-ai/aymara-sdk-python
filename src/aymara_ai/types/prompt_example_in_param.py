# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .example_type import ExampleType

__all__ = ["PromptExampleInParam"]


class PromptExampleInParam(TypedDict, total=False):
    content: Required[str]

    explanation: Optional[str]

    type: ExampleType
