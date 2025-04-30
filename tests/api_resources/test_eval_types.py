# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from aymara_ai import AymaraAI, AsyncAymaraAI
from tests.utils import assert_matches_type
from aymara_ai.types import (
    EvalType,
    AIInstruction,
)
from aymara_ai.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvalTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: AymaraAI) -> None:
        eval_type = client.eval_types.list()
        assert_matches_type(SyncOffsetPage[EvalType], eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: AymaraAI) -> None:
        eval_type = client.eval_types.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[EvalType], eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: AymaraAI) -> None:
        response = client.eval_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_type = response.parse()
        assert_matches_type(SyncOffsetPage[EvalType], eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: AymaraAI) -> None:
        with client.eval_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_type = response.parse()
            assert_matches_type(SyncOffsetPage[EvalType], eval_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_find_instructions(self, client: AymaraAI) -> None:
        eval_type = client.eval_types.find_instructions(
            eval_type_slug="eval_type_slug",
        )
        assert_matches_type(SyncOffsetPage[AIInstruction], eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_find_instructions_with_all_params(self, client: AymaraAI) -> None:
        eval_type = client.eval_types.find_instructions(
            eval_type_slug="eval_type_slug",
            limit=1,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[AIInstruction], eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_find_instructions(self, client: AymaraAI) -> None:
        response = client.eval_types.with_raw_response.find_instructions(
            eval_type_slug="eval_type_slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_type = response.parse()
        assert_matches_type(SyncOffsetPage[AIInstruction], eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_find_instructions(self, client: AymaraAI) -> None:
        with client.eval_types.with_streaming_response.find_instructions(
            eval_type_slug="eval_type_slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_type = response.parse()
            assert_matches_type(SyncOffsetPage[AIInstruction], eval_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: AymaraAI) -> None:
        eval_type = client.eval_types.get(
            "eval_type_uuid",
        )
        assert_matches_type(EvalType, eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: AymaraAI) -> None:
        response = client.eval_types.with_raw_response.get(
            "eval_type_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_type = response.parse()
        assert_matches_type(EvalType, eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: AymaraAI) -> None:
        with client.eval_types.with_streaming_response.get(
            "eval_type_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_type = response.parse()
            assert_matches_type(EvalType, eval_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_type_uuid` but received ''"):
            client.eval_types.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_instructions(self, client: AymaraAI) -> None:
        eval_type = client.eval_types.list_instructions(
            eval_type_uuid="eval_type_uuid",
        )
        assert_matches_type(SyncOffsetPage[AIInstruction], eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_instructions_with_all_params(self, client: AymaraAI) -> None:
        eval_type = client.eval_types.list_instructions(
            eval_type_uuid="eval_type_uuid",
            limit=1,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[AIInstruction], eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_instructions(self, client: AymaraAI) -> None:
        response = client.eval_types.with_raw_response.list_instructions(
            eval_type_uuid="eval_type_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_type = response.parse()
        assert_matches_type(SyncOffsetPage[AIInstruction], eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_instructions(self, client: AymaraAI) -> None:
        with client.eval_types.with_streaming_response.list_instructions(
            eval_type_uuid="eval_type_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_type = response.parse()
            assert_matches_type(SyncOffsetPage[AIInstruction], eval_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_instructions(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_type_uuid` but received ''"):
            client.eval_types.with_raw_response.list_instructions(
                eval_type_uuid="",
            )


class TestAsyncEvalTypes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncAymaraAI) -> None:
        eval_type = await async_client.eval_types.list()
        assert_matches_type(AsyncOffsetPage[EvalType], eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        eval_type = await async_client.eval_types.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[EvalType], eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.eval_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_type = await response.parse()
        assert_matches_type(AsyncOffsetPage[EvalType], eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.eval_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_type = await response.parse()
            assert_matches_type(AsyncOffsetPage[EvalType], eval_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_find_instructions(self, async_client: AsyncAymaraAI) -> None:
        eval_type = await async_client.eval_types.find_instructions(
            eval_type_slug="eval_type_slug",
        )
        assert_matches_type(AsyncOffsetPage[AIInstruction], eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_find_instructions_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        eval_type = await async_client.eval_types.find_instructions(
            eval_type_slug="eval_type_slug",
            limit=1,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[AIInstruction], eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_find_instructions(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.eval_types.with_raw_response.find_instructions(
            eval_type_slug="eval_type_slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_type = await response.parse()
        assert_matches_type(AsyncOffsetPage[AIInstruction], eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_find_instructions(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.eval_types.with_streaming_response.find_instructions(
            eval_type_slug="eval_type_slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_type = await response.parse()
            assert_matches_type(AsyncOffsetPage[AIInstruction], eval_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncAymaraAI) -> None:
        eval_type = await async_client.eval_types.get(
            "eval_type_uuid",
        )
        assert_matches_type(EvalType, eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.eval_types.with_raw_response.get(
            "eval_type_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_type = await response.parse()
        assert_matches_type(EvalType, eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.eval_types.with_streaming_response.get(
            "eval_type_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_type = await response.parse()
            assert_matches_type(EvalType, eval_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_type_uuid` but received ''"):
            await async_client.eval_types.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_instructions(self, async_client: AsyncAymaraAI) -> None:
        eval_type = await async_client.eval_types.list_instructions(
            eval_type_uuid="eval_type_uuid",
        )
        assert_matches_type(AsyncOffsetPage[AIInstruction], eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_instructions_with_all_params(self, async_client: AsyncAymaraAI) -> None:
        eval_type = await async_client.eval_types.list_instructions(
            eval_type_uuid="eval_type_uuid",
            limit=1,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[AIInstruction], eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_instructions(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.eval_types.with_raw_response.list_instructions(
            eval_type_uuid="eval_type_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_type = await response.parse()
        assert_matches_type(AsyncOffsetPage[AIInstruction], eval_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_instructions(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.eval_types.with_streaming_response.list_instructions(
            eval_type_uuid="eval_type_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_type = await response.parse()
            assert_matches_type(AsyncOffsetPage[AIInstruction], eval_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_instructions(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_type_uuid` but received ''"):
            await async_client.eval_types.with_raw_response.list_instructions(
                eval_type_uuid="",
            )
