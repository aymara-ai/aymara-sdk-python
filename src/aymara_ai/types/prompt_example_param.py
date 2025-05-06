# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PromptExampleParam"]


class PromptExampleParam(TypedDict, total=False):
    content: Required[str]
    """Content of the example prompt."""

    example_uuid: Optional[str]
    """Unique identifier for the example, if any."""

    explanation: Optional[str]
    """Explanation for the example, if any."""

    type: Literal["good", "bad"]
    """Type of the example (e.g., GOOD, BAD)."""
