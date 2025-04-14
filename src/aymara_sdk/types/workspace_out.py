# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["WorkspaceOut"]


class WorkspaceOut(BaseModel):
    name: str

    organization_name: str

    workspace_uuid: str
