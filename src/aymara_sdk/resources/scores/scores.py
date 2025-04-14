# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .image import (
    ImageResource,
    AsyncImageResource,
    ImageResourceWithRawResponse,
    AsyncImageResourceWithRawResponse,
    ImageResourceWithStreamingResponse,
    AsyncImageResourceWithStreamingResponse,
)
from ...types import score_delete_params, score_retrieve_params, score_get_answers_params
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
from ...types.score_run_out import ScoreRunOut
from ...types.score_get_answers_response import ScoreGetAnswersResponse

__all__ = ["ScoresResource", "AsyncScoresResource"]


class ScoresResource(SyncAPIResource):
    @cached_property
    def image(self) -> ImageResource:
        return ImageResource(self._client)

    @cached_property
    def summary(self) -> SummaryResource:
        return SummaryResource(self._client)

    @cached_property
    def with_raw_response(self) -> ScoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ScoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#with_streaming_response
        """
        return ScoresResourceWithStreamingResponse(self)

    def retrieve(
        self,
        score_run_uuid: str,
        *,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScoreRunOut:
        """
        Get Score Run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not score_run_uuid:
            raise ValueError(f"Expected a non-empty value for `score_run_uuid` but received {score_run_uuid!r}")
        return self._get(
            f"/v1/scores/{score_run_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"workspace_uuid": workspace_uuid}, score_retrieve_params.ScoreRetrieveParams),
            ),
            cast_to=ScoreRunOut,
        )

    def delete(
        self,
        score_run_uuid: str,
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
        Delete Score Run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not score_run_uuid:
            raise ValueError(f"Expected a non-empty value for `score_run_uuid` but received {score_run_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/scores/{score_run_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"workspace_uuid": workspace_uuid}, score_delete_params.ScoreDeleteParams),
            ),
            cast_to=NoneType,
        )

    def get_answers(
        self,
        score_run_uuid: str,
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
    ) -> ScoreGetAnswersResponse:
        """
        Get Score Run Answers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not score_run_uuid:
            raise ValueError(f"Expected a non-empty value for `score_run_uuid` but received {score_run_uuid!r}")
        return self._get(
            f"/v1/scores/{score_run_uuid}/answers",
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
                    score_get_answers_params.ScoreGetAnswersParams,
                ),
            ),
            cast_to=ScoreGetAnswersResponse,
        )


class AsyncScoresResource(AsyncAPIResource):
    @cached_property
    def image(self) -> AsyncImageResource:
        return AsyncImageResource(self._client)

    @cached_property
    def summary(self) -> AsyncSummaryResource:
        return AsyncSummaryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncScoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#with_streaming_response
        """
        return AsyncScoresResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        score_run_uuid: str,
        *,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScoreRunOut:
        """
        Get Score Run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not score_run_uuid:
            raise ValueError(f"Expected a non-empty value for `score_run_uuid` but received {score_run_uuid!r}")
        return await self._get(
            f"/v1/scores/{score_run_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"workspace_uuid": workspace_uuid}, score_retrieve_params.ScoreRetrieveParams
                ),
            ),
            cast_to=ScoreRunOut,
        )

    async def delete(
        self,
        score_run_uuid: str,
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
        Delete Score Run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not score_run_uuid:
            raise ValueError(f"Expected a non-empty value for `score_run_uuid` but received {score_run_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/scores/{score_run_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"workspace_uuid": workspace_uuid}, score_delete_params.ScoreDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    async def get_answers(
        self,
        score_run_uuid: str,
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
    ) -> ScoreGetAnswersResponse:
        """
        Get Score Run Answers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not score_run_uuid:
            raise ValueError(f"Expected a non-empty value for `score_run_uuid` but received {score_run_uuid!r}")
        return await self._get(
            f"/v1/scores/{score_run_uuid}/answers",
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
                    score_get_answers_params.ScoreGetAnswersParams,
                ),
            ),
            cast_to=ScoreGetAnswersResponse,
        )


class ScoresResourceWithRawResponse:
    def __init__(self, scores: ScoresResource) -> None:
        self._scores = scores

        self.retrieve = to_raw_response_wrapper(
            scores.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            scores.delete,
        )
        self.get_answers = to_raw_response_wrapper(
            scores.get_answers,
        )

    @cached_property
    def image(self) -> ImageResourceWithRawResponse:
        return ImageResourceWithRawResponse(self._scores.image)

    @cached_property
    def summary(self) -> SummaryResourceWithRawResponse:
        return SummaryResourceWithRawResponse(self._scores.summary)


class AsyncScoresResourceWithRawResponse:
    def __init__(self, scores: AsyncScoresResource) -> None:
        self._scores = scores

        self.retrieve = async_to_raw_response_wrapper(
            scores.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            scores.delete,
        )
        self.get_answers = async_to_raw_response_wrapper(
            scores.get_answers,
        )

    @cached_property
    def image(self) -> AsyncImageResourceWithRawResponse:
        return AsyncImageResourceWithRawResponse(self._scores.image)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithRawResponse:
        return AsyncSummaryResourceWithRawResponse(self._scores.summary)


class ScoresResourceWithStreamingResponse:
    def __init__(self, scores: ScoresResource) -> None:
        self._scores = scores

        self.retrieve = to_streamed_response_wrapper(
            scores.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            scores.delete,
        )
        self.get_answers = to_streamed_response_wrapper(
            scores.get_answers,
        )

    @cached_property
    def image(self) -> ImageResourceWithStreamingResponse:
        return ImageResourceWithStreamingResponse(self._scores.image)

    @cached_property
    def summary(self) -> SummaryResourceWithStreamingResponse:
        return SummaryResourceWithStreamingResponse(self._scores.summary)


class AsyncScoresResourceWithStreamingResponse:
    def __init__(self, scores: AsyncScoresResource) -> None:
        self._scores = scores

        self.retrieve = async_to_streamed_response_wrapper(
            scores.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            scores.delete,
        )
        self.get_answers = async_to_streamed_response_wrapper(
            scores.get_answers,
        )

    @cached_property
    def image(self) -> AsyncImageResourceWithStreamingResponse:
        return AsyncImageResourceWithStreamingResponse(self._scores.image)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithStreamingResponse:
        return AsyncSummaryResourceWithStreamingResponse(self._scores.summary)
