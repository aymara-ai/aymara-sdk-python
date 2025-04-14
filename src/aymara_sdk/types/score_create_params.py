# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .answer_in_param import AnswerInParam

__all__ = ["ScoreCreateParams", "ScoreRunExample"]


class ScoreCreateParams(TypedDict, total=False):
    answers: Required[Iterable[AnswerInParam]]

    test_uuid: Required[str]

    is_sandbox: Optional[bool]

    workspace_uuid: str

    score_run_examples: Optional[Iterable[ScoreRunExample]]

    student_description: Optional[str]


class ScoreRunExample(TypedDict, total=False):
    answer_text: Required[str]

    example_type: Required[Literal["pass", "fail"]]

    explanation: Required[str]

    question_text: Required[str]
