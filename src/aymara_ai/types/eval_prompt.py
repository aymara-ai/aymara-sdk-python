# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["EvalPrompt"]


class EvalPrompt(BaseModel):
    content: str
    """Content of the prompt."""

    prompt_uuid: str
    """Unique identifier for the prompt."""

    category: Optional[str] = None
    """Category of the prompt, if any."""

    thread_uuid: Optional[str] = None
    """Unique identifier for the thread, if any."""

    turn_number: Optional[int] = None
    """Turn number in the conversation (default: 1)."""
