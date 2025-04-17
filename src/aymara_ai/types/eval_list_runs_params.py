# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EvalListRunsParams"]


class EvalListRunsParams(TypedDict, total=False):
    eval_uuid: str

    limit: int

    offset: int

    workspace_uuid: str
