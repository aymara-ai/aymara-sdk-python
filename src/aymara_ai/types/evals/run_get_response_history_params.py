# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RunGetResponseHistoryParams"]


class RunGetResponseHistoryParams(TypedDict, total=False):
    eval_run_uuid: Required[str]

    workspace_uuid: str
