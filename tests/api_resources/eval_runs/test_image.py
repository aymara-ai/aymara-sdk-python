# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from aymara_sdk import AymaraSDK, AsyncAymaraSDK
from tests.utils import assert_matches_type
from aymara_sdk.types.eval_runs import ImageGetPresignedURLsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_presigned_urls(self, client: AymaraSDK) -> None:
        image = client.eval_runs.image.get_presigned_urls(
            answers=[{"question_uuid": "question_uuid"}],
            test_uuid="test_uuid",
        )
        assert_matches_type(ImageGetPresignedURLsResponse, image, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_presigned_urls(self, client: AymaraSDK) -> None:
        response = client.eval_runs.image.with_raw_response.get_presigned_urls(
            answers=[{"question_uuid": "question_uuid"}],
            test_uuid="test_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(ImageGetPresignedURLsResponse, image, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_presigned_urls(self, client: AymaraSDK) -> None:
        with client.eval_runs.image.with_streaming_response.get_presigned_urls(
            answers=[{"question_uuid": "question_uuid"}],
            test_uuid="test_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(ImageGetPresignedURLsResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncImage:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_presigned_urls(self, async_client: AsyncAymaraSDK) -> None:
        image = await async_client.eval_runs.image.get_presigned_urls(
            answers=[{"question_uuid": "question_uuid"}],
            test_uuid="test_uuid",
        )
        assert_matches_type(ImageGetPresignedURLsResponse, image, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_presigned_urls(self, async_client: AsyncAymaraSDK) -> None:
        response = await async_client.eval_runs.image.with_raw_response.get_presigned_urls(
            answers=[{"question_uuid": "question_uuid"}],
            test_uuid="test_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(ImageGetPresignedURLsResponse, image, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_presigned_urls(self, async_client: AsyncAymaraSDK) -> None:
        async with async_client.eval_runs.image.with_streaming_response.get_presigned_urls(
            answers=[{"question_uuid": "question_uuid"}],
            test_uuid="test_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(ImageGetPresignedURLsResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True
