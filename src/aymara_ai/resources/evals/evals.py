# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime

import httpx

from .runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
from ...types import (
    eval_get_params,
    eval_list_params,
    eval_create_params,
    eval_delete_params,
    eval_list_prompts_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ...types.eval import Eval
from ..._base_client import AsyncPaginator, make_request_options
from ...types.eval_prompt import EvalPrompt
from ...types.shared.status import Status
from ...types.shared.content_type import ContentType
from ...types.prompt_example_param import PromptExampleParam

__all__ = ["EvalsResource", "AsyncEvalsResource"]


class EvalsResource(SyncAPIResource):
    @cached_property
    def runs(self) -> RunsResource:
        return RunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EvalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aymara-ai/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EvalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aymara-ai/aymara-sdk-python#with_streaming_response
        """
        return EvalsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        ai_description: str,
        eval_type: str,
        ai_instructions: Optional[str] | NotGiven = NOT_GIVEN,
        created_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        eval_instructions: Optional[str] | NotGiven = NOT_GIVEN,
        eval_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        ground_truth: Optional[eval_create_params.GroundTruth] | NotGiven = NOT_GIVEN,
        is_jailbreak: bool | NotGiven = NOT_GIVEN,
        is_sandbox: bool | NotGiven = NOT_GIVEN,
        language: Optional[str] | NotGiven = NOT_GIVEN,
        modality: ContentType | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        num_prompts: Optional[int] | NotGiven = NOT_GIVEN,
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
        Create a new eval using an eval type configuration.

        Args: eval_request (Eval): Data for the eval to create, including eval type and
        configuration.

        Returns: Eval: The created eval object.

        Raises: AymaraAPIError: If the workspace is not found or the request is invalid.

        Example: POST /api/evals { "eval_type": "...", "workspace_uuid": "...", ... }

        Args:
          ai_description: Description of the AI under evaluation.

          eval_type: Type of the eval (safety, accuracy, etc.)

          ai_instructions: Instructions the AI should follow.

          created_at: Timestamp when the eval was created.

          eval_instructions: Additional instructions for the eval, if any.

          eval_uuid: Unique identifier for the evaluation.

          ground_truth: Ground truth data or reference file, if any.

          is_jailbreak: Indicates if the eval is a jailbreak test.

          is_sandbox: Indicates if the eval results are sandboxed.

          language: Language code for the eval (default: "en").

          modality: Content type for AI interactions.

          name: Name of the evaluation.

          num_prompts: Number of prompts/questions in the eval (default: 50).

          prompt_examples: List of example prompts for the eval.

          status: Resource status.

          updated_at: Timestamp when the eval was last updated.

          workspace_uuid: UUID of the associated workspace, if any.

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
                    "ai_instructions": ai_instructions,
                    "created_at": created_at,
                    "eval_instructions": eval_instructions,
                    "eval_uuid": eval_uuid,
                    "ground_truth": ground_truth,
                    "is_jailbreak": is_jailbreak,
                    "is_sandbox": is_sandbox,
                    "language": language,
                    "modality": modality,
                    "name": name,
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

        Args: workspace_uuid (str, optional): Optional workspace UUID for filtering.

        Returns: list[Eval]: List of evals matching the filter.

        Raises: AymaraAPIError: If the request is invalid.

        Example: GET /api/evals?workspace_uuid=...

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
        """Delete an eval.

        Args: eval_uuid (str): UUID of the eval to delete.

        workspace_uuid (str,
        optional): Optional workspace UUID for filtering.

        Returns: None

        Raises: AymaraAPIError: If the eval is not found.

        Example: DELETE /api/evals/{eval_uuid}

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
        Retrieve a specific eval by its UUID.

        Args: eval_uuid (str): UUID of the eval to retrieve. workspace_uuid (str,
        optional): Optional workspace UUID for filtering.

        Returns: Eval: The eval data.

        Raises: AymaraAPIError: If the eval is not found.

        Example: GET /api/evals/{eval_uuid}

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
        Retrieve prompts for a specific eval if they exist.

        Args: eval_uuid (str): UUID of the eval to get prompts for. workspace_uuid (str,
        optional): Optional workspace UUID for filtering.

        Returns: list[EvalPrompt]: List of prompts and metadata for the eval.

        Raises: AymaraAPIError: If the eval is not found.

        Example: GET /api/evals/{eval_uuid}/prompts

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


class AsyncEvalsResource(AsyncAPIResource):
    @cached_property
    def runs(self) -> AsyncRunsResource:
        return AsyncRunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEvalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aymara-ai/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aymara-ai/aymara-sdk-python#with_streaming_response
        """
        return AsyncEvalsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        ai_description: str,
        eval_type: str,
        ai_instructions: Optional[str] | NotGiven = NOT_GIVEN,
        created_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        eval_instructions: Optional[str] | NotGiven = NOT_GIVEN,
        eval_uuid: Optional[str] | NotGiven = NOT_GIVEN,
        ground_truth: Optional[eval_create_params.GroundTruth] | NotGiven = NOT_GIVEN,
        is_jailbreak: bool | NotGiven = NOT_GIVEN,
        is_sandbox: bool | NotGiven = NOT_GIVEN,
        language: Optional[str] | NotGiven = NOT_GIVEN,
        modality: ContentType | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        num_prompts: Optional[int] | NotGiven = NOT_GIVEN,
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
        Create a new eval using an eval type configuration.

        Args: eval_request (Eval): Data for the eval to create, including eval type and
        configuration.

        Returns: Eval: The created eval object.

        Raises: AymaraAPIError: If the workspace is not found or the request is invalid.

        Example: POST /api/evals { "eval_type": "...", "workspace_uuid": "...", ... }

        Args:
          ai_description: Description of the AI under evaluation.

          eval_type: Type of the eval (safety, accuracy, etc.)

          ai_instructions: Instructions the AI should follow.

          created_at: Timestamp when the eval was created.

          eval_instructions: Additional instructions for the eval, if any.

          eval_uuid: Unique identifier for the evaluation.

          ground_truth: Ground truth data or reference file, if any.

          is_jailbreak: Indicates if the eval is a jailbreak test.

          is_sandbox: Indicates if the eval results are sandboxed.

          language: Language code for the eval (default: "en").

          modality: Content type for AI interactions.

          name: Name of the evaluation.

          num_prompts: Number of prompts/questions in the eval (default: 50).

          prompt_examples: List of example prompts for the eval.

          status: Resource status.

          updated_at: Timestamp when the eval was last updated.

          workspace_uuid: UUID of the associated workspace, if any.

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
                    "ai_instructions": ai_instructions,
                    "created_at": created_at,
                    "eval_instructions": eval_instructions,
                    "eval_uuid": eval_uuid,
                    "ground_truth": ground_truth,
                    "is_jailbreak": is_jailbreak,
                    "is_sandbox": is_sandbox,
                    "language": language,
                    "modality": modality,
                    "name": name,
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

        Args: workspace_uuid (str, optional): Optional workspace UUID for filtering.

        Returns: list[Eval]: List of evals matching the filter.

        Raises: AymaraAPIError: If the request is invalid.

        Example: GET /api/evals?workspace_uuid=...

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
        """Delete an eval.

        Args: eval_uuid (str): UUID of the eval to delete.

        workspace_uuid (str,
        optional): Optional workspace UUID for filtering.

        Returns: None

        Raises: AymaraAPIError: If the eval is not found.

        Example: DELETE /api/evals/{eval_uuid}

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
        Retrieve a specific eval by its UUID.

        Args: eval_uuid (str): UUID of the eval to retrieve. workspace_uuid (str,
        optional): Optional workspace UUID for filtering.

        Returns: Eval: The eval data.

        Raises: AymaraAPIError: If the eval is not found.

        Example: GET /api/evals/{eval_uuid}

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
        Retrieve prompts for a specific eval if they exist.

        Args: eval_uuid (str): UUID of the eval to get prompts for. workspace_uuid (str,
        optional): Optional workspace UUID for filtering.

        Returns: list[EvalPrompt]: List of prompts and metadata for the eval.

        Raises: AymaraAPIError: If the eval is not found.

        Example: GET /api/evals/{eval_uuid}/prompts

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
        self.get = to_raw_response_wrapper(
            evals.get,
        )
        self.list_prompts = to_raw_response_wrapper(
            evals.list_prompts,
        )

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self._evals.runs)


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
        self.get = async_to_raw_response_wrapper(
            evals.get,
        )
        self.list_prompts = async_to_raw_response_wrapper(
            evals.list_prompts,
        )

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self._evals.runs)


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
        self.get = to_streamed_response_wrapper(
            evals.get,
        )
        self.list_prompts = to_streamed_response_wrapper(
            evals.list_prompts,
        )

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self._evals.runs)


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
        self.get = async_to_streamed_response_wrapper(
            evals.get,
        )
        self.list_prompts = async_to_streamed_response_wrapper(
            evals.list_prompts,
        )

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self._evals.runs)
