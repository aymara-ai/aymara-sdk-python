# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["EvalType"]


class EvalType(BaseModel):
    description: str

    eval_type_uuid: str

    name: str

    slug: str

    supported_generation_inputs: List[str]

    supported_modalities: Optional[List[str]] = None
