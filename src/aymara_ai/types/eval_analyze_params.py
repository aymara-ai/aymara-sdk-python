# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EvalAnalyzeParams"]


class EvalAnalyzeParams(TypedDict, total=False):
    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter evals created after this date"""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter evals created before this date"""

    created_by: Optional[str]
    """Filter by creator email"""

    eval_type: Optional[str]
    """Filter by eval type (safety, accuracy, jailbreak, image_safety)"""

    has_score_runs: Optional[bool]
    """Only include evals that have score runs"""

    is_jailbreak: Optional[bool]
    """Filter by jailbreak status"""

    is_sandbox: Optional[bool]
    """Filter by sandbox status"""

    language: Optional[str]
    """Filter by language code (e.g., en, es)"""

    limit: int
    """Maximum number of results (1-100)"""

    max_pass_rate: Optional[float]
    """Maximum average pass rate (0.0-1.0)"""

    min_pass_rate: Optional[float]
    """Minimum average pass rate (0.0-1.0)"""

    modality: Optional[str]
    """Filter by modality (text, image)"""

    name: Optional[str]
    """Filter by eval names (case-insensitive partial match)"""

    offset: int
    """Number of results to skip"""

    run_created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter by score runs created after this date"""

    run_created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter by score runs created before this date"""

    score_run_status: Optional[str]
    """Filter by any score run status"""

    sort_by: Literal["created_at", "updated_at", "name", "pass_rate", "num_score_runs", "last_run_date"]
    """Field to sort by"""

    sort_order: Literal["asc", "desc"]
    """Sort order"""

    status: Optional[str]
    """Filter by eval status (created, processing, finished, failed)"""

    workspace_uuid: Optional[str]
    """Filter by workspace UUID"""
