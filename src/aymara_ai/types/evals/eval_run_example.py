# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EvalRunExample"]


class EvalRunExample(BaseModel):
    prompt: str
    """Prompt text for the example."""

    response: str
    """Expected response for the example."""

    type: Literal["pass", "fail"]
    """Type of the example: "pass" or "fail"."""

    example_uuid: Optional[str] = None
    """Unique identifier for the example, if any."""

    explanation: Optional[str] = None
    """Explanation for the example, if any."""
