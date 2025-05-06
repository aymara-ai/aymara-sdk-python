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
    """Description of the AI under evaluation."""

    eval_type: str
    """Type of the eval (safety, accuracy, etc.)"""

    ai_instructions: Optional[str] = None
    """Instructions the AI should follow."""

    created_at: Optional[datetime] = None
    """Timestamp when the eval was created."""

    eval_instructions: Optional[str] = None
    """Additional instructions for the eval, if any."""

    eval_uuid: Optional[str] = None
    """Unique identifier for the evaluation."""

    ground_truth: Optional[GroundTruth] = None
    """Ground truth data or reference file, if any."""

    is_jailbreak: Optional[bool] = None
    """Indicates if the eval is a jailbreak test."""

    is_sandbox: Optional[bool] = None
    """Indicates if the eval results are sandboxed."""

    language: Optional[str] = None
    """Language code for the eval (default: "en")."""

    modality: Optional[ContentType] = None
    """Content type for AI interactions."""

    name: Optional[str] = None
    """Name of the evaluation."""

    num_prompts: Optional[int] = None
    """Number of prompts/questions in the eval (default: 50)."""

    prompt_examples: Optional[List[PromptExample]] = None
    """List of example prompts for the eval."""

    status: Optional[Status] = None
    """Resource status."""

    updated_at: Optional[datetime] = None
    """Timestamp when the eval was last updated."""

    workspace_uuid: Optional[str] = None
    """UUID of the associated workspace, if any."""
