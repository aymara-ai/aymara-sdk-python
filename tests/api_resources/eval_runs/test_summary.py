# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from aymara import Aymara, AsyncAymara
from tests.utils import assert_matches_type
from aymara.pagination import SyncOffsetPage, AsyncOffsetPage
from aymara.types.eval_runs import (
    EvalRunSuiteSummary,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSummary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Aymara) -> None:
        summary = client.eval_runs.summary.create(
            eval_run_uuids=["string"],
        )
        assert_matches_type(EvalRunSuiteSummary, summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Aymara) -> None:
        summary = client.eval_runs.summary.create(
            eval_run_uuids=["string"],
            is_sandbox=True,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalRunSuiteSummary, summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Aymara) -> None:
        response = client.eval_runs.summary.with_raw_response.create(
            eval_run_uuids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(EvalRunSuiteSummary, summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Aymara) -> None:
        with client.eval_runs.summary.with_streaming_response.create(
            eval_run_uuids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(EvalRunSuiteSummary, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Aymara) -> None:
        summary = client.eval_runs.summary.retrieve(
            summary_uuid="summary_uuid",
        )
        assert_matches_type(EvalRunSuiteSummary, summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Aymara) -> None:
        summary = client.eval_runs.summary.retrieve(
            summary_uuid="summary_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalRunSuiteSummary, summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Aymara) -> None:
        response = client.eval_runs.summary.with_raw_response.retrieve(
            summary_uuid="summary_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(EvalRunSuiteSummary, summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Aymara) -> None:
        with client.eval_runs.summary.with_streaming_response.retrieve(
            summary_uuid="summary_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(EvalRunSuiteSummary, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Aymara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `summary_uuid` but received ''"):
            client.eval_runs.summary.with_raw_response.retrieve(
                summary_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Aymara) -> None:
        summary = client.eval_runs.summary.list()
        assert_matches_type(SyncOffsetPage[EvalRunSuiteSummary], summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Aymara) -> None:
        summary = client.eval_runs.summary.list(
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(SyncOffsetPage[EvalRunSuiteSummary], summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Aymara) -> None:
        response = client.eval_runs.summary.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SyncOffsetPage[EvalRunSuiteSummary], summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Aymara) -> None:
        with client.eval_runs.summary.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SyncOffsetPage[EvalRunSuiteSummary], summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Aymara) -> None:
        summary = client.eval_runs.summary.delete(
            summary_uuid="summary_uuid",
        )
        assert summary is None

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Aymara) -> None:
        summary = client.eval_runs.summary.delete(
            summary_uuid="summary_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert summary is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Aymara) -> None:
        response = client.eval_runs.summary.with_raw_response.delete(
            summary_uuid="summary_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert summary is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Aymara) -> None:
        with client.eval_runs.summary.with_streaming_response.delete(
            summary_uuid="summary_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert summary is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Aymara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `summary_uuid` but received ''"):
            client.eval_runs.summary.with_raw_response.delete(
                summary_uuid="",
            )


class TestAsyncSummary:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncAymara) -> None:
        summary = await async_client.eval_runs.summary.create(
            eval_run_uuids=["string"],
        )
        assert_matches_type(EvalRunSuiteSummary, summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAymara) -> None:
        summary = await async_client.eval_runs.summary.create(
            eval_run_uuids=["string"],
            is_sandbox=True,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalRunSuiteSummary, summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAymara) -> None:
        response = await async_client.eval_runs.summary.with_raw_response.create(
            eval_run_uuids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(EvalRunSuiteSummary, summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAymara) -> None:
        async with async_client.eval_runs.summary.with_streaming_response.create(
            eval_run_uuids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(EvalRunSuiteSummary, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAymara) -> None:
        summary = await async_client.eval_runs.summary.retrieve(
            summary_uuid="summary_uuid",
        )
        assert_matches_type(EvalRunSuiteSummary, summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncAymara) -> None:
        summary = await async_client.eval_runs.summary.retrieve(
            summary_uuid="summary_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalRunSuiteSummary, summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAymara) -> None:
        response = await async_client.eval_runs.summary.with_raw_response.retrieve(
            summary_uuid="summary_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(EvalRunSuiteSummary, summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAymara) -> None:
        async with async_client.eval_runs.summary.with_streaming_response.retrieve(
            summary_uuid="summary_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(EvalRunSuiteSummary, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAymara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `summary_uuid` but received ''"):
            await async_client.eval_runs.summary.with_raw_response.retrieve(
                summary_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncAymara) -> None:
        summary = await async_client.eval_runs.summary.list()
        assert_matches_type(AsyncOffsetPage[EvalRunSuiteSummary], summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAymara) -> None:
        summary = await async_client.eval_runs.summary.list(
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(AsyncOffsetPage[EvalRunSuiteSummary], summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAymara) -> None:
        response = await async_client.eval_runs.summary.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(AsyncOffsetPage[EvalRunSuiteSummary], summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAymara) -> None:
        async with async_client.eval_runs.summary.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(AsyncOffsetPage[EvalRunSuiteSummary], summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncAymara) -> None:
        summary = await async_client.eval_runs.summary.delete(
            summary_uuid="summary_uuid",
        )
        assert summary is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncAymara) -> None:
        summary = await async_client.eval_runs.summary.delete(
            summary_uuid="summary_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert summary is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAymara) -> None:
        response = await async_client.eval_runs.summary.with_raw_response.delete(
            summary_uuid="summary_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert summary is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAymara) -> None:
        async with async_client.eval_runs.summary.with_streaming_response.delete(
            summary_uuid="summary_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert summary is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAymara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `summary_uuid` but received ''"):
            await async_client.eval_runs.summary.with_raw_response.delete(
                summary_uuid="",
            )
