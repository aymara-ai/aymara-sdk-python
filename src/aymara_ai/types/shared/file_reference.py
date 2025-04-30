# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FileReference"]


class FileReference(BaseModel):
    remote_file_path: Optional[str] = None
