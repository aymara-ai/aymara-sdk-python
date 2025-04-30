# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .shared.content_type import ContentType
from .shared_params.file_reference import FileReference

__all__ = ["EvalResponseParam", "Content"]

Content: TypeAlias = Union[str, FileReference]


class EvalResponseParam(TypedDict, total=False):
    prompt_uuid: Required[str]

    ai_refused: bool

    content: Optional[Content]

    content_type: ContentType
    """Content type for AI interactions."""

    continue_thread: bool

    exclude_from_scoring: bool

    thread_uuid: Optional[str]

    turn_number: int
