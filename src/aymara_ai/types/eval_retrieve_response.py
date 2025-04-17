# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .status import Status
from .._models import BaseModel
from .content_type import ContentType
from .example_type import ExampleType

__all__ = ["EvalRetrieveResponse", "PromptExample"]


class PromptExample(BaseModel):
    content: str

    explanation: Optional[str] = None

    type: Optional[ExampleType] = None


class EvalRetrieveResponse(BaseModel):
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

    prompt_examples: Optional[List[PromptExample]] = None

    workspace_uuid: Optional[str] = None
