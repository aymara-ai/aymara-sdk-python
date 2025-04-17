# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from aymara_ai import AymaraAI, AsyncAymaraAI
from tests.utils import assert_matches_type
from aymara_ai.types import (
    EvalGetRunResponse,
    EvalRetrieveResponse,
    EvalScoreRunResponse,
    EvalGetPromptsResponse,
    EvalGetResponsesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: AymaraAI) -> None:
        eval = client.evals.retrieve(
            eval_uuid="eval_uuid",
        )
        assert_matches_type(EvalRetrieveResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: AymaraAI) -> None:
        eval = client.evals.retrieve(
            eval_uuid="eval_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalRetrieveResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: AymaraAI) -> None:
        response = client.evals.with_raw_response.retrieve(
            eval_uuid="eval_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(EvalRetrieveResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: AymaraAI) -> None:
        with client.evals.with_streaming_response.retrieve(
            eval_uuid="eval_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(EvalRetrieveResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_uuid` but received ''"):
            client.evals.with_raw_response.retrieve(
                eval_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: AymaraAI) -> None:
        eval = client.evals.delete(
            eval_uuid="eval_uuid",
        )
        assert eval is None

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: AymaraAI) -> None:
        eval = client.evals.delete(
            eval_uuid="eval_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert eval is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: AymaraAI) -> None:
        response = client.evals.with_raw_response.delete(
            eval_uuid="eval_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert eval is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: AymaraAI) -> None:
        with client.evals.with_streaming_response.delete(
            eval_uuid="eval_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert eval is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_uuid` but received ''"):
            client.evals.with_raw_response.delete(
                eval_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_run(self, client: AymaraAI) -> None:
        eval = client.evals.delete_run(
            eval_run_uuid="eval_run_uuid",
        )
        assert eval is None

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_run_with_all_params(self, client: AymaraAI) -> None:
        eval = client.evals.delete_run(
            eval_run_uuid="eval_run_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert eval is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete_run(self, client: AymaraAI) -> None:
        response = client.evals.with_raw_response.delete_run(
            eval_run_uuid="eval_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert eval is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete_run(self, client: AymaraAI) -> None:
        with client.evals.with_streaming_response.delete_run(
            eval_run_uuid="eval_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert eval is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete_run(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_run_uuid` but received ''"):
            client.evals.with_raw_response.delete_run(
                eval_run_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_prompts(self, client: AymaraAI) -> None:
        eval = client.evals.get_prompts(
            eval_uuid="eval_uuid",
        )
        assert_matches_type(EvalGetPromptsResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_prompts_with_all_params(self, client: AymaraAI) -> None:
        eval = client.evals.get_prompts(
            eval_uuid="eval_uuid",
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalGetPromptsResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_prompts(self, client: AymaraAI) -> None:
        response = client.evals.with_raw_response.get_prompts(
            eval_uuid="eval_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(EvalGetPromptsResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_prompts(self, client: AymaraAI) -> None:
        with client.evals.with_streaming_response.get_prompts(
            eval_uuid="eval_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(EvalGetPromptsResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_prompts(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_uuid` but received ''"):
            client.evals.with_raw_response.get_prompts(
                eval_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_responses(self, client: AymaraAI) -> None:
        eval = client.evals.get_responses(
            eval_run_uuid="eval_run_uuid",
        )
        assert_matches_type(EvalGetResponsesResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_responses_with_all_params(self, client: AymaraAI) -> None:
        eval = client.evals.get_responses(
            eval_run_uuid="eval_run_uuid",
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalGetResponsesResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_responses(self, client: AymaraAI) -> None:
        response = client.evals.with_raw_response.get_responses(
            eval_run_uuid="eval_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(EvalGetResponsesResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_responses(self, client: AymaraAI) -> None:
        with client.evals.with_streaming_response.get_responses(
            eval_run_uuid="eval_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(EvalGetResponsesResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_responses(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_run_uuid` but received ''"):
            client.evals.with_raw_response.get_responses(
                eval_run_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_run(self, client: AymaraAI) -> None:
        eval = client.evals.get_run(
            eval_run_uuid="eval_run_uuid",
        )
        assert_matches_type(EvalGetRunResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_run_with_all_params(self, client: AymaraAI) -> None:
        eval = client.evals.get_run(
            eval_run_uuid="eval_run_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalGetRunResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_run(self, client: AymaraAI) -> None:
        response = client.evals.with_raw_response.get_run(
            eval_run_uuid="eval_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(EvalGetRunResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_run(self, client: AymaraAI) -> None:
        with client.evals.with_streaming_response.get_run(
            eval_run_uuid="eval_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(EvalGetRunResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_run(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_run_uuid` but received ''"):
            client.evals.with_raw_response.get_run(
                eval_run_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_score_run(self, client: AymaraAI) -> None:
        eval = client.evals.score_run(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                }
            ],
        )
        assert_matches_type(EvalScoreRunResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_score_run_with_all_params(self, client: AymaraAI) -> None:
        eval = client.evals.score_run(
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
        assert_matches_type(EvalScoreRunResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_score_run(self, client: AymaraAI) -> None:
        response = client.evals.with_raw_response.score_run(
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
        eval = response.parse()
        assert_matches_type(EvalScoreRunResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_score_run(self, client: AymaraAI) -> None:
        with client.evals.with_streaming_response.score_run(
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

            eval = response.parse()
            assert_matches_type(EvalScoreRunResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvals:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.retrieve(
            eval_uuid="eval_uuid",
        )
        assert_matches_type(EvalRetrieveResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.retrieve(
            eval_uuid="eval_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalRetrieveResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.evals.with_raw_response.retrieve(
            eval_uuid="eval_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(EvalRetrieveResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.evals.with_streaming_response.retrieve(
            eval_uuid="eval_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(EvalRetrieveResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_uuid` but received ''"):
            await async_client.evals.with_raw_response.retrieve(
                eval_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.delete(
            eval_uuid="eval_uuid",
        )
        assert eval is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.delete(
            eval_uuid="eval_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert eval is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.evals.with_raw_response.delete(
            eval_uuid="eval_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert eval is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.evals.with_streaming_response.delete(
            eval_uuid="eval_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert eval is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_uuid` but received ''"):
            await async_client.evals.with_raw_response.delete(
                eval_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_run(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.delete_run(
            eval_run_uuid="eval_run_uuid",
        )
        assert eval is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_run_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.delete_run(
            eval_run_uuid="eval_run_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert eval is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete_run(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.evals.with_raw_response.delete_run(
            eval_run_uuid="eval_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert eval is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete_run(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.evals.with_streaming_response.delete_run(
            eval_run_uuid="eval_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert eval is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete_run(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_run_uuid` but received ''"):
            await async_client.evals.with_raw_response.delete_run(
                eval_run_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_prompts(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.get_prompts(
            eval_uuid="eval_uuid",
        )
        assert_matches_type(EvalGetPromptsResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_prompts_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.get_prompts(
            eval_uuid="eval_uuid",
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalGetPromptsResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_prompts(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.evals.with_raw_response.get_prompts(
            eval_uuid="eval_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(EvalGetPromptsResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_prompts(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.evals.with_streaming_response.get_prompts(
            eval_uuid="eval_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(EvalGetPromptsResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_prompts(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_uuid` but received ''"):
            await async_client.evals.with_raw_response.get_prompts(
                eval_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_responses(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.get_responses(
            eval_run_uuid="eval_run_uuid",
        )
        assert_matches_type(EvalGetResponsesResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_responses_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.get_responses(
            eval_run_uuid="eval_run_uuid",
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalGetResponsesResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_responses(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.evals.with_raw_response.get_responses(
            eval_run_uuid="eval_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(EvalGetResponsesResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_responses(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.evals.with_streaming_response.get_responses(
            eval_run_uuid="eval_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(EvalGetResponsesResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_responses(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_run_uuid` but received ''"):
            await async_client.evals.with_raw_response.get_responses(
                eval_run_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_run(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.get_run(
            eval_run_uuid="eval_run_uuid",
        )
        assert_matches_type(EvalGetRunResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_run_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.get_run(
            eval_run_uuid="eval_run_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalGetRunResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_run(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.evals.with_raw_response.get_run(
            eval_run_uuid="eval_run_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(EvalGetRunResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_run(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.evals.with_streaming_response.get_run(
            eval_run_uuid="eval_run_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(EvalGetRunResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_run(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_run_uuid` but received ''"):
            await async_client.evals.with_raw_response.get_run(
                eval_run_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_score_run(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.score_run(
            eval_uuid="eval_uuid",
            responses=[
                {
                    "content": "content",
                    "prompt_uuid": "prompt_uuid",
                }
            ],
        )
        assert_matches_type(EvalScoreRunResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_score_run_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.score_run(
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
        assert_matches_type(EvalScoreRunResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_score_run(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.evals.with_raw_response.score_run(
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
        eval = await response.parse()
        assert_matches_type(EvalScoreRunResponse, eval, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_score_run(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.evals.with_streaming_response.score_run(
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

            eval = await response.parse()
            assert_matches_type(EvalScoreRunResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True
