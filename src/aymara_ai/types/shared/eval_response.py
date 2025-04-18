# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .content_type import ContentType

__all__ = ["EvalResponse"]


class EvalResponse(BaseModel):
    content: str

    prompt_uuid: str

    ai_refused: Optional[bool] = None

    content_type: Optional[ContentType] = None
    """Content type for AI interactions."""

    continue_thread: Optional[bool] = None

    exclude_from_scoring: Optional[bool] = None

    thread_uuid: Optional[str] = None

    turn_number: Optional[int] = None
