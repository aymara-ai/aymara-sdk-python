# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from aymara_sdk import AymaraSDK, AsyncAymaraSDK
from tests.utils import assert_matches_type
from aymara_sdk.types import (
    EvalRun,
    EvalRunListResponse,
    EvalRunRunScoreResponse,
    EvalRunGetResponsesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvalRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: AymaraSDK) -> None:
        eval_run = client.eval_runs.create(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                }
            ],
        )
        assert_matches_type(EvalRun, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: AymaraSDK) -> None:
        eval_run = client.eval_runs.create(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                    "ai_refused": True,
                    "content_type": "text",
                    "exclude_from_scoring": True,
                    "generate_prompt": True,
                    "thread_uuid": "thread_uuid",
                    "turn_number": 0,
                }
            ],
            is_sandbox=True,
            workspace_uuid="workspace_uuid",
            ai_description="ai_description",
            eval_run_examples=[
                {
                    "prompt": "prompt",
                    "response": "response",
                    "type": "pass",
                    "explanation": "explanation",
                }
            ],
            eval_run_uuid="eval_run_uuid",
            generate_prompts=True,
            name="name",
        )
        assert_matches_type(EvalRun, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: AymaraSDK) -> None:
        response = client.eval_runs.with_raw_response.create(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_run = response.parse()
        assert_matches_type(EvalRun, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: AymaraSDK) -> None:
        with client.eval_runs.with_streaming_response.create(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_run = response.parse()
            assert_matches_type(EvalRun, eval_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: AymaraSDK) -> None:
        eval_run = client.eval_runs.retrieve(
            eval_run_uuid="eval_run_uuid",
        )
        assert_matches_type(EvalRun, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: AymaraSDK) -> None:
        eval_run = client.eval_runs.retrieve(
            eval_run_uuid="eval_run_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalRun, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: AymaraSDK) -> None:
        response = client.eval_runs.with_raw_response.retrieve(
            eval_run_uuid="eval_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_run = response.parse()
        assert_matches_type(EvalRun, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: AymaraSDK) -> None:
        with client.eval_runs.with_streaming_response.retrieve(
            eval_run_uuid="eval_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_run = response.parse()
            assert_matches_type(EvalRun, eval_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: AymaraSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_run_uuid` but received ''"):
            client.eval_runs.with_raw_response.retrieve(
                eval_run_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: AymaraSDK) -> None:
        eval_run = client.eval_runs.list()
        assert_matches_type(EvalRunListResponse, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: AymaraSDK) -> None:
        eval_run = client.eval_runs.list(
            eval_uuid="eval_uuid",
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalRunListResponse, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: AymaraSDK) -> None:
        response = client.eval_runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_run = response.parse()
        assert_matches_type(EvalRunListResponse, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: AymaraSDK) -> None:
        with client.eval_runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_run = response.parse()
            assert_matches_type(EvalRunListResponse, eval_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: AymaraSDK) -> None:
        eval_run = client.eval_runs.delete(
            eval_run_uuid="eval_run_uuid",
        )
        assert eval_run is None

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: AymaraSDK) -> None:
        eval_run = client.eval_runs.delete(
            eval_run_uuid="eval_run_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert eval_run is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: AymaraSDK) -> None:
        response = client.eval_runs.with_raw_response.delete(
            eval_run_uuid="eval_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_run = response.parse()
        assert eval_run is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: AymaraSDK) -> None:
        with client.eval_runs.with_streaming_response.delete(
            eval_run_uuid="eval_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_run = response.parse()
            assert eval_run is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: AymaraSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_run_uuid` but received ''"):
            client.eval_runs.with_raw_response.delete(
                eval_run_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_responses(self, client: AymaraSDK) -> None:
        eval_run = client.eval_runs.get_responses(
            eval_run_uuid="eval_run_uuid",
        )
        assert_matches_type(EvalRunGetResponsesResponse, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_responses_with_all_params(self, client: AymaraSDK) -> None:
        eval_run = client.eval_runs.get_responses(
            eval_run_uuid="eval_run_uuid",
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalRunGetResponsesResponse, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_responses(self, client: AymaraSDK) -> None:
        response = client.eval_runs.with_raw_response.get_responses(
            eval_run_uuid="eval_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_run = response.parse()
        assert_matches_type(EvalRunGetResponsesResponse, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_responses(self, client: AymaraSDK) -> None:
        with client.eval_runs.with_streaming_response.get_responses(
            eval_run_uuid="eval_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_run = response.parse()
            assert_matches_type(EvalRunGetResponsesResponse, eval_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_responses(self, client: AymaraSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_run_uuid` but received ''"):
            client.eval_runs.with_raw_response.get_responses(
                eval_run_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_run_score(self, client: AymaraSDK) -> None:
        eval_run = client.eval_runs.run_score(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                }
            ],
        )
        assert_matches_type(EvalRunRunScoreResponse, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_score_with_all_params(self, client: AymaraSDK) -> None:
        eval_run = client.eval_runs.run_score(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                    "ai_refused": True,
                    "content_type": "text",
                    "exclude_from_scoring": True,
                    "generate_prompt": True,
                    "thread_uuid": "thread_uuid",
                    "turn_number": 0,
                }
            ],
            is_sandbox=True,
            workspace_uuid="workspace_uuid",
            ai_description="ai_description",
            eval_run_examples=[
                {
                    "prompt": "prompt",
                    "response": "response",
                    "type": "pass",
                    "explanation": "explanation",
                }
            ],
            eval_run_uuid="eval_run_uuid",
            generate_prompts=True,
            name="name",
        )
        assert_matches_type(EvalRunRunScoreResponse, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_score(self, client: AymaraSDK) -> None:
        response = client.eval_runs.with_raw_response.run_score(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_run = response.parse()
        assert_matches_type(EvalRunRunScoreResponse, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_score(self, client: AymaraSDK) -> None:
        with client.eval_runs.with_streaming_response.run_score(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_run = response.parse()
            assert_matches_type(EvalRunRunScoreResponse, eval_run, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvalRuns:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncAymaraSDK) -> None:
        eval_run = await async_client.eval_runs.create(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                }
            ],
        )
        assert_matches_type(EvalRun, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAymaraSDK) -> None:
        eval_run = await async_client.eval_runs.create(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                    "ai_refused": True,
                    "content_type": "text",
                    "exclude_from_scoring": True,
                    "generate_prompt": True,
                    "thread_uuid": "thread_uuid",
                    "turn_number": 0,
                }
            ],
            is_sandbox=True,
            workspace_uuid="workspace_uuid",
            ai_description="ai_description",
            eval_run_examples=[
                {
                    "prompt": "prompt",
                    "response": "response",
                    "type": "pass",
                    "explanation": "explanation",
                }
            ],
            eval_run_uuid="eval_run_uuid",
            generate_prompts=True,
            name="name",
        )
        assert_matches_type(EvalRun, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAymaraSDK) -> None:
        response = await async_client.eval_runs.with_raw_response.create(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_run = await response.parse()
        assert_matches_type(EvalRun, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAymaraSDK) -> None:
        async with async_client.eval_runs.with_streaming_response.create(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_run = await response.parse()
            assert_matches_type(EvalRun, eval_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAymaraSDK) -> None:
        eval_run = await async_client.eval_runs.retrieve(
            eval_run_uuid="eval_run_uuid",
        )
        assert_matches_type(EvalRun, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncAymaraSDK) -> None:
        eval_run = await async_client.eval_runs.retrieve(
            eval_run_uuid="eval_run_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalRun, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAymaraSDK) -> None:
        response = await async_client.eval_runs.with_raw_response.retrieve(
            eval_run_uuid="eval_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_run = await response.parse()
        assert_matches_type(EvalRun, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAymaraSDK) -> None:
        async with async_client.eval_runs.with_streaming_response.retrieve(
            eval_run_uuid="eval_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_run = await response.parse()
            assert_matches_type(EvalRun, eval_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAymaraSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_run_uuid` but received ''"):
            await async_client.eval_runs.with_raw_response.retrieve(
                eval_run_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncAymaraSDK) -> None:
        eval_run = await async_client.eval_runs.list()
        assert_matches_type(EvalRunListResponse, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAymaraSDK) -> None:
        eval_run = await async_client.eval_runs.list(
            eval_uuid="eval_uuid",
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalRunListResponse, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAymaraSDK) -> None:
        response = await async_client.eval_runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_run = await response.parse()
        assert_matches_type(EvalRunListResponse, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAymaraSDK) -> None:
        async with async_client.eval_runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_run = await response.parse()
            assert_matches_type(EvalRunListResponse, eval_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncAymaraSDK) -> None:
        eval_run = await async_client.eval_runs.delete(
            eval_run_uuid="eval_run_uuid",
        )
        assert eval_run is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncAymaraSDK) -> None:
        eval_run = await async_client.eval_runs.delete(
            eval_run_uuid="eval_run_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert eval_run is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAymaraSDK) -> None:
        response = await async_client.eval_runs.with_raw_response.delete(
            eval_run_uuid="eval_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_run = await response.parse()
        assert eval_run is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAymaraSDK) -> None:
        async with async_client.eval_runs.with_streaming_response.delete(
            eval_run_uuid="eval_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_run = await response.parse()
            assert eval_run is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAymaraSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_run_uuid` but received ''"):
            await async_client.eval_runs.with_raw_response.delete(
                eval_run_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_responses(self, async_client: AsyncAymaraSDK) -> None:
        eval_run = await async_client.eval_runs.get_responses(
            eval_run_uuid="eval_run_uuid",
        )
        assert_matches_type(EvalRunGetResponsesResponse, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_responses_with_all_params(self, async_client: AsyncAymaraSDK) -> None:
        eval_run = await async_client.eval_runs.get_responses(
            eval_run_uuid="eval_run_uuid",
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalRunGetResponsesResponse, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_responses(self, async_client: AsyncAymaraSDK) -> None:
        response = await async_client.eval_runs.with_raw_response.get_responses(
            eval_run_uuid="eval_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_run = await response.parse()
        assert_matches_type(EvalRunGetResponsesResponse, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_responses(self, async_client: AsyncAymaraSDK) -> None:
        async with async_client.eval_runs.with_streaming_response.get_responses(
            eval_run_uuid="eval_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_run = await response.parse()
            assert_matches_type(EvalRunGetResponsesResponse, eval_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_responses(self, async_client: AsyncAymaraSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_run_uuid` but received ''"):
            await async_client.eval_runs.with_raw_response.get_responses(
                eval_run_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_score(self, async_client: AsyncAymaraSDK) -> None:
        eval_run = await async_client.eval_runs.run_score(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                }
            ],
        )
        assert_matches_type(EvalRunRunScoreResponse, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_score_with_all_params(self, async_client: AsyncAymaraSDK) -> None:
        eval_run = await async_client.eval_runs.run_score(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                    "ai_refused": True,
                    "content_type": "text",
                    "exclude_from_scoring": True,
                    "generate_prompt": True,
                    "thread_uuid": "thread_uuid",
                    "turn_number": 0,
                }
            ],
            is_sandbox=True,
            workspace_uuid="workspace_uuid",
            ai_description="ai_description",
            eval_run_examples=[
                {
                    "prompt": "prompt",
                    "response": "response",
                    "type": "pass",
                    "explanation": "explanation",
                }
            ],
            eval_run_uuid="eval_run_uuid",
            generate_prompts=True,
            name="name",
        )
        assert_matches_type(EvalRunRunScoreResponse, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_score(self, async_client: AsyncAymaraSDK) -> None:
        response = await async_client.eval_runs.with_raw_response.run_score(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_run = await response.parse()
        assert_matches_type(EvalRunRunScoreResponse, eval_run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_score(self, async_client: AsyncAymaraSDK) -> None:
        async with async_client.eval_runs.with_streaming_response.run_score(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_run = await response.parse()
            assert_matches_type(EvalRunRunScoreResponse, eval_run, path=["response"])

        assert cast(Any, response.is_closed) is True
