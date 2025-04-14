# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

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
from ..._base_client import make_request_options
from ...types.eval_runs import (
    summary_list_params,
    summary_create_params,
    summary_delete_params,
    summary_retrieve_params,
)
from ...types.eval_runs.summary_list_response import SummaryListResponse
from ...types.eval_runs.eval_run_suite_summary import EvalRunSuiteSummary

__all__ = ["SummaryResource", "AsyncSummaryResource"]


class SummaryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#with_streaming_response
        """
        return SummaryResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        eval_run_uuids: List[str],
        is_sandbox: Optional[bool] | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalRunSuiteSummary:
        """
        Create a summary for a suite of eval runs.

        This function converts the EvalRunSuiteSummaryInSchema to
        ScoreRunSuiteSummaryInSchema and delegates to the create_score_run_suite_summary
        function.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/eval-runs/summary/",
            body=maybe_transform({"eval_run_uuids": eval_run_uuids}, summary_create_params.SummaryCreateParams),
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
                    summary_create_params.SummaryCreateParams,
                ),
            ),
            cast_to=EvalRunSuiteSummary,
        )

    def retrieve(
        self,
        summary_uuid: str,
        *,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalRunSuiteSummary:
        """
        Get a specific eval run suite summary by UUID.

        This function delegates to the get_score_run_suite_summary function.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not summary_uuid:
            raise ValueError(f"Expected a non-empty value for `summary_uuid` but received {summary_uuid!r}")
        return self._get(
            f"/v2/eval-runs/summary/{summary_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"workspace_uuid": workspace_uuid}, summary_retrieve_params.SummaryRetrieveParams
                ),
            ),
            cast_to=EvalRunSuiteSummary,
        )

    def list(
        self,
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
    ) -> SummaryListResponse:
        """
        List all eval run suite summaries, with optional filtering.

        This function delegates to the list_score_run_suite_summaries function.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/eval-runs/summary/",
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
                    summary_list_params.SummaryListParams,
                ),
            ),
            cast_to=SummaryListResponse,
        )

    def delete(
        self,
        summary_uuid: str,
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
        Delete an eval run suite summary.

        This function delegates to the delete_score_run_suite_summary function.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not summary_uuid:
            raise ValueError(f"Expected a non-empty value for `summary_uuid` but received {summary_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/eval-runs/summary/{summary_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"workspace_uuid": workspace_uuid}, summary_delete_params.SummaryDeleteParams),
            ),
            cast_to=NoneType,
        )


class AsyncSummaryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#with_streaming_response
        """
        return AsyncSummaryResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        eval_run_uuids: List[str],
        is_sandbox: Optional[bool] | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalRunSuiteSummary:
        """
        Create a summary for a suite of eval runs.

        This function converts the EvalRunSuiteSummaryInSchema to
        ScoreRunSuiteSummaryInSchema and delegates to the create_score_run_suite_summary
        function.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/eval-runs/summary/",
            body=await async_maybe_transform(
                {"eval_run_uuids": eval_run_uuids}, summary_create_params.SummaryCreateParams
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
                    summary_create_params.SummaryCreateParams,
                ),
            ),
            cast_to=EvalRunSuiteSummary,
        )

    async def retrieve(
        self,
        summary_uuid: str,
        *,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalRunSuiteSummary:
        """
        Get a specific eval run suite summary by UUID.

        This function delegates to the get_score_run_suite_summary function.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not summary_uuid:
            raise ValueError(f"Expected a non-empty value for `summary_uuid` but received {summary_uuid!r}")
        return await self._get(
            f"/v2/eval-runs/summary/{summary_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"workspace_uuid": workspace_uuid}, summary_retrieve_params.SummaryRetrieveParams
                ),
            ),
            cast_to=EvalRunSuiteSummary,
        )

    async def list(
        self,
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
    ) -> SummaryListResponse:
        """
        List all eval run suite summaries, with optional filtering.

        This function delegates to the list_score_run_suite_summaries function.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/eval-runs/summary/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "workspace_uuid": workspace_uuid,
                    },
                    summary_list_params.SummaryListParams,
                ),
            ),
            cast_to=SummaryListResponse,
        )

    async def delete(
        self,
        summary_uuid: str,
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
        Delete an eval run suite summary.

        This function delegates to the delete_score_run_suite_summary function.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not summary_uuid:
            raise ValueError(f"Expected a non-empty value for `summary_uuid` but received {summary_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/eval-runs/summary/{summary_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"workspace_uuid": workspace_uuid}, summary_delete_params.SummaryDeleteParams
                ),
            ),
            cast_to=NoneType,
        )


class SummaryResourceWithRawResponse:
    def __init__(self, summary: SummaryResource) -> None:
        self._summary = summary

        self.create = to_raw_response_wrapper(
            summary.create,
        )
        self.retrieve = to_raw_response_wrapper(
            summary.retrieve,
        )
        self.list = to_raw_response_wrapper(
            summary.list,
        )
        self.delete = to_raw_response_wrapper(
            summary.delete,
        )


class AsyncSummaryResourceWithRawResponse:
    def __init__(self, summary: AsyncSummaryResource) -> None:
        self._summary = summary

        self.create = async_to_raw_response_wrapper(
            summary.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            summary.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            summary.list,
        )
        self.delete = async_to_raw_response_wrapper(
            summary.delete,
        )


class SummaryResourceWithStreamingResponse:
    def __init__(self, summary: SummaryResource) -> None:
        self._summary = summary

        self.create = to_streamed_response_wrapper(
            summary.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            summary.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            summary.list,
        )
        self.delete = to_streamed_response_wrapper(
            summary.delete,
        )


class AsyncSummaryResourceWithStreamingResponse:
    def __init__(self, summary: AsyncSummaryResource) -> None:
        self._summary = summary

        self.create = async_to_streamed_response_wrapper(
            summary.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            summary.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            summary.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            summary.delete,
        )
