# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from aymara import Aymara, AsyncAymara
from tests.utils import assert_matches_type
from aymara.types import User

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_me(self, client: Aymara) -> None:
        account = client.accounts.retrieve_me()
        assert_matches_type(User, account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_me(self, client: Aymara) -> None:
        response = client.accounts.with_raw_response.retrieve_me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(User, account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_me(self, client: Aymara) -> None:
        with client.accounts.with_streaming_response.retrieve_me() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(User, account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_me(self, async_client: AsyncAymara) -> None:
        account = await async_client.accounts.retrieve_me()
        assert_matches_type(User, account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_me(self, async_client: AsyncAymara) -> None:
        response = await async_client.accounts.with_raw_response.retrieve_me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(User, account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_me(self, async_client: AsyncAymara) -> None:
        async with async_client.accounts.with_streaming_response.retrieve_me() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(User, account, path=["response"])

        assert cast(Any, response.is_closed) is True
