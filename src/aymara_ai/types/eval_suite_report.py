# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.status import Status
from .evals.eval_run_result import EvalRunResult

__all__ = ["EvalSuiteReport", "EvalRunReport"]


class EvalRunReport(BaseModel):
    eval_run: EvalRunResult
    """Schema for returning eval run data."""

    eval_run_report_uuid: str

    eval_run_uuid: str

    failing_responses_summary: str

    improvement_advice: str

    passing_responses_summary: str


class EvalSuiteReport(BaseModel):
    created_at: datetime

    eval_run_reports: List[EvalRunReport]

    eval_suite_report_uuid: str

    status: Status
    """Resource status."""

    updated_at: datetime

    overall_failing_responses_summary: Optional[str] = None

    overall_improvement_advice: Optional[str] = None

    overall_passing_responses_summary: Optional[str] = None

    remaining_reports: Optional[int] = None
