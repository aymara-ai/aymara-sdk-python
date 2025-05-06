# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["FileCreateParams", "File"]


class FileCreateParams(TypedDict, total=False):
    files: Required[Iterable[File]]
    """List of files to upload."""

    workspace_uuid: Optional[str]
    """UUID of the workspace to associate with the upload, if any."""


class File(TypedDict, total=False):
    local_file_path: Optional[str]
    """Local file path of the uploaded file, if available."""
