# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared.status import Status
from .shared.content_type import ContentType
from .prompt_example_param import PromptExampleParam

__all__ = ["EvalCreateParams", "GroundTruth", "GroundTruthFileReference"]


class EvalCreateParams(TypedDict, total=False):
    ai_description: Required[str]

    eval_type: Required[str]

    name: Required[str]

    ai_instructions: Optional[str]

    created_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    eval_instructions: Optional[str]

    eval_uuid: Optional[str]

    ground_truth: Optional[GroundTruth]

    is_jailbreak: bool

    is_sandbox: bool

    language: Optional[str]

    modality: ContentType
    """Content type for AI interactions."""

    num_prompts: Optional[int]

    prompt_examples: Optional[Iterable[PromptExampleParam]]

    status: Optional[Status]
    """Resource status."""

    updated_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    workspace_uuid: Optional[str]


class GroundTruthFileReference(TypedDict, total=False):
    remote_file_path: Optional[str]


GroundTruth: TypeAlias = Union[str, GroundTruthFileReference]
