# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .content_type import ContentType

__all__ = ["EvalGetResponsesResponse", "Item", "ItemPrompt", "ItemNextPrompt"]


class ItemPrompt(BaseModel):
    content: str

    prompt_uuid: str

    category: Optional[str] = None

    thread_uuid: Optional[str] = None

    turn_number: Optional[int] = None


class ItemNextPrompt(BaseModel):
    content: str

    prompt_uuid: str

    category: Optional[str] = None

    thread_uuid: Optional[str] = None

    turn_number: Optional[int] = None


class Item(BaseModel):
    content: str

    prompt: ItemPrompt

    prompt_uuid: str

    response_uuid: str

    ai_refused: Optional[bool] = None

    confidence: Optional[float] = None

    content_type: Optional[ContentType] = None
    """Content type for AI interactions."""

    exclude_from_scoring: Optional[bool] = None

    explanation: Optional[str] = None

    generate_prompt: Optional[bool] = None

    is_passed: Optional[bool] = None

    next_prompt: Optional[ItemNextPrompt] = None

    thread_uuid: Optional[str] = None

    turn_number: Optional[int] = None


class EvalGetResponsesResponse(BaseModel):
    count: int

    items: List[Item]
