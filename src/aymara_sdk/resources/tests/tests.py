# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ...types import (
    ContentType,
    test_list_params,
    test_create_params,
    test_delete_params,
    test_retrieve_params,
    test_retrieve_questions_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .multiturn import (
    MultiturnResource,
    AsyncMultiturnResource,
    MultiturnResourceWithRawResponse,
    AsyncMultiturnResourceWithRawResponse,
    MultiturnResourceWithStreamingResponse,
    AsyncMultiturnResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.test_out import TestOut
from ...types.content_type import ContentType
from ...types.test_list_response import TestListResponse
from ...types.test_retrieve_questions_response import TestRetrieveQuestionsResponse

__all__ = ["TestsResource", "AsyncTestsResource"]


class TestsResource(SyncAPIResource):
    __test__ = False

    @cached_property
    def multiturn(self) -> MultiturnResource:
        return MultiturnResource(self._client)

    @cached_property
    def with_raw_response(self) -> TestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#with_streaming_response
        """
        return TestsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        student_description: str,
        test_name: str,
        is_sandbox: Optional[bool] | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        additional_instructions: Optional[str] | NotGiven = NOT_GIVEN,
        is_jailbreak: bool | NotGiven = NOT_GIVEN,
        knowledge_base: Optional[str] | NotGiven = NOT_GIVEN,
        modality: ContentType | NotGiven = NOT_GIVEN,
        num_test_questions: Optional[int] | NotGiven = NOT_GIVEN,
        test_examples: Optional[Iterable[test_create_params.TestExample]] | NotGiven = NOT_GIVEN,
        test_language: str | NotGiven = NOT_GIVEN,
        test_policy: Optional[str] | NotGiven = NOT_GIVEN,
        test_system_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        test_type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestOut:
        """
        Create Test

        Args:
          modality: Content type for AI interactions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tests/",
            body=maybe_transform(
                {
                    "student_description": student_description,
                    "test_name": test_name,
                    "additional_instructions": additional_instructions,
                    "is_jailbreak": is_jailbreak,
                    "knowledge_base": knowledge_base,
                    "modality": modality,
                    "num_test_questions": num_test_questions,
                    "test_examples": test_examples,
                    "test_language": test_language,
                    "test_policy": test_policy,
                    "test_system_prompt": test_system_prompt,
                    "test_type": test_type,
                },
                test_create_params.TestCreateParams,
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
                    test_create_params.TestCreateParams,
                ),
            ),
            cast_to=TestOut,
        )

    def retrieve(
        self,
        test_uuid: str,
        *,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestOut:
        """
        Get Test

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_uuid:
            raise ValueError(f"Expected a non-empty value for `test_uuid` but received {test_uuid!r}")
        return self._get(
            f"/v1/tests/{test_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"workspace_uuid": workspace_uuid}, test_retrieve_params.TestRetrieveParams),
            ),
            cast_to=TestOut,
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
    ) -> TestListResponse:
        """
        List Tests

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/tests/",
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
                    test_list_params.TestListParams,
                ),
            ),
            cast_to=TestListResponse,
        )

    def delete(
        self,
        test_uuid: str,
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
        Delete Test

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_uuid:
            raise ValueError(f"Expected a non-empty value for `test_uuid` but received {test_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/tests/{test_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"workspace_uuid": workspace_uuid}, test_delete_params.TestDeleteParams),
            ),
            cast_to=NoneType,
        )

    def retrieve_questions(
        self,
        test_uuid: str,
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
    ) -> TestRetrieveQuestionsResponse:
        """
        Get Test Questions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_uuid:
            raise ValueError(f"Expected a non-empty value for `test_uuid` but received {test_uuid!r}")
        return self._get(
            f"/v1/tests/{test_uuid}/questions",
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
                    test_retrieve_questions_params.TestRetrieveQuestionsParams,
                ),
            ),
            cast_to=TestRetrieveQuestionsResponse,
        )


class AsyncTestsResource(AsyncAPIResource):
    @cached_property
    def multiturn(self) -> AsyncMultiturnResource:
        return AsyncMultiturnResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/aymara-sdk-python#with_streaming_response
        """
        return AsyncTestsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        student_description: str,
        test_name: str,
        is_sandbox: Optional[bool] | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        additional_instructions: Optional[str] | NotGiven = NOT_GIVEN,
        is_jailbreak: bool | NotGiven = NOT_GIVEN,
        knowledge_base: Optional[str] | NotGiven = NOT_GIVEN,
        modality: ContentType | NotGiven = NOT_GIVEN,
        num_test_questions: Optional[int] | NotGiven = NOT_GIVEN,
        test_examples: Optional[Iterable[test_create_params.TestExample]] | NotGiven = NOT_GIVEN,
        test_language: str | NotGiven = NOT_GIVEN,
        test_policy: Optional[str] | NotGiven = NOT_GIVEN,
        test_system_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        test_type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestOut:
        """
        Create Test

        Args:
          modality: Content type for AI interactions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tests/",
            body=await async_maybe_transform(
                {
                    "student_description": student_description,
                    "test_name": test_name,
                    "additional_instructions": additional_instructions,
                    "is_jailbreak": is_jailbreak,
                    "knowledge_base": knowledge_base,
                    "modality": modality,
                    "num_test_questions": num_test_questions,
                    "test_examples": test_examples,
                    "test_language": test_language,
                    "test_policy": test_policy,
                    "test_system_prompt": test_system_prompt,
                    "test_type": test_type,
                },
                test_create_params.TestCreateParams,
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
                    test_create_params.TestCreateParams,
                ),
            ),
            cast_to=TestOut,
        )

    async def retrieve(
        self,
        test_uuid: str,
        *,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestOut:
        """
        Get Test

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_uuid:
            raise ValueError(f"Expected a non-empty value for `test_uuid` but received {test_uuid!r}")
        return await self._get(
            f"/v1/tests/{test_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"workspace_uuid": workspace_uuid}, test_retrieve_params.TestRetrieveParams
                ),
            ),
            cast_to=TestOut,
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
    ) -> TestListResponse:
        """
        List Tests

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/tests/",
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
                    test_list_params.TestListParams,
                ),
            ),
            cast_to=TestListResponse,
        )

    async def delete(
        self,
        test_uuid: str,
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
        Delete Test

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_uuid:
            raise ValueError(f"Expected a non-empty value for `test_uuid` but received {test_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/tests/{test_uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"workspace_uuid": workspace_uuid}, test_delete_params.TestDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    async def retrieve_questions(
        self,
        test_uuid: str,
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
    ) -> TestRetrieveQuestionsResponse:
        """
        Get Test Questions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_uuid:
            raise ValueError(f"Expected a non-empty value for `test_uuid` but received {test_uuid!r}")
        return await self._get(
            f"/v1/tests/{test_uuid}/questions",
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
                    test_retrieve_questions_params.TestRetrieveQuestionsParams,
                ),
            ),
            cast_to=TestRetrieveQuestionsResponse,
        )


