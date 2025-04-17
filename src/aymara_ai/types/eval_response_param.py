# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .content_type import ContentType

__all__ = ["EvalResponseParam"]


class EvalResponseParam(TypedDict, total=False):
    content: Required[str]

    prompt_uuid: Required[str]

    ai_refused: bool

    content_type: ContentType
    """Content type for AI interactions."""

    continue_thread: bool

    exclude_from_scoring: bool

    thread_uuid: Optional[str]

    turn_number: int
