# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .eval import Eval
from .._models import BaseModel

__all__ = ["EvalAnalyzeResponse", "Result", "ResultStats"]


class ResultStats(BaseModel):
    total_responses_scored: int
    """Total number of responses scored across all runs"""

    total_score_runs: int
    """Total number of score runs for this eval"""

    avg_pass_rate: Optional[float] = None
    """Average pass rate across all score runs"""

    best_pass_rate: Optional[float] = None
    """Best (highest) pass rate achieved"""

    last_run_date: Optional[datetime] = None
    """Date of the most recent score run"""

    worst_pass_rate: Optional[float] = None
    """Worst (lowest) pass rate achieved"""


class Result(BaseModel):
    eval: Eval
    """The eval data"""

    stats: ResultStats
    """Aggregated statistics for this eval"""


class EvalAnalyzeResponse(BaseModel):
    has_more: bool
    """Whether there are more results available"""

    results: List[Result]
    """List of matching evals with statistics"""

    total_count: int
    """Total number of evals matching the analysis criteria"""
