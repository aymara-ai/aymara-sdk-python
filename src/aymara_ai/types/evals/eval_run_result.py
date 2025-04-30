# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..eval import Eval
from ..._models import BaseModel
from ..shared.status import Status
from .scored_response import ScoredResponse

__all__ = ["EvalRunResult"]


class EvalRunResult(BaseModel):
    created_at: datetime

    eval_run_uuid: str

    eval_uuid: str

    status: Status
    """Resource status."""

    updated_at: datetime

    ai_description: Optional[str] = None

    evaluation: Optional[Eval] = None
    """Schema for configuring an Eval based on a eval_type."""

    name: Optional[str] = None

    num_prompts: Optional[int] = None

    num_responses_scored: Optional[int] = None

    pass_rate: Optional[float] = None

    responses: Optional[List[ScoredResponse]] = None

    workspace_uuid: Optional[str] = None
