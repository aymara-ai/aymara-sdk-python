# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .eval_prompt import EvalPrompt

__all__ = ["EvalGetPromptsResponse"]


class EvalGetPromptsResponse(BaseModel):
    count: int

    items: List[EvalPrompt]
