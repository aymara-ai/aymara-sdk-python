# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FileReference"]


class FileReference(TypedDict, total=False):
    remote_file_path: Optional[str]
