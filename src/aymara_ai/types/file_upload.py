# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["FileUpload"]


class FileUpload(BaseModel):
    content_type: Optional[str] = None
    """MIME type of the file (e.g., 'video/mp4').

    If not provided, will be inferred from file extension.
    """

    file_url: Optional[str] = None
    """URL to access the uploaded file, if available."""

    file_uuid: Optional[str] = None
    """Unique identifier for the uploaded file."""

    local_file_path: Optional[str] = None
    """Local file path of the uploaded file, if available."""

    processing_status: Optional[str] = None
    """Processing status: pending, processing, completed, or failed."""

    remote_file_path: Optional[str] = None
    """Remote file path of the uploaded file, if available."""

    remote_uri: Optional[str] = None
    """Remote URI to fetch the file from, if available."""
