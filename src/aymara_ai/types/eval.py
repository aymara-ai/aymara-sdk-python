# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .status import Status
from .._models import BaseModel
from .content_type import ContentType
from .prompt_example_in import PromptExampleIn

__all__ = ["Eval"]


class Eval(BaseModel):
    ai_description: str

    eval_type: str

    eval_uuid: str

    name: str

    ai_instructions: Optional[str] = None

    created_at: Optional[datetime] = None

    eval_instructions: Optional[str] = None

    is_jailbreak: Optional[bool] = None

    is_sandbox: Optional[bool] = None

    language: Optional[str] = None

    modality: Optional[ContentType] = None
    """Content type for AI interactions."""

    num_prompts: Optional[int] = None

    prompt_examples: Optional[List[PromptExampleIn]] = None

    status: Optional[Status] = None
    """Resource status."""

    updated_at: Optional[datetime] = None

    workspace_uuid: Optional[str] = None
