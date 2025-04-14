# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from .image import (
    ImageResource,
    AsyncImageResource,
    ImageResourceWithRawResponse,
    AsyncImageResourceWithRawResponse,
    ImageResourceWithStreamingResponse,
    AsyncImageResourceWithStreamingResponse,
)
from ...types import (
    eval_run_list_params,
    eval_run_create_params,
    eval_run_delete_params,
    eval_run_retrieve_params,
    eval_run_run_score_params,
    eval_run_get_responses_params,
)
from .summary import (
    SummaryResource,
    AsyncSummaryResource,
    SummaryResourceWithRawResponse,
    AsyncSummaryResourceWithRawResponse,
    SummaryResourceWithStreamingResponse,
    AsyncSummaryResourceWithStreamingResponse,
)
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
from ...types.eval_run import EvalRun
from ...types.eval_run_list_response import EvalRunListResponse
from ...types.eval_run_run_score_response import EvalRunRunScoreResponse
from ...types.eval_run_get_responses_response import EvalRunGetResponsesResponse

__all__ = ["EvalRunsResource", "AsyncEvalRunsResource"]


class EvalRunsResource(SyncAPIResource):
    @cached_property
    def image(self) -> ImageResource:
        return ImageResource(self._client)

    @cached_property
    def summary(self) -> SummaryResource:
        return SummaryResource(self._client)

    @cached_property
    def with_raw_response(self) -> EvalRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EvalRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvalRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#with_streaming_response
        """
        return EvalRunsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        eval_uuid: str,
        responses: Iterable[eval_run_create_params.Response],
        is_sandbox: Optional[bool] | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        ai_description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_run_examples: Optional[Iterable[eval_run_create_params.EvalRunExample]] | NotGiven = NOT_GIVEN,
        eval_run_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        generate_prompts: Optional[bool] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalRun:
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
            "/v2/eval-runs/",
            body=maybe_transform(
                {
                    "eval_uuid": eval_uuid,
                    "responses": responses,
                    "ai_description": ai_description,
                    "eval_run_examples": eval_run_examples,
                    "eval_run_uuid": eval_run_uuid,
                    "generate_prompts": generate_prompts,
                    "name": name,
                },
                eval_run_create_params.EvalRunCreateParams,
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
                    eval_run_create_params.EvalRunCreateParams,
                ),
            ),
            cast_to=EvalRun,
        )

    def retrieve(
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
    ) -> EvalRun:
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
                query=maybe_transform(
                    {"workspace_uuid": workspace_uuid}, eval_run_retrieve_params.EvalRunRetrieveParams
                ),
            ),
            cast_to=EvalRun,
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
    ) -> EvalRunListResponse:
        """
        List all eval runs, with optional filtering.

        This function delegates to the list_score_runs function.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/eval-runs/",
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
                    eval_run_list_params.EvalRunListParams,
                ),
            ),
            cast_to=EvalRunListResponse,
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
                query=maybe_transform({"workspace_uuid": workspace_uuid}, eval_run_delete_params.EvalRunDeleteParams),
            ),
            cast_to=NoneType,
        )

    def get_responses(
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
    ) -> EvalRunGetResponsesResponse:
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
        return self._get(
            f"/v2/eval-runs/{eval_run_uuid}/responses",
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
                    eval_run_get_responses_params.EvalRunGetResponsesParams,
                ),
            ),
            cast_to=EvalRunGetResponsesResponse,
        )

    def run_score(
        self,
        *,
        eval_uuid: str,
        responses: Iterable[eval_run_run_score_params.Response],
        is_sandbox: bool | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        ai_description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_run_examples: Optional[Iterable[eval_run_run_score_params.EvalRunExample]] | NotGiven = NOT_GIVEN,
        eval_run_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        generate_prompts: Optional[bool] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalRunRunScoreResponse:
        """Run the eval with the provided responses.

        This function is used to submit AI
        responses to the eval prompts.

        Args:
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
                    "eval_run_examples": eval_run_examples,
                    "eval_run_uuid": eval_run_uuid,
                    "generate_prompts": generate_prompts,
                    "name": name,
                },
                eval_run_run_score_params.EvalRunRunScoreParams,
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
                    eval_run_run_score_params.EvalRunRunScoreParams,
                ),
            ),
            cast_to=EvalRunRunScoreResponse,
        )


class AsyncEvalRunsResource(AsyncAPIResource):
    @cached_property
    def image(self) -> AsyncImageResource:
        return AsyncImageResource(self._client)

    @cached_property
    def summary(self) -> AsyncSummaryResource:
        return AsyncSummaryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEvalRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvalRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvalRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#with_streaming_response
        """
        return AsyncEvalRunsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        eval_uuid: str,
        responses: Iterable[eval_run_create_params.Response],
        is_sandbox: Optional[bool] | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        ai_description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_run_examples: Optional[Iterable[eval_run_create_params.EvalRunExample]] | NotGiven = NOT_GIVEN,
        eval_run_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        generate_prompts: Optional[bool] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalRun:
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
            "/v2/eval-runs/",
            body=await async_maybe_transform(
                {
                    "eval_uuid": eval_uuid,
                    "responses": responses,
                    "ai_description": ai_description,
                    "eval_run_examples": eval_run_examples,
                    "eval_run_uuid": eval_run_uuid,
                    "generate_prompts": generate_prompts,
                    "name": name,
                },
                eval_run_create_params.EvalRunCreateParams,
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
                    eval_run_create_params.EvalRunCreateParams,
                ),
            ),
            cast_to=EvalRun,
        )

    async def retrieve(
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
    ) -> EvalRun:
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
                query=await async_maybe_transform(
                    {"workspace_uuid": workspace_uuid}, eval_run_retrieve_params.EvalRunRetrieveParams
                ),
            ),
            cast_to=EvalRun,
        )

    async def list(
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
    ) -> EvalRunListResponse:
        """
        List all eval runs, with optional filtering.

        This function delegates to the list_score_runs function.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/eval-runs/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "eval_uuid": eval_uuid,
                        "limit": limit,
                        "offset": offset,
                        "workspace_uuid": workspace_uuid,
                    },
                    eval_run_list_params.EvalRunListParams,
                ),
            ),
            cast_to=EvalRunListResponse,
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
                    {"workspace_uuid": workspace_uuid}, eval_run_delete_params.EvalRunDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    async def get_responses(
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
    ) -> EvalRunGetResponsesResponse:
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
        return await self._get(
            f"/v2/eval-runs/{eval_run_uuid}/responses",
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
                    eval_run_get_responses_params.EvalRunGetResponsesParams,
                ),
            ),
            cast_to=EvalRunGetResponsesResponse,
        )

    async def run_score(
        self,
        *,
        eval_uuid: str,
        responses: Iterable[eval_run_run_score_params.Response],
        is_sandbox: bool | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        ai_description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_run_examples: Optional[Iterable[eval_run_run_score_params.EvalRunExample]] | NotGiven = NOT_GIVEN,
        eval_run_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        generate_prompts: Optional[bool] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalRunRunScoreResponse:
        """Run the eval with the provided responses.

        This function is used to submit AI
        responses to the eval prompts.

        Args:
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
                    "eval_run_examples": eval_run_examples,
                    "eval_run_uuid": eval_run_uuid,
                    "generate_prompts": generate_prompts,
                    "name": name,
                },
                eval_run_run_score_params.EvalRunRunScoreParams,
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
                    eval_run_run_score_params.EvalRunRunScoreParams,
                ),
            ),
            cast_to=EvalRunRunScoreResponse,
        )


