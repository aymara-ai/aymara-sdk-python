# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["FileFrames"]


class FileFrames(BaseModel):
    file_uuid: str
    """Unique identifier for the file."""

    frame_count: int
    """Total number of frames available."""

    frame_urls: List[str]
    """List of presigned URLs to video frames, sorted by frame number."""
