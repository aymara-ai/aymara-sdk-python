# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from aymara import Aymara, AsyncAymara
from tests.utils import assert_matches_type
from aymara.types import UsageListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Aymara) -> None:
        usage = client.usage.list()
        assert_matches_type(UsageListResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Aymara) -> None:
        usage = client.usage.list(
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(UsageListResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Aymara) -> None:
        response = client.usage.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageListResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Aymara) -> None:
        with client.usage.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageListResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncAymara) -> None:
        usage = await async_client.usage.list()
        assert_matches_type(UsageListResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAymara) -> None:
        usage = await async_client.usage.list(
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(UsageListResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAymara) -> None:
        response = await async_client.usage.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageListResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAymara) -> None:
        async with async_client.usage.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageListResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True
