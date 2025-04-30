# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .run_example_param import RunExampleParam
from ..eval_response_param import EvalResponseParam

__all__ = ["RunCreateParams"]


class RunCreateParams(TypedDict, total=False):
    eval_uuid: Required[str]

    responses: Required[Iterable[EvalResponseParam]]

    is_sandbox: Optional[bool]

    workspace_uuid: str

    ai_description: Optional[str]

    continue_thread: Optional[bool]

    eval_run_examples: Optional[Iterable[RunExampleParam]]

    eval_run_uuid: Optional[str]

    name: Optional[str]
