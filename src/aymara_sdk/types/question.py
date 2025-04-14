# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Question"]


class Question(BaseModel):
    question_text: str

    question_uuid: str

    accuracy_question_type: Optional[str] = None

    conversation_turn: Optional[int] = None

    conversation_uuid: Optional[str] = None
