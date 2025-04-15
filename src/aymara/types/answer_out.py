# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .question import Question

__all__ = ["AnswerOut"]


class AnswerOut(BaseModel):
    answer_uuid: str

    question: Question

    answer_image_path: Optional[str] = None

    answer_image_url: Optional[str] = None

    answer_text: Optional[str] = None

    confidence: Optional[float] = None

    exclude_from_scoring: Optional[bool] = None

    explanation: Optional[str] = None

    is_passed: Optional[bool] = None

    student_refused: Optional[bool] = None
