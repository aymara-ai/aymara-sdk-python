# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel
from ..eval_prompt import EvalPrompt
from .answer_history import AnswerHistory
from ..shared.content_type import ContentType
from ..shared.file_reference import FileReference

__all__ = [
    "ScoredResponse",
    "Content",
    "ManuallyUpdatedBy",
    "ManuallyUpdatedByFeatureFlags",
    "ManuallyUpdatedByOrganization",
    "ManuallyUpdatedByWorkspace",
]

Content: TypeAlias = Union[str, FileReference, None]


class ManuallyUpdatedByFeatureFlags(BaseModel):
    enable_dashboard: bool


class ManuallyUpdatedByOrganization(BaseModel):
    name: str

    org_uuid: str


class ManuallyUpdatedByWorkspace(BaseModel):
    name: Optional[str] = None

    organization_name: Optional[str] = None

    organization_uuid: Optional[str] = None

    workspace_uuid: Optional[str] = None


class ManuallyUpdatedBy(BaseModel):
    email: str

    feature_flags: ManuallyUpdatedByFeatureFlags

    is_admin: bool

    is_impersonating: bool

    org_admin_emails: Optional[List[str]] = None

    organization: Optional[ManuallyUpdatedByOrganization] = None

    workspace: Optional[ManuallyUpdatedByWorkspace] = None


class ScoredResponse(BaseModel):
    prompt_uuid: str
    """Unique identifier for the prompt."""

    ai_refused: Optional[bool] = None
    """Whether the AI refused to answer the prompt."""

    confidence: Optional[float] = None
    """Confidence score for the response, if any."""

    content: Optional[Content] = None
    """Content of the AI response or a file reference."""

    content_type: Optional[ContentType] = None
    """Content type for AI interactions."""

    continue_thread: Optional[bool] = None
    """Whether to continue the thread after this response."""

    exclude_from_scoring: Optional[bool] = None
    """Whether to exclude this response from scoring."""

    explanation: Optional[str] = None
    """Explanation for the response, if any."""

    is_passed: Optional[bool] = None
    """Whether the response passed the evaluation, if any."""

    manually_updated: Optional[bool] = None
    """Whether this response was manually updated."""

    manually_updated_at: Optional[datetime] = None
    """Timestamp when this response was last manually updated."""

    manually_updated_by: Optional[ManuallyUpdatedBy] = None
    """User who last manually updated this response."""

    next_prompt: Optional[EvalPrompt] = None
    """Next prompt in the evaluation, if any."""

    response_uuid: Optional[str] = None
    """Unique identifier for the response, if any."""

    thread_uuid: Optional[str] = None
    """Unique identifier for the thread, if any."""

    turn_number: Optional[int] = None
    """Turn number in the conversation (default: 1)."""

    update_history: Optional[List[AnswerHistory]] = None
    """History of manual updates, if requested."""