class TestsResourceWithRawResponse:
    __test__ = False

    def __init__(self, tests: TestsResource) -> None:
        self._tests = tests

        self.create = to_raw_response_wrapper(
            tests.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tests.retrieve,
        )
        self.list = to_raw_response_wrapper(
            tests.list,
        )
        self.delete = to_raw_response_wrapper(
            tests.delete,
        )
        self.retrieve_questions = to_raw_response_wrapper(
            tests.retrieve_questions,
        )

    @cached_property
    def multiturn(self) -> MultiturnResourceWithRawResponse:
        return MultiturnResourceWithRawResponse(self._tests.multiturn)


class AsyncTestsResourceWithRawResponse:
    def __init__(self, tests: AsyncTestsResource) -> None:
        self._tests = tests

        self.create = async_to_raw_response_wrapper(
            tests.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tests.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            tests.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tests.delete,
        )
        self.retrieve_questions = async_to_raw_response_wrapper(
            tests.retrieve_questions,
        )

    @cached_property
    def multiturn(self) -> AsyncMultiturnResourceWithRawResponse:
        return AsyncMultiturnResourceWithRawResponse(self._tests.multiturn)


class TestsResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, tests: TestsResource) -> None:
        self._tests = tests

        self.create = to_streamed_response_wrapper(
            tests.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tests.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            tests.list,
        )
        self.delete = to_streamed_response_wrapper(
            tests.delete,
        )
        self.retrieve_questions = to_streamed_response_wrapper(
            tests.retrieve_questions,
        )

    @cached_property
    def multiturn(self) -> MultiturnResourceWithStreamingResponse:
        return MultiturnResourceWithStreamingResponse(self._tests.multiturn)


class AsyncTestsResourceWithStreamingResponse:
    def __init__(self, tests: AsyncTestsResource) -> None:
        self._tests = tests

        self.create = async_to_streamed_response_wrapper(
            tests.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tests.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            tests.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tests.delete,
        )
        self.retrieve_questions = async_to_streamed_response_wrapper(
            tests.retrieve_questions,
        )

    @cached_property
    def multiturn(self) -> AsyncMultiturnResourceWithStreamingResponse:
        return AsyncMultiturnResourceWithStreamingResponse(self._tests.multiturn)
