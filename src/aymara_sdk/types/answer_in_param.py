# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AnswerInParam"]


class AnswerInParam(TypedDict, total=False):
    question_uuid: Required[str]

    answer_image_path: Optional[str]

    answer_text: Optional[str]

    exclude_from_scoring: bool

    student_refused: bool
