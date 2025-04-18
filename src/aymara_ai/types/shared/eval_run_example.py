# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EvalRunExample"]


class EvalRunExample(BaseModel):
    prompt: str

    response: str

    type: Literal["pass", "fail"]

    example_uuid: Optional[str] = None

    explanation: Optional[str] = None
