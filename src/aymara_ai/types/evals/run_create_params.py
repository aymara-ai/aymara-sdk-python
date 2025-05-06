# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..eval_response_param import EvalResponseParam
from .eval_run_example_param import EvalRunExampleParam

__all__ = ["RunCreateParams"]


class RunCreateParams(TypedDict, total=False):
    eval_uuid: Required[str]
    """Unique identifier for the eval."""

    responses: Required[Iterable[EvalResponseParam]]
    """List of AI responses to eval prompts."""

    is_sandbox: Optional[bool]

    workspace_uuid: str

    ai_description: Optional[str]
    """Description of the AI for this run, if any."""

    continue_thread: Optional[bool]
    """Whether to continue the thread after this run."""

    eval_run_examples: Optional[Iterable[EvalRunExampleParam]]
    """Examples to include with the eval run, if any."""

    eval_run_uuid: Optional[str]
    """Unique identifier for the eval run, if any."""

    name: Optional[str]
    """Name of the eval run, if any (defaults to the eval name + timestamp)."""
