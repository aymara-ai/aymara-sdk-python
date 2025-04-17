# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import (
    eval_delete_params,
    eval_get_run_params,
    eval_retrieve_params,
    eval_score_run_params,
    eval_delete_run_params,
    eval_get_prompts_params,
    eval_get_responses_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.eval_get_run_response import EvalGetRunResponse
from ..types.eval_retrieve_response import EvalRetrieveResponse
from ..types.eval_score_run_response import EvalScoreRunResponse
from ..types.eval_get_prompts_response import EvalGetPromptsResponse
from ..types.eval_get_responses_response import EvalGetResponsesResponse

__all__ = ["EvalsResource", "AsyncEvalsResource"]


class EvalsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EvalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#with_streaming_response
        """
        return EvalsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        eval_uuid: str,
        *,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalRetrieveResponse:
        """
        Get a specific eval by UUID.

        Args: eval_uuid: UUID of the eval to retrieve workspace_uuid: Optional workspace
        UUID for filtering

        Returns: The eval data

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not eval_uuid:
            raise ValueError(f"Expected a non-empty value for `eval_uuid` but received {eval_uuid!r}")
        return self._get(
            f"/v2/evals/{eval_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"workspace_uuid": workspace_uuid}, eval_retrieve_params.EvalRetrieveParams),
            ),
            cast_to=EvalRetrieveResponse,
        )

    def delete(
        self,
        eval_uuid: str,
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
        Delete an eval.

        Args: eval_uuid: UUID of the eval to delete workspace_uuid: Optional workspace
        UUID for filtering

        Returns: 204 No Content on success

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not eval_uuid:
            raise ValueError(f"Expected a non-empty value for `eval_uuid` but received {eval_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/evals/{eval_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"workspace_uuid": workspace_uuid}, eval_delete_params.EvalDeleteParams),
            ),
            cast_to=NoneType,
        )

    def delete_run(
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
                query=maybe_transform({"workspace_uuid": workspace_uuid}, eval_delete_run_params.EvalDeleteRunParams),
            ),
            cast_to=NoneType,
        )

    def get_prompts(
        self,
        eval_uuid: str,
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
    ) -> EvalGetPromptsResponse:
        """
        Find and return prompts for an eval if they exist.

        Args: eval_uuid: UUID of the eval to get questions for workspace_uuid: Optional
        workspace UUID for filtering

        Returns: List of questions and metadata

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not eval_uuid:
            raise ValueError(f"Expected a non-empty value for `eval_uuid` but received {eval_uuid!r}")
        return self._get(
            f"/v2/evals/{eval_uuid}/prompts",
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
                    eval_get_prompts_params.EvalGetPromptsParams,
                ),
            ),
            cast_to=EvalGetPromptsResponse,
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
    ) -> EvalGetResponsesResponse:
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
                    eval_get_responses_params.EvalGetResponsesParams,
                ),
            ),
            cast_to=EvalGetResponsesResponse,
        )

    def get_run(
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
    ) -> EvalGetRunResponse:
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
                query=maybe_transform({"workspace_uuid": workspace_uuid}, eval_get_run_params.EvalGetRunParams),
            ),
            cast_to=EvalGetRunResponse,
        )

    def score_run(
        self,
        *,
        eval_uuid: str,
        responses: Iterable[eval_score_run_params.Response],
        is_sandbox: bool | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        ai_description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_run_examples: Optional[Iterable[eval_score_run_params.EvalRunExample]] | NotGiven = NOT_GIVEN,
        eval_run_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        generate_prompts: Optional[bool] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalScoreRunResponse:
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
                eval_score_run_params.EvalScoreRunParams,
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
                    eval_score_run_params.EvalScoreRunParams,
                ),
            ),
            cast_to=EvalScoreRunResponse,
        )


class AsyncEvalsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#with_streaming_response
        """
        return AsyncEvalsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        eval_uuid: str,
        *,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalRetrieveResponse:
        """
        Get a specific eval by UUID.

        Args: eval_uuid: UUID of the eval to retrieve workspace_uuid: Optional workspace
        UUID for filtering

        Returns: The eval data

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not eval_uuid:
            raise ValueError(f"Expected a non-empty value for `eval_uuid` but received {eval_uuid!r}")
        return await self._get(
            f"/v2/evals/{eval_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"workspace_uuid": workspace_uuid}, eval_retrieve_params.EvalRetrieveParams
                ),
            ),
            cast_to=EvalRetrieveResponse,
        )

    async def delete(
        self,
        eval_uuid: str,
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
        Delete an eval.

        Args: eval_uuid: UUID of the eval to delete workspace_uuid: Optional workspace
        UUID for filtering

        Returns: 204 No Content on success

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not eval_uuid:
            raise ValueError(f"Expected a non-empty value for `eval_uuid` but received {eval_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/evals/{eval_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"workspace_uuid": workspace_uuid}, eval_delete_params.EvalDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    async def delete_run(
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
                    {"workspace_uuid": workspace_uuid}, eval_delete_run_params.EvalDeleteRunParams
                ),
            ),
            cast_to=NoneType,
        )

    async def get_prompts(
        self,
        eval_uuid: str,
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
    ) -> EvalGetPromptsResponse:
        """
        Find and return prompts for an eval if they exist.

        Args: eval_uuid: UUID of the eval to get questions for workspace_uuid: Optional
        workspace UUID for filtering

        Returns: List of questions and metadata

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not eval_uuid:
            raise ValueError(f"Expected a non-empty value for `eval_uuid` but received {eval_uuid!r}")
        return await self._get(
            f"/v2/evals/{eval_uuid}/prompts",
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
                    eval_get_prompts_params.EvalGetPromptsParams,
                ),
            ),
            cast_to=EvalGetPromptsResponse,
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
    ) -> EvalGetResponsesResponse:
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
                    eval_get_responses_params.EvalGetResponsesParams,
                ),
            ),
            cast_to=EvalGetResponsesResponse,
        )

    async def get_run(
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
    ) -> EvalGetRunResponse:
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
                    {"workspace_uuid": workspace_uuid}, eval_get_run_params.EvalGetRunParams
                ),
            ),
            cast_to=EvalGetRunResponse,
        )

    async def score_run(
        self,
        *,
        eval_uuid: str,
        responses: Iterable[eval_score_run_params.Response],
        is_sandbox: bool | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        ai_description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_run_examples: Optional[Iterable[eval_score_run_params.EvalRunExample]] | NotGiven = NOT_GIVEN,
        eval_run_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        generate_prompts: Optional[bool] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalScoreRunResponse:
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
                eval_score_run_params.EvalScoreRunParams,
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
                    eval_score_run_params.EvalScoreRunParams,
                ),
            ),
            cast_to=EvalScoreRunResponse,
        )


