# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .eval_run import EvalRun

__all__ = ["EvalRunListResponse"]


class EvalRunListResponse(BaseModel):
    count: int

    items: List[EvalRun]
