# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime

import httpx

from ..types import (
    Status,
    ContentType,
    eval_get_params,
    eval_list_params,
    eval_create_params,
    eval_delete_params,
    eval_get_run_params,
    eval_list_runs_params,
    eval_create_run_params,
    eval_delete_run_params,
    eval_continue_run_params,
    eval_list_prompts_params,
    eval_list_responses_params,
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
from ..pagination import SyncOffsetPage, AsyncOffsetPage
from ..types.eval import Eval
from .._base_client import AsyncPaginator, make_request_options
from ..types.status import Status
from ..types.eval_prompt import EvalPrompt
from ..types.content_type import ContentType
from ..types.eval_run_result import EvalRunResult
from ..types.eval_response_param import EvalResponseParam
from ..types.prompt_example_param import PromptExampleParam
from ..types.eval_list_responses_response import EvalListResponsesResponse

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
        created_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        eval_instructions: Optional[str] | NotGiven = NOT_GIVEN,
        eval_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        is_jailbreak: bool | NotGiven = NOT_GIVEN,
        is_sandbox: bool | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        modality: ContentType | NotGiven = NOT_GIVEN,
        num_prompts: int | NotGiven = NOT_GIVEN,
        prompt_examples: Optional[Iterable[PromptExampleParam]] | NotGiven = NOT_GIVEN,
        status: Optional[Status] | NotGiven = NOT_GIVEN,
        updated_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        workspace_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Eval:
        """
        Create a new eval using a template configuration.

        This function converts the EvalInSchema to TestInSchema and delegates to the
        create_test function.

        Args:
          modality: Content type for AI interactions.

          status: Resource status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/evals",
            body=maybe_transform(
                {
                    "ai_description": ai_description,
                    "eval_type": eval_type,
                    "name": name,
                    "ai_instructions": ai_instructions,
                    "created_at": created_at,
                    "eval_instructions": eval_instructions,
                    "eval_uuid": eval_uuid,
                    "is_jailbreak": is_jailbreak,
                    "is_sandbox": is_sandbox,
                    "language": language,
                    "modality": modality,
                    "num_prompts": num_prompts,
                    "prompt_examples": prompt_examples,
                    "status": status,
                    "updated_at": updated_at,
                    "workspace_uuid": workspace_uuid,
                },
                eval_create_params.EvalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Eval,
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
    ) -> SyncOffsetPage[Eval]:
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
        return self._get_api_list(
            "/v2/evals",
            page=SyncOffsetPage[Eval],
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
            model=Eval,
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

    def continue_run(
        self,
        path_eval_run_uuid: str,
        *,
        eval_uuid: str,
        responses: Iterable[EvalResponseParam],
        is_sandbox: bool | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        ai_description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_run_examples: Optional[Iterable[eval_continue_run_params.EvalRunExample]] | NotGiven = NOT_GIVEN,
        body_eval_run_uuid: Optional[str] | NotGiven = NOT_GIVEN,
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
        if not path_eval_run_uuid:
            raise ValueError(f"Expected a non-empty value for `path_eval_run_uuid` but received {path_eval_run_uuid!r}")
        return self._post(
            f"/v2/eval-runs/{path_eval_run_uuid}/continue",
            body=maybe_transform(
                {
                    "eval_uuid": eval_uuid,
                    "responses": responses,
                    "ai_description": ai_description,
                    "eval_run_examples": eval_run_examples,
                    "body_eval_run_uuid": body_eval_run_uuid,
                    "generate_prompts": generate_prompts,
                    "name": name,
                },
                eval_continue_run_params.EvalContinueRunParams,
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
                    eval_continue_run_params.EvalContinueRunParams,
                ),
            ),
            cast_to=EvalRunResult,
        )

    def create_run(
        self,
        *,
        eval_uuid: str,
        responses: Iterable[EvalResponseParam],
        is_sandbox: Optional[bool] | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        ai_description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_run_examples: Optional[Iterable[eval_create_run_params.EvalRunExample]] | NotGiven = NOT_GIVEN,
        eval_run_uuid: Optional[str] | NotGiven = NOT_GIVEN,
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
                    "eval_run_uuid": eval_run_uuid,
                    "generate_prompts": generate_prompts,
                    "name": name,
                },
                eval_create_run_params.EvalCreateRunParams,
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
                    eval_create_run_params.EvalCreateRunParams,
                ),
            ),
            cast_to=EvalRunResult,
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

    def get(
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
    ) -> Eval:
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
                query=maybe_transform({"workspace_uuid": workspace_uuid}, eval_get_params.EvalGetParams),
            ),
            cast_to=Eval,
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
                query=maybe_transform({"workspace_uuid": workspace_uuid}, eval_get_run_params.EvalGetRunParams),
            ),
            cast_to=EvalRunResult,
        )

    def list_prompts(
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
    ) -> SyncOffsetPage[EvalPrompt]:
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
        return self._get_api_list(
            f"/v2/evals/{eval_uuid}/prompts",
            page=SyncOffsetPage[EvalPrompt],
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
                    eval_list_prompts_params.EvalListPromptsParams,
                ),
            ),
            model=EvalPrompt,
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
    ) -> SyncOffsetPage[EvalListResponsesResponse]:
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
            page=SyncOffsetPage[EvalListResponsesResponse],
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
                    eval_list_responses_params.EvalListResponsesParams,
                ),
            ),
            model=EvalListResponsesResponse,
        )

    def list_runs(
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
                    eval_list_runs_params.EvalListRunsParams,
                ),
            ),
            model=EvalRunResult,
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
        created_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        eval_instructions: Optional[str] | NotGiven = NOT_GIVEN,
        eval_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        is_jailbreak: bool | NotGiven = NOT_GIVEN,
        is_sandbox: bool | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        modality: ContentType | NotGiven = NOT_GIVEN,
        num_prompts: int | NotGiven = NOT_GIVEN,
        prompt_examples: Optional[Iterable[PromptExampleParam]] | NotGiven = NOT_GIVEN,
        status: Optional[Status] | NotGiven = NOT_GIVEN,
        updated_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        workspace_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Eval:
        """
        Create a new eval using a template configuration.

        This function converts the EvalInSchema to TestInSchema and delegates to the
        create_test function.

        Args:
          modality: Content type for AI interactions.

          status: Resource status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/evals",
            body=await async_maybe_transform(
                {
                    "ai_description": ai_description,
                    "eval_type": eval_type,
                    "name": name,
                    "ai_instructions": ai_instructions,
                    "created_at": created_at,
                    "eval_instructions": eval_instructions,
                    "eval_uuid": eval_uuid,
                    "is_jailbreak": is_jailbreak,
                    "is_sandbox": is_sandbox,
                    "language": language,
                    "modality": modality,
                    "num_prompts": num_prompts,
                    "prompt_examples": prompt_examples,
                    "status": status,
                    "updated_at": updated_at,
                    "workspace_uuid": workspace_uuid,
                },
                eval_create_params.EvalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Eval,
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
    ) -> AsyncPaginator[Eval, AsyncOffsetPage[Eval]]:
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
        return self._get_api_list(
            "/v2/evals",
            page=AsyncOffsetPage[Eval],
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
            model=Eval,
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

    async def continue_run(
        self,
        path_eval_run_uuid: str,
        *,
        eval_uuid: str,
        responses: Iterable[EvalResponseParam],
        is_sandbox: bool | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        ai_description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_run_examples: Optional[Iterable[eval_continue_run_params.EvalRunExample]] | NotGiven = NOT_GIVEN,
        body_eval_run_uuid: Optional[str] | NotGiven = NOT_GIVEN,
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
        if not path_eval_run_uuid:
            raise ValueError(f"Expected a non-empty value for `path_eval_run_uuid` but received {path_eval_run_uuid!r}")
        return await self._post(
            f"/v2/eval-runs/{path_eval_run_uuid}/continue",
            body=await async_maybe_transform(
                {
                    "eval_uuid": eval_uuid,
                    "responses": responses,
                    "ai_description": ai_description,
                    "eval_run_examples": eval_run_examples,
                    "body_eval_run_uuid": body_eval_run_uuid,
                    "generate_prompts": generate_prompts,
                    "name": name,
                },
                eval_continue_run_params.EvalContinueRunParams,
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
                    eval_continue_run_params.EvalContinueRunParams,
                ),
            ),
            cast_to=EvalRunResult,
        )

    async def create_run(
        self,
        *,
        eval_uuid: str,
        responses: Iterable[EvalResponseParam],
        is_sandbox: Optional[bool] | NotGiven = NOT_GIVEN,
        workspace_uuid: str | NotGiven = NOT_GIVEN,
        ai_description: Optional[str] | NotGiven = NOT_GIVEN,
        eval_run_examples: Optional[Iterable[eval_create_run_params.EvalRunExample]] | NotGiven = NOT_GIVEN,
        eval_run_uuid: Optional[str] | NotGiven = NOT_GIVEN,
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
                    "eval_run_uuid": eval_run_uuid,
                    "generate_prompts": generate_prompts,
                    "name": name,
                },
                eval_create_run_params.EvalCreateRunParams,
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
                    eval_create_run_params.EvalCreateRunParams,
                ),
            ),
            cast_to=EvalRunResult,
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

    async def get(
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
    ) -> Eval:
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
                query=await async_maybe_transform({"workspace_uuid": workspace_uuid}, eval_get_params.EvalGetParams),
            ),
            cast_to=Eval,
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
                query=await async_maybe_transform(
                    {"workspace_uuid": workspace_uuid}, eval_get_run_params.EvalGetRunParams
                ),
            ),
            cast_to=EvalRunResult,
        )

    def list_prompts(
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
    ) -> AsyncPaginator[EvalPrompt, AsyncOffsetPage[EvalPrompt]]:
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
        return self._get_api_list(
            f"/v2/evals/{eval_uuid}/prompts",
            page=AsyncOffsetPage[EvalPrompt],
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
                    eval_list_prompts_params.EvalListPromptsParams,
                ),
            ),
            model=EvalPrompt,
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
    ) -> AsyncPaginator[EvalListResponsesResponse, AsyncOffsetPage[EvalListResponsesResponse]]:
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
            page=AsyncOffsetPage[EvalListResponsesResponse],
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
                    eval_list_responses_params.EvalListResponsesParams,
                ),
            ),
            model=EvalListResponsesResponse,
        )

    def list_runs(
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
                    eval_list_runs_params.EvalListRunsParams,
                ),
            ),
            model=EvalRunResult,
        )


