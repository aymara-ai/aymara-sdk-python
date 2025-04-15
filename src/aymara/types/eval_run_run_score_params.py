# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .content_type import ContentType

__all__ = ["EvalRunRunScoreParams", "Response", "EvalRunExample"]


class EvalRunRunScoreParams(TypedDict, total=False):
    eval_uuid: Required[str]

    responses: Required[Iterable[Response]]

    is_sandbox: bool

    workspace_uuid: str

    ai_description: Optional[str]

    eval_run_examples: Optional[Iterable[EvalRunExample]]

    eval_run_uuid: Optional[str]

    generate_prompts: Optional[bool]

    name: Optional[str]


class Response(TypedDict, total=False):
    content: Required[str]

    prompt_uuid: Required[str]

    ai_refused: bool

    content_type: ContentType
    """Content type for AI interactions."""

    exclude_from_scoring: bool

    generate_prompt: bool

    thread_uuid: Optional[str]

    turn_number: int


class EvalRunExample(TypedDict, total=False):
    prompt: Required[str]

    response: Required[str]

    type: Required[Literal["pass", "fail"]]

    explanation: Optional[str]
