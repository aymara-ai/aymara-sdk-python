# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .user import User
from .._models import BaseModel
from .test_out import TestOut

__all__ = ["ScoreRunOut", "ScoreRunExample"]


class ScoreRunExample(BaseModel):
    answer_text: str

    example_type: Literal["pass", "fail"]

    example_uuid: str

    explanation: str

    question_text: str


class ScoreRunOut(BaseModel):
    created_at: datetime

    price: float

    score_run_status: Literal["record_created", "image_uploading", "scoring", "finished", "failed"]

    score_run_uuid: str

    test: TestOut

    updated_at: datetime

    created_by: Optional[User] = None

    pass_rate: Optional[float] = None

    price_adjustment_note: Optional[str] = None

    remaining_score_runs: Optional[int] = None

    score_run_examples: Optional[List[ScoreRunExample]] = None
