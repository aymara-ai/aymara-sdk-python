# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from aymara_sdk import AymaraSDK, AsyncAymaraSDK
from tests.utils import assert_matches_type
from aymara_sdk.types import (
    ScoreRunOut,
    ScoreGetAnswersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScores:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: AymaraSDK) -> None:
        score = client.scores.retrieve(
            score_run_uuid="score_run_uuid",
        )
        assert_matches_type(ScoreRunOut, score, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: AymaraSDK) -> None:
        score = client.scores.retrieve(
            score_run_uuid="score_run_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(ScoreRunOut, score, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: AymaraSDK) -> None:
        response = client.scores.with_raw_response.retrieve(
            score_run_uuid="score_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = response.parse()
        assert_matches_type(ScoreRunOut, score, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: AymaraSDK) -> None:
        with client.scores.with_streaming_response.retrieve(
            score_run_uuid="score_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = response.parse()
            assert_matches_type(ScoreRunOut, score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: AymaraSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `score_run_uuid` but received ''"):
            client.scores.with_raw_response.retrieve(
                score_run_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: AymaraSDK) -> None:
        score = client.scores.delete(
            score_run_uuid="score_run_uuid",
        )
        assert score is None

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: AymaraSDK) -> None:
        score = client.scores.delete(
            score_run_uuid="score_run_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert score is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: AymaraSDK) -> None:
        response = client.scores.with_raw_response.delete(
            score_run_uuid="score_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = response.parse()
        assert score is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: AymaraSDK) -> None:
        with client.scores.with_streaming_response.delete(
            score_run_uuid="score_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = response.parse()
            assert score is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: AymaraSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `score_run_uuid` but received ''"):
            client.scores.with_raw_response.delete(
                score_run_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_answers(self, client: AymaraSDK) -> None:
        score = client.scores.get_answers(
            score_run_uuid="score_run_uuid",
        )
        assert_matches_type(ScoreGetAnswersResponse, score, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_answers_with_all_params(self, client: AymaraSDK) -> None:
        score = client.scores.get_answers(
            score_run_uuid="score_run_uuid",
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(ScoreGetAnswersResponse, score, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_answers(self, client: AymaraSDK) -> None:
        response = client.scores.with_raw_response.get_answers(
            score_run_uuid="score_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = response.parse()
        assert_matches_type(ScoreGetAnswersResponse, score, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_answers(self, client: AymaraSDK) -> None:
        with client.scores.with_streaming_response.get_answers(
            score_run_uuid="score_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = response.parse()
            assert_matches_type(ScoreGetAnswersResponse, score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_answers(self, client: AymaraSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `score_run_uuid` but received ''"):
            client.scores.with_raw_response.get_answers(
                score_run_uuid="",
            )


class TestAsyncScores:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAymaraSDK) -> None:
        score = await async_client.scores.retrieve(
            score_run_uuid="score_run_uuid",
        )
        assert_matches_type(ScoreRunOut, score, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncAymaraSDK) -> None:
        score = await async_client.scores.retrieve(
            score_run_uuid="score_run_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(ScoreRunOut, score, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAymaraSDK) -> None:
        response = await async_client.scores.with_raw_response.retrieve(
            score_run_uuid="score_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = await response.parse()
        assert_matches_type(ScoreRunOut, score, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAymaraSDK) -> None:
        async with async_client.scores.with_streaming_response.retrieve(
            score_run_uuid="score_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = await response.parse()
            assert_matches_type(ScoreRunOut, score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAymaraSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `score_run_uuid` but received ''"):
            await async_client.scores.with_raw_response.retrieve(
                score_run_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncAymaraSDK) -> None:
        score = await async_client.scores.delete(
            score_run_uuid="score_run_uuid",
        )
        assert score is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncAymaraSDK) -> None:
        score = await async_client.scores.delete(
            score_run_uuid="score_run_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert score is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAymaraSDK) -> None:
        response = await async_client.scores.with_raw_response.delete(
            score_run_uuid="score_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = await response.parse()
        assert score is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAymaraSDK) -> None:
        async with async_client.scores.with_streaming_response.delete(
            score_run_uuid="score_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = await response.parse()
            assert score is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAymaraSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `score_run_uuid` but received ''"):
            await async_client.scores.with_raw_response.delete(
                score_run_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_answers(self, async_client: AsyncAymaraSDK) -> None:
        score = await async_client.scores.get_answers(
            score_run_uuid="score_run_uuid",
        )
        assert_matches_type(ScoreGetAnswersResponse, score, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_answers_with_all_params(self, async_client: AsyncAymaraSDK) -> None:
        score = await async_client.scores.get_answers(
            score_run_uuid="score_run_uuid",
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(ScoreGetAnswersResponse, score, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_answers(self, async_client: AsyncAymaraSDK) -> None:
        response = await async_client.scores.with_raw_response.get_answers(
            score_run_uuid="score_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = await response.parse()
        assert_matches_type(ScoreGetAnswersResponse, score, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_answers(self, async_client: AsyncAymaraSDK) -> None:
        async with async_client.scores.with_streaming_response.get_answers(
            score_run_uuid="score_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = await response.parse()
            assert_matches_type(ScoreGetAnswersResponse, score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_answers(self, async_client: AsyncAymaraSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `score_run_uuid` but received ''"):
            await async_client.scores.with_raw_response.get_answers(
                score_run_uuid="",
            )
