# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ReportCreateParams"]


class ReportCreateParams(TypedDict, total=False):
    eval_run_uuids: Required[List[str]]
    """List of eval run UUIDs to include in the suite summary."""

    is_sandbox: Optional[bool]

    workspace_uuid: str
