# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Iterable, Optional, cast

import httpx

from ..types import file_list_params, file_create_params, file_upload_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
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
from ..types.file_detail import FileDetail
from ..types.file_frames import FileFrames
from ..types.file_status import FileStatus
from ..types.file_upload import FileUpload
from ..types.file_create_response import FileCreateResponse

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aymara-ai/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aymara-ai/aymara-sdk-python#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        files: Iterable[file_create_params.File],
        workspace_uuid: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileCreateResponse:
        """Request upload URLs for one or more files.

        Use this for batch uploads or when
        uploading files hosted at remote URLs.

        Args: upload_request (FileUploadRequest): Contains files to upload and workspace
        UUID. - Set remote_uri to fetch files from external URLs - Set local_file_path
        to generate an upload URL for client-side uploads

        Returns: FileUploadResponse: For each file, includes: - file_uuid: Use this to
        reference the file in eval runs - file_url: Upload URL (PUT your file here) or
        download URL (for remote_uri files) - processing_status: "pending" for remote
        files or videos, "completed" otherwise

        Example: POST /api/files { "workspace_uuid": "...", "files": [
        {"local_file_path": "data.csv"}, {"remote_uri": "https://example.com/file.mp4"}
        ] }

        Args:
          files: List of files to upload.

          workspace_uuid: UUID of the workspace to associate with the upload, if any.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/files",
            body=maybe_transform(
                {
                    "files": files,
                    "workspace_uuid": workspace_uuid,
                },
                file_create_params.FileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileCreateResponse,
        )

    def list(
        self,
        *,
        file_type: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        workspace_uuid: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[FileDetail]:
        """
        List all files for the authenticated organization, with optional filtering.

        Args: workspace_uuid (str, optional): Filter by workspace UUID. file_type (str,
        optional): Filter by file type (image, video, text, document).

        Returns: list[FileDetail]: List of files matching the filters.

        Raises: AymaraAPIError: If the organization is missing.

        Example: GET /api/v2/files?workspace_uuid=...&file_type=image

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/files",
            page=SyncOffsetPage[FileDetail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "file_type": file_type,
                        "limit": limit,
                        "offset": offset,
                        "workspace_uuid": workspace_uuid,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            model=FileDetail,
        )

    def delete(
        self,
        file_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a file (soft delete).

        Args: file_uuid (str): UUID of the file to delete.

        Returns: None (204 No Content)

        Raises: AymaraAPIError: If the file is not found or user lacks access.

        Example: DELETE /api/v2/files/{file_uuid}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_uuid:
            raise ValueError(f"Expected a non-empty value for `file_uuid` but received {file_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/files/{file_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        file_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileDetail:
        """
        Retrieve file metadata and access URL.

        Args: file_uuid (str): UUID of the file to retrieve.

        Returns: FileDetail: File metadata including: - file_url: Use this URL to
        download/view the file (valid for 30 minutes) - file_type: "image", "video",
        "text", or "document" - processing_status: For videos, check if "completed"
        before accessing frames - video_metadata: Contains frame_count and other
        video-specific info

        Note: For videos, use GET /files/{file_uuid}/frames to access individual frames.

        Example: GET /api/v2/files/{file_uuid}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_uuid:
            raise ValueError(f"Expected a non-empty value for `file_uuid` but received {file_uuid!r}")
        return self._get(
            f"/v2/files/{file_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileDetail,
        )

    def get_frames(
        self,
        file_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileFrames:
        """
        Get download URLs for all extracted frames from a video file.

        Only available for video files after processing completes. Check processing
        status with GET /files/{file_uuid}/status first.

        Args: file_uuid (str): UUID of the video file.

        Returns: FileFramesResponse: Contains: - frame_urls: List of URLs to access each
        frame (sorted by frame number) - frame_count: Total number of frames available

            Each frame URL is valid for 30 minutes. Use these URLs to download or display
            individual video frames for analysis.

        Raises: AymaraAPIError: - If file is not a video (use file_type field to
        check) - If processing not complete (check processing_status first)

        Example: GET /api/v2/files/{file_uuid}/frames

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_uuid:
            raise ValueError(f"Expected a non-empty value for `file_uuid` but received {file_uuid!r}")
        return self._get(
            f"/v2/files/{file_uuid}/frames",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileFrames,
        )

    def get_status(
        self,
        file_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileStatus:
        """Check processing status for a file.

        Use this to poll video processing progress.

        Args: file_uuid (str): UUID of the file to check status for.

        Returns: FileStatusResponse: Contains: - processing_status: "pending",
        "processing", "completed", or "failed" - error_message: If status is "failed",
        contains error details - remote_file_path: Available when status is "completed"

        Use this endpoint to poll until processing_status == "completed" before calling
        GET /files/{file_uuid}/frames for video files.

        Example: GET /api/v2/files/{file_uuid}/status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_uuid:
            raise ValueError(f"Expected a non-empty value for `file_uuid` but received {file_uuid!r}")
        return self._get(
            f"/v2/files/{file_uuid}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileStatus,
        )

    def upload(
        self,
        *,
        file: FileTypes,
        workspace_uuid: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileUpload:
        """Upload a file directly in the request body.

        Use this for single file uploads
        from your application.

        For video files, processing happens asynchronously - use GET
        /files/{file_uuid}/status to check processing status before accessing frames.

        Args: file: The file to upload (multipart form data) workspace_uuid: Optional
        workspace to associate the file with

        Returns: FileUploadResult with file_uuid for future reference and file_url for
        immediate access. For videos, check processing_status field - use status
        endpoint to poll until "completed".

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v2/files/-/uploads",
            body=maybe_transform(body, file_upload_params.FileUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"workspace_uuid": workspace_uuid}, file_upload_params.FileUploadParams),
            ),
            cast_to=FileUpload,
        )


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aymara-ai/aymara-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aymara-ai/aymara-sdk-python#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        files: Iterable[file_create_params.File],
        workspace_uuid: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileCreateResponse:
        """Request upload URLs for one or more files.

        Use this for batch uploads or when
        uploading files hosted at remote URLs.

        Args: upload_request (FileUploadRequest): Contains files to upload and workspace
        UUID. - Set remote_uri to fetch files from external URLs - Set local_file_path
        to generate an upload URL for client-side uploads

        Returns: FileUploadResponse: For each file, includes: - file_uuid: Use this to
        reference the file in eval runs - file_url: Upload URL (PUT your file here) or
        download URL (for remote_uri files) - processing_status: "pending" for remote
        files or videos, "completed" otherwise

        Example: POST /api/files { "workspace_uuid": "...", "files": [
        {"local_file_path": "data.csv"}, {"remote_uri": "https://example.com/file.mp4"}
        ] }

        Args:
          files: List of files to upload.

          workspace_uuid: UUID of the workspace to associate with the upload, if any.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/files",
            body=await async_maybe_transform(
                {
                    "files": files,
                    "workspace_uuid": workspace_uuid,
                },
                file_create_params.FileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileCreateResponse,
        )

    def list(
        self,
        *,
        file_type: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        workspace_uuid: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[FileDetail, AsyncOffsetPage[FileDetail]]:
        """
        List all files for the authenticated organization, with optional filtering.

        Args: workspace_uuid (str, optional): Filter by workspace UUID. file_type (str,
        optional): Filter by file type (image, video, text, document).

        Returns: list[FileDetail]: List of files matching the filters.

        Raises: AymaraAPIError: If the organization is missing.

        Example: GET /api/v2/files?workspace_uuid=...&file_type=image

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/files",
            page=AsyncOffsetPage[FileDetail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "file_type": file_type,
                        "limit": limit,
                        "offset": offset,
                        "workspace_uuid": workspace_uuid,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            model=FileDetail,
        )

    async def delete(
        self,
        file_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a file (soft delete).

        Args: file_uuid (str): UUID of the file to delete.

        Returns: None (204 No Content)

        Raises: AymaraAPIError: If the file is not found or user lacks access.

        Example: DELETE /api/v2/files/{file_uuid}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_uuid:
            raise ValueError(f"Expected a non-empty value for `file_uuid` but received {file_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/files/{file_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        file_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileDetail:
        """
        Retrieve file metadata and access URL.

        Args: file_uuid (str): UUID of the file to retrieve.

        Returns: FileDetail: File metadata including: - file_url: Use this URL to
        download/view the file (valid for 30 minutes) - file_type: "image", "video",
        "text", or "document" - processing_status: For videos, check if "completed"
        before accessing frames - video_metadata: Contains frame_count and other
        video-specific info

        Note: For videos, use GET /files/{file_uuid}/frames to access individual frames.

        Example: GET /api/v2/files/{file_uuid}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_uuid:
            raise ValueError(f"Expected a non-empty value for `file_uuid` but received {file_uuid!r}")
        return await self._get(
            f"/v2/files/{file_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileDetail,
        )

    async def get_frames(
        self,
        file_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileFrames:
        """
        Get download URLs for all extracted frames from a video file.

        Only available for video files after processing completes. Check processing
        status with GET /files/{file_uuid}/status first.

        Args: file_uuid (str): UUID of the video file.

        Returns: FileFramesResponse: Contains: - frame_urls: List of URLs to access each
        frame (sorted by frame number) - frame_count: Total number of frames available

            Each frame URL is valid for 30 minutes. Use these URLs to download or display
            individual video frames for analysis.

        Raises: AymaraAPIError: - If file is not a video (use file_type field to
        check) - If processing not complete (check processing_status first)

        Example: GET /api/v2/files/{file_uuid}/frames

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_uuid:
            raise ValueError(f"Expected a non-empty value for `file_uuid` but received {file_uuid!r}")
        return await self._get(
            f"/v2/files/{file_uuid}/frames",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileFrames,
        )

    async def get_status(
        self,
        file_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileStatus:
        """Check processing status for a file.

        Use this to poll video processing progress.

        Args: file_uuid (str): UUID of the file to check status for.

        Returns: FileStatusResponse: Contains: - processing_status: "pending",
        "processing", "completed", or "failed" - error_message: If status is "failed",
        contains error details - remote_file_path: Available when status is "completed"

        Use this endpoint to poll until processing_status == "completed" before calling
        GET /files/{file_uuid}/frames for video files.

        Example: GET /api/v2/files/{file_uuid}/status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_uuid:
            raise ValueError(f"Expected a non-empty value for `file_uuid` but received {file_uuid!r}")
        return await self._get(
            f"/v2/files/{file_uuid}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileStatus,
        )

    async def upload(
        self,
        *,
        file: FileTypes,
        workspace_uuid: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileUpload:
        """Upload a file directly in the request body.

        Use this for single file uploads
        from your application.

        For video files, processing happens asynchronously - use GET
        /files/{file_uuid}/status to check processing status before accessing frames.

        Args: file: The file to upload (multipart form data) workspace_uuid: Optional
        workspace to associate the file with

        Returns: FileUploadResult with file_uuid for future reference and file_url for
        immediate access. For videos, check processing_status field - use status
        endpoint to poll until "completed".

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v2/files/-/uploads",
            body=await async_maybe_transform(body, file_upload_params.FileUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"workspace_uuid": workspace_uuid}, file_upload_params.FileUploadParams
                ),
            ),
            cast_to=FileUpload,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.create = to_raw_response_wrapper(
            files.create,
        )
        self.list = to_raw_response_wrapper(
            files.list,
        )
        self.delete = to_raw_response_wrapper(
            files.delete,
        )
        self.get = to_raw_response_wrapper(
            files.get,
        )
        self.get_frames = to_raw_response_wrapper(
            files.get_frames,
        )
        self.get_status = to_raw_response_wrapper(
            files.get_status,
        )
        self.upload = to_raw_response_wrapper(
            files.upload,
        )


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.create = async_to_raw_response_wrapper(
            files.create,
        )
        self.list = async_to_raw_response_wrapper(
            files.list,
        )
        self.delete = async_to_raw_response_wrapper(
            files.delete,
        )
        self.get = async_to_raw_response_wrapper(
            files.get,
        )
        self.get_frames = async_to_raw_response_wrapper(
            files.get_frames,
        )
        self.get_status = async_to_raw_response_wrapper(
            files.get_status,
        )
        self.upload = async_to_raw_response_wrapper(
            files.upload,
        )


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.create = to_streamed_response_wrapper(
            files.create,
        )
        self.list = to_streamed_response_wrapper(
            files.list,
        )
        self.delete = to_streamed_response_wrapper(
            files.delete,
        )
        self.get = to_streamed_response_wrapper(
            files.get,
        )
        self.get_frames = to_streamed_response_wrapper(
            files.get_frames,
        )
        self.get_status = to_streamed_response_wrapper(
            files.get_status,
        )
        self.upload = to_streamed_response_wrapper(
            files.upload,
        )


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.create = async_to_streamed_response_wrapper(
            files.create,
        )
        self.list = async_to_streamed_response_wrapper(
            files.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            files.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            files.get,
        )
        self.get_frames = async_to_streamed_response_wrapper(
            files.get_frames,
        )
        self.get_status = async_to_streamed_response_wrapper(
            files.get_status,
        )
        self.upload = async_to_streamed_response_wrapper(
            files.upload,
        )
