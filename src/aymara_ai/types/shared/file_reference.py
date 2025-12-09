# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FileReference"]


class FileReference(BaseModel):
    """Reference to a file, either by file_uuid (preferred) or legacy remote_file_path.

    When file_uuid is provided, the system will look up the File record and use its
    remote_file_path. The remote_file_path field is maintained for backwards compatibility.
    """

    file_uuid: Optional[str] = None

    remote_file_path: Optional[str] = None
