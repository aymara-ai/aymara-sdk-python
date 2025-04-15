# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from aymara import Aymara, AsyncAymara
from tests.utils import assert_matches_type
from aymara.types import IntegrationTestRunResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntegrationTest:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run(self, client: Aymara) -> None:
        integration_test = client.integration_test.run()
        assert_matches_type(IntegrationTestRunResponse, integration_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run(self, client: Aymara) -> None:
        response = client.integration_test.with_raw_response.run()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_test = response.parse()
        assert_matches_type(IntegrationTestRunResponse, integration_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run(self, client: Aymara) -> None:
        with client.integration_test.with_streaming_response.run() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_test = response.parse()
            assert_matches_type(IntegrationTestRunResponse, integration_test, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIntegrationTest:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run(self, async_client: AsyncAymara) -> None:
        integration_test = await async_client.integration_test.run()
        assert_matches_type(IntegrationTestRunResponse, integration_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncAymara) -> None:
        response = await async_client.integration_test.with_raw_response.run()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_test = await response.parse()
        assert_matches_type(IntegrationTestRunResponse, integration_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncAymara) -> None:
        async with async_client.integration_test.with_streaming_response.run() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_test = await response.parse()
            assert_matches_type(IntegrationTestRunResponse, integration_test, path=["response"])

        assert cast(Any, response.is_closed) is True
