# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .eval_response import EvalResponse

__all__ = ["EvalRunGetResponsesResponse"]


class EvalRunGetResponsesResponse(BaseModel):
    count: int

    items: List[EvalResponse]
