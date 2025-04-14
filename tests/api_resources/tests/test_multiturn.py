# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from aymara_sdk import AymaraSDK, AsyncAymaraSDK
from tests.utils import assert_matches_type
from aymara_sdk.types.tests import MultiturnContinueResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMultiturn:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_continue(self, client: AymaraSDK) -> None:
        multiturn = client.tests.multiturn.continue_(
            test_uuid="test_uuid",
        )
        assert_matches_type(MultiturnContinueResponse, multiturn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_continue_with_all_params(self, client: AymaraSDK) -> None:
        multiturn = client.tests.multiturn.continue_(
            test_uuid="test_uuid",
            continue_eval=True,
            is_sandbox=True,
            answers=[
                {
                    "question_uuid": "question_uuid",
                    "answer_image_path": "answer_image_path",
                    "answer_text": "answer_text",
                    "exclude_from_scoring": True,
                    "student_refused": True,
                }
            ],
        )
        assert_matches_type(MultiturnContinueResponse, multiturn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_continue(self, client: AymaraSDK) -> None:
        response = client.tests.multiturn.with_raw_response.continue_(
            test_uuid="test_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multiturn = response.parse()
        assert_matches_type(MultiturnContinueResponse, multiturn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_continue(self, client: AymaraSDK) -> None:
        with client.tests.multiturn.with_streaming_response.continue_(
            test_uuid="test_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multiturn = response.parse()
            assert_matches_type(MultiturnContinueResponse, multiturn, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMultiturn:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_continue(self, async_client: AsyncAymaraSDK) -> None:
        multiturn = await async_client.tests.multiturn.continue_(
            test_uuid="test_uuid",
        )
        assert_matches_type(MultiturnContinueResponse, multiturn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_continue_with_all_params(self, async_client: AsyncAymaraSDK) -> None:
        multiturn = await async_client.tests.multiturn.continue_(
            test_uuid="test_uuid",
            continue_eval=True,
            is_sandbox=True,
            answers=[
                {
                    "question_uuid": "question_uuid",
                    "answer_image_path": "answer_image_path",
                    "answer_text": "answer_text",
                    "exclude_from_scoring": True,
                    "student_refused": True,
                }
            ],
        )
        assert_matches_type(MultiturnContinueResponse, multiturn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_continue(self, async_client: AsyncAymaraSDK) -> None:
        response = await async_client.tests.multiturn.with_raw_response.continue_(
            test_uuid="test_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multiturn = await response.parse()
        assert_matches_type(MultiturnContinueResponse, multiturn, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_continue(self, async_client: AsyncAymaraSDK) -> None:
        async with async_client.tests.multiturn.with_streaming_response.continue_(
            test_uuid="test_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multiturn = await response.parse()
            assert_matches_type(MultiturnContinueResponse, multiturn, path=["response"])

        assert cast(Any, response.is_closed) is True
