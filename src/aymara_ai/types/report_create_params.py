# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ReportCreateParams"]


class ReportCreateParams(TypedDict, total=False):
    eval_run_uuids: Required[SequenceNotStr[str]]
    """List of eval run UUIDs to include in the suite summary."""

    workspace_uuid: str
