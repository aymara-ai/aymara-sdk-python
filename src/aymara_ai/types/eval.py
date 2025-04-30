# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel
from .shared.status import Status
from .prompt_example import PromptExample
from .shared.content_type import ContentType
from .shared.file_reference import FileReference

__all__ = ["Eval", "GroundTruth"]

GroundTruth: TypeAlias = Union[str, FileReference, None]


class Eval(BaseModel):
    ai_description: str

    eval_type: str

    name: str

    ai_instructions: Optional[str] = None

    created_at: Optional[datetime] = None

    eval_instructions: Optional[str] = None

    eval_uuid: Optional[str] = None

    ground_truth: Optional[GroundTruth] = None

    is_jailbreak: Optional[bool] = None

    is_sandbox: Optional[bool] = None

    language: Optional[str] = None

    modality: Optional[ContentType] = None
    """Content type for AI interactions."""

    num_prompts: Optional[int] = None

    prompt_examples: Optional[List[PromptExample]] = None

    status: Optional[Status] = None
    """Resource status."""

    updated_at: Optional[datetime] = None

    workspace_uuid: Optional[str] = None
