# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["PolicyListResponse"]


class PolicyListResponse(BaseModel):
    aymara_policy_name: str

    display_name: str

    policy_text: str

    test_language: str

    test_type: str
