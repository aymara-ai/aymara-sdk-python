# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import eval_type_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncOffsetPage, AsyncOffsetPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.shared.eval_type import EvalType

__all__ = ["EvalTypesResource", "AsyncEvalTypesResource"]


class EvalTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvalTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aymara-ai/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EvalTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvalTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aymara-ai/aymara-sdk-python#with_streaming_response
        """
        return EvalTypesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[EvalType]:
        """
        List all available eval types.

        Returns: list[EvalTypeSchema]: List of available eval types.

        Raises: AymaraAPIError: If the request is invalid.

        Example: GET /api/eval-types

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/eval-types",
            page=SyncOffsetPage[EvalType],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    eval_type_list_params.EvalTypeListParams,
                ),
            ),
            model=EvalType,
        )

    def get(
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
        Retrieve a specific eval type by its UUID.

        Args: eval_type_uuid (str): UUID of the eval type to retrieve.

        Returns: EvalTypeSchema: The eval type data.

        Raises: AymaraAPIError: If the eval type is not found.

        Example: GET /api/eval-types/{eval_type_uuid}

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


class AsyncEvalTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvalTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aymara-ai/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvalTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvalTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aymara-ai/aymara-sdk-python#with_streaming_response
        """
        return AsyncEvalTypesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EvalType, AsyncOffsetPage[EvalType]]:
        """
        List all available eval types.

        Returns: list[EvalTypeSchema]: List of available eval types.

        Raises: AymaraAPIError: If the request is invalid.

        Example: GET /api/eval-types

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/eval-types",
            page=AsyncOffsetPage[EvalType],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    eval_type_list_params.EvalTypeListParams,
                ),
            ),
            model=EvalType,
        )

    async def get(
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
        Retrieve a specific eval type by its UUID.

        Args: eval_type_uuid (str): UUID of the eval type to retrieve.

        Returns: EvalTypeSchema: The eval type data.

        Raises: AymaraAPIError: If the eval type is not found.

        Example: GET /api/eval-types/{eval_type_uuid}

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


class EvalTypesResourceWithRawResponse:
    def __init__(self, eval_types: EvalTypesResource) -> None:
        self._eval_types = eval_types

        self.list = to_raw_response_wrapper(
            eval_types.list,
        )
        self.get = to_raw_response_wrapper(
            eval_types.get,
        )


class AsyncEvalTypesResourceWithRawResponse:
    def __init__(self, eval_types: AsyncEvalTypesResource) -> None:
        self._eval_types = eval_types

        self.list = async_to_raw_response_wrapper(
            eval_types.list,
        )
        self.get = async_to_raw_response_wrapper(
            eval_types.get,
        )


class EvalTypesResourceWithStreamingResponse:
    def __init__(self, eval_types: EvalTypesResource) -> None:
        self._eval_types = eval_types

        self.list = to_streamed_response_wrapper(
            eval_types.list,
        )
        self.get = to_streamed_response_wrapper(
            eval_types.get,
        )


class AsyncEvalTypesResourceWithStreamingResponse:
    def __init__(self, eval_types: AsyncEvalTypesResource) -> None:
        self._eval_types = eval_types

        self.list = async_to_streamed_response_wrapper(
            eval_types.list,
        )
        self.get = async_to_streamed_response_wrapper(
            eval_types.get,
        )
