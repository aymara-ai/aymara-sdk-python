# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from aymara_ai import AymaraAI, AsyncAymaraAI
from tests.utils import assert_matches_type
from aymara_ai.types import (
    EvalSuiteReport,
)
from aymara_ai.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: AymaraAI) -> None:
        report = client.reports.create(
            eval_run_uuids=["string"],
        )
        assert_matches_type(EvalSuiteReport, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: AymaraAI) -> None:
        report = client.reports.create(
            eval_run_uuids=["string"],
            is_sandbox=True,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalSuiteReport, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: AymaraAI) -> None:
        response = client.reports.with_raw_response.create(
            eval_run_uuids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(EvalSuiteReport, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: AymaraAI) -> None:
        with client.reports.with_streaming_response.create(
            eval_run_uuids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(EvalSuiteReport, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: AymaraAI) -> None:
        report = client.reports.list()
        assert_matches_type(SyncOffsetPage[EvalSuiteReport], report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: AymaraAI) -> None:
        report = client.reports.list(
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(SyncOffsetPage[EvalSuiteReport], report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: AymaraAI) -> None:
        response = client.reports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(SyncOffsetPage[EvalSuiteReport], report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: AymaraAI) -> None:
        with client.reports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(SyncOffsetPage[EvalSuiteReport], report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: AymaraAI) -> None:
        report = client.reports.delete(
            report_uuid="report_uuid",
        )
        assert report is None

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: AymaraAI) -> None:
        report = client.reports.delete(
            report_uuid="report_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert report is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: AymaraAI) -> None:
        response = client.reports.with_raw_response.delete(
            report_uuid="report_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert report is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: AymaraAI) -> None:
        with client.reports.with_streaming_response.delete(
            report_uuid="report_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert report is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_uuid` but received ''"):
            client.reports.with_raw_response.delete(
                report_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: AymaraAI) -> None:
        report = client.reports.get(
            report_uuid="report_uuid",
        )
        assert_matches_type(EvalSuiteReport, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: AymaraAI) -> None:
        report = client.reports.get(
            report_uuid="report_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalSuiteReport, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: AymaraAI) -> None:
        response = client.reports.with_raw_response.get(
            report_uuid="report_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(EvalSuiteReport, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: AymaraAI) -> None:
        with client.reports.with_streaming_response.get(
            report_uuid="report_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(EvalSuiteReport, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_uuid` but received ''"):
            client.reports.with_raw_response.get(
                report_uuid="",
            )


class TestAsyncReports:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncAymaraAI) -> None:
        report = await async_client.reports.create(
            eval_run_uuids=["string"],
        )
        assert_matches_type(EvalSuiteReport, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        report = await async_client.reports.create(
            eval_run_uuids=["string"],
            is_sandbox=True,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalSuiteReport, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.reports.with_raw_response.create(
            eval_run_uuids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(EvalSuiteReport, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.reports.with_streaming_response.create(
            eval_run_uuids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(EvalSuiteReport, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncAymaraAI) -> None:
        report = await async_client.reports.list()
        assert_matches_type(AsyncOffsetPage[EvalSuiteReport], report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        report = await async_client.reports.list(
            limit=1,
            offset=0,
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(AsyncOffsetPage[EvalSuiteReport], report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.reports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(AsyncOffsetPage[EvalSuiteReport], report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.reports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(AsyncOffsetPage[EvalSuiteReport], report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncAymaraAI) -> None:
        report = await async_client.reports.delete(
            report_uuid="report_uuid",
        )
        assert report is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        report = await async_client.reports.delete(
            report_uuid="report_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert report is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.reports.with_raw_response.delete(
            report_uuid="report_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert report is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.reports.with_streaming_response.delete(
            report_uuid="report_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert report is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_uuid` but received ''"):
            await async_client.reports.with_raw_response.delete(
                report_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncAymaraAI) -> None:
        report = await async_client.reports.get(
            report_uuid="report_uuid",
        )
        assert_matches_type(EvalSuiteReport, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        report = await async_client.reports.get(
            report_uuid="report_uuid",
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(EvalSuiteReport, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.reports.with_raw_response.get(
            report_uuid="report_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(EvalSuiteReport, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.reports.with_streaming_response.get(
            report_uuid="report_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(EvalSuiteReport, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_uuid` but received ''"):
            await async_client.reports.with_raw_response.get(
                report_uuid="",
            )
