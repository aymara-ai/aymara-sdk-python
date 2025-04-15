# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from aymara_ai import AymaraAI, AsyncAymaraAI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_propel(self, client: AymaraAI) -> None:
        webhook = client.webhooks.propel()
        assert webhook is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_propel(self, client: AymaraAI) -> None:
        response = client.webhooks.with_raw_response.propel()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert webhook is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_propel(self, client: AymaraAI) -> None:
        with client.webhooks.with_streaming_response.propel() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_propel(self, async_client: AsyncAymaraAI) -> None:
        webhook = await async_client.webhooks.propel()
        assert webhook is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_propel(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.webhooks.with_raw_response.propel()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert webhook is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_propel(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.webhooks.with_streaming_response.propel() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True
