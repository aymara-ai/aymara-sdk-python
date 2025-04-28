# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["FileCreateResponse", "File"]


class File(BaseModel):
    file_url: Optional[str] = None

    file_uuid: Optional[str] = None

    local_file_path: Optional[str] = None

    remote_file_path: Optional[str] = None


class FileCreateResponse(BaseModel):
    files: List[File]

    workspace_uuid: Optional[str] = None
