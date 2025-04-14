# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import (
    ContentType,
    eval_list_params,
    eval_create_params,
    eval_delete_params,
    eval_retrieve_params,
    eval_get_prompts_params,
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
from ..types.eval_out import EvalOut
from ..types.content_type import ContentType
from ..types.eval_list_response import EvalListResponse
from ..types.prompt_example_in_param import PromptExampleInParam
from ..types.eval_get_prompts_response import EvalGetPromptsResponse

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

    def create(
        self,
        *,
        ai_description: str,
        eval_type: str,
        name: str,
        ai_instructions: Optional[str] | NotGiven = NOT_GIVEN,
        eval_instructions: Optional[str] | NotGiven = NOT_GIVEN,
        is_jailbreak: bool | NotGiven = NOT_GIVEN,
        is_sandbox: bool | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        modality: ContentType | NotGiven = NOT_GIVEN,
        num_prompts: int | NotGiven = NOT_GIVEN,
        prompt_examples: Optional[Iterable[PromptExampleInParam]] | NotGiven = NOT_GIVEN,
        workspace_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalOut:
        """
        Create a new eval using a template configuration.

        This function converts the EvalInSchema to TestInSchema and delegates to the
        create_test function.

        Args:
          modality: Content type for AI interactions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/evals/",
            body=maybe_transform(
                {
                    "ai_description": ai_description,
                    "eval_type": eval_type,
                    "name": name,
                    "ai_instructions": ai_instructions,
                    "eval_instructions": eval_instructions,
                    "is_jailbreak": is_jailbreak,
                    "is_sandbox": is_sandbox,
                    "language": language,
                    "modality": modality,
                    "num_prompts": num_prompts,
                    "prompt_examples": prompt_examples,
                    "workspace_uuid": workspace_uuid,
                },
                eval_create_params.EvalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvalOut,
        )

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
    ) -> EvalOut:
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
            cast_to=EvalOut,
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
    ) -> EvalListResponse:
        """
        List all evals, with optional filtering.

        Args: workspace_uuid: Optional workspace UUID for filtering

        Returns: List of evals

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/evals/",
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
                    eval_list_params.EvalListParams,
                ),
            ),
            cast_to=EvalListResponse,
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

    async def create(
        self,
        *,
        ai_description: str,
        eval_type: str,
        name: str,
        ai_instructions: Optional[str] | NotGiven = NOT_GIVEN,
        eval_instructions: Optional[str] | NotGiven = NOT_GIVEN,
        is_jailbreak: bool | NotGiven = NOT_GIVEN,
        is_sandbox: bool | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        modality: ContentType | NotGiven = NOT_GIVEN,
        num_prompts: int | NotGiven = NOT_GIVEN,
        prompt_examples: Optional[Iterable[PromptExampleInParam]] | NotGiven = NOT_GIVEN,
        workspace_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvalOut:
        """
        Create a new eval using a template configuration.

        This function converts the EvalInSchema to TestInSchema and delegates to the
        create_test function.

        Args:
          modality: Content type for AI interactions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/evals/",
            body=await async_maybe_transform(
                {
                    "ai_description": ai_description,
                    "eval_type": eval_type,
                    "name": name,
                    "ai_instructions": ai_instructions,
                    "eval_instructions": eval_instructions,
                    "is_jailbreak": is_jailbreak,
                    "is_sandbox": is_sandbox,
                    "language": language,
                    "modality": modality,
                    "num_prompts": num_prompts,
                    "prompt_examples": prompt_examples,
                    "workspace_uuid": workspace_uuid,
                },
                eval_create_params.EvalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvalOut,
        )

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
    ) -> EvalOut:
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
            cast_to=EvalOut,
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
    ) -> EvalListResponse:
        """
        List all evals, with optional filtering.

        Args: workspace_uuid: Optional workspace UUID for filtering

        Returns: List of evals

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/evals/",
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
                    eval_list_params.EvalListParams,
                ),
            ),
            cast_to=EvalListResponse,
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


class EvalsResourceWithRawResponse:
    def __init__(self, evals: EvalsResource) -> None:
        self._evals = evals

        self.create = to_raw_response_wrapper(
            evals.create,
        )
        self.retrieve = to_raw_response_wrapper(
            evals.retrieve,
        )
        self.list = to_raw_response_wrapper(
            evals.list,
        )
        self.delete = to_raw_response_wrapper(
            evals.delete,
        )
        self.get_prompts = to_raw_response_wrapper(
            evals.get_prompts,
        )


class AsyncEvalsResourceWithRawResponse:
    def __init__(self, evals: AsyncEvalsResource) -> None:
        self._evals = evals

        self.create = async_to_raw_response_wrapper(
            evals.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            evals.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            evals.list,
        )
        self.delete = async_to_raw_response_wrapper(
            evals.delete,
        )
        self.get_prompts = async_to_raw_response_wrapper(
            evals.get_prompts,
        )


class EvalsResourceWithStreamingResponse:
    def __init__(self, evals: EvalsResource) -> None:
        self._evals = evals

        self.create = to_streamed_response_wrapper(
            evals.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            evals.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            evals.list,
        )
        self.delete = to_streamed_response_wrapper(
            evals.delete,
        )
        self.get_prompts = to_streamed_response_wrapper(
            evals.get_prompts,
        )


class AsyncEvalsResourceWithStreamingResponse:
    def __init__(self, evals: AsyncEvalsResource) -> None:
        self._evals = evals

        self.create = async_to_streamed_response_wrapper(
            evals.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            evals.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            evals.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            evals.delete,
        )
        self.get_prompts = async_to_streamed_response_wrapper(
            evals.get_prompts,
        )
