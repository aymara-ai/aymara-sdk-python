# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.tests import multiturn_continue_params
from ..._base_client import make_request_options
from ...types.answer_in_param import AnswerInParam
from ...types.tests.multiturn_continue_response import MultiturnContinueResponse

__all__ = ["MultiturnResource", "AsyncMultiturnResource"]


class MultiturnResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MultiturnResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MultiturnResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MultiturnResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#with_streaming_response
        """
        return MultiturnResourceWithStreamingResponse(self)

    def continue_(
        self,
        *,
        test_uuid: str,
        continue_eval: bool | NotGiven = NOT_GIVEN,
        is_sandbox: bool | NotGiven = NOT_GIVEN,
        answers: Optional[Iterable[AnswerInParam]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MultiturnContinueResponse:
        """
        Continue multiple conversations in a multiturn test with user messages.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tests/multiturn/continue",
            body=maybe_transform(
                {
                    "test_uuid": test_uuid,
                    "answers": answers,
                },
                multiturn_continue_params.MultiturnContinueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "continue_eval": continue_eval,
                        "is_sandbox": is_sandbox,
                    },
                    multiturn_continue_params.MultiturnContinueParams,
                ),
            ),
            cast_to=MultiturnContinueResponse,
        )


class AsyncMultiturnResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMultiturnResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMultiturnResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMultiturnResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#with_streaming_response
        """
        return AsyncMultiturnResourceWithStreamingResponse(self)

    async def continue_(
        self,
        *,
        test_uuid: str,
        continue_eval: bool | NotGiven = NOT_GIVEN,
        is_sandbox: bool | NotGiven = NOT_GIVEN,
        answers: Optional[Iterable[AnswerInParam]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MultiturnContinueResponse:
        """
        Continue multiple conversations in a multiturn test with user messages.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tests/multiturn/continue",
            body=await async_maybe_transform(
                {
                    "test_uuid": test_uuid,
                    "answers": answers,
                },
                multiturn_continue_params.MultiturnContinueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "continue_eval": continue_eval,
                        "is_sandbox": is_sandbox,
                    },
                    multiturn_continue_params.MultiturnContinueParams,
                ),
            ),
            cast_to=MultiturnContinueResponse,
        )


class MultiturnResourceWithRawResponse:
    def __init__(self, multiturn: MultiturnResource) -> None:
        self._multiturn = multiturn

        self.continue_ = to_raw_response_wrapper(
            multiturn.continue_,
        )


class AsyncMultiturnResourceWithRawResponse:
    def __init__(self, multiturn: AsyncMultiturnResource) -> None:
        self._multiturn = multiturn

        self.continue_ = async_to_raw_response_wrapper(
            multiturn.continue_,
        )


class MultiturnResourceWithStreamingResponse:
    def __init__(self, multiturn: MultiturnResource) -> None:
        self._multiturn = multiturn

        self.continue_ = to_streamed_response_wrapper(
            multiturn.continue_,
        )


class AsyncMultiturnResourceWithStreamingResponse:
    def __init__(self, multiturn: AsyncMultiturnResource) -> None:
        self._multiturn = multiturn

        self.continue_ = async_to_streamed_response_wrapper(
            multiturn.continue_,
        )
