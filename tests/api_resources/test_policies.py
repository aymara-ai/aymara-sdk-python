# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from aymara import Aymara, AsyncAymara
from tests.utils import assert_matches_type
from aymara.types import PolicyListResponse
from aymara.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Aymara) -> None:
        policy = client.policies.list()
        assert_matches_type(SyncOffsetPage[PolicyListResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Aymara) -> None:
        policy = client.policies.list(
            limit=1,
            offset=0,
            test_type="test_type",
        )
        assert_matches_type(SyncOffsetPage[PolicyListResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Aymara) -> None:
        response = client.policies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(SyncOffsetPage[PolicyListResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Aymara) -> None:
        with client.policies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(SyncOffsetPage[PolicyListResponse], policy, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPolicies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncAymara) -> None:
        policy = await async_client.policies.list()
        assert_matches_type(AsyncOffsetPage[PolicyListResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAymara) -> None:
        policy = await async_client.policies.list(
            limit=1,
            offset=0,
            test_type="test_type",
        )
        assert_matches_type(AsyncOffsetPage[PolicyListResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAymara) -> None:
        response = await async_client.policies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(AsyncOffsetPage[PolicyListResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAymara) -> None:
        async with async_client.policies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(AsyncOffsetPage[PolicyListResponse], policy, path=["response"])

        assert cast(Any, response.is_closed) is True
