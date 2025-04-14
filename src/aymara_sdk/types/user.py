# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["User", "FeatureFlags", "Organization"]


class FeatureFlags(BaseModel):
    enable_dashboard: bool


class Organization(BaseModel):
    name: str

    org_uuid: str


class User(BaseModel):
    email: str

    feature_flags: FeatureFlags

    is_admin: bool

    is_impersonating: bool

    organization: Optional[Organization] = None
