# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["PolicyListResponse", "Item"]


class Item(BaseModel):
    aymara_policy_name: str

    display_name: str

    policy_text: str

    test_language: str

    test_type: str


class PolicyListResponse(BaseModel):
    count: int

    items: List[Item]
