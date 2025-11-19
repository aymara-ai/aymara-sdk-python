# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .shared_params.file_reference import FileReference
from .shared_params.agent_instructions import AgentInstructions
from .shared_params.workflow_instructions import WorkflowInstructions

__all__ = ["EvalUpdateParams", "AIInstructions", "GroundTruth", "PromptCreate", "PromptUpdate"]


class EvalUpdateParams(TypedDict, total=False):
    workspace_uuid: str

    ai_description: Optional[str]
    """New description of the AI under evaluation."""

    ai_instructions: Optional[AIInstructions]
    """New instructions the AI should follow.

    String for normal evals, AgentInstructions for single-agent evals,
    WorkflowInstructions for multi-agent workflows.
    """

    eval_instructions: Optional[str]
    """New additional instructions for the eval."""

    ground_truth: Optional[GroundTruth]
    """New ground truth data or reference file."""

    name: Optional[str]
    """New name for the evaluation."""

    prompt_creates: Optional[Iterable[PromptCreate]]
    """List of new prompts to add."""

    prompt_updates: Optional[Iterable[PromptUpdate]]
    """List of prompt updates to apply."""


AIInstructions: TypeAlias = Union[str, AgentInstructions, WorkflowInstructions]

GroundTruth: TypeAlias = Union[str, FileReference]


class PromptCreate(TypedDict, total=False):
    content: Required[str]
    """Content of the new prompt."""

    category: Optional[str]
    """Category of the new prompt."""


class PromptUpdate(TypedDict, total=False):
    prompt_uuid: Required[str]
    """UUID of the prompt to update or delete."""

    action: str
    """Action to perform: 'update' or 'delete'."""

    category: Optional[str]
    """New category for the prompt (if updating)."""

    content: Optional[str]
    """New content for the prompt (if updating)."""
