# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .question import Question

__all__ = ["TestRetrieveQuestionsResponse"]


class TestRetrieveQuestionsResponse(BaseModel):
    __test__ = False
    count: int

    items: List[Question]
