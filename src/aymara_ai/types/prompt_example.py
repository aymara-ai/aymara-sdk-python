# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PromptExample"]


class PromptExample(BaseModel):
    content: str
    """Content of the example prompt."""

    example_uuid: Optional[str] = None
    """Unique identifier for the example, if any."""

    explanation: Optional[str] = None
    """Explanation for the example, if any."""

    type: Optional[Literal["good", "bad"]] = None
    """Type of the example (e.g., GOOD, BAD)."""
