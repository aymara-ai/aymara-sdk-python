# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
    run_continue_run_params,
    run_list_responses_params,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.eval_response_param import EvalResponseParam
from ...types.evals.eval_run_result import EvalRunResult
from ...types.eval_run_example_param import EvalRunExampleParam
from ...types.evals.run_list_responses_response import RunListResponsesResponse

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#with_streaming_response
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
        eval_run_examples: Optional[Iterable[EvalRunExampleParam]] | NotGiven = NOT_GIVEN,
        generate_prompts: Optional[bool] | NotGiven = NOT_GIVEN,
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

        This function converts the EvalRunInSchema to ScoreRunInSchema and delegates to
        the create_score_run function.

        Args:
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
                    "eval_run_examples": eval_run_examples,
                    "generate_prompts": generate_prompts,
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

        This function delegates to the list_score_runs function.

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
        """
        Delete an eval run.

        This function delegates to the delete_score_run function.

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

    def continue_run(
        self,
        eval_run_uuid: str,
        *,
        eval_uuid: str,
        responses: Iterable[EvalResponseParam],
        is_sandbox: bool | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        ai_description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_run_examples: Optional[Iterable[EvalRunExampleParam]] | NotGiven = NOT_GIVEN,
        generate_prompts: Optional[bool] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalRunResult:
        """Run the eval with the provided responses.

        This function is used to submit AI
        responses to the eval prompts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not eval_run_uuid:
            raise ValueError(f"Expected a non-empty value for `eval_run_uuid` but received {eval_run_uuid!r}")
        return self._post(
            f"/v2/eval-runs/{eval_run_uuid}/continue",
            body=maybe_transform(
                {
                    "eval_uuid": eval_uuid,
                    "responses": responses,
                    "ai_description": ai_description,
                    "eval_run_examples": eval_run_examples,
                    "generate_prompts": generate_prompts,
                    "name": name,
                },
                run_continue_run_params.RunContinueRunParams,
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
                    run_continue_run_params.RunContinueRunParams,
                ),
            ),
            cast_to=EvalRunResult,
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
        Get a specific eval run by UUID.

        This function delegates to the get_score_run function.

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
    ) -> SyncOffsetPage[RunListResponsesResponse]:
        """
        Get responses for a specific eval run.

        This function delegates to the get_score_run_answers function.

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
            page=SyncOffsetPage[RunListResponsesResponse],
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
            model=RunListResponsesResponse,
        )


class AsyncRunsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#with_streaming_response
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
        eval_run_examples: Optional[Iterable[EvalRunExampleParam]] | NotGiven = NOT_GIVEN,
        generate_prompts: Optional[bool] | NotGiven = NOT_GIVEN,
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

        This function converts the EvalRunInSchema to ScoreRunInSchema and delegates to
        the create_score_run function.

        Args:
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
                    "eval_run_examples": eval_run_examples,
                    "generate_prompts": generate_prompts,
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

        This function delegates to the list_score_runs function.

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
        """
        Delete an eval run.

        This function delegates to the delete_score_run function.

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

    async def continue_run(
        self,
        eval_run_uuid: str,
        *,
        eval_uuid: str,
        responses: Iterable[EvalResponseParam],
        is_sandbox: bool | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        ai_description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_run_examples: Optional[Iterable[EvalRunExampleParam]] | NotGiven = NOT_GIVEN,
        generate_prompts: Optional[bool] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalRunResult:
        """Run the eval with the provided responses.

        This function is used to submit AI
        responses to the eval prompts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not eval_run_uuid:
            raise ValueError(f"Expected a non-empty value for `eval_run_uuid` but received {eval_run_uuid!r}")
        return await self._post(
            f"/v2/eval-runs/{eval_run_uuid}/continue",
            body=await async_maybe_transform(
                {
                    "eval_uuid": eval_uuid,
                    "responses": responses,
                    "ai_description": ai_description,
                    "eval_run_examples": eval_run_examples,
                    "generate_prompts": generate_prompts,
                    "name": name,
                },
                run_continue_run_params.RunContinueRunParams,
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
                    run_continue_run_params.RunContinueRunParams,
                ),
            ),
            cast_to=EvalRunResult,
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
        Get a specific eval run by UUID.

        This function delegates to the get_score_run function.

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
    ) -> AsyncPaginator[RunListResponsesResponse, AsyncOffsetPage[RunListResponsesResponse]]:
        """
        Get responses for a specific eval run.

        This function delegates to the get_score_run_answers function.

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
            page=AsyncOffsetPage[RunListResponsesResponse],
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
            model=RunListResponsesResponse,
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
        self.continue_run = to_raw_response_wrapper(
            runs.continue_run,
        )
        self.get = to_raw_response_wrapper(
            runs.get,
        )
        self.list_responses = to_raw_response_wrapper(
            runs.list_responses,
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
        self.continue_run = async_to_raw_response_wrapper(
            runs.continue_run,
        )
        self.get = async_to_raw_response_wrapper(
            runs.get,
        )
        self.list_responses = async_to_raw_response_wrapper(
            runs.list_responses,
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
        self.continue_run = to_streamed_response_wrapper(
            runs.continue_run,
        )
        self.get = to_streamed_response_wrapper(
            runs.get,
        )
        self.list_responses = to_streamed_response_wrapper(
            runs.list_responses,
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
        self.continue_run = async_to_streamed_response_wrapper(
            runs.continue_run,
        )
        self.get = async_to_streamed_response_wrapper(
            runs.get,
        )
        self.list_responses = async_to_streamed_response_wrapper(
            runs.list_responses,
        )
