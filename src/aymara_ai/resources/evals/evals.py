# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

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
    eval_update_params,
    eval_analyze_params,
    eval_list_prompts_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...types.eval_analyze_response import EvalAnalyzeResponse

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
        ai_instructions: Optional[eval_create_params.AIInstructions] | Omit = omit,
        created_at: Union[str, datetime, None] | Omit = omit,
        created_by: Optional[str] | Omit = omit,
        eval_instructions: Optional[str] | Omit = omit,
        eval_uuid: Optional[str] | Omit = omit,
        ground_truth: Optional[eval_create_params.GroundTruth] | Omit = omit,
        is_jailbreak: bool | Omit = omit,
        is_sandbox: bool | Omit = omit,
        language: Optional[str] | Omit = omit,
        modality: ContentType | Omit = omit,
        name: Optional[str] | Omit = omit,
        num_prompts: Optional[int] | Omit = omit,
        prompt_examples: Optional[Iterable[PromptExampleParam]] | Omit = omit,
        status: Optional[Status] | Omit = omit,
        task_timeout: Optional[int] | Omit = omit,
        updated_at: Union[str, datetime, None] | Omit = omit,
        workspace_uuid: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Eval:
        """
        Create a new eval using an eval type configuration.

        Args: eval_request (Eval): Data for the eval to create, including eval type and
        configuration.

        Returns: Eval: The created eval object.

        Raises: AymaraAPIError: If the request is invalid.

        Example: POST /api/evals { "eval_type": "...", "workspace_uuid": "...", ... }

        Args:
          ai_description: Description of the AI under evaluation.

          eval_type: Type of the eval (safety, accuracy, etc.)

          ai_instructions: Instructions the AI should follow. String for normal evals, AgentInstructions
              for single-agent evals, WorkflowInstructions for multi-agent workflows.

          created_at: Timestamp when the eval was created.

          created_by: Name of the user who created the evaluation.

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

          task_timeout: Custom timeout in seconds for task execution warning threshold. If not set,
              defaults to 180 seconds.

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
                    "created_by": created_by,
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
                    "task_timeout": task_timeout,
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

    def update(
        self,
        eval_uuid: str,
        *,
        workspace_uuid: str | Omit = omit,
        ai_description: Optional[str] | Omit = omit,
        ai_instructions: Optional[eval_update_params.AIInstructions] | Omit = omit,
        eval_instructions: Optional[str] | Omit = omit,
        ground_truth: Optional[eval_update_params.GroundTruth] | Omit = omit,
        name: Optional[str] | Omit = omit,
        prompt_creates: Optional[Iterable[eval_update_params.PromptCreate]] | Omit = omit,
        prompt_updates: Optional[Iterable[eval_update_params.PromptUpdate]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Eval:
        """
        Update an existing eval's fields and prompts.

        Args: eval_uuid (str): UUID of the eval to update. update_request
        (EvalUpdateRequest): Update data including fields and prompt modifications.
        workspace_uuid (str, optional): Optional workspace UUID for filtering.

        Returns: Eval: The updated eval data.

        Raises: AymaraAPIError: If the eval is not found or update is invalid.

        Example: PUT /api/evals/{eval_uuid} { "name": "Updated Eval Name",
        "ai_description": "Updated description", "prompt_updates": [ {"prompt_uuid":
        "...", "content": "New content", "action": "update"}, {"prompt_uuid": "...",
        "action": "delete"} ], "prompt_creates": [ {"content": "New prompt", "category":
        "test"} ] }

        Args:
          ai_description: New description of the AI under evaluation.

          ai_instructions: New instructions the AI should follow. String for normal evals,
              AgentInstructions for single-agent evals, WorkflowInstructions for multi-agent
              workflows.

          eval_instructions: New additional instructions for the eval.

          ground_truth: New ground truth data or reference file.

          name: New name for the evaluation.

          prompt_creates: List of new prompts to add.

          prompt_updates: List of prompt updates to apply.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not eval_uuid:
            raise ValueError(f"Expected a non-empty value for `eval_uuid` but received {eval_uuid!r}")
        return self._put(
            f"/v2/evals/{eval_uuid}",
            body=maybe_transform(
                {
                    "ai_description": ai_description,
                    "ai_instructions": ai_instructions,
                    "eval_instructions": eval_instructions,
                    "ground_truth": ground_truth,
                    "name": name,
                    "prompt_creates": prompt_creates,
                    "prompt_updates": prompt_updates,
                },
                eval_update_params.EvalUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"workspace_uuid": workspace_uuid}, eval_update_params.EvalUpdateParams),
            ),
            cast_to=Eval,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        workspace_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[Eval]:
        """
        List all evals, with optional filtering.

        Args: workspace_uuid (str, optional): Optional workspace UUID for filtering. Use
        "\\**" for enterprise-wide access, omit for user's current workspace.

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
        workspace_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    def analyze(
        self,
        *,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        created_by: Optional[str] | Omit = omit,
        eval_type: Optional[str] | Omit = omit,
        has_score_runs: Optional[bool] | Omit = omit,
        is_jailbreak: Optional[bool] | Omit = omit,
        is_sandbox: Optional[bool] | Omit = omit,
        language: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        max_pass_rate: Optional[float] | Omit = omit,
        min_pass_rate: Optional[float] | Omit = omit,
        modality: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        run_created_after: Union[str, datetime, None] | Omit = omit,
        run_created_before: Union[str, datetime, None] | Omit = omit,
        score_run_status: Optional[str] | Omit = omit,
        sort_by: Literal["created_at", "updated_at", "name", "pass_rate", "num_score_runs", "last_run_date"]
        | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        status: Optional[str] | Omit = omit,
        workspace_uuid: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvalAnalyzeResponse:
        """
        Analysis for evals with advanced filtering and aggregated statistics.

        This endpoint allows analyzing across both eval metadata and score run
        performance data, providing comprehensive filtering capabilities and aggregated
        statistics for each eval.

        Args: analysis_request (EvalAnalysisRequest): Analysis parameters and filters
        including: - Eval metadata filters (name, type, status, language, etc.) - Score
        run performance filters (pass rate, run count, etc.) - Sorting and pagination
        options

        Returns: EvalAnalysisResponse: Paginated results with matching evals and their
        statistics

        Raises: AymaraAPIError: If the request is invalid or analysis parameters are
        malformed

        Example: POST /api/v2/eval_analysis { "name": "safety", "eval_type": "safety",
        "min_pass_rate": 0.8, "has_score_runs": true, "sort_by": "pass_rate",
        "sort_order": "desc", "limit": 20, "offset": 0 }

        Args:
          created_after: Filter evals created after this date

          created_before: Filter evals created before this date

          created_by: Filter by creator email

          eval_type: Filter by eval type (safety, accuracy, jailbreak, image_safety)

          has_score_runs: Only include evals that have score runs

          is_jailbreak: Filter by jailbreak status

          is_sandbox: Filter by sandbox status

          language: Filter by language code (e.g., en, es)

          limit: Maximum number of results (1-100)

          max_pass_rate: Maximum average pass rate (0.0-1.0)

          min_pass_rate: Minimum average pass rate (0.0-1.0)

          modality: Filter by modality (text, image)

          name: Filter by eval names (case-insensitive partial match)

          offset: Number of results to skip

          run_created_after: Filter by score runs created after this date

          run_created_before: Filter by score runs created before this date

          score_run_status: Filter by any score run status

          sort_by: Field to sort by

          sort_order: Sort order

          status: Filter by eval status (created, processing, finished, failed)

          workspace_uuid: Filter by workspace UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/eval-analysis",
            body=maybe_transform(
                {
                    "created_after": created_after,
                    "created_before": created_before,
                    "created_by": created_by,
                    "eval_type": eval_type,
                    "has_score_runs": has_score_runs,
                    "is_jailbreak": is_jailbreak,
                    "is_sandbox": is_sandbox,
                    "language": language,
                    "limit": limit,
                    "max_pass_rate": max_pass_rate,
                    "min_pass_rate": min_pass_rate,
                    "modality": modality,
                    "name": name,
                    "offset": offset,
                    "run_created_after": run_created_after,
                    "run_created_before": run_created_before,
                    "score_run_status": score_run_status,
                    "sort_by": sort_by,
                    "sort_order": sort_order,
                    "status": status,
                    "workspace_uuid": workspace_uuid,
                },
                eval_analyze_params.EvalAnalyzeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvalAnalyzeResponse,
        )

    def get(
        self,
        eval_uuid: str,
        *,
        workspace_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        workspace_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        ai_instructions: Optional[eval_create_params.AIInstructions] | Omit = omit,
        created_at: Union[str, datetime, None] | Omit = omit,
        created_by: Optional[str] | Omit = omit,
        eval_instructions: Optional[str] | Omit = omit,
        eval_uuid: Optional[str] | Omit = omit,
        ground_truth: Optional[eval_create_params.GroundTruth] | Omit = omit,
        is_jailbreak: bool | Omit = omit,
        is_sandbox: bool | Omit = omit,
        language: Optional[str] | Omit = omit,
        modality: ContentType | Omit = omit,
        name: Optional[str] | Omit = omit,
        num_prompts: Optional[int] | Omit = omit,
        prompt_examples: Optional[Iterable[PromptExampleParam]] | Omit = omit,
        status: Optional[Status] | Omit = omit,
        task_timeout: Optional[int] | Omit = omit,
        updated_at: Union[str, datetime, None] | Omit = omit,
        workspace_uuid: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Eval:
        """
        Create a new eval using an eval type configuration.

        Args: eval_request (Eval): Data for the eval to create, including eval type and
        configuration.

        Returns: Eval: The created eval object.

        Raises: AymaraAPIError: If the request is invalid.

        Example: POST /api/evals { "eval_type": "...", "workspace_uuid": "...", ... }

        Args:
          ai_description: Description of the AI under evaluation.

          eval_type: Type of the eval (safety, accuracy, etc.)

          ai_instructions: Instructions the AI should follow. String for normal evals, AgentInstructions
              for single-agent evals, WorkflowInstructions for multi-agent workflows.

          created_at: Timestamp when the eval was created.

          created_by: Name of the user who created the evaluation.

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

          task_timeout: Custom timeout in seconds for task execution warning threshold. If not set,
              defaults to 180 seconds.

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
                    "created_by": created_by,
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
                    "task_timeout": task_timeout,
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

    async def update(
        self,
        eval_uuid: str,
        *,
        workspace_uuid: str | Omit = omit,
        ai_description: Optional[str] | Omit = omit,
        ai_instructions: Optional[eval_update_params.AIInstructions] | Omit = omit,
        eval_instructions: Optional[str] | Omit = omit,
        ground_truth: Optional[eval_update_params.GroundTruth] | Omit = omit,
        name: Optional[str] | Omit = omit,
        prompt_creates: Optional[Iterable[eval_update_params.PromptCreate]] | Omit = omit,
        prompt_updates: Optional[Iterable[eval_update_params.PromptUpdate]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Eval:
        """
        Update an existing eval's fields and prompts.

        Args: eval_uuid (str): UUID of the eval to update. update_request
        (EvalUpdateRequest): Update data including fields and prompt modifications.
        workspace_uuid (str, optional): Optional workspace UUID for filtering.

        Returns: Eval: The updated eval data.

        Raises: AymaraAPIError: If the eval is not found or update is invalid.

        Example: PUT /api/evals/{eval_uuid} { "name": "Updated Eval Name",
        "ai_description": "Updated description", "prompt_updates": [ {"prompt_uuid":
        "...", "content": "New content", "action": "update"}, {"prompt_uuid": "...",
        "action": "delete"} ], "prompt_creates": [ {"content": "New prompt", "category":
        "test"} ] }

        Args:
          ai_description: New description of the AI under evaluation.

          ai_instructions: New instructions the AI should follow. String for normal evals,
              AgentInstructions for single-agent evals, WorkflowInstructions for multi-agent
              workflows.

          eval_instructions: New additional instructions for the eval.

          ground_truth: New ground truth data or reference file.

          name: New name for the evaluation.

          prompt_creates: List of new prompts to add.

          prompt_updates: List of prompt updates to apply.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not eval_uuid:
            raise ValueError(f"Expected a non-empty value for `eval_uuid` but received {eval_uuid!r}")
        return await self._put(
            f"/v2/evals/{eval_uuid}",
            body=await async_maybe_transform(
                {
                    "ai_description": ai_description,
                    "ai_instructions": ai_instructions,
                    "eval_instructions": eval_instructions,
                    "ground_truth": ground_truth,
                    "name": name,
                    "prompt_creates": prompt_creates,
                    "prompt_updates": prompt_updates,
                },
                eval_update_params.EvalUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"workspace_uuid": workspace_uuid}, eval_update_params.EvalUpdateParams
                ),
            ),
            cast_to=Eval,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        workspace_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Eval, AsyncOffsetPage[Eval]]:
        """
        List all evals, with optional filtering.

        Args: workspace_uuid (str, optional): Optional workspace UUID for filtering. Use
        "\\**" for enterprise-wide access, omit for user's current workspace.

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
        workspace_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    async def analyze(
        self,
        *,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        created_by: Optional[str] | Omit = omit,
        eval_type: Optional[str] | Omit = omit,
        has_score_runs: Optional[bool] | Omit = omit,
        is_jailbreak: Optional[bool] | Omit = omit,
        is_sandbox: Optional[bool] | Omit = omit,
        language: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        max_pass_rate: Optional[float] | Omit = omit,
        min_pass_rate: Optional[float] | Omit = omit,
        modality: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        run_created_after: Union[str, datetime, None] | Omit = omit,
        run_created_before: Union[str, datetime, None] | Omit = omit,
        score_run_status: Optional[str] | Omit = omit,
        sort_by: Literal["created_at", "updated_at", "name", "pass_rate", "num_score_runs", "last_run_date"]
        | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        status: Optional[str] | Omit = omit,
        workspace_uuid: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvalAnalyzeResponse:
        """
        Analysis for evals with advanced filtering and aggregated statistics.

        This endpoint allows analyzing across both eval metadata and score run
        performance data, providing comprehensive filtering capabilities and aggregated
        statistics for each eval.

        Args: analysis_request (EvalAnalysisRequest): Analysis parameters and filters
        including: - Eval metadata filters (name, type, status, language, etc.) - Score
        run performance filters (pass rate, run count, etc.) - Sorting and pagination
        options

        Returns: EvalAnalysisResponse: Paginated results with matching evals and their
        statistics

        Raises: AymaraAPIError: If the request is invalid or analysis parameters are
        malformed

        Example: POST /api/v2/eval_analysis { "name": "safety", "eval_type": "safety",
        "min_pass_rate": 0.8, "has_score_runs": true, "sort_by": "pass_rate",
        "sort_order": "desc", "limit": 20, "offset": 0 }

        Args:
          created_after: Filter evals created after this date

          created_before: Filter evals created before this date

          created_by: Filter by creator email

          eval_type: Filter by eval type (safety, accuracy, jailbreak, image_safety)

          has_score_runs: Only include evals that have score runs

          is_jailbreak: Filter by jailbreak status

          is_sandbox: Filter by sandbox status

          language: Filter by language code (e.g., en, es)

          limit: Maximum number of results (1-100)

          max_pass_rate: Maximum average pass rate (0.0-1.0)

          min_pass_rate: Minimum average pass rate (0.0-1.0)

          modality: Filter by modality (text, image)

          name: Filter by eval names (case-insensitive partial match)

          offset: Number of results to skip

          run_created_after: Filter by score runs created after this date

          run_created_before: Filter by score runs created before this date

          score_run_status: Filter by any score run status

          sort_by: Field to sort by

          sort_order: Sort order

          status: Filter by eval status (created, processing, finished, failed)

          workspace_uuid: Filter by workspace UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/eval-analysis",
            body=await async_maybe_transform(
                {
                    "created_after": created_after,
                    "created_before": created_before,
                    "created_by": created_by,
                    "eval_type": eval_type,
                    "has_score_runs": has_score_runs,
                    "is_jailbreak": is_jailbreak,
                    "is_sandbox": is_sandbox,
                    "language": language,
                    "limit": limit,
                    "max_pass_rate": max_pass_rate,
                    "min_pass_rate": min_pass_rate,
                    "modality": modality,
                    "name": name,
                    "offset": offset,
                    "run_created_after": run_created_after,
                    "run_created_before": run_created_before,
                    "score_run_status": score_run_status,
                    "sort_by": sort_by,
                    "sort_order": sort_order,
                    "status": status,
                    "workspace_uuid": workspace_uuid,
                },
                eval_analyze_params.EvalAnalyzeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvalAnalyzeResponse,
        )

    async def get(
        self,
        eval_uuid: str,
        *,
        workspace_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        workspace_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        self.update = to_raw_response_wrapper(
            evals.update,
        )
        self.list = to_raw_response_wrapper(
            evals.list,
        )
        self.delete = to_raw_response_wrapper(
            evals.delete,
        )
        self.analyze = to_raw_response_wrapper(
            evals.analyze,
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
        self.update = async_to_raw_response_wrapper(
            evals.update,
        )
        self.list = async_to_raw_response_wrapper(
            evals.list,
        )
        self.delete = async_to_raw_response_wrapper(
            evals.delete,
        )
        self.analyze = async_to_raw_response_wrapper(
            evals.analyze,
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
        self.update = to_streamed_response_wrapper(
            evals.update,
        )
        self.list = to_streamed_response_wrapper(
            evals.list,
        )
        self.delete = to_streamed_response_wrapper(
            evals.delete,
        )
        self.analyze = to_streamed_response_wrapper(
            evals.analyze,
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
        self.update = async_to_streamed_response_wrapper(
            evals.update,
        )
        self.list = async_to_streamed_response_wrapper(
            evals.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            evals.delete,
        )
        self.analyze = async_to_streamed_response_wrapper(
            evals.analyze,
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
