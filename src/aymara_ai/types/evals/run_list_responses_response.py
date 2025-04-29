# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from ..eval_prompt import EvalPrompt
from ..file_reference import FileReference
from ..shared.content_type import ContentType

__all__ = ["RunListResponsesResponse", "Content"]

Content: TypeAlias = Union[str, FileReference, None]


class RunListResponsesResponse(BaseModel):
    prompt_uuid: str

    ai_refused: Optional[bool] = None

    confidence: Optional[float] = None

    content: Optional[Content] = None

    content_type: Optional[ContentType] = None
    """Content type for AI interactions."""

    continue_thread: Optional[bool] = None

    exclude_from_scoring: Optional[bool] = None

    explanation: Optional[str] = None

    is_passed: Optional[bool] = None

    next_prompt: Optional[EvalPrompt] = None

    response_uuid: Optional[str] = None

    thread_uuid: Optional[str] = None

    turn_number: Optional[int] = None
