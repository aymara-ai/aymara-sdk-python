# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EvalListPromptsParams"]


class EvalListPromptsParams(TypedDict, total=False):
    limit: int

    offset: int

    workspace_uuid: str
