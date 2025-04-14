# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .answer_out import AnswerOut

__all__ = ["ScoreGetAnswersResponse"]


class ScoreGetAnswersResponse(BaseModel):
    count: int

    items: List[AnswerOut]
