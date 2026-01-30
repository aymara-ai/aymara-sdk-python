# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from aymara_ai import AymaraAI, AsyncAymaraAI
from tests.utils import assert_matches_type
from aymara_ai.types import (
    Eval,
    EvalPrompt,
    EvalAnalyzeResponse,
)
from aymara_ai._utils import parse_datetime
from aymara_ai.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: AymaraAI) -> None:
        eval = client.evals.create(
            ai_description="ai_description",
            eval_type="eval_type",
        )
        assert_matches_type(Eval, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: AymaraAI) -> None:
        eval = client.evals.create(
            ai_description="ai_description",
            eval_type="eval_type",
            ai_instructions="string",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="created_by",
            eval_instructions="eval_instructions",
            eval_uuid="eval_uuid",
            ground_truth="string",
            is_jailbreak=True,
            is_sandbox=True,
            language="language",
            modality="text",
            name="name",
            num_prompts=0,
            prompt_examples=[
                {
                    "content": "content",
                    "example_uuid": "example_uuid",
                    "explanation": "explanation",
                    "type": "good",
                }
            ],
            status="created",
            task_timeout=0,
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(Eval, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: AymaraAI) -> None:
        response = client.evals.with_raw_response.create(
            ai_description="ai_description",
            eval_type="eval_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(Eval, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: AymaraAI) -> None:
        with client.evals.with_streaming_response.create(
            ai_description="ai_description",
            eval_type="eval_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(Eval, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: AymaraAI) -> None:
        eval = client.evals.update(
            eval_uuid="eval_uuid",
        )
        assert_matches_type(Eval, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: AymaraAI) -> None:
        eval = client.evals.update(
            eval_uuid="eval_uuid",
            workspace_uuid="workspace_uuid",
            ai_description="ai_description",
            ai_instructions="string",
            eval_instructions="eval_instructions",
            ground_truth="string",
            name="name",
            prompt_creates=[
                {
                    "content": "content",
                    "category": "category",
                }
            ],
            prompt_updates=[
                {
                    "prompt_uuid": "prompt_uuid",
                    "action": "action",
                    "category": "category",
                    "content": "content",
                }
            ],
        )
        assert_matches_type(Eval, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: AymaraAI) -> None:
        response = client.evals.with_raw_response.update(
            eval_uuid="eval_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(Eval, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: AymaraAI) -> None:
        with client.evals.with_streaming_response.update(
            eval_uuid="eval_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(Eval, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_uuid` but received ''"):
            client.evals.with_raw_response.update(
                eval_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: AymaraAI) -> None:
        eval = client.evals.list()
        assert_matches_type(SyncOffsetPage[Eval], eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: AymaraAI) -> None:
        eval = client.evals.list(
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(SyncOffsetPage[Eval], eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: AymaraAI) -> None:
        response = client.evals.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(SyncOffsetPage[Eval], eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: AymaraAI) -> None:
        with client.evals.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(SyncOffsetPage[Eval], eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: AymaraAI) -> None:
        eval = client.evals.delete(
            eval_uuid="eval_uuid",
        )
        assert eval is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: AymaraAI) -> None:
        eval = client.evals.delete(
            eval_uuid="eval_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert eval is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: AymaraAI) -> None:
        response = client.evals.with_raw_response.delete(
            eval_uuid="eval_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert eval is None

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_uuid` but received ''"):
            client.evals.with_raw_response.delete(
                eval_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_analyze(self, client: AymaraAI) -> None:
        eval = client.evals.analyze()
        assert_matches_type(EvalAnalyzeResponse, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_analyze_with_all_params(self, client: AymaraAI) -> None:
        eval = client.evals.analyze(
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="created_by",
            eval_type="eval_type",
            has_score_runs=True,
            is_jailbreak=True,
            is_sandbox=True,
            language="language",
            limit=1,
            max_pass_rate=0,
            min_pass_rate=0,
            modality="modality",
            name="name",
            offset=0,
            run_created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            run_created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            score_run_status="score_run_status",
            sort_by="created_at",
            sort_order="asc",
            status="status",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalAnalyzeResponse, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_analyze(self, client: AymaraAI) -> None:
        response = client.evals.with_raw_response.analyze()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(EvalAnalyzeResponse, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_analyze(self, client: AymaraAI) -> None:
        with client.evals.with_streaming_response.analyze() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(EvalAnalyzeResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: AymaraAI) -> None:
        eval = client.evals.get(
            eval_uuid="eval_uuid",
        )
        assert_matches_type(Eval, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: AymaraAI) -> None:
        eval = client.evals.get(
            eval_uuid="eval_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(Eval, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: AymaraAI) -> None:
        response = client.evals.with_raw_response.get(
            eval_uuid="eval_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(Eval, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: AymaraAI) -> None:
        with client.evals.with_streaming_response.get(
            eval_uuid="eval_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(Eval, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_uuid` but received ''"):
            client.evals.with_raw_response.get(
                eval_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_prompts(self, client: AymaraAI) -> None:
        eval = client.evals.list_prompts(
            eval_uuid="eval_uuid",
        )
        assert_matches_type(SyncOffsetPage[EvalPrompt], eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_prompts_with_all_params(self, client: AymaraAI) -> None:
        eval = client.evals.list_prompts(
            eval_uuid="eval_uuid",
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(SyncOffsetPage[EvalPrompt], eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_prompts(self, client: AymaraAI) -> None:
        response = client.evals.with_raw_response.list_prompts(
            eval_uuid="eval_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(SyncOffsetPage[EvalPrompt], eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_prompts(self, client: AymaraAI) -> None:
        with client.evals.with_streaming_response.list_prompts(
            eval_uuid="eval_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(SyncOffsetPage[EvalPrompt], eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_prompts(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_uuid` but received ''"):
            client.evals.with_raw_response.list_prompts(
                eval_uuid="",
            )


class TestAsyncEvals:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.create(
            ai_description="ai_description",
            eval_type="eval_type",
        )
        assert_matches_type(Eval, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.create(
            ai_description="ai_description",
            eval_type="eval_type",
            ai_instructions="string",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="created_by",
            eval_instructions="eval_instructions",
            eval_uuid="eval_uuid",
            ground_truth="string",
            is_jailbreak=True,
            is_sandbox=True,
            language="language",
            modality="text",
            name="name",
            num_prompts=0,
            prompt_examples=[
                {
                    "content": "content",
                    "example_uuid": "example_uuid",
                    "explanation": "explanation",
                    "type": "good",
                }
            ],
            status="created",
            task_timeout=0,
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(Eval, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.evals.with_raw_response.create(
            ai_description="ai_description",
            eval_type="eval_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(Eval, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.evals.with_streaming_response.create(
            ai_description="ai_description",
            eval_type="eval_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(Eval, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.update(
            eval_uuid="eval_uuid",
        )
        assert_matches_type(Eval, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.update(
            eval_uuid="eval_uuid",
            workspace_uuid="workspace_uuid",
            ai_description="ai_description",
            ai_instructions="string",
            eval_instructions="eval_instructions",
            ground_truth="string",
            name="name",
            prompt_creates=[
                {
                    "content": "content",
                    "category": "category",
                }
            ],
            prompt_updates=[
                {
                    "prompt_uuid": "prompt_uuid",
                    "action": "action",
                    "category": "category",
                    "content": "content",
                }
            ],
        )
        assert_matches_type(Eval, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.evals.with_raw_response.update(
            eval_uuid="eval_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(Eval, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.evals.with_streaming_response.update(
            eval_uuid="eval_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(Eval, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_uuid` but received ''"):
            await async_client.evals.with_raw_response.update(
                eval_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.list()
        assert_matches_type(AsyncOffsetPage[Eval], eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.list(
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(AsyncOffsetPage[Eval], eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.evals.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(AsyncOffsetPage[Eval], eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.evals.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(AsyncOffsetPage[Eval], eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.delete(
            eval_uuid="eval_uuid",
        )
        assert eval is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.delete(
            eval_uuid="eval_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert eval is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.evals.with_raw_response.delete(
            eval_uuid="eval_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert eval is None

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_uuid` but received ''"):
            await async_client.evals.with_raw_response.delete(
                eval_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_analyze(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.analyze()
        assert_matches_type(EvalAnalyzeResponse, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_analyze_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.analyze(
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by="created_by",
            eval_type="eval_type",
            has_score_runs=True,
            is_jailbreak=True,
            is_sandbox=True,
            language="language",
            limit=1,
            max_pass_rate=0,
            min_pass_rate=0,
            modality="modality",
            name="name",
            offset=0,
            run_created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            run_created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            score_run_status="score_run_status",
            sort_by="created_at",
            sort_order="asc",
            status="status",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalAnalyzeResponse, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_analyze(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.evals.with_raw_response.analyze()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(EvalAnalyzeResponse, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_analyze(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.evals.with_streaming_response.analyze() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(EvalAnalyzeResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.get(
            eval_uuid="eval_uuid",
        )
        assert_matches_type(Eval, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.get(
            eval_uuid="eval_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(Eval, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.evals.with_raw_response.get(
            eval_uuid="eval_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(Eval, eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.evals.with_streaming_response.get(
            eval_uuid="eval_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(Eval, eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_uuid` but received ''"):
            await async_client.evals.with_raw_response.get(
                eval_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_prompts(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.list_prompts(
            eval_uuid="eval_uuid",
        )
        assert_matches_type(AsyncOffsetPage[EvalPrompt], eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_prompts_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        eval = await async_client.evals.list_prompts(
            eval_uuid="eval_uuid",
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(AsyncOffsetPage[EvalPrompt], eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_prompts(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.evals.with_raw_response.list_prompts(
            eval_uuid="eval_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(AsyncOffsetPage[EvalPrompt], eval, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_prompts(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.evals.with_streaming_response.list_prompts(
            eval_uuid="eval_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(AsyncOffsetPage[EvalPrompt], eval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_prompts(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_uuid` but received ''"):
            await async_client.evals.with_raw_response.list_prompts(
                eval_uuid="",
            )
