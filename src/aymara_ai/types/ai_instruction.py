# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AIInstruction"]


class AIInstruction(BaseModel):
    content: str

    eval_type: str

    instruction_uuid: str

    name: str

    language: Optional[str] = None
