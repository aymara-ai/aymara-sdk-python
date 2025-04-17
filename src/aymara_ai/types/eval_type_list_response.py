# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["EvalTypeListResponse", "EvalTypeListResponseItem"]


class EvalTypeListResponseItem(BaseModel):
    description: str

    eval_type_uuid: str

    name: str

    slug: str

    supported_modalities: Optional[List[str]] = None


EvalTypeListResponse: TypeAlias = List[EvalTypeListResponseItem]
