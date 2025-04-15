# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from aymara_ai import AymaraSDK, AsyncAymaraSDK
from tests.utils import assert_matches_type
from aymara_ai.types import FileUploadResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_upload(self, client: AymaraSDK) -> None:
        file = client.files.upload(
            answers=[{"question_uuid": "question_uuid"}],
            test_uuid="test_uuid",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_upload(self, client: AymaraSDK) -> None:
        response = client.files.with_raw_response.upload(
            answers=[{"question_uuid": "question_uuid"}],
            test_uuid="test_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_upload(self, client: AymaraSDK) -> None:
        with client.files.with_streaming_response.upload(
            answers=[{"question_uuid": "question_uuid"}],
            test_uuid="test_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileUploadResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_upload(self, async_client: AsyncAymaraSDK) -> None:
        file = await async_client.files.upload(
            answers=[{"question_uuid": "question_uuid"}],
            test_uuid="test_uuid",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncAymaraSDK) -> None:
        response = await async_client.files.with_raw_response.upload(
            answers=[{"question_uuid": "question_uuid"}],
            test_uuid="test_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncAymaraSDK) -> None:
        async with async_client.files.with_streaming_response.upload(
            answers=[{"question_uuid": "question_uuid"}],
            test_uuid="test_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileUploadResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True
