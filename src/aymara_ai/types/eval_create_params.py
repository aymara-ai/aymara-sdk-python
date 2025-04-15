# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .content_type import ContentType
from .prompt_example_in_param import PromptExampleInParam

__all__ = ["EvalCreateParams"]


class EvalCreateParams(TypedDict, total=False):
    ai_description: Required[str]

    eval_type: Required[str]

    name: Required[str]

    ai_instructions: Optional[str]

    eval_instructions: Optional[str]

    is_jailbreak: bool

    is_sandbox: bool

    language: str

    modality: ContentType
    """Content type for AI interactions."""

    num_prompts: int

    prompt_examples: Optional[Iterable[PromptExampleInParam]]

    workspace_uuid: Optional[str]