class EvalsResourceWithRawResponse:
    def __init__(self, evals: EvalsResource) -> None:
        self._evals = evals

        self.create = to_raw_response_wrapper(
            evals.create,
        )
        self.list = to_raw_response_wrapper(
            evals.list,
        )
        self.delete = to_raw_response_wrapper(
            evals.delete,
        )
        self.continue_run = to_raw_response_wrapper(
            evals.continue_run,
        )
        self.create_run = to_raw_response_wrapper(
            evals.create_run,
        )
        self.delete_run = to_raw_response_wrapper(
            evals.delete_run,
        )
        self.get = to_raw_response_wrapper(
            evals.get,
        )
        self.get_run = to_raw_response_wrapper(
            evals.get_run,
        )
        self.list_prompts = to_raw_response_wrapper(
            evals.list_prompts,
        )
        self.list_responses = to_raw_response_wrapper(
            evals.list_responses,
        )
        self.list_runs = to_raw_response_wrapper(
            evals.list_runs,
        )


class AsyncEvalsResourceWithRawResponse:
    def __init__(self, evals: AsyncEvalsResource) -> None:
        self._evals = evals

        self.create = async_to_raw_response_wrapper(
            evals.create,
        )
        self.list = async_to_raw_response_wrapper(
            evals.list,
        )
        self.delete = async_to_raw_response_wrapper(
            evals.delete,
        )
        self.continue_run = async_to_raw_response_wrapper(
            evals.continue_run,
        )
        self.create_run = async_to_raw_response_wrapper(
            evals.create_run,
        )
        self.delete_run = async_to_raw_response_wrapper(
            evals.delete_run,
        )
        self.get = async_to_raw_response_wrapper(
            evals.get,
        )
        self.get_run = async_to_raw_response_wrapper(
            evals.get_run,
        )
        self.list_prompts = async_to_raw_response_wrapper(
            evals.list_prompts,
        )
        self.list_responses = async_to_raw_response_wrapper(
            evals.list_responses,
        )
        self.list_runs = async_to_raw_response_wrapper(
            evals.list_runs,
        )


