# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from aymara_ai import AymaraAI, AsyncAymaraAI
from tests.utils import assert_matches_type
from aymara_ai.types import (
    FileDetail,
    FileFrames,
    FileStatus,
    FileUpload,
    FileCreateResponse,
)
from aymara_ai.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: AymaraAI) -> None:
        file = client.files.create(
            files=[{}],
        )
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: AymaraAI) -> None:
        file = client.files.create(
            files=[
                {
                    "content_type": "content_type",
                    "local_file_path": "local_file_path",
                    "remote_uri": "remote_uri",
                }
            ],
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: AymaraAI) -> None:
        response = client.files.with_raw_response.create(
            files=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: AymaraAI) -> None:
        file = client.files.list()
        assert_matches_type(SyncOffsetPage[FileDetail], file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: AymaraAI) -> None:
        file = client.files.list(
            file_type="file_type",
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(SyncOffsetPage[FileDetail], file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: AymaraAI) -> None:
        response = client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(SyncOffsetPage[FileDetail], file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: AymaraAI) -> None:
        with client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(SyncOffsetPage[FileDetail], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: AymaraAI) -> None:
        file = client.files.delete(
            "file_uuid",
        )
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: AymaraAI) -> None:
        response = client.files.with_raw_response.delete(
            "file_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: AymaraAI) -> None:
        with client.files.with_streaming_response.delete(
            "file_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_uuid` but received ''"):
            client.files.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: AymaraAI) -> None:
        file = client.files.get(
            "file_uuid",
        )
        assert_matches_type(FileDetail, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: AymaraAI) -> None:
        response = client.files.with_raw_response.get(
            "file_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileDetail, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: AymaraAI) -> None:
        with client.files.with_streaming_response.get(
            "file_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileDetail, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_uuid` but received ''"):
            client.files.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_frames(self, client: AymaraAI) -> None:
        file = client.files.get_frames(
            "file_uuid",
        )
        assert_matches_type(FileFrames, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_frames(self, client: AymaraAI) -> None:
        response = client.files.with_raw_response.get_frames(
            "file_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileFrames, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_frames(self, client: AymaraAI) -> None:
        with client.files.with_streaming_response.get_frames(
            "file_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileFrames, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_frames(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_uuid` but received ''"):
            client.files.with_raw_response.get_frames(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_status(self, client: AymaraAI) -> None:
        file = client.files.get_status(
            "file_uuid",
        )
        assert_matches_type(FileStatus, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: AymaraAI) -> None:
        response = client.files.with_raw_response.get_status(
            "file_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileStatus, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: AymaraAI) -> None:
        with client.files.with_streaming_response.get_status(
            "file_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileStatus, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_status(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_uuid` but received ''"):
            client.files.with_raw_response.get_status(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload(self, client: AymaraAI) -> None:
        file = client.files.upload(
            file=b"raw file contents",
        )
        assert_matches_type(FileUpload, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: AymaraAI) -> None:
        file = client.files.upload(
            file=b"raw file contents",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(FileUpload, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: AymaraAI) -> None:
        response = client.files.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileUpload, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAymaraAI) -> None:
        file = await async_client.files.create(
            files=[{}],
        )
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        file = await async_client.files.create(
            files=[
                {
                    "content_type": "content_type",
                    "local_file_path": "local_file_path",
                    "remote_uri": "remote_uri",
                }
            ],
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.files.with_raw_response.create(
            files=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAymaraAI) -> None:
        file = await async_client.files.list()
        assert_matches_type(AsyncOffsetPage[FileDetail], file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        file = await async_client.files.list(
            file_type="file_type",
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(AsyncOffsetPage[FileDetail], file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(AsyncOffsetPage[FileDetail], file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(AsyncOffsetPage[FileDetail], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncAymaraAI) -> None:
        file = await async_client.files.delete(
            "file_uuid",
        )
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.files.with_raw_response.delete(
            "file_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.files.with_streaming_response.delete(
            "file_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_uuid` but received ''"):
            await async_client.files.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncAymaraAI) -> None:
        file = await async_client.files.get(
            "file_uuid",
        )
        assert_matches_type(FileDetail, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.files.with_raw_response.get(
            "file_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileDetail, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.files.with_streaming_response.get(
            "file_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileDetail, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_uuid` but received ''"):
            await async_client.files.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_frames(self, async_client: AsyncAymaraAI) -> None:
        file = await async_client.files.get_frames(
            "file_uuid",
        )
        assert_matches_type(FileFrames, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_frames(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.files.with_raw_response.get_frames(
            "file_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileFrames, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_frames(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.files.with_streaming_response.get_frames(
            "file_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileFrames, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_frames(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_uuid` but received ''"):
            await async_client.files.with_raw_response.get_frames(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncAymaraAI) -> None:
        file = await async_client.files.get_status(
            "file_uuid",
        )
        assert_matches_type(FileStatus, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.files.with_raw_response.get_status(
            "file_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileStatus, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.files.with_streaming_response.get_status(
            "file_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileStatus, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_uuid` but received ''"):
            await async_client.files.with_raw_response.get_status(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncAymaraAI) -> None:
        file = await async_client.files.upload(
            file=b"raw file contents",
        )
        assert_matches_type(FileUpload, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        file = await async_client.files.upload(
            file=b"raw file contents",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(FileUpload, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.files.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileUpload, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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
