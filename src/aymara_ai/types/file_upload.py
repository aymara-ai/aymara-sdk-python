# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["FileUpload"]


class FileUpload(BaseModel):
    file_url: Optional[str] = None

    file_uuid: Optional[str] = None

    local_file_path: Optional[str] = None

    remote_file_path: Optional[str] = None
