# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .eval import Eval
from .status import Status
from .._models import BaseModel
from .eval_prompt import EvalPrompt
from .content_type import ContentType

__all__ = ["EvalSuiteReport", "EvalRunSummary", "EvalRunSummaryEvalRun", "EvalRunSummaryEvalRunResponse"]


class EvalRunSummaryEvalRunResponse(BaseModel):
    content: str

    prompt: EvalPrompt

    prompt_uuid: str

    ai_refused: Optional[bool] = None

    confidence: Optional[float] = None

    content_type: Optional[ContentType] = None
    """Content type for AI interactions."""

    continue_thread: Optional[bool] = None

    exclude_from_scoring: Optional[bool] = None

    explanation: Optional[str] = None

    is_passed: Optional[bool] = None

    next_prompt: Optional[EvalPrompt] = None

    response_uuid: Optional[str] = None

    thread_uuid: Optional[str] = None

    turn_number: Optional[int] = None


class EvalRunSummaryEvalRun(BaseModel):
    created_at: datetime

    eval_run_uuid: str

    status: Status
    """Resource status."""

    updated_at: datetime

    ai_description: Optional[str] = None

    evaluation: Optional[Eval] = None
    """Schema for configuring an Eval based on a eval_type."""

    num_prompts: Optional[int] = None

    num_responses_scored: Optional[int] = None

    pass_rate: Optional[float] = None

    responses: Optional[List[EvalRunSummaryEvalRunResponse]] = None

    workspace_uuid: Optional[str] = None


class EvalRunSummary(BaseModel):
    eval_run: EvalRunSummaryEvalRun
    """Schema for returning eval run data."""

    eval_run_summary_uuid: str

    eval_run_uuid: str

    failing_responses_summary: str

    improvement_advice: str

    passing_responses_summary: str


class EvalSuiteReport(BaseModel):
    created_at: datetime

    eval_run_suite_summary_uuid: str

    eval_run_summaries: List[EvalRunSummary]

    status: Status
    """Resource status."""

    updated_at: datetime

    overall_failing_responses_summary: Optional[str] = None

    overall_improvement_advice: Optional[str] = None

    overall_passing_responses_summary: Optional[str] = None

    remaining_summaries: Optional[int] = None
