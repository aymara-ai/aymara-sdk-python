# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared.status import Status
from .shared.content_type import ContentType
from .prompt_example_param import PromptExampleParam
from .shared_params.file_reference import FileReference
from .shared_params.agent_instructions import AgentInstructions
from .shared_params.workflow_instructions import WorkflowInstructions

__all__ = ["EvalCreateParams", "AIInstructions", "GroundTruth"]


class EvalCreateParams(TypedDict, total=False):
    ai_description: Required[str]
    """Description of the AI under evaluation."""

    eval_type: Required[str]
    """Type of the eval (safety, accuracy, etc.)"""

    ai_instructions: Optional[AIInstructions]
    """Instructions the AI should follow.

    String for normal evals, AgentInstructions for single-agent evals,
    WorkflowInstructions for multi-agent workflows.
    """

    created_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Timestamp when the eval was created."""

    created_by: Optional[str]
    """Name of the user who created the evaluation."""

    eval_instructions: Optional[str]
    """Additional instructions for the eval, if any."""

    eval_uuid: Optional[str]
    """Unique identifier for the evaluation."""

    ground_truth: Optional[GroundTruth]
    """Ground truth data or reference file, if any."""

    is_jailbreak: bool
    """Indicates if the eval is a jailbreak test."""

    is_sandbox: bool
    """Indicates if the eval results are sandboxed."""

    language: Optional[str]
    """Language code for the eval (default: "en")."""

    modality: ContentType
    """Content type for AI interactions."""

    name: Optional[str]
    """Name of the evaluation."""

    num_prompts: Optional[int]
    """Number of prompts/questions in the eval (default: 50)."""

    prompt_examples: Optional[Iterable[PromptExampleParam]]
    """List of example prompts for the eval."""

    status: Optional[Status]
    """Resource status."""

    task_timeout: Optional[int]
    """Custom timeout in seconds for task execution warning threshold.

    If not set, defaults to 180 seconds.
    """

    updated_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Timestamp when the eval was last updated."""

    workspace_uuid: Optional[str]
    """UUID of the associated workspace, if any."""


AIInstructions: TypeAlias = Union[str, AgentInstructions, WorkflowInstructions]

GroundTruth: TypeAlias = Union[str, FileReference]
