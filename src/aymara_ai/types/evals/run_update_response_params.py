# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["RunUpdateResponseParams"]


class RunUpdateResponseParams(TypedDict, total=False):
    eval_run_uuid: Required[str]

    workspace_uuid: str

    confidence: Optional[float]
    """Confidence score for the response."""

    explanation: Optional[str]
    """Explanation for the response."""

    is_passed: Optional[bool]
    """Whether the response passed the evaluation."""
