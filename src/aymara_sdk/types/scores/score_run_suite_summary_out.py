# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..score_run_out import ScoreRunOut

__all__ = ["ScoreRunSuiteSummaryOut", "ScoreRunSummary"]


class ScoreRunSummary(BaseModel):
    explanation_summary: str

    failing_answers_summary: str

    improvement_advice: str

    passing_answers_summary: str

    score_run: ScoreRunOut

    score_run_summary_uuid: str


class ScoreRunSuiteSummaryOut(BaseModel):
    created_at: datetime

    score_run_suite_summary_uuid: str

    score_run_summaries: List[ScoreRunSummary]

    status: Literal["record_created", "generating", "finished", "failed"]

    updated_at: datetime

    overall_failing_answers_summary: Optional[str] = None

    overall_improvement_advice: Optional[str] = None

    overall_passing_answers_summary: Optional[str] = None

    overall_summary: Optional[str] = None

    remaining_summaries: Optional[int] = None
