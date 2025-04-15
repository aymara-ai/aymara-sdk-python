# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import date

from .._models import BaseModel
from .score_run_out import ScoreRunOut

__all__ = ["UsageListResponse", "BillingCycle"]


class BillingCycle(BaseModel):
    billing_cycle_end_date: date

    billing_cycle_start_date: date

    billing_cycle_uuid: str

    paid_amount_usd: Union[float, str]

    score_runs: List[ScoreRunOut]


class UsageListResponse(BaseModel):
    test_type_displays: Dict[str, str]

    billing_cycles: Optional[List[BillingCycle]] = None

    free_score_runs: Optional[List[ScoreRunOut]] = None