class EvalsResourceWithRawResponse:
    def __init__(self, evals: EvalsResource) -> None:
        self._evals = evals

        self.retrieve = to_raw_response_wrapper(
            evals.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            evals.delete,
        )
        self.delete_run = to_raw_response_wrapper(
            evals.delete_run,
        )
        self.get_prompts = to_raw_response_wrapper(
            evals.get_prompts,
        )
        self.get_responses = to_raw_response_wrapper(
            evals.get_responses,
        )
        self.get_run = to_raw_response_wrapper(
            evals.get_run,
        )
        self.score_run = to_raw_response_wrapper(
            evals.score_run,
        )


class AsyncEvalsResourceWithRawResponse:
    def __init__(self, evals: AsyncEvalsResource) -> None:
        self._evals = evals

        self.retrieve = async_to_raw_response_wrapper(
            evals.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            evals.delete,
        )
        self.delete_run = async_to_raw_response_wrapper(
            evals.delete_run,
        )
        self.get_prompts = async_to_raw_response_wrapper(
            evals.get_prompts,
        )
        self.get_responses = async_to_raw_response_wrapper(
            evals.get_responses,
        )
        self.get_run = async_to_raw_response_wrapper(
            evals.get_run,
        )
        self.score_run = async_to_raw_response_wrapper(
            evals.score_run,
        )


class EvalsResourceWithStreamingResponse:
    def __init__(self, evals: EvalsResource) -> None:
        self._evals = evals

        self.retrieve = to_streamed_response_wrapper(
            evals.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            evals.delete,
        )
        self.delete_run = to_streamed_response_wrapper(
            evals.delete_run,
        )
        self.get_prompts = to_streamed_response_wrapper(
            evals.get_prompts,
        )
        self.get_responses = to_streamed_response_wrapper(
            evals.get_responses,
        )
        self.get_run = to_streamed_response_wrapper(
            evals.get_run,
        )
        self.score_run = to_streamed_response_wrapper(
            evals.score_run,
        )


class AsyncEvalsResourceWithStreamingResponse:
    def __init__(self, evals: AsyncEvalsResource) -> None:
        self._evals = evals

        self.retrieve = async_to_streamed_response_wrapper(
            evals.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            evals.delete,
        )
        self.delete_run = async_to_streamed_response_wrapper(
            evals.delete_run,
        )
        self.get_prompts = async_to_streamed_response_wrapper(
            evals.get_prompts,
        )
        self.get_responses = async_to_streamed_response_wrapper(
            evals.get_responses,
        )
        self.get_run = async_to_streamed_response_wrapper(
            evals.get_run,
        )
        self.score_run = async_to_streamed_response_wrapper(
            evals.score_run,
        )
