# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..status import Status
from ..._models import BaseModel
from ..eval_run import EvalRun

__all__ = ["EvalRunSuiteSummary", "EvalRunSummary"]


class EvalRunSummary(BaseModel):
    eval_run: EvalRun
    """Schema for returning eval run data."""

    eval_run_summary_uuid: str

    eval_run_uuid: str

    failing_responses_summary: str

    improvement_advice: str

    passing_responses_summary: str


class EvalRunSuiteSummary(BaseModel):
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
