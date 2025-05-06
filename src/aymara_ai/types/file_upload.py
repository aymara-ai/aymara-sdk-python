# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["FileUpload"]


class FileUpload(BaseModel):
    file_url: Optional[str] = None
    """URL to access the uploaded file, if available."""

    file_uuid: Optional[str] = None
    """Unique identifier for the uploaded file."""

    local_file_path: Optional[str] = None
    """Local file path of the uploaded file, if available."""

    remote_file_path: Optional[str] = None
    """Remote file path of the uploaded file, if available."""
