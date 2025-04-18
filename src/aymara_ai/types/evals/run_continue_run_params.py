# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..shared_params.eval_response import EvalResponse
from ..shared_params.eval_run_example import EvalRunExample

__all__ = ["RunContinueRunParams"]


class RunContinueRunParams(TypedDict, total=False):
    eval_uuid: Required[str]

    responses: Required[Iterable[EvalResponse]]

    is_sandbox: bool

    workspace_uuid: str

    ai_description: Optional[str]

    eval_run_examples: Optional[Iterable[EvalRunExample]]

    generate_prompts: Optional[bool]

    name: Optional[str]
