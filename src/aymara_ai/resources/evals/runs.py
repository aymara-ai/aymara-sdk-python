# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ...types.evals import (
    run_get_params,
    run_list_params,
    run_create_params,
    run_delete_params,
    run_list_responses_params,
    run_score_responses_params,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.eval_response_param import EvalResponseParam
from ...types.evals.eval_run_result import EvalRunResult
from ...types.evals.scored_response import ScoredResponse
from ...types.evals.eval_run_example_param import EvalRunExampleParam

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aymara-ai/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aymara-ai/aymara-sdk-python#with_streaming_response
        """
        return RunsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        eval_uuid: str,
        responses: Iterable[EvalResponseParam],
        is_sandbox: Optional[bool] | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        ai_description: Optional[str] | NotGiven = NOT_GIVEN,
        continue_thread: Optional[bool] | NotGiven = NOT_GIVEN,
        eval_run_examples: Optional[Iterable[EvalRunExampleParam]] | NotGiven = NOT_GIVEN,
        eval_run_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalRunResult:
        """
        Create a new eval run for an eval.

        Args: eval_run_data (EvalRunRequest): Data for the eval run to create.
        workspace_uuid (str, optional): UUID of the workspace. Defaults to None.
        is_sandbox (bool, optional): Whether to run in sandbox mode. Defaults to None.

        Returns: EvalRunResult: The created eval run result.

        Raises: AymaraAPIError: If the organization is missing or the request is
        invalid.

        Example: POST /api/eval-runs { "eval_uuid": "...", ... }

        Args:
          eval_uuid: Unique identifier for the eval.

          responses: List of AI responses to eval prompts.

          ai_description: Description of the AI for this run, if any.

          continue_thread: Whether to continue the thread after this run.

          eval_run_examples: Examples to include with the eval run, if any.

          eval_run_uuid: Unique identifier for the eval run, if any.

          name: Name of the eval run, if any (defaults to the eval name + timestamp).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/eval-runs",
            body=maybe_transform(
                {
                    "eval_uuid": eval_uuid,
                    "responses": responses,
                    "ai_description": ai_description,
                    "continue_thread": continue_thread,
                    "eval_run_examples": eval_run_examples,
                    "eval_run_uuid": eval_run_uuid,
                    "name": name,
                },
                run_create_params.RunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "is_sandbox": is_sandbox,
                        "workspace_uuid": workspace_uuid,
                    },
                    run_create_params.RunCreateParams,
                ),
            ),
            cast_to=EvalRunResult,
        )

    def list(
        self,
        *,
        eval_uuid: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[EvalRunResult]:
        """
        List all eval runs, with optional filtering.

        Args: eval_uuid (str, optional): UUID of the eval to filter runs by. Defaults to
        None. workspace_uuid (str, optional): UUID of the workspace. Defaults to None.

        Returns: list[EvalRunResult]: List of eval runs matching the filters.

        Raises: AymaraAPIError: If the organization is missing.

        Example: GET /api/eval-runs?eval_uuid=...&workspace_uuid=...

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/eval-runs",
            page=SyncOffsetPage[EvalRunResult],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "eval_uuid": eval_uuid,
                        "limit": limit,
                        "offset": offset,
                        "workspace_uuid": workspace_uuid,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            model=EvalRunResult,
        )

    def delete(
        self,
        eval_run_uuid: str,
        *,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete an eval run.

        Args: eval_run_uuid (str): UUID of the eval run to delete.

        workspace_uuid (str,
        optional): UUID of the workspace. Defaults to None.

        Returns: None

        Raises: AymaraAPIError: If the organization is missing or the eval run is not
        found.

        Example: DELETE /api/eval-runs/{eval_run_uuid}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not eval_run_uuid:
            raise ValueError(f"Expected a non-empty value for `eval_run_uuid` but received {eval_run_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/eval-runs/{eval_run_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"workspace_uuid": workspace_uuid}, run_delete_params.RunDeleteParams),
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        eval_run_uuid: str,
        *,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalRunResult:
        """
        Retrieve a specific eval run by its UUID.

        Args: eval_run_uuid (str): UUID of the eval run to retrieve. workspace_uuid
        (str, optional): UUID of the workspace. Defaults to None.

        Returns: EvalRunResult: The eval run data.

        Raises: AymaraAPIError: If the organization is missing or the eval run is not
        found.

        Example: GET /api/eval-runs/{eval_run_uuid}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not eval_run_uuid:
            raise ValueError(f"Expected a non-empty value for `eval_run_uuid` but received {eval_run_uuid!r}")
        return self._get(
            f"/v2/eval-runs/{eval_run_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"workspace_uuid": workspace_uuid}, run_get_params.RunGetParams),
            ),
            cast_to=EvalRunResult,
        )

    def list_responses(
        self,
        eval_run_uuid: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[ScoredResponse]:
        """
        Retrieve all responses for a specific eval run.

        Args: eval_run_uuid (str): UUID of the eval run to retrieve responses for.
        workspace_uuid (str, optional): UUID of the workspace. Defaults to None.

        Returns: list[EvalScoredResponse]: List of scored responses for the eval run.

        Raises: AymaraAPIError: If the organization is missing or the eval run is not
        found.

        Example: GET /api/eval-runs/{eval_run_uuid}/responses

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not eval_run_uuid:
            raise ValueError(f"Expected a non-empty value for `eval_run_uuid` but received {eval_run_uuid!r}")
        return self._get_api_list(
            f"/v2/eval-runs/{eval_run_uuid}/responses",
            page=SyncOffsetPage[ScoredResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "workspace_uuid": workspace_uuid,
                    },
                    run_list_responses_params.RunListResponsesParams,
                ),
            ),
            model=ScoredResponse,
        )

    def score_responses(
        self,
        *,
        eval_uuid: str,
        responses: Iterable[EvalResponseParam],
        is_sandbox: bool | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        ai_description: Optional[str] | NotGiven = NOT_GIVEN,
        continue_thread: Optional[bool] | NotGiven = NOT_GIVEN,
        eval_run_examples: Optional[Iterable[EvalRunExampleParam]] | NotGiven = NOT_GIVEN,
        eval_run_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalRunResult:
        """
        Run the eval with the provided responses.

        Args: eval_run_data (EvalRunRequest): Data for the eval run, including
        responses. workspace_uuid (str, optional): UUID of the workspace. Defaults to
        None. is_sandbox (bool, optional): Whether to run in sandbox mode. Defaults to
        False.

        Returns: EvalRunResult: The result of the eval run after scoring the responses.

        Raises: AymaraAPIError: If the organization is missing or the request is
        invalid.

        Example: POST /api/eval-runs/-/score-responses { "eval_uuid": "...",
        "responses": [...] }

        Args:
          eval_uuid: Unique identifier for the eval.

          responses: List of AI responses to eval prompts.

          ai_description: Description of the AI for this run, if any.

          continue_thread: Whether to continue the thread after this run.

          eval_run_examples: Examples to include with the eval run, if any.

          eval_run_uuid: Unique identifier for the eval run, if any.

          name: Name of the eval run, if any (defaults to the eval name + timestamp).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/eval-runs/-/score-responses",
            body=maybe_transform(
                {
                    "eval_uuid": eval_uuid,
                    "responses": responses,
                    "ai_description": ai_description,
                    "continue_thread": continue_thread,
                    "eval_run_examples": eval_run_examples,
                    "eval_run_uuid": eval_run_uuid,
                    "name": name,
                },
                run_score_responses_params.RunScoreResponsesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "is_sandbox": is_sandbox,
                        "workspace_uuid": workspace_uuid,
                    },
                    run_score_responses_params.RunScoreResponsesParams,
                ),
            ),
            cast_to=EvalRunResult,
        )


class AsyncRunsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aymara-ai/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aymara-ai/aymara-sdk-python#with_streaming_response
        """
        return AsyncRunsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        eval_uuid: str,
        responses: Iterable[EvalResponseParam],
        is_sandbox: Optional[bool] | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        ai_description: Optional[str] | NotGiven = NOT_GIVEN,
        continue_thread: Optional[bool] | NotGiven = NOT_GIVEN,
        eval_run_examples: Optional[Iterable[EvalRunExampleParam]] | NotGiven = NOT_GIVEN,
        eval_run_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalRunResult:
        """
        Create a new eval run for an eval.

        Args: eval_run_data (EvalRunRequest): Data for the eval run to create.
        workspace_uuid (str, optional): UUID of the workspace. Defaults to None.
        is_sandbox (bool, optional): Whether to run in sandbox mode. Defaults to None.

        Returns: EvalRunResult: The created eval run result.

        Raises: AymaraAPIError: If the organization is missing or the request is
        invalid.

        Example: POST /api/eval-runs { "eval_uuid": "...", ... }

        Args:
          eval_uuid: Unique identifier for the eval.

          responses: List of AI responses to eval prompts.

          ai_description: Description of the AI for this run, if any.

          continue_thread: Whether to continue the thread after this run.

          eval_run_examples: Examples to include with the eval run, if any.

          eval_run_uuid: Unique identifier for the eval run, if any.

          name: Name of the eval run, if any (defaults to the eval name + timestamp).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/eval-runs",
            body=await async_maybe_transform(
                {
                    "eval_uuid": eval_uuid,
                    "responses": responses,
                    "ai_description": ai_description,
                    "continue_thread": continue_thread,
                    "eval_run_examples": eval_run_examples,
                    "eval_run_uuid": eval_run_uuid,
                    "name": name,
                },
                run_create_params.RunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "is_sandbox": is_sandbox,
                        "workspace_uuid": workspace_uuid,
                    },
                    run_create_params.RunCreateParams,
                ),
            ),
            cast_to=EvalRunResult,
        )

    def list(
        self,
        *,
        eval_uuid: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EvalRunResult, AsyncOffsetPage[EvalRunResult]]:
        """
        List all eval runs, with optional filtering.

        Args: eval_uuid (str, optional): UUID of the eval to filter runs by. Defaults to
        None. workspace_uuid (str, optional): UUID of the workspace. Defaults to None.

        Returns: list[EvalRunResult]: List of eval runs matching the filters.

        Raises: AymaraAPIError: If the organization is missing.

        Example: GET /api/eval-runs?eval_uuid=...&workspace_uuid=...

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/eval-runs",
            page=AsyncOffsetPage[EvalRunResult],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "eval_uuid": eval_uuid,
                        "limit": limit,
                        "offset": offset,
                        "workspace_uuid": workspace_uuid,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            model=EvalRunResult,
        )

    async def delete(
        self,
        eval_run_uuid: str,
        *,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete an eval run.

        Args: eval_run_uuid (str): UUID of the eval run to delete.

        workspace_uuid (str,
        optional): UUID of the workspace. Defaults to None.

        Returns: None

        Raises: AymaraAPIError: If the organization is missing or the eval run is not
        found.

        Example: DELETE /api/eval-runs/{eval_run_uuid}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not eval_run_uuid:
            raise ValueError(f"Expected a non-empty value for `eval_run_uuid` but received {eval_run_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/eval-runs/{eval_run_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"workspace_uuid": workspace_uuid}, run_delete_params.RunDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        eval_run_uuid: str,
        *,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalRunResult:
        """
        Retrieve a specific eval run by its UUID.

        Args: eval_run_uuid (str): UUID of the eval run to retrieve. workspace_uuid
        (str, optional): UUID of the workspace. Defaults to None.

        Returns: EvalRunResult: The eval run data.

        Raises: AymaraAPIError: If the organization is missing or the eval run is not
        found.

        Example: GET /api/eval-runs/{eval_run_uuid}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not eval_run_uuid:
            raise ValueError(f"Expected a non-empty value for `eval_run_uuid` but received {eval_run_uuid!r}")
        return await self._get(
            f"/v2/eval-runs/{eval_run_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"workspace_uuid": workspace_uuid}, run_get_params.RunGetParams),
            ),
            cast_to=EvalRunResult,
        )

    def list_responses(
        self,
        eval_run_uuid: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ScoredResponse, AsyncOffsetPage[ScoredResponse]]:
        """
        Retrieve all responses for a specific eval run.

        Args: eval_run_uuid (str): UUID of the eval run to retrieve responses for.
        workspace_uuid (str, optional): UUID of the workspace. Defaults to None.

        Returns: list[EvalScoredResponse]: List of scored responses for the eval run.

        Raises: AymaraAPIError: If the organization is missing or the eval run is not
        found.

        Example: GET /api/eval-runs/{eval_run_uuid}/responses

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not eval_run_uuid:
            raise ValueError(f"Expected a non-empty value for `eval_run_uuid` but received {eval_run_uuid!r}")
        return self._get_api_list(
            f"/v2/eval-runs/{eval_run_uuid}/responses",
            page=AsyncOffsetPage[ScoredResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "workspace_uuid": workspace_uuid,
                    },
                    run_list_responses_params.RunListResponsesParams,
                ),
            ),
            model=ScoredResponse,
        )

    async def score_responses(
        self,
        *,
        eval_uuid: str,
        responses: Iterable[EvalResponseParam],
        is_sandbox: bool | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        ai_description: Optional[str] | NotGiven = NOT_GIVEN,
        continue_thread: Optional[bool] | NotGiven = NOT_GIVEN,
        eval_run_examples: Optional[Iterable[EvalRunExampleParam]] | NotGiven = NOT_GIVEN,
        eval_run_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalRunResult:
        """
        Run the eval with the provided responses.

        Args: eval_run_data (EvalRunRequest): Data for the eval run, including
        responses. workspace_uuid (str, optional): UUID of the workspace. Defaults to
        None. is_sandbox (bool, optional): Whether to run in sandbox mode. Defaults to
        False.

        Returns: EvalRunResult: The result of the eval run after scoring the responses.

        Raises: AymaraAPIError: If the organization is missing or the request is
        invalid.

        Example: POST /api/eval-runs/-/score-responses { "eval_uuid": "...",
        "responses": [...] }

        Args:
          eval_uuid: Unique identifier for the eval.

          responses: List of AI responses to eval prompts.

          ai_description: Description of the AI for this run, if any.

          continue_thread: Whether to continue the thread after this run.

          eval_run_examples: Examples to include with the eval run, if any.

          eval_run_uuid: Unique identifier for the eval run, if any.

          name: Name of the eval run, if any (defaults to the eval name + timestamp).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/eval-runs/-/score-responses",
            body=await async_maybe_transform(
                {
                    "eval_uuid": eval_uuid,
                    "responses": responses,
                    "ai_description": ai_description,
                    "continue_thread": continue_thread,
                    "eval_run_examples": eval_run_examples,
                    "eval_run_uuid": eval_run_uuid,
                    "name": name,
                },
                run_score_responses_params.RunScoreResponsesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "is_sandbox": is_sandbox,
                        "workspace_uuid": workspace_uuid,
                    },
                    run_score_responses_params.RunScoreResponsesParams,
                ),
            ),
            cast_to=EvalRunResult,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.create = to_raw_response_wrapper(
            runs.create,
        )
        self.list = to_raw_response_wrapper(
            runs.list,
        )
        self.delete = to_raw_response_wrapper(
            runs.delete,
        )
        self.get = to_raw_response_wrapper(
            runs.get,
        )
        self.list_responses = to_raw_response_wrapper(
            runs.list_responses,
        )
        self.score_responses = to_raw_response_wrapper(
            runs.score_responses,
        )


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.create = async_to_raw_response_wrapper(
            runs.create,
        )
        self.list = async_to_raw_response_wrapper(
            runs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            runs.delete,
        )
        self.get = async_to_raw_response_wrapper(
            runs.get,
        )
        self.list_responses = async_to_raw_response_wrapper(
            runs.list_responses,
        )
        self.score_responses = async_to_raw_response_wrapper(
            runs.score_responses,
        )


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.create = to_streamed_response_wrapper(
            runs.create,
        )
        self.list = to_streamed_response_wrapper(
            runs.list,
        )
        self.delete = to_streamed_response_wrapper(
            runs.delete,
        )
        self.get = to_streamed_response_wrapper(
            runs.get,
        )
        self.list_responses = to_streamed_response_wrapper(
            runs.list_responses,
        )
        self.score_responses = to_streamed_response_wrapper(
            runs.score_responses,
        )


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.create = async_to_streamed_response_wrapper(
            runs.create,
        )
        self.list = async_to_streamed_response_wrapper(
            runs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            runs.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            runs.get,
        )
        self.list_responses = async_to_streamed_response_wrapper(
            runs.list_responses,
        )
        self.score_responses = async_to_streamed_response_wrapper(
            runs.score_responses,
        )
