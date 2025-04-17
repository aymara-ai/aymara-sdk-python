# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .status import Status
from .._models import BaseModel
from .content_type import ContentType
from .example_type import ExampleType

__all__ = ["EvalGetRunResponse", "Evaluation", "EvaluationPromptExample"]


class EvaluationPromptExample(BaseModel):
    content: str

    explanation: Optional[str] = None

    type: Optional[ExampleType] = None


class Evaluation(BaseModel):
    ai_description: str

    created_at: datetime

    eval_type: str

    eval_uuid: str

    name: str

    status: Status
    """Resource status."""

    updated_at: datetime

    ai_instructions: Optional[str] = None

    eval_instructions: Optional[str] = None

    is_jailbreak: Optional[bool] = None

    is_sandbox: Optional[bool] = None

    language: Optional[str] = None

    modality: Optional[ContentType] = None
    """Content type for AI interactions."""

    num_prompts: Optional[int] = None

    prompt_examples: Optional[List[EvaluationPromptExample]] = None

    workspace_uuid: Optional[str] = None


class EvalGetRunResponse(BaseModel):
    created_at: datetime

    eval_run_uuid: str

    status: Status
    """Resource status."""

    updated_at: datetime

    ai_description: Optional[str] = None

    evaluation: Optional[Evaluation] = None

    num_prompts: Optional[int] = None

    num_responses_scored: Optional[int] = None

    pass_rate: Optional[float] = None

    workspace_uuid: Optional[str] = None
