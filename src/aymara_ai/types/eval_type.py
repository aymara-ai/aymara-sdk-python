# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["EvalType"]


class EvalType(BaseModel):
    description: str
    """Description of the eval type."""

    eval_type_uuid: str
    """Unique identifier for the eval type."""

    name: str
    """Name of the eval type."""

    slug: str
    """Slug for the eval type."""

    supported_generation_inputs: List[str]
    """List of supported generation input types."""

    supported_modalities: Optional[List[str]] = None
    """List of supported modalities (e.g., text, image)."""
