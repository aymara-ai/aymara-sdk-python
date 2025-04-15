# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from aymara_ai import AymaraAI, AsyncAymaraAI
from tests.utils import assert_matches_type
from aymara_ai.types import WorkspaceOut

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkspaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: AymaraAI) -> None:
        workspace = client.workspaces.retrieve(
            "workspace_uuid",
        )
        assert_matches_type(WorkspaceOut, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: AymaraAI) -> None:
        response = client.workspaces.with_raw_response.retrieve(
            "workspace_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceOut, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: AymaraAI) -> None:
        with client.workspaces.with_streaming_response.retrieve(
            "workspace_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceOut, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_uuid` but received ''"):
            client.workspaces.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: AymaraAI) -> None:
        workspace = client.workspaces.update(
            workspace_uuid="workspace_uuid",
            name="name",
            organization_uuid="organization_uuid",
        )
        assert_matches_type(WorkspaceOut, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: AymaraAI) -> None:
        response = client.workspaces.with_raw_response.update(
            workspace_uuid="workspace_uuid",
            name="name",
            organization_uuid="organization_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceOut, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: AymaraAI) -> None:
        with client.workspaces.with_streaming_response.update(
            workspace_uuid="workspace_uuid",
            name="name",
            organization_uuid="organization_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceOut, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_uuid` but received ''"):
            client.workspaces.with_raw_response.update(
                workspace_uuid="",
                name="name",
                organization_uuid="organization_uuid",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: AymaraAI) -> None:
        workspace = client.workspaces.delete(
            "workspace_uuid",
        )
        assert workspace is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: AymaraAI) -> None:
        response = client.workspaces.with_raw_response.delete(
            "workspace_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert workspace is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: AymaraAI) -> None:
        with client.workspaces.with_streaming_response.delete(
            "workspace_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert workspace is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: AymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_uuid` but received ''"):
            client.workspaces.with_raw_response.delete(
                "",
            )


class TestAsyncWorkspaces:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAymaraAI) -> None:
        workspace = await async_client.workspaces.retrieve(
            "workspace_uuid",
        )
        assert_matches_type(WorkspaceOut, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.workspaces.with_raw_response.retrieve(
            "workspace_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceOut, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.workspaces.with_streaming_response.retrieve(
            "workspace_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceOut, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_uuid` but received ''"):
            await async_client.workspaces.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncAymaraAI) -> None:
        workspace = await async_client.workspaces.update(
            workspace_uuid="workspace_uuid",
            name="name",
            organization_uuid="organization_uuid",
        )
        assert_matches_type(WorkspaceOut, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.workspaces.with_raw_response.update(
            workspace_uuid="workspace_uuid",
            name="name",
            organization_uuid="organization_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceOut, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.workspaces.with_streaming_response.update(
            workspace_uuid="workspace_uuid",
            name="name",
            organization_uuid="organization_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceOut, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_uuid` but received ''"):
            await async_client.workspaces.with_raw_response.update(
                workspace_uuid="",
                name="name",
                organization_uuid="organization_uuid",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncAymaraAI) -> None:
        workspace = await async_client.workspaces.delete(
            "workspace_uuid",
        )
        assert workspace is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAymaraAI) -> None:
        response = await async_client.workspaces.with_raw_response.delete(
            "workspace_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert workspace is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAymaraAI) -> None:
        async with async_client.workspaces.with_streaming_response.delete(
            "workspace_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert workspace is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAymaraAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_uuid` but received ''"):
            await async_client.workspaces.with_raw_response.delete(
                "",
            )
