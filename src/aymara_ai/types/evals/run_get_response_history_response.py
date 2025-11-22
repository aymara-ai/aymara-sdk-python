# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .answer_history import AnswerHistory

__all__ = ["RunGetResponseHistoryResponse"]

RunGetResponseHistoryResponse: TypeAlias = List[AnswerHistory]