class EvalRunsResourceWithRawResponse:
    def __init__(self, eval_runs: EvalRunsResource) -> None:
        self._eval_runs = eval_runs

        self.create = to_raw_response_wrapper(
            eval_runs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            eval_runs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            eval_runs.list,
        )
        self.delete = to_raw_response_wrapper(
            eval_runs.delete,
        )
        self.get_responses = to_raw_response_wrapper(
            eval_runs.get_responses,
        )
        self.run_score = to_raw_response_wrapper(
            eval_runs.run_score,
        )

    @cached_property
    def image(self) -> ImageResourceWithRawResponse:
        return ImageResourceWithRawResponse(self._eval_runs.image)

    @cached_property
    def summary(self) -> SummaryResourceWithRawResponse:
        return SummaryResourceWithRawResponse(self._eval_runs.summary)


class AsyncEvalRunsResourceWithRawResponse:
    def __init__(self, eval_runs: AsyncEvalRunsResource) -> None:
        self._eval_runs = eval_runs

        self.create = async_to_raw_response_wrapper(
            eval_runs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            eval_runs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            eval_runs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            eval_runs.delete,
        )
        self.get_responses = async_to_raw_response_wrapper(
            eval_runs.get_responses,
        )
        self.run_score = async_to_raw_response_wrapper(
            eval_runs.run_score,
        )

    @cached_property
    def image(self) -> AsyncImageResourceWithRawResponse:
        return AsyncImageResourceWithRawResponse(self._eval_runs.image)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithRawResponse:
        return AsyncSummaryResourceWithRawResponse(self._eval_runs.summary)


class EvalRunsResourceWithStreamingResponse:
    def __init__(self, eval_runs: EvalRunsResource) -> None:
        self._eval_runs = eval_runs

        self.create = to_streamed_response_wrapper(
            eval_runs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            eval_runs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            eval_runs.list,
        )
        self.delete = to_streamed_response_wrapper(
            eval_runs.delete,
        )
        self.get_responses = to_streamed_response_wrapper(
            eval_runs.get_responses,
        )
        self.run_score = to_streamed_response_wrapper(
            eval_runs.run_score,
        )

    @cached_property
    def image(self) -> ImageResourceWithStreamingResponse:
        return ImageResourceWithStreamingResponse(self._eval_runs.image)

    @cached_property
    def summary(self) -> SummaryResourceWithStreamingResponse:
        return SummaryResourceWithStreamingResponse(self._eval_runs.summary)


class AsyncEvalRunsResourceWithStreamingResponse:
    def __init__(self, eval_runs: AsyncEvalRunsResource) -> None:
        self._eval_runs = eval_runs

        self.create = async_to_streamed_response_wrapper(
            eval_runs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            eval_runs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            eval_runs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            eval_runs.delete,
        )
        self.get_responses = async_to_streamed_response_wrapper(
            eval_runs.get_responses,
        )
        self.run_score = async_to_streamed_response_wrapper(
            eval_runs.run_score,
        )

    @cached_property
    def image(self) -> AsyncImageResourceWithStreamingResponse:
        return AsyncImageResourceWithStreamingResponse(self._eval_runs.image)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithStreamingResponse:
        return AsyncSummaryResourceWithStreamingResponse(self._eval_runs.summary)
