# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from aymara_ai import AymaraAI, AsyncAymaraAI
from tests.utils import assert_matches_type
from aymara_ai.pagination import SyncOffsetPage, AsyncOffsetPage
from aymara_ai.types.evals import (
    EvalRunResult,
    RunListResponsesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: AymaraAI) -> None:
        run = client.evals.runs.create(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                }
            ],
        )
        assert_matches_type(EvalRunResult, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: AymaraAI) -> None:
        run = client.evals.runs.create(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                    "ai_refused": True,
                    "content_type": "text",
                    "continue_thread": True,
                    "exclude_from_scoring": True,
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
                    "example_uuid": "example_uuid",
                    "explanation": "explanation",
                }
            ],
            generate_prompts=True,
            name="name",
        )
        assert_matches_type(EvalRunResult, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: AymaraAI) -> None:
        response = client.evals.runs.with_raw_response.create(
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
        run = response.parse()
        assert_matches_type(EvalRunResult, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: AymaraAI) -> None:
        with client.evals.runs.with_streaming_response.create(
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

            run = response.parse()
            assert_matches_type(EvalRunResult, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: AymaraAI) -> None:
        run = client.evals.runs.list()
        assert_matches_type(SyncOffsetPage[EvalRunResult], run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: AymaraAI) -> None:
        run = client.evals.runs.list(
            eval_uuid="eval_uuid",
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(SyncOffsetPage[EvalRunResult], run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: AymaraAI) -> None:
        response = client.evals.runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(SyncOffsetPage[EvalRunResult], run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: AymaraAI) -> None:
        with client.evals.runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(SyncOffsetPage[EvalRunResult], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: AymaraAI) -> None:
        run = client.evals.runs.delete(
            eval_run_uuid="eval_run_uuid",
        )
        assert run is None

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: AymaraAI) -> None:
        run = client.evals.runs.delete(
            eval_run_uuid="eval_run_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert run is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: AymaraAI) -> None:
        response = client.evals.runs.with_raw_response.delete(
            eval_run_uuid="eval_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert run is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: AymaraAI) -> None:
        with client.evals.runs.with_streaming_response.delete(
            eval_run_uuid="eval_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert run is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_run_uuid` but received ''"):
            client.evals.runs.with_raw_response.delete(
                eval_run_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_continue_run(self, client: AymaraAI) -> None:
        run = client.evals.runs.continue_run(
            eval_run_uuid="eval_run_uuid",
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                }
            ],
        )
        assert_matches_type(EvalRunResult, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_continue_run_with_all_params(self, client: AymaraAI) -> None:
        run = client.evals.runs.continue_run(
            eval_run_uuid="eval_run_uuid",
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                    "ai_refused": True,
                    "content_type": "text",
                    "continue_thread": True,
                    "exclude_from_scoring": True,
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
                    "example_uuid": "example_uuid",
                    "explanation": "explanation",
                }
            ],
            generate_prompts=True,
            name="name",
        )
        assert_matches_type(EvalRunResult, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_continue_run(self, client: AymaraAI) -> None:
        response = client.evals.runs.with_raw_response.continue_run(
            eval_run_uuid="eval_run_uuid",
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
        run = response.parse()
        assert_matches_type(EvalRunResult, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_continue_run(self, client: AymaraAI) -> None:
        with client.evals.runs.with_streaming_response.continue_run(
            eval_run_uuid="eval_run_uuid",
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

            run = response.parse()
            assert_matches_type(EvalRunResult, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_continue_run(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_run_uuid` but received ''"):
            client.evals.runs.with_raw_response.continue_run(
                eval_run_uuid="",
                eval_uuid="eval_uuid",
                responses=[
                    {
                        "content": "content",
                        "prompt_uuid": "prompt_uuid",
                    }
                ],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: AymaraAI) -> None:
        run = client.evals.runs.get(
            eval_run_uuid="eval_run_uuid",
        )
        assert_matches_type(EvalRunResult, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: AymaraAI) -> None:
        run = client.evals.runs.get(
            eval_run_uuid="eval_run_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalRunResult, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: AymaraAI) -> None:
        response = client.evals.runs.with_raw_response.get(
            eval_run_uuid="eval_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(EvalRunResult, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: AymaraAI) -> None:
        with client.evals.runs.with_streaming_response.get(
            eval_run_uuid="eval_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(EvalRunResult, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_run_uuid` but received ''"):
            client.evals.runs.with_raw_response.get(
                eval_run_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_responses(self, client: AymaraAI) -> None:
        run = client.evals.runs.list_responses(
            eval_run_uuid="eval_run_uuid",
        )
        assert_matches_type(SyncOffsetPage[RunListResponsesResponse], run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_responses_with_all_params(self, client: AymaraAI) -> None:
        run = client.evals.runs.list_responses(
            eval_run_uuid="eval_run_uuid",
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(SyncOffsetPage[RunListResponsesResponse], run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_responses(self, client: AymaraAI) -> None:
        response = client.evals.runs.with_raw_response.list_responses(
            eval_run_uuid="eval_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(SyncOffsetPage[RunListResponsesResponse], run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_responses(self, client: AymaraAI) -> None:
        with client.evals.runs.with_streaming_response.list_responses(
            eval_run_uuid="eval_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(SyncOffsetPage[RunListResponsesResponse], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_responses(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_run_uuid` but received ''"):
            client.evals.runs.with_raw_response.list_responses(
                eval_run_uuid="",
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncAymaraAI) -> None:
        run = await async_client.evals.runs.create(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                }
            ],
        )
        assert_matches_type(EvalRunResult, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        run = await async_client.evals.runs.create(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                    "ai_refused": True,
                    "content_type": "text",
                    "continue_thread": True,
                    "exclude_from_scoring": True,
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
                    "example_uuid": "example_uuid",
                    "explanation": "explanation",
                }
            ],
            generate_prompts=True,
            name="name",
        )
        assert_matches_type(EvalRunResult, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.evals.runs.with_raw_response.create(
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
        run = await response.parse()
        assert_matches_type(EvalRunResult, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.evals.runs.with_streaming_response.create(
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

            run = await response.parse()
            assert_matches_type(EvalRunResult, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncAymaraAI) -> None:
        run = await async_client.evals.runs.list()
        assert_matches_type(AsyncOffsetPage[EvalRunResult], run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        run = await async_client.evals.runs.list(
            eval_uuid="eval_uuid",
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(AsyncOffsetPage[EvalRunResult], run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.evals.runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(AsyncOffsetPage[EvalRunResult], run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.evals.runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(AsyncOffsetPage[EvalRunResult], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncAymaraAI) -> None:
        run = await async_client.evals.runs.delete(
            eval_run_uuid="eval_run_uuid",
        )
        assert run is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        run = await async_client.evals.runs.delete(
            eval_run_uuid="eval_run_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert run is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.evals.runs.with_raw_response.delete(
            eval_run_uuid="eval_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert run is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.evals.runs.with_streaming_response.delete(
            eval_run_uuid="eval_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert run is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_run_uuid` but received ''"):
            await async_client.evals.runs.with_raw_response.delete(
                eval_run_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_continue_run(self, async_client: AsyncAymaraAI) -> None:
        run = await async_client.evals.runs.continue_run(
            eval_run_uuid="eval_run_uuid",
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                }
            ],
        )
        assert_matches_type(EvalRunResult, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_continue_run_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        run = await async_client.evals.runs.continue_run(
            eval_run_uuid="eval_run_uuid",
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                    "ai_refused": True,
                    "content_type": "text",
                    "continue_thread": True,
                    "exclude_from_scoring": True,
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
                    "example_uuid": "example_uuid",
                    "explanation": "explanation",
                }
            ],
            generate_prompts=True,
            name="name",
        )
        assert_matches_type(EvalRunResult, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_continue_run(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.evals.runs.with_raw_response.continue_run(
            eval_run_uuid="eval_run_uuid",
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
        run = await response.parse()
        assert_matches_type(EvalRunResult, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_continue_run(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.evals.runs.with_streaming_response.continue_run(
            eval_run_uuid="eval_run_uuid",
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

            run = await response.parse()
            assert_matches_type(EvalRunResult, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_continue_run(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_run_uuid` but received ''"):
            await async_client.evals.runs.with_raw_response.continue_run(
                eval_run_uuid="",
                eval_uuid="eval_uuid",
                responses=[
                    {
                        "content": "content",
                        "prompt_uuid": "prompt_uuid",
                    }
                ],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncAymaraAI) -> None:
        run = await async_client.evals.runs.get(
            eval_run_uuid="eval_run_uuid",
        )
        assert_matches_type(EvalRunResult, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        run = await async_client.evals.runs.get(
            eval_run_uuid="eval_run_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalRunResult, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.evals.runs.with_raw_response.get(
            eval_run_uuid="eval_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(EvalRunResult, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.evals.runs.with_streaming_response.get(
            eval_run_uuid="eval_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(EvalRunResult, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_run_uuid` but received ''"):
            await async_client.evals.runs.with_raw_response.get(
                eval_run_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_responses(self, async_client: AsyncAymaraAI) -> None:
        run = await async_client.evals.runs.list_responses(
            eval_run_uuid="eval_run_uuid",
        )
        assert_matches_type(AsyncOffsetPage[RunListResponsesResponse], run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_responses_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        run = await async_client.evals.runs.list_responses(
            eval_run_uuid="eval_run_uuid",
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(AsyncOffsetPage[RunListResponsesResponse], run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_responses(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.evals.runs.with_raw_response.list_responses(
            eval_run_uuid="eval_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(AsyncOffsetPage[RunListResponsesResponse], run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_responses(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.evals.runs.with_streaming_response.list_responses(
            eval_run_uuid="eval_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(AsyncOffsetPage[RunListResponsesResponse], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_responses(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_run_uuid` but received ''"):
            await async_client.evals.runs.with_raw_response.list_responses(
                eval_run_uuid="",
            )
