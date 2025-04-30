# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EvalTypeFindInstructionsParams"]


class EvalTypeFindInstructionsParams(TypedDict, total=False):
    eval_type_slug: Required[str]

    limit: int

    offset: int
