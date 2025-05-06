# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.status import Status
from .evals.eval_run_result import EvalRunResult

__all__ = ["EvalSuiteReport", "EvalRunReport"]


class EvalRunReport(BaseModel):
    eval_run: EvalRunResult
    """Eval run result data."""

    eval_run_report_uuid: str
    """Unique identifier for the eval run report."""

    eval_run_uuid: str
    """Unique identifier for the eval run."""

    failing_responses_summary: str
    """Summary of failing responses."""

    improvement_advice: str
    """Advice for improving future responses."""

    passing_responses_summary: str
    """Summary of passing responses."""


class EvalSuiteReport(BaseModel):
    created_at: datetime
    """Timestamp when the eval suite report was created."""

    eval_run_reports: List[EvalRunReport]
    """List of eval run reports included in the suite."""

    eval_suite_report_uuid: str
    """Unique identifier for the eval suite report."""

    status: Status
    """Status of the eval suite report."""

    updated_at: datetime
    """Timestamp when the eval suite report was last updated."""

    overall_failing_responses_summary: Optional[str] = None
    """Overall summary of failing responses, if any."""

    overall_improvement_advice: Optional[str] = None
    """Overall advice for improving future responses, if any."""

    overall_passing_responses_summary: Optional[str] = None
    """Overall summary of passing responses, if any."""

    remaining_reports: Optional[int] = None
    """Number of remaining reports to be generated, if any."""
