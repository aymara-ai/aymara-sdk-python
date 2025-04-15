# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .eval_prompt import EvalPrompt
from .content_type import ContentType

__all__ = ["EvalResponse"]


class EvalResponse(BaseModel):
    content: str

    prompt: EvalPrompt

    prompt_uuid: str

    response_uuid: str

    ai_refused: Optional[bool] = None

    confidence: Optional[float] = None

    content_type: Optional[ContentType] = None
    """Content type for AI interactions."""

    exclude_from_scoring: Optional[bool] = None

    explanation: Optional[str] = None

    generate_prompt: Optional[bool] = None

    is_passed: Optional[bool] = None

    next_prompt: Optional[EvalPrompt] = None

    thread_uuid: Optional[str] = None

    turn_number: Optional[int] = None
