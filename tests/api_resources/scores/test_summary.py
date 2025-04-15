# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from aymara_ai import AymaraAI, AsyncAymaraAI
from tests.utils import assert_matches_type
from aymara_ai.types.scores import (
    ScoreRunSuiteSummaryOut,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSummary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_summary(self, client: AymaraAI) -> None:
        summary = client.scores.summary.delete_summary(
            summary_uuid="summary_uuid",
        )
        assert summary is None

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_summary_with_all_params(self, client: AymaraAI) -> None:
        summary = client.scores.summary.delete_summary(
            summary_uuid="summary_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert summary is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete_summary(self, client: AymaraAI) -> None:
        response = client.scores.summary.with_raw_response.delete_summary(
            summary_uuid="summary_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert summary is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete_summary(self, client: AymaraAI) -> None:
        with client.scores.summary.with_streaming_response.delete_summary(
            summary_uuid="summary_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert summary is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete_summary(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `summary_uuid` but received ''"):
            client.scores.summary.with_raw_response.delete_summary(
                summary_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_summary(self, client: AymaraAI) -> None:
        summary = client.scores.summary.retrieve_summary(
            summary_uuid="summary_uuid",
        )
        assert_matches_type(ScoreRunSuiteSummaryOut, summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_summary_with_all_params(self, client: AymaraAI) -> None:
        summary = client.scores.summary.retrieve_summary(
            summary_uuid="summary_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(ScoreRunSuiteSummaryOut, summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_summary(self, client: AymaraAI) -> None:
        response = client.scores.summary.with_raw_response.retrieve_summary(
            summary_uuid="summary_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(ScoreRunSuiteSummaryOut, summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_summary(self, client: AymaraAI) -> None:
        with client.scores.summary.with_streaming_response.retrieve_summary(
            summary_uuid="summary_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(ScoreRunSuiteSummaryOut, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_summary(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `summary_uuid` but received ''"):
            client.scores.summary.with_raw_response.retrieve_summary(
                summary_uuid="",
            )


class TestAsyncSummary:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_summary(self, async_client: AsyncAymaraAI) -> None:
        summary = await async_client.scores.summary.delete_summary(
            summary_uuid="summary_uuid",
        )
        assert summary is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_summary_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        summary = await async_client.scores.summary.delete_summary(
            summary_uuid="summary_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert summary is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete_summary(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.scores.summary.with_raw_response.delete_summary(
            summary_uuid="summary_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert summary is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete_summary(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.scores.summary.with_streaming_response.delete_summary(
            summary_uuid="summary_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert summary is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete_summary(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `summary_uuid` but received ''"):
            await async_client.scores.summary.with_raw_response.delete_summary(
                summary_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_summary(self, async_client: AsyncAymaraAI) -> None:
        summary = await async_client.scores.summary.retrieve_summary(
            summary_uuid="summary_uuid",
        )
        assert_matches_type(ScoreRunSuiteSummaryOut, summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_summary_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        summary = await async_client.scores.summary.retrieve_summary(
            summary_uuid="summary_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(ScoreRunSuiteSummaryOut, summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_summary(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.scores.summary.with_raw_response.retrieve_summary(
            summary_uuid="summary_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(ScoreRunSuiteSummaryOut, summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_summary(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.scores.summary.with_streaming_response.retrieve_summary(
            summary_uuid="summary_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(ScoreRunSuiteSummaryOut, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_summary(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `summary_uuid` but received ''"):
            await async_client.scores.summary.with_raw_response.retrieve_summary(
                summary_uuid="",
            )
