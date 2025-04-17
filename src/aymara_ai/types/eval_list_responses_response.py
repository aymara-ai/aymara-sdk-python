# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .eval_prompt import EvalPrompt

__all__ = ["EvalListResponsesResponse"]


class EvalListResponsesResponse(BaseModel):
    content: str

    prompt: EvalPrompt

    prompt_uuid: str

    ai_refused: Optional[bool] = None

    confidence: Optional[float] = None

    content_type: Optional[Literal["text", "image", "audio", "video"]] = None
    """Content type for AI interactions."""

    continue_thread: Optional[bool] = None

    exclude_from_scoring: Optional[bool] = None

    explanation: Optional[str] = None

    is_passed: Optional[bool] = None

    next_prompt: Optional[EvalPrompt] = None

    response_uuid: Optional[str] = None

    thread_uuid: Optional[str] = None

    turn_number: Optional[int] = None
