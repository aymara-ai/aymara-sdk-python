# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from aymara_ai import AymaraAI, AsyncAymaraAI
from tests.utils import assert_matches_type
from aymara_ai.types import FileUpload, FileCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: AymaraAI) -> None:
        file = client.files.create(
            files=[{}],
        )
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: AymaraAI) -> None:
        file = client.files.create(
            files=[{"local_file_path": "local_file_path"}],
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: AymaraAI) -> None:
        response = client.files.with_raw_response.create(
            files=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: AymaraAI) -> None:
        with client.files.with_streaming_response.create(
            files=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileCreateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_upload(self, client: AymaraAI) -> None:
        file = client.files.upload(
            file=b"raw file contents",
        )
        assert_matches_type(FileUpload, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_upload(self, client: AymaraAI) -> None:
        response = client.files.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileUpload, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_upload(self, client: AymaraAI) -> None:
        with client.files.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileUpload, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncAymaraAI) -> None:
        file = await async_client.files.create(
            files=[{}],
        )
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        file = await async_client.files.create(
            files=[{"local_file_path": "local_file_path"}],
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.files.with_raw_response.create(
            files=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.files.with_streaming_response.create(
            files=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileCreateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_upload(self, async_client: AsyncAymaraAI) -> None:
        file = await async_client.files.upload(
            file=b"raw file contents",
        )
        assert_matches_type(FileUpload, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.files.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileUpload, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.files.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileUpload, file, path=["response"])

        assert cast(Any, response.is_closed) is True
