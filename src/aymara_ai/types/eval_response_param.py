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
    """Unique identifier for the prompt."""

    ai_refused: bool
    """Whether the AI refused to answer the prompt."""

    content: Optional[Content]
    """Content of the AI response or a file reference."""

    content_type: ContentType
    """Content type for AI interactions."""

    continue_thread: bool
    """Whether to continue the thread after this response."""

    exclude_from_scoring: bool
    """Whether to exclude this response from scoring."""

    thread_uuid: Optional[str]
    """Unique identifier for the thread, if any."""

    turn_number: int
    """Turn number in the conversation (default: 1)."""
