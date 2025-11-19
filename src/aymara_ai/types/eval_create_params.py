# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared.status import Status
from .shared.content_type import ContentType
from .prompt_example_param import PromptExampleParam
from .shared_params.file_reference import FileReference

__all__ = [
    "EvalCreateParams",
    "AIInstructions",
    "AIInstructionsAgentInstructions",
    "AIInstructionsAgentInstructionsTools",
    "AIInstructionsAgentInstructionsToolsToolArray",
    "AIInstructionsAgentInstructionsToolsToolArrayValue",
    "AIInstructionsAgentInstructionsToolsToolDict",
    "AIInstructionsAgentInstructionsToolsToolString",
    "AIInstructionsWorkflowInstructions",
    "AIInstructionsWorkflowInstructionsInstruction",
    "AIInstructionsWorkflowInstructionsInstructionTools",
    "AIInstructionsWorkflowInstructionsInstructionToolsToolArray",
    "AIInstructionsWorkflowInstructionsInstructionToolsToolArrayValue",
    "AIInstructionsWorkflowInstructionsInstructionToolsToolDict",
    "AIInstructionsWorkflowInstructionsInstructionToolsToolString",
    "GroundTruth",
]


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

    updated_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Timestamp when the eval was last updated."""

    workspace_uuid: Optional[str]
    """UUID of the associated workspace, if any."""


class AIInstructionsAgentInstructionsToolsToolArrayValue(TypedDict, total=False):
    id: Required[str]

    content: Required[Union[str, object, None]]

    name: Required[str]


class AIInstructionsAgentInstructionsToolsToolArray(TypedDict, total=False):
    value: Required[Iterable[AIInstructionsAgentInstructionsToolsToolArrayValue]]

    type: Literal["array"]


class AIInstructionsAgentInstructionsToolsToolDictTyped(TypedDict, total=False):
    value: Required[object]

    type: Literal["dict"]


AIInstructionsAgentInstructionsToolsToolDict: TypeAlias = Union[
    AIInstructionsAgentInstructionsToolsToolDictTyped, Dict[str, object]
]


class AIInstructionsAgentInstructionsToolsToolString(TypedDict, total=False):
    value: Required[str]

    type: Literal["string"]


AIInstructionsAgentInstructionsTools: TypeAlias = Union[
    AIInstructionsAgentInstructionsToolsToolArray,
    AIInstructionsAgentInstructionsToolsToolDict,
    AIInstructionsAgentInstructionsToolsToolString,
]


class AIInstructionsAgentInstructions(TypedDict, total=False):
    system_prompt: Required[str]

    agent_name: Optional[str]

    tools: AIInstructionsAgentInstructionsTools
    """Instructions for the agent, can be a string or a list/dict of tools."""


class AIInstructionsWorkflowInstructionsInstructionToolsToolArrayValue(TypedDict, total=False):
    id: Required[str]

    content: Required[Union[str, object, None]]

    name: Required[str]


class AIInstructionsWorkflowInstructionsInstructionToolsToolArray(TypedDict, total=False):
    value: Required[Iterable[AIInstructionsWorkflowInstructionsInstructionToolsToolArrayValue]]

    type: Literal["array"]


class AIInstructionsWorkflowInstructionsInstructionToolsToolDictTyped(TypedDict, total=False):
    value: Required[object]

    type: Literal["dict"]


AIInstructionsWorkflowInstructionsInstructionToolsToolDict: TypeAlias = Union[
    AIInstructionsWorkflowInstructionsInstructionToolsToolDictTyped, Dict[str, object]
]


class AIInstructionsWorkflowInstructionsInstructionToolsToolString(TypedDict, total=False):
    value: Required[str]

    type: Literal["string"]


AIInstructionsWorkflowInstructionsInstructionTools: TypeAlias = Union[
    AIInstructionsWorkflowInstructionsInstructionToolsToolArray,
    AIInstructionsWorkflowInstructionsInstructionToolsToolDict,
    AIInstructionsWorkflowInstructionsInstructionToolsToolString,
]


class AIInstructionsWorkflowInstructionsInstruction(TypedDict, total=False):
    system_prompt: Required[str]

    agent_name: Optional[str]

    tools: AIInstructionsWorkflowInstructionsInstructionTools
    """Instructions for the agent, can be a string or a list/dict of tools."""


class AIInstructionsWorkflowInstructions(TypedDict, total=False):
    instructions: Required[Iterable[AIInstructionsWorkflowInstructionsInstruction]]
    """List of agent instructions for the workflow. Must contain at least one agent."""


AIInstructions: TypeAlias = Union[str, AIInstructionsAgentInstructions, AIInstructionsWorkflowInstructions]

GroundTruth: TypeAlias = Union[str, FileReference]
