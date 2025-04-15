# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..question import Question
from ..answer_out import AnswerOut

__all__ = ["MultiturnContinueResponse", "Conversation"]


class Conversation(BaseModel):
    conversation_uuid: str

    current_turn: int

    response: AnswerOut

    prompt: Optional[Question] = None


class MultiturnContinueResponse(BaseModel):
    conversations: List[Conversation]

    test_uuid: str

    score_run_uuid: Optional[str] = None
