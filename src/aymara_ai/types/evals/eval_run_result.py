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
    """Timestamp when the eval run was created."""

    eval_run_uuid: str
    """Unique identifier for the eval run."""

    eval_uuid: str
    """Unique identifier for the eval."""

    status: Status
    """Status of the eval run."""

    updated_at: datetime
    """Timestamp when the eval run was last updated."""

    ai_description: Optional[str] = None
    """Description of the AI for this run, if any."""

    evaluation: Optional[Eval] = None
    """Schema for configuring an Eval based on a eval_type."""

    name: Optional[str] = None
    """Name of the eval run, if any (defaults to the eval name + timestamp)."""

    num_prompts: Optional[int] = None
    """Number of prompts in the eval run, if any."""

    num_responses_scored: Optional[int] = None
    """Number of responses scored in the eval run, if any."""

    pass_rate: Optional[float] = None
    """Pass rate for the eval run, if any."""

    responses: Optional[List[ScoredResponse]] = None
    """List of scored responses for the eval run, if any."""

    workspace_uuid: Optional[str] = None
    """UUID of the associated workspace, if any."""
