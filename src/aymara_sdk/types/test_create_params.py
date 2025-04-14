# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .content_type import ContentType
from .example_type import ExampleType

__all__ = ["TestCreateParams", "TestExample"]


class TestCreateParams(TypedDict, total=False):
    student_description: Required[str]

    test_name: Required[str]

    is_sandbox: Optional[bool]

    workspace_uuid: str

    additional_instructions: Optional[str]

    is_jailbreak: bool

    knowledge_base: Optional[str]

    modality: ContentType
    """Content type for AI interactions."""

    num_test_questions: Optional[int]

    test_examples: Optional[Iterable[TestExample]]

    test_language: str

    test_policy: Optional[str]

    test_system_prompt: Optional[str]

    test_type: str


class TestExample(TypedDict, total=False):
    example_text: Required[str]

    example_type: Required[ExampleType]

    explanation: Optional[str]
