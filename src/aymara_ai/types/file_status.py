# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FileStatus"]


class FileStatus(BaseModel):
    created_at: datetime
    """Timestamp when the file was created."""

    file_uuid: str
    """Unique identifier for the file."""

    processing_status: str
    """Current processing status: pending, processing, completed, or failed."""

    updated_at: datetime
    """Timestamp when the file was last updated."""

    error_message: Optional[str] = None
    """Error message if processing failed."""

    remote_file_path: Optional[str] = None
    """S3 path to the file (available when completed)."""
