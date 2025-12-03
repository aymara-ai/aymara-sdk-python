# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["RunUpdateResponseParams"]


class RunUpdateResponseParams(TypedDict, total=False):
    eval_run_uuid: Required[str]

    confidence: Required[float]
    """Confidence score between 0 and 1"""

    explanation: Required[str]
    """Explanation for the response."""

    workspace_uuid: str

    is_passed: Optional[bool]
    """Whether the response passed the evaluation."""
