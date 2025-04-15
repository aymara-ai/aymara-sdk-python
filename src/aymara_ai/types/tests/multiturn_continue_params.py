# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..answer_in_param import AnswerInParam

__all__ = ["MultiturnContinueParams"]


class MultiturnContinueParams(TypedDict, total=False):
    test_uuid: Required[str]

    continue_eval: bool

    is_sandbox: bool

    answers: Optional[Iterable[AnswerInParam]]
