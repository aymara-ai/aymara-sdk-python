# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .content_type import ContentType
from .example_type import ExampleType

__all__ = ["TestOut", "TestExample"]


class TestExample(BaseModel):
    __test__ = False
    example_text: str

    example_type: ExampleType

    example_uuid: str

    explanation: Optional[str] = None


class TestOut(BaseModel):
    __test__ = False
    created_at: datetime

    test_name: str

    test_status: Literal["record_created", "generating_questions", "finished", "failed"]
    """Test status."""

    test_type: str

    test_uuid: str

    updated_at: datetime

    additional_instructions: Optional[str] = None

    is_jailbreak: Optional[bool] = None

    knowledge_base: Optional[str] = None

    modality: Optional[ContentType] = None
    """Content type for AI interactions."""

    num_test_questions: Optional[int] = None

    organization_name: Optional[str] = None

    test_examples: Optional[List[TestExample]] = None

    test_policy: Optional[str] = None

    test_system_prompt: Optional[str] = None
