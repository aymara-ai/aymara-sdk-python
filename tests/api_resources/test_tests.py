# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from aymara_sdk import AymaraSDK, AsyncAymaraSDK
from tests.utils import assert_matches_type
from aymara_sdk.types import (
    TestOut,
    TestListResponse,
    TestRetrieveQuestionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: AymaraSDK) -> None:
        test = client.tests.create(
            student_description="student_description",
            test_name="test_name",
        )
        assert_matches_type(TestOut, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: AymaraSDK) -> None:
        test = client.tests.create(
            student_description="student_description",
            test_name="test_name",
            is_sandbox=True,
            workspace_uuid="workspace_uuid",
            additional_instructions="additional_instructions",
            is_jailbreak=True,
            knowledge_base="knowledge_base",
            modality="text",
            num_test_questions=0,
            test_examples=[
                {
                    "example_text": "example_text",
                    "example_type": "good",
                    "explanation": "explanation",
                }
            ],
            test_language="test_language",
            test_policy="test_policy",
            test_system_prompt="test_system_prompt",
            test_type="test_type",
        )
        assert_matches_type(TestOut, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: AymaraSDK) -> None:
        response = client.tests.with_raw_response.create(
            student_description="student_description",
            test_name="test_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(TestOut, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: AymaraSDK) -> None:
        with client.tests.with_streaming_response.create(
            student_description="student_description",
            test_name="test_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(TestOut, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: AymaraSDK) -> None:
        test = client.tests.retrieve(
            test_uuid="test_uuid",
        )
        assert_matches_type(TestOut, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: AymaraSDK) -> None:
        test = client.tests.retrieve(
            test_uuid="test_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(TestOut, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: AymaraSDK) -> None:
        response = client.tests.with_raw_response.retrieve(
            test_uuid="test_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(TestOut, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: AymaraSDK) -> None:
        with client.tests.with_streaming_response.retrieve(
            test_uuid="test_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(TestOut, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: AymaraSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_uuid` but received ''"):
            client.tests.with_raw_response.retrieve(
                test_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: AymaraSDK) -> None:
        test = client.tests.list()
        assert_matches_type(TestListResponse, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: AymaraSDK) -> None:
        test = client.tests.list(
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(TestListResponse, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: AymaraSDK) -> None:
        response = client.tests.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(TestListResponse, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: AymaraSDK) -> None:
        with client.tests.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(TestListResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: AymaraSDK) -> None:
        test = client.tests.delete(
            test_uuid="test_uuid",
        )
        assert test is None

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: AymaraSDK) -> None:
        test = client.tests.delete(
            test_uuid="test_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert test is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: AymaraSDK) -> None:
        response = client.tests.with_raw_response.delete(
            test_uuid="test_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert test is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: AymaraSDK) -> None:
        with client.tests.with_streaming_response.delete(
            test_uuid="test_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert test is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: AymaraSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_uuid` but received ''"):
            client.tests.with_raw_response.delete(
                test_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_questions(self, client: AymaraSDK) -> None:
        test = client.tests.retrieve_questions(
            test_uuid="test_uuid",
        )
        assert_matches_type(TestRetrieveQuestionsResponse, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_questions_with_all_params(self, client: AymaraSDK) -> None:
        test = client.tests.retrieve_questions(
            test_uuid="test_uuid",
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(TestRetrieveQuestionsResponse, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_questions(self, client: AymaraSDK) -> None:
        response = client.tests.with_raw_response.retrieve_questions(
            test_uuid="test_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(TestRetrieveQuestionsResponse, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_questions(self, client: AymaraSDK) -> None:
        with client.tests.with_streaming_response.retrieve_questions(
            test_uuid="test_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(TestRetrieveQuestionsResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_questions(self, client: AymaraSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_uuid` but received ''"):
            client.tests.with_raw_response.retrieve_questions(
                test_uuid="",
            )


class TestAsyncTests:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncAymaraSDK) -> None:
        test = await async_client.tests.create(
            student_description="student_description",
            test_name="test_name",
        )
        assert_matches_type(TestOut, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAymaraSDK) -> None:
        test = await async_client.tests.create(
            student_description="student_description",
            test_name="test_name",
            is_sandbox=True,
            workspace_uuid="workspace_uuid",
            additional_instructions="additional_instructions",
            is_jailbreak=True,
            knowledge_base="knowledge_base",
            modality="text",
            num_test_questions=0,
            test_examples=[
                {
                    "example_text": "example_text",
                    "example_type": "good",
                    "explanation": "explanation",
                }
            ],
            test_language="test_language",
            test_policy="test_policy",
            test_system_prompt="test_system_prompt",
            test_type="test_type",
        )
        assert_matches_type(TestOut, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAymaraSDK) -> None:
        response = await async_client.tests.with_raw_response.create(
            student_description="student_description",
            test_name="test_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(TestOut, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAymaraSDK) -> None:
        async with async_client.tests.with_streaming_response.create(
            student_description="student_description",
            test_name="test_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(TestOut, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAymaraSDK) -> None:
        test = await async_client.tests.retrieve(
            test_uuid="test_uuid",
        )
        assert_matches_type(TestOut, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncAymaraSDK) -> None:
        test = await async_client.tests.retrieve(
            test_uuid="test_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(TestOut, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAymaraSDK) -> None:
        response = await async_client.tests.with_raw_response.retrieve(
            test_uuid="test_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(TestOut, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAymaraSDK) -> None:
        async with async_client.tests.with_streaming_response.retrieve(
            test_uuid="test_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(TestOut, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAymaraSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_uuid` but received ''"):
            await async_client.tests.with_raw_response.retrieve(
                test_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncAymaraSDK) -> None:
        test = await async_client.tests.list()
        assert_matches_type(TestListResponse, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAymaraSDK) -> None:
        test = await async_client.tests.list(
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(TestListResponse, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAymaraSDK) -> None:
        response = await async_client.tests.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(TestListResponse, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAymaraSDK) -> None:
        async with async_client.tests.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(TestListResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncAymaraSDK) -> None:
        test = await async_client.tests.delete(
            test_uuid="test_uuid",
        )
        assert test is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncAymaraSDK) -> None:
        test = await async_client.tests.delete(
            test_uuid="test_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert test is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAymaraSDK) -> None:
        response = await async_client.tests.with_raw_response.delete(
            test_uuid="test_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert test is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAymaraSDK) -> None:
        async with async_client.tests.with_streaming_response.delete(
            test_uuid="test_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert test is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAymaraSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_uuid` but received ''"):
            await async_client.tests.with_raw_response.delete(
                test_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_questions(self, async_client: AsyncAymaraSDK) -> None:
        test = await async_client.tests.retrieve_questions(
            test_uuid="test_uuid",
        )
        assert_matches_type(TestRetrieveQuestionsResponse, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_questions_with_all_params(self, async_client: AsyncAymaraSDK) -> None:
        test = await async_client.tests.retrieve_questions(
            test_uuid="test_uuid",
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(TestRetrieveQuestionsResponse, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_questions(self, async_client: AsyncAymaraSDK) -> None:
        response = await async_client.tests.with_raw_response.retrieve_questions(
            test_uuid="test_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(TestRetrieveQuestionsResponse, test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_questions(self, async_client: AsyncAymaraSDK) -> None:
        async with async_client.tests.with_streaming_response.retrieve_questions(
            test_uuid="test_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(TestRetrieveQuestionsResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_questions(self, async_client: AsyncAymaraSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_uuid` but received ''"):
            await async_client.tests.with_raw_response.retrieve_questions(
                test_uuid="",
            )
