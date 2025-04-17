# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .example_type import ExampleType

__all__ = ["PromptExampleIn"]


class PromptExampleIn(BaseModel):
    content: str

    example_uuid: Optional[str] = None

    explanation: Optional[str] = None

    type: Optional[ExampleType] = None
