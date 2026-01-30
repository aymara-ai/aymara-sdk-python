# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["AnswerHistory", "UpdatedBy", "UpdatedByFeatureFlags", "UpdatedByOrganization", "UpdatedByWorkspace"]


class UpdatedByFeatureFlags(BaseModel):
    enable_dashboard: bool


class UpdatedByOrganization(BaseModel):
    name: str

    org_uuid: str


class UpdatedByWorkspace(BaseModel):
    name: Optional[str] = None

    organization_name: Optional[str] = None

    organization_uuid: Optional[str] = None

    workspace_uuid: Optional[str] = None


class UpdatedBy(BaseModel):
    email: str

    feature_flags: UpdatedByFeatureFlags

    is_admin: bool

    is_impersonating: bool

    org_admin_emails: Optional[List[str]] = None

    organization: Optional[UpdatedByOrganization] = None

    workspace: Optional[UpdatedByWorkspace] = None


class AnswerHistory(BaseModel):
    answer_history_uuid: str
    """Unique identifier for the history entry."""

    updated_at: datetime
    """Timestamp when the update was made."""

    new_confidence: Optional[float] = None
    """New confidence value."""

    new_explanation: Optional[str] = None
    """New explanation value."""

    new_is_passed: Optional[bool] = None
    """New is_passed value."""

    previous_confidence: Optional[float] = None
    """Previous confidence value."""

    previous_explanation: Optional[str] = None
    """Previous explanation value."""

    previous_is_passed: Optional[bool] = None
    """Previous is_passed value."""

    updated_by: Optional[UpdatedBy] = None
    """User who made the update."""
