# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .eval_out import EvalOut

__all__ = ["EvalListResponse"]


class EvalListResponse(BaseModel):
    count: int

    items: List[EvalOut]
