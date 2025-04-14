# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .eval_run_suite_summary import EvalRunSuiteSummary

__all__ = ["SummaryListResponse"]


class SummaryListResponse(BaseModel):
    count: int

    items: List[EvalRunSuiteSummary]
