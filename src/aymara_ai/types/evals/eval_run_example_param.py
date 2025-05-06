# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["EvalRunExampleParam"]


class EvalRunExampleParam(TypedDict, total=False):
    prompt: Required[str]
    """Prompt text for the example."""

    response: Required[str]
    """Expected response for the example."""

    type: Required[Literal["pass", "fail"]]
    """Type of the example: "pass" or "fail"."""

    example_uuid: Optional[str]
    """Unique identifier for the example, if any."""

    explanation: Optional[str]
    """Explanation for the example, if any."""
