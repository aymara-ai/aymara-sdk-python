# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .eval_response_param import EvalResponseParam

__all__ = ["EvalContinueRunParams", "EvalRunExample"]


class EvalContinueRunParams(TypedDict, total=False):
    eval_uuid: Required[str]

    responses: Required[Iterable[EvalResponseParam]]

    is_sandbox: bool

    workspace_uuid: str

    ai_description: Optional[str]

    eval_run_examples: Optional[Iterable[EvalRunExample]]

    body_eval_run_uuid: Annotated[Optional[str], PropertyInfo(alias="eval_run_uuid")]

    generate_prompts: Optional[bool]

    name: Optional[str]


class EvalRunExample(TypedDict, total=False):
    prompt: Required[str]

    response: Required[str]

    type: Required[Literal["pass", "fail"]]

    example_uuid: Optional[str]

    explanation: Optional[str]
