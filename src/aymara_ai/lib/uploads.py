import mimetypes
from typing import Union, Optional
from pathlib import Path

import httpx
import aiofiles

from aymara_ai import AymaraAI, AsyncAymaraAI
from aymara_ai.types.shared_params import FileReference


def _default_file_name(content_type: Optional[str]) -> str:
    if content_type:
        ext = mimetypes.guess_extension(content_type)
        if ext:
            return f"file{ext}"
        # fallback if extension can't be guessed
        return "file.bin"
    return "file.png"


def upload_file(
    client: Optional[AymaraAI] = None,
    http_client: Optional[httpx.Client] = None,
    file_name: Optional[str] = None,
    file_content: Union[Path, bytes, None] = None,
    content_type: Optional[str] = None,
) -> FileReference:
    """
    Helper to upload file content (from Path or bytes) and return (FileReference).
    Both client and http_client are optional and will be constructed if not provided.
    file_name is optional and will be defaulted based on content_type or to 'file.png'.
    content_type is optional and will be guessed from file_name if not provided.
    """
    if client is None:
        client = AymaraAI()
    close_http_client = False
    if http_client is None:
        http_client = httpx.Client()
        close_http_client = True

    try:
        # Determine file_name
        if file_name is None:
            file_name = _default_file_name(content_type)
        # Determine content_type
        mime_type = content_type or mimetypes.guess_type(file_name)[0] or "application/octet-stream"
        headers = {"Content-Type": mime_type}

        upload_resp = client.files.create(files=[{"local_file_path": file_name}])
        file_info = upload_resp.files[0]
        if not file_info.file_url:
            raise RuntimeError("No presigned file_url returned for upload.")

        if isinstance(file_content, Path):
            with open(str(file_content), "rb") as f:
                put_resp = http_client.put(file_info.file_url, content=f, headers=headers)
                put_resp.raise_for_status()
        elif isinstance(file_content, bytes):
            put_resp = http_client.put(file_info.file_url, content=file_content, headers=headers)
            put_resp.raise_for_status()
        else:
            raise ValueError("Unsupported file_content type for upload.")
        return FileReference(remote_file_path=file_info.remote_file_path)
    finally:
        if close_http_client:
            http_client.close()


async def upload_file_async(
    client: Optional[AsyncAymaraAI] = None,
    http_client: Optional[httpx.AsyncClient] = None,
    file_name: Optional[str] = None,
    file_content: Union[Path, bytes, None] = None,
    content_type: Optional[str] = None,
) -> FileReference:
    """
    Async helper to upload file content (from Path or bytes) and return (FileReference).
    Both client and http_client are optional and will be constructed if not provided.
    file_name is optional and will be defaulted based on content_type or to 'file.png'.
    content_type is optional and will be guessed from file_name if not provided.
    """
    if client is None:
        client = AsyncAymaraAI()
    close_http_client = False
    if http_client is None:
        http_client = httpx.AsyncClient()
        close_http_client = True

    try:
        # Determine file_name
        if file_name is None:
            file_name = _default_file_name(content_type)
        # Determine content_type
        mime_type = content_type or mimetypes.guess_type(file_name)[0] or "application/octet-stream"
        headers = {"Content-Type": mime_type}

        upload_resp = await client.files.create(files=[{"local_file_path": file_name}])
        file_info = upload_resp.files[0]
        if not file_info.file_url:
            raise RuntimeError("No presigned file_url returned for upload.")

        if isinstance(file_content, Path):
            async with aiofiles.open(str(file_content), mode="rb") as f:
                put_resp = await http_client.put(file_info.file_url, content=f, headers=headers)
                if put_resp.status_code != 200:
                    raise RuntimeError(f"Failed to upload file: {put_resp.status_code}")
        elif isinstance(file_content, bytes):
            put_resp = await http_client.put(file_info.file_url, content=file_content, headers=headers)
            if put_resp.status_code != 200:
                raise RuntimeError(f"Failed to upload file: {put_resp.status_code}")
        else:
            raise ValueError("Unsupported file_content type for upload.")
        return FileReference(remote_file_path=file_info.remote_file_path)
    finally:
        if close_http_client:
            await http_client.aclose()
