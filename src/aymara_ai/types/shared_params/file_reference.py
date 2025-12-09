# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FileReference"]


class FileReference(TypedDict, total=False):
    """Reference to a file, either by file_uuid (preferred) or legacy remote_file_path.

    When file_uuid is provided, the system will look up the File record and use its
    remote_file_path. The remote_file_path field is maintained for backwards compatibility.
    """

    file_uuid: Optional[str]

    remote_file_path: Optional[str]
