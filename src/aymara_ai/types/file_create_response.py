# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .file_upload import FileUpload

__all__ = ["FileCreateResponse"]


class FileCreateResponse(BaseModel):
    files: List[FileUpload]
    """List of results for each uploaded file."""

    workspace_uuid: Optional[str] = None
    """UUID of the workspace associated with the upload, if any."""
