# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.status import Status
from .prompt_example import PromptExample
from .shared.content_type import ContentType
from .shared.file_reference import FileReference

__all__ = [
    "Eval",
    "AIInstructions",
    "AIInstructionsAgentInstructions",
    "AIInstructionsAgentInstructionsTools",
    "AIInstructionsAgentInstructionsToolsToolArray",
    "AIInstructionsAgentInstructionsToolsToolArrayValue",
    "AIInstructionsAgentInstructionsToolsToolDict",
    "AIInstructionsAgentInstructionsToolsToolString",
    "GroundTruth",
]


class AIInstructionsAgentInstructionsToolsToolArrayValue(BaseModel):
    id: str

    content: Union[str, object, None] = None

    name: str


class AIInstructionsAgentInstructionsToolsToolArray(BaseModel):
    value: List[AIInstructionsAgentInstructionsToolsToolArrayValue]

    type: Optional[Literal["array"]] = None


class AIInstructionsAgentInstructionsToolsToolDict(BaseModel):
    value: object

    type: Optional[Literal["dict"]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class AIInstructionsAgentInstructionsToolsToolString(BaseModel):
    value: str

    type: Optional[Literal["string"]] = None


AIInstructionsAgentInstructionsTools: TypeAlias = Annotated[
    Union[
        AIInstructionsAgentInstructionsToolsToolArray,
        AIInstructionsAgentInstructionsToolsToolDict,
        AIInstructionsAgentInstructionsToolsToolString,
    ],
    PropertyInfo(discriminator="type"),
]


class AIInstructionsAgentInstructions(BaseModel):
    system_prompt: str

    tools: Optional[AIInstructionsAgentInstructionsTools] = None
    """Instructions for the agent, can be a string or a list/dict of tools."""


AIInstructions: TypeAlias = Union[str, AIInstructionsAgentInstructions, None]

GroundTruth: TypeAlias = Union[str, FileReference, None]


class Eval(BaseModel):
    ai_description: str
    """Description of the AI under evaluation."""

    eval_type: str
    """Type of the eval (safety, accuracy, etc.)"""

    ai_instructions: Optional[AIInstructions] = None
    """Instructions the AI should follow.

    String for normal evals, AgentInstructions for agent evals.
    """

    created_at: Optional[datetime] = None
    """Timestamp when the eval was created."""

    created_by: Optional[str] = None
    """Name of the user who created the evaluation."""

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
