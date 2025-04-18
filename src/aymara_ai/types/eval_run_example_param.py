# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["EvalRunExampleParam"]


class EvalRunExampleParam(TypedDict, total=False):
    prompt: Required[str]

    response: Required[str]

    type: Required[Literal["pass", "fail"]]

    example_uuid: Optional[str]

    explanation: Optional[str]
