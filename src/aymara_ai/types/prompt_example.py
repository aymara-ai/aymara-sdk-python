# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PromptExample"]


class PromptExample(BaseModel):
    content: str

    example_uuid: Optional[str] = None

    explanation: Optional[str] = None

    type: Optional[Literal["good", "bad"]] = None
