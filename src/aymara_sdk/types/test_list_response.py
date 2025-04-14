# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .test_out import TestOut

__all__ = ["TestListResponse"]


class TestListResponse(BaseModel):
    __test__ = False
    count: int

    items: List[TestOut]
