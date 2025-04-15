# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.eval_type import EvalType
from ..types.eval_type_list_response import EvalTypeListResponse

__all__ = ["EvalTypesResource", "AsyncEvalTypesResource"]


class EvalTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvalTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EvalTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvalTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#with_streaming_response
        """
        return EvalTypesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        eval_type_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalType:
        """
        Get a specific eval type by UUID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not eval_type_uuid:
            raise ValueError(f"Expected a non-empty value for `eval_type_uuid` but received {eval_type_uuid!r}")
        return self._get(
            f"/v2/eval-types/{eval_type_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvalType,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalTypeListResponse:
        """List all available eval types."""
        return self._get(
            "/v2/eval-types/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvalTypeListResponse,
        )


class AsyncEvalTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvalTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvalTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvalTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#with_streaming_response
        """
        return AsyncEvalTypesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        eval_type_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalType:
        """
        Get a specific eval type by UUID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not eval_type_uuid:
            raise ValueError(f"Expected a non-empty value for `eval_type_uuid` but received {eval_type_uuid!r}")
        return await self._get(
            f"/v2/eval-types/{eval_type_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvalType,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalTypeListResponse:
        """List all available eval types."""
        return await self._get(
            "/v2/eval-types/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvalTypeListResponse,
        )


class EvalTypesResourceWithRawResponse:
    def __init__(self, eval_types: EvalTypesResource) -> None:
        self._eval_types = eval_types

        self.retrieve = to_raw_response_wrapper(
            eval_types.retrieve,
        )
        self.list = to_raw_response_wrapper(
            eval_types.list,
        )


class AsyncEvalTypesResourceWithRawResponse:
    def __init__(self, eval_types: AsyncEvalTypesResource) -> None:
        self._eval_types = eval_types

        self.retrieve = async_to_raw_response_wrapper(
            eval_types.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            eval_types.list,
        )


class EvalTypesResourceWithStreamingResponse:
    def __init__(self, eval_types: EvalTypesResource) -> None:
        self._eval_types = eval_types

        self.retrieve = to_streamed_response_wrapper(
            eval_types.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            eval_types.list,
        )


class AsyncEvalTypesResourceWithStreamingResponse:
    def __init__(self, eval_types: AsyncEvalTypesResource) -> None:
        self._eval_types = eval_types

        self.retrieve = async_to_streamed_response_wrapper(
            eval_types.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            eval_types.list,
        )
