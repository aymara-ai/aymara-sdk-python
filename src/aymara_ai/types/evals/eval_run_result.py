# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..eval import Eval
from ..._models import BaseModel
from ..eval_prompt import EvalPrompt
from ..shared.status import Status
from ..shared.content_type import ContentType

__all__ = ["EvalRunResult", "Response", "ResponseContent", "ResponseContentFileReference"]


class ResponseContentFileReference(BaseModel):
    remote_file_path: Optional[str] = None


ResponseContent: TypeAlias = Union[str, ResponseContentFileReference, None]


class Response(BaseModel):
    prompt_uuid: str

    ai_refused: Optional[bool] = None

    confidence: Optional[float] = None

    content: Optional[ResponseContent] = None

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


class EvalRunResult(BaseModel):
    created_at: datetime

    eval_run_uuid: str

    eval_uuid: str

    status: Status
    """Resource status."""

    updated_at: datetime

    ai_description: Optional[str] = None

    evaluation: Optional[Eval] = None
    """Schema for configuring an Eval based on a eval_type."""

    name: Optional[str] = None

    num_prompts: Optional[int] = None

    num_responses_scored: Optional[int] = None

    pass_rate: Optional[float] = None

    responses: Optional[List[Response]] = None

    workspace_uuid: Optional[str] = None
