# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["FileUploadParams", "File"]


class FileUploadParams(TypedDict, total=False):
    files: Required[Iterable[File]]

    workspace_uuid: Optional[str]


class File(TypedDict, total=False):
    file_uuid: Required[str]

    file_path: Optional[str]
