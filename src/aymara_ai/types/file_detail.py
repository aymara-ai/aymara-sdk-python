# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FileDetail"]


class FileDetail(BaseModel):
    content_type: str
    """MIME type of the file."""

    created_at: datetime
    """Timestamp when the file was created."""

    file_type: str
    """Type of file content (text, image, video, document)."""

    file_url: str
    """Presigned URL to access the file."""

    file_uuid: str
    """Unique identifier for the file."""

    organization_uuid: str
    """UUID of the organization that owns this file."""

    remote_file_path: str
    """S3 path to the file (or directory for videos)."""

    updated_at: datetime
    """Timestamp when the file was last updated."""

    file_size_bytes: Optional[int] = None
    """Size of file in bytes, if known."""

    original_file_url: Optional[str] = None
    """Original file URL or path from upload."""

    uploaded_by_uuid: Optional[str] = None
    """UUID of user who uploaded the file."""

    video_metadata: Optional[object] = None
    """Video metadata (fps, duration, etc.) for video files."""

    workspace_uuid: Optional[str] = None
    """UUID of the workspace this file belongs to, if any."""
