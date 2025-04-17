# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["EvalGetPromptsResponse", "Item"]


class Item(BaseModel):
    content: str

    prompt_uuid: str

    category: Optional[str] = None

    thread_uuid: Optional[str] = None

    turn_number: Optional[int] = None


class EvalGetPromptsResponse(BaseModel):
    count: int

    items: List[Item]