class EvalsResourceWithStreamingResponse:
    def __init__(self, evals: EvalsResource) -> None:
        self._evals = evals

        self.create = to_streamed_response_wrapper(
            evals.create,
        )
        self.list = to_streamed_response_wrapper(
            evals.list,
        )
        self.delete = to_streamed_response_wrapper(
            evals.delete,
        )
        self.continue_run = to_streamed_response_wrapper(
            evals.continue_run,
        )
        self.create_run = to_streamed_response_wrapper(
            evals.create_run,
        )
        self.delete_run = to_streamed_response_wrapper(
            evals.delete_run,
        )
        self.get = to_streamed_response_wrapper(
            evals.get,
        )
        self.get_run = to_streamed_response_wrapper(
            evals.get_run,
        )
        self.list_prompts = to_streamed_response_wrapper(
            evals.list_prompts,
        )
        self.list_responses = to_streamed_response_wrapper(
            evals.list_responses,
        )
        self.list_runs = to_streamed_response_wrapper(
            evals.list_runs,
        )


class AsyncEvalsResourceWithStreamingResponse:
    def __init__(self, evals: AsyncEvalsResource) -> None:
        self._evals = evals

        self.create = async_to_streamed_response_wrapper(
            evals.create,
        )
        self.list = async_to_streamed_response_wrapper(
            evals.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            evals.delete,
        )
        self.continue_run = async_to_streamed_response_wrapper(
            evals.continue_run,
        )
        self.create_run = async_to_streamed_response_wrapper(
            evals.create_run,
        )
        self.delete_run = async_to_streamed_response_wrapper(
            evals.delete_run,
        )
        self.get = async_to_streamed_response_wrapper(
            evals.get,
        )
        self.get_run = async_to_streamed_response_wrapper(
            evals.get_run,
        )
        self.list_prompts = async_to_streamed_response_wrapper(
            evals.list_prompts,
        )
        self.list_responses = async_to_streamed_response_wrapper(
            evals.list_responses,
        )
        self.list_runs = async_to_streamed_response_wrapper(
            evals.list_runs,
        )
