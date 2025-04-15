# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .answer_in_param import AnswerInParam

__all__ = ["FileUploadParams"]


class FileUploadParams(TypedDict, total=False):
    answers: Required[Iterable[AnswerInParam]]

    test_uuid: Required[str]
