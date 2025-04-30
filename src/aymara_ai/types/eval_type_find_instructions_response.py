# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.ai_instruction import AIInstruction

__all__ = ["EvalTypeFindInstructionsResponse"]


class EvalTypeFindInstructionsResponse(BaseModel):
    count: int

    items: List[AIInstruction]
