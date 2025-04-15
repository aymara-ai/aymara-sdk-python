# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .status import Status
from .._models import BaseModel
from .eval_out import EvalOut

__all__ = ["EvalRun"]


class EvalRun(BaseModel):
    created_at: datetime

    eval_run_uuid: str

    status: Status
    """Resource status."""

    updated_at: datetime

    ai_description: Optional[str] = None

    evaluation: Optional[EvalOut] = None

    num_prompts: Optional[int] = None

    num_responses_scored: Optional[int] = None

    pass_rate: Optional[float] = None

    workspace_uuid: Optional[str] = None
