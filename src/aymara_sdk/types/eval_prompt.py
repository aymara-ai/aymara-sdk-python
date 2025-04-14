# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["EvalPrompt"]


class EvalPrompt(BaseModel):
    content: str

    prompt_uuid: str

    category: Optional[str] = None

    thread_uuid: Optional[str] = None

    turn_number: Optional[int] = None
