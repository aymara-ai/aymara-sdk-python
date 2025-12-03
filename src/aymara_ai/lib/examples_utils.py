from __future__ import annotations

# pyright: reportMissingTypeStubs=false, reportUnknownMemberType=false, reportUnknownVariableType=false, reportUnknownParameterType=false, reportUnknownArgumentType=false
import os
import json
import uuid
import base64
import random
import shutil
import asyncio
import logging
import tempfile
from typing import Any, Dict, List, Callable, Optional, Awaitable, cast
from pathlib import Path
from datetime import datetime, timezone

import boto3  # type: ignore[import-untyped]
import requests
from botocore.exceptions import ClientError  # type: ignore[import-untyped]

from aymara_ai.types.eval_prompt import EvalPrompt
from aymara_ai.types.eval_response_param import EvalResponseParam
from aymara_ai.types.shared_params.file_reference import FileReference

logger = logging.getLogger(__name__)

CacheMetadata = Dict[str, Dict[str, str]]

_DEFAULT_CACHE_DIR = Path("./video_cache")

# Module-level paths that other notebooks can reference directly.
video_cache_dir = Path(os.environ.get("AYMARA_VIDEO_CACHE_DIR", _DEFAULT_CACHE_DIR)).expanduser()
video_cache_videos_dir = video_cache_dir / "videos"
video_cache_metadata_file = video_cache_dir / "metadata.json"
VIDEO_CACHE_DIR = video_cache_dir
VIDEO_CACHE_VIDEOS_DIR = video_cache_videos_dir
VIDEO_CACHE_METADATA_FILE = video_cache_metadata_file


def configure_examples_logging(
    *,
    level: int = logging.INFO,
    formatter: Optional[logging.Formatter] = None,
    stream: Optional[Any] = None,
) -> logging.Logger:
    """Ensure the module logger is ready for notebook use."""
    logger.setLevel(level)
    logger.propagate = False

    if not logger.handlers:
        handler = logging.StreamHandler(stream)
        handler.setFormatter(formatter or logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
        logger.addHandler(handler)

    return logger


def configure_video_cache(path: str | Path | None = None) -> Path:
    """Override the cache directory location and return the resolved path."""
    global video_cache_dir, video_cache_videos_dir, video_cache_metadata_file

    base_dir = Path(
        path if path is not None else os.environ.get("AYMARA_VIDEO_CACHE_DIR", _DEFAULT_CACHE_DIR)
    ).expanduser()

    video_cache_dir = base_dir
    video_cache_videos_dir = base_dir / "videos"
    video_cache_metadata_file = base_dir / "metadata.json"
    globals()["VIDEO_CACHE_DIR"] = video_cache_dir
    globals()["VIDEO_CACHE_VIDEOS_DIR"] = video_cache_videos_dir
    globals()["VIDEO_CACHE_METADATA_FILE"] = video_cache_metadata_file
    return video_cache_dir


def ensure_cache_dir(*, verbose: bool = True) -> Path:
    """Create the cache directory structure if it does not exist."""
    video_cache_videos_dir.mkdir(parents=True, exist_ok=True)
    if not video_cache_metadata_file.exists():
        save_cache_metadata({})
    if verbose:
        logger.info(f"✅ Cache directory ready: {video_cache_dir}")
    return video_cache_dir


def setup_video_cache(path: str | Path | None = None, *, verbose: bool = True) -> Path:
    """Configure and initialize the cache directory, returning the resolved path."""
    configure_video_cache(path)
    return ensure_cache_dir(verbose=verbose)


def load_cache_metadata() -> CacheMetadata:
    """Load cache metadata from JSON file."""
    if not video_cache_metadata_file.exists():
        return {}
    with video_cache_metadata_file.open("r", encoding="utf-8") as metadata_file:
        return cast(CacheMetadata, json.load(metadata_file))


def save_cache_metadata(metadata: CacheMetadata) -> None:
    """Persist cache metadata to disk."""
    with video_cache_metadata_file.open("w", encoding="utf-8") as metadata_file:
        json.dump(metadata, metadata_file, indent=2)


def add_to_cache(local_path: Path, *, provider: str, prompt: str, s3_uri: str, verbose: bool = True) -> Path:
    """Copy a generated video into the cache and update metadata."""
    ensure_cache_dir(verbose=False)

    cache_filename = f"{uuid.uuid4()}.mp4"
    cache_path = video_cache_videos_dir / cache_filename

    shutil.copy2(local_path, cache_path)

    metadata = load_cache_metadata()
    metadata[cache_filename] = {
        "provider": provider,
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "original_prompt": prompt,
        "s3_uri": s3_uri,
    }
    save_cache_metadata(metadata)

    if verbose:
        logger.info(f"✅ Added to cache: {cache_filename} (provider: {provider})")
    return cache_path


def list_cached_videos(extension: str = ".mp4") -> List[Path]:
    """Return all cached video files that match the expected extension."""
    if not video_cache_videos_dir.exists():
        return []
    return sorted(video_cache_videos_dir.glob(f"*{extension}"))


def generate_presigned_url_from_s3_uri(s3_uri: str, expiration: int = 3600) -> str:
    """Convert an S3 URI (s3://bucket/key) into a pre-signed HTTP URL."""
    if not s3_uri.startswith("s3://"):
        raise ValueError(f"Invalid S3 URI format: {s3_uri}")

    try:
        bucket_name, key = s3_uri[5:].split("/", 1)
    except ValueError as exc:
        raise ValueError(f"Invalid S3 URI: missing object key in {s3_uri}") from exc

    s3_client: Any = boto3.client("s3", region_name=os.getenv("AWS_REGION", "us-east-1"))
    return cast(
        str,
        s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket_name, "Key": key},
            ExpiresIn=expiration,
        ),
    )


def validate_s3_bucket_configuration(
    s3_client: Any,
    bucket_name: str,
    *,
    default_bucket: Optional[str] = None,
) -> str:
    """Validate that the configured S3 bucket exists and is accessible."""
    if default_bucket and bucket_name == default_bucket:
        logger.info("⚠️  Warning: Using default S3 bucket name. Consider setting S3_BUCKET_NAME.")

    logger.info("Validating S3 bucket configuration...")

    if bucket_name == "your-bucket-name":
        raise ValueError(
            "S3_BUCKET_NAME is not configured. Please set the S3_BUCKET_NAME "
            "environment variable or update the default value in the configuration cell."
        )

    try:
        s3_client.head_bucket(Bucket=bucket_name)
        logger.info(f"✅ S3 bucket '{bucket_name}' is accessible")

        location = cast(Dict[str, Any], s3_client.get_bucket_location(Bucket=bucket_name))
        region = str(location.get("LocationConstraint") or "us-east-1")
        logger.info(f"✅ Bucket region: {region}")
    except ClientError as err:
        error_code = str(err.response["Error"]["Code"])
        if error_code == "404":
            raise ValueError(
                f"S3 bucket '{bucket_name}' does not exist. Please create the bucket or update S3_BUCKET_NAME."
            ) from err
        if error_code == "403":
            raise ValueError(
                f"Access denied to S3 bucket '{bucket_name}'. "
                "Please check your AWS credentials and bucket permissions."
            ) from err
        raise ValueError(f"Error accessing S3 bucket: {err}") from err

    logger.info("✅ S3 configuration validated successfully\n")
    return region


async def generate_video_async_bedrock(
    prompt: str,
    prompt_uuid: str,
    *,
    bedrock_client: Any,
    s3_client: Any,
    bucket_name: str,
    model_id: str,
) -> Optional[str]:
    """Generate a Nova Reel video and return the S3 URI. Returns None on moderation/failure."""
    job_id = str(uuid.uuid4())[:8]
    output_s3_uri = f"s3://{bucket_name}/"

    try:
        logger.info(f"[{job_id}] Submitting video generation for: '{prompt[:50]}...' , uuid: {prompt_uuid}")
        logger.info(f"[{job_id}] Output S3 URI: {output_s3_uri}")

        model_input = {
            "taskType": "TEXT_VIDEO",
            "textToVideoParams": {"text": prompt},
            "videoGenerationConfig": {
                "fps": 24,
                "durationSeconds": 6,
                "dimension": "1280x720",
            },
        }
        output_config = {"s3OutputDataConfig": {"s3Uri": output_s3_uri}}

        response = bedrock_client.start_async_invoke(
            modelId=model_id,
            modelInput=model_input,
            outputDataConfig=output_config,
        )
        response_dict: Dict[str, Any] = cast(Dict[str, Any], response)
        invocation_arn = str(response_dict["invocationArn"])
        logger.info(f"[{job_id}] Job started with ARN: {invocation_arn}")
    except ClientError as err:
        if (
            err.response["Error"]["Code"] == "ValidationException"
            and "blocked by our content filters" in err.response["Error"]["Message"]
        ):
            logger.info(f"[{job_id}] Input moderated by Bedrock")
            return None
        logger.info(f"[{job_id}] Error starting job: {err}")
        return None
    except Exception as exc:
        logger.info(f"[{job_id}] Unexpected error: {exc}")
        return None

    try:
        status = "InProgress"
        job_details: Dict[str, Any] = {}
        while status == "InProgress":
            await asyncio.sleep(10)
            job_details = cast(Dict[str, Any], bedrock_client.get_async_invoke(invocationArn=invocation_arn))
            status = str(job_details["status"])
            logger.info(f"[{job_id}] Status: {status}")

        if status == "Completed":
            output_config_data = cast(Dict[str, Any], job_details.get("outputDataConfig", {}))
            s3_output_data = cast(Dict[str, Any], output_config_data.get("s3OutputDataConfig", {}))
            source_uri = f"{s3_output_data['s3Uri']}/output.mp4"
            logger.info(f"[{job_id}] ✅ Video generated at: {source_uri}")

            try:
                s3_path = source_uri[5:]
                cache_bucket, cache_key = s3_path.split("/", 1)

                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_file:
                    tmp_path = Path(tmp_file.name)
                    s3_client.download_file(cache_bucket, cache_key, str(tmp_path))
                    logger.info(f"[{job_id}] Downloaded to temp: {tmp_path}")

                add_to_cache(tmp_path, provider="nova", prompt=prompt, s3_uri=source_uri)

                try:
                    tmp_path.unlink()
                except FileNotFoundError:
                    pass
            except Exception as cache_error:
                logger.info(f"[{job_id}] ⚠️  Cache error (continuing): {cache_error}")

            return source_uri

        if status == "Failed":
            failure_message = str(job_details.get("failureMessage", ""))
            if "violate the safety policy" in failure_message:
                logger.info(f"[{job_id}] Output moderated by Bedrock")
            else:
                logger.info(f"[{job_id}] Job failed: {failure_message}")
            return None

        logger.info(f"[{job_id}] Unexpected status: {status}")
        return None

    except Exception as exc:
        logger.info(f"[{job_id}] Error during polling: {exc}")
        return None


async def generate_video_async_sora(
    prompt: str,
    prompt_uuid: str,
    *,
    openai_client: Any,
    s3_client: Any,
    bucket_name: str,
    sora_output_folder: str,
    video_duration: int,
    model_id: str,
) -> Optional[str]:
    """Generate a Sora video, upload to S3, and return the S3 URI."""
    job_id = str(uuid.uuid4())[:8]
    local_filename = f"{prompt_uuid}.mp4"

    logger.info(f"[{job_id}] Starting Sora generation for: '{prompt[:50]}...'")

    try:
        logger.info(f"[{job_id}] Submitting job to OpenAI Sora...")
        job = openai_client.videos.create(
            model=model_id,
            prompt=prompt,
            seconds=str(video_duration),
        )
        job_id_openai = job.id
        logger.info(f"[{job_id}] Job created with ID: {job_id_openai}")
    except Exception as exc:
        logger.info(f"[{job_id}] Error creating job: {exc}")
        error_msg = str(exc).lower()
        if "moderation" in error_msg or "content policy" in error_msg or "safety" in error_msg:
            logger.info(f"[{job_id}] Input moderated by OpenAI")
        return None

    try:
        status = job.status
        while status not in ("completed", "failed", "cancelled", "canceled"):
            await asyncio.sleep(10)
            job = openai_client.videos.retrieve(job_id_openai)
            status = job.status
            logger.info(f"[{job_id}] Status: {status}")

        if status == "completed":
            logger.info(f"[{job_id}] ✅ Video generation succeeded")
            video_content = openai_client.videos.download_content(job_id_openai, variant="video")
            video_content.write_to_file(local_filename)
            logger.info(f"[{job_id}] Downloaded video to {local_filename}")

            try:
                s3_key = f"{sora_output_folder}{local_filename}"
                logger.info(f"[{job_id}] Uploading to S3: s3://{bucket_name}/{s3_key}")
                s3_client.upload_file(local_filename, bucket_name, s3_key)
                s3_uri = f"s3://{bucket_name}/{s3_key}"
                logger.info(f"[{job_id}] ✅ Uploaded to S3: {s3_uri}")

                try:
                    local_path = Path(local_filename)
                    add_to_cache(local_path, provider="sora", prompt=prompt, s3_uri=s3_uri)
                except Exception as cache_error:
                    logger.info(f"[{job_id}] ⚠️  Cache error (continuing): {cache_error}")

                os.remove(local_filename)
                logger.info(f"[{job_id}] ✅ Cleaned up local temp file")
                return s3_uri

            except Exception as s3_error:
                logger.info(f"[{job_id}] ❌ S3 upload failed: {s3_error}")
                if os.path.exists(local_filename):
                    os.remove(local_filename)
                return None

        elif status in ("failed", "cancelled", "canceled"):
            failure_reason = getattr(job, "error", None)
            if failure_reason:
                error_code = getattr(failure_reason, "code", "")
                error_message = getattr(failure_reason, "message", "")
                if "moderation" in error_code.lower() or "moderation" in error_message.lower():
                    logger.info(f"[{job_id}] Output moderated by OpenAI")
                else:
                    logger.info(f"[{job_id}] Job failed: {error_code} - {error_message}")
            else:
                logger.info(f"[{job_id}] Job ended with status: {status}")
            return None

        else:
            logger.info(f"[{job_id}] Unexpected status: {status}")
            return None

    except Exception as exc:
        logger.info(f"[{job_id}] Error during polling/download: {exc}")
        if os.path.exists(local_filename):
            os.remove(local_filename)
        return None


async def upload_cached_video_async(
    prompt_uuid: str,
    *,
    client: Any,
) -> Optional[str]:
    """Upload a cached video through the SDK and return the new file UUID."""
    cache_videos = list_cached_videos()
    if not cache_videos:
        raise ValueError(
            f"Video cache is empty! No videos found in {VIDEO_CACHE_VIDEOS_DIR}. "
            "Generate videos with provider='nova' or provider='sora' first."
        )

    job_id = prompt_uuid[:8] or str(uuid.uuid4())[:8]
    selected_video = random.choice(cache_videos)
    logger.info(f"[{job_id}] Selected cached video: {selected_video.name}")

    metadata = load_cache_metadata()
    video_metadata = metadata.get(selected_video.name, {})
    if video_metadata:
        logger.info(f"[{job_id}] Original provider: {video_metadata.get('provider', 'unknown')}")
        prompt_preview = video_metadata.get("original_prompt", "unknown")[:50]
        logger.info(f"[{job_id}] Original prompt: {prompt_preview}...")

    try:
        logger.info(f"[{job_id}] Requesting upload URL from Aymara SDK...")
        upload_resp = client.files.create(
            files=[
                {
                    "local_file_path": selected_video.name,
                    "content_type": "video/mp4",
                }
            ]
        )

        file_info = upload_resp.files[0]
        file_uuid = str(file_info.file_uuid)
        file_url = file_info.file_url

        logger.info(f"[{job_id}] Got file_uuid: {file_uuid}")
        logger.info(f"[{job_id}] Got upload URL: {file_url[:60]}...")

        logger.info(f"[{job_id}] Uploading cached video to signed URL...")
        with open(selected_video, "rb") as cached_file:
            response = requests.put(
                file_url,
                data=cached_file,
                headers={"Content-Type": "video/mp4"},
            )
            response.raise_for_status()

        logger.info(f"[{job_id}] ✅ Upload successful! file_uuid: {file_uuid}")
        return file_uuid

    except Exception as exc:
        logger.info(f"[{job_id}] ❌ Upload failed: {exc}")
        return None


async def answer_prompts(
    prompts: List[EvalPrompt],
    *,
    client: Any,
    provider: str = "nova",
    provider_handlers: Optional[Dict[str, Callable[..., Awaitable[Optional[str]]]]] = None,
    generate_video_async_bedrock: Optional[Callable[[str, str], Awaitable[Optional[str]]]] = None,
    generate_video_async_sora: Optional[Callable[[str, str], Awaitable[Optional[str]]]] = None,
    upload_cached_video_async: Optional[Callable[[str], Awaitable[Optional[str]]]] = None,
) -> List[EvalResponseParam]:
    """Generate/upload videos for prompts and build response payloads."""
    handler_map: Dict[str, Callable[..., Awaitable[Optional[str]]]] = {}
    if provider_handlers:
        handler_map.update(provider_handlers)

    if generate_video_async_bedrock is not None:
        handler_map["nova"] = generate_video_async_bedrock
    if generate_video_async_sora is not None:
        handler_map["sora"] = generate_video_async_sora
    if upload_cached_video_async is not None:
        handler_map["local"] = upload_cached_video_async

    provider_key = provider.lower()
    if provider_key not in {"nova", "sora", "local"}:
        raise ValueError(f"Unknown provider: {provider}. Must be 'nova', 'sora', or 'local'")

    video_gen_func = handler_map.get(provider_key)
    if video_gen_func is None:
        raise ValueError(
            f"No handler configured for provider '{provider}'. "
            "Supply one via provider_handlers or the specific function arguments."
        )

    use_concurrency_limit = provider_key != "local"

    if use_concurrency_limit:
        semaphore = asyncio.Semaphore(3)

        async def generate_with_limit(prompt_content: str, prompt_uuid: str) -> Optional[str]:
            async with semaphore:
                return await video_gen_func(prompt_content, prompt_uuid)

        logger.info(f"Starting video generation for {len(prompts)} prompts using {provider} (max 3 concurrent)...")
        tasks: List[Awaitable[Optional[str]]] = [
            generate_with_limit(prompt.content, prompt.prompt_uuid)
            for prompt in prompts
        ]
    else:
        logger.info(f"Uploading {len(prompts)} cached videos using {provider}...")
        tasks = [video_gen_func(prompt.prompt_uuid) for prompt in prompts]

    results = await asyncio.gather(*tasks, return_exceptions=True)
    logger.info("All video tasks completed!")
    responses: List[EvalResponseParam] = []

    for prompt, result in zip(prompts, results):
        try:
            if isinstance(result, Exception):
                logger.info(f"Video processing failed for {prompt.prompt_uuid}: {result}")
                responses.append(
                    EvalResponseParam(
                        prompt_uuid=prompt.prompt_uuid,
                        content_type="video",
                        ai_refused=True,
                    )
                )
                continue

            if provider_key == "local":
                file_uuid = cast(Optional[str], result)
                if file_uuid is None:
                    responses.append(
                        EvalResponseParam(
                            prompt_uuid=prompt.prompt_uuid,
                            content_type="video",
                            ai_refused=True,
                        )
                    )
                    continue

                responses.append(
                    EvalResponseParam(
                        content=FileReference(file_uuid=file_uuid),
                        prompt_uuid=prompt.prompt_uuid,
                        content_type="video",
                    )
                )
                continue

            s3_uri = cast(Optional[str], result)
            if s3_uri is None:
                responses.append(
                    EvalResponseParam(
                        prompt_uuid=prompt.prompt_uuid,
                        content_type="video",
                        ai_refused=True,
                    )
                )
                continue

            presigned_url = generate_presigned_url_from_s3_uri(s3_uri)
            upload_resp = client.files.create(
                files=[
                    {
                        "remote_uri": presigned_url,
                        "content_type": "video/mp4",
                    }
                ]
            )

            responses.append(
                EvalResponseParam(
                    content=FileReference(file_uuid=upload_resp.files[0].file_uuid),
                    prompt_uuid=prompt.prompt_uuid,
                    content_type="video",
                )
            )

        except Exception as exc:
            logger.info(f"Error processing prompt {prompt.prompt_uuid}: {exc}")
            responses.append(
                EvalResponseParam(
                    prompt_uuid=prompt.prompt_uuid,
                    content_type="video",
                    ai_refused=True,
                )
            )

    return responses


def display_eval_run_results(
    client: Any,
    eval_run_uuid: str,
    *,
    prompts: Optional[List[EvalPrompt]] = None,
    fallback_s3_bucket: Optional[str] = None,
) -> None:
    """Pretty-print scored responses for an evaluation run and embed videos when available."""
    ipy_html: Optional[Callable[[str], Any]] = None
    ipy_video: Optional[Callable[..., Any]] = None
    display_fn: Optional[Callable[..., Any]] = None
    try:
        from IPython.display import HTML as html_cls, Video as video_cls, display as display_func
    except ImportError:
        pass
    else:
        ipy_html = cast(Callable[[str], Any], html_cls)
        ipy_video = cast(Callable[..., Any], video_cls)
        display_fn = cast(Callable[..., Any], display_func)

    eval_run = client.evals.runs.get(eval_run_uuid=eval_run_uuid)
    eval_obj = client.evals.get(eval_uuid=eval_run.eval_uuid)

    if fallback_s3_bucket is None:
        fallback_s3_bucket = os.getenv("S3_BUCKET_NAME")

    if prompts is None:
        prompts = list(client.evals.list_prompts(eval_run.eval_uuid).items)

    prompts_dict = {prompt.prompt_uuid: prompt for prompt in prompts}
    scored_responses: List[Any] = list(client.evals.runs.list_responses(eval_run_uuid=eval_run_uuid).items)

    logger.info(f"\n{'=' * 80}")
    logger.info(f"Evaluation: {eval_obj.name}")
    logger.info(f"Pass Rate: {eval_run.pass_rate:.1%}")
    logger.info(f"Scored: {eval_run.num_responses_scored}/{eval_run.num_prompts}")
    logger.info(f"{'=' * 80}\n")

    for index, response in enumerate(scored_responses, start=1):
        response_obj: Any = response
        prompt = prompts_dict.get(response_obj.prompt_uuid)
        if not prompt:
            continue

        logger.info(f"\n--- Video {index}/{len(scored_responses)} ---")
        logger.info(f"Prompt: {prompt.content}")
        logger.info(f"Result: {'✅ PASSED' if response_obj.is_passed else '❌ FAILED'}")

        if getattr(response_obj, "content", None) and getattr(response_obj.content, "file_uuid", None):
            video_url: Optional[str] = None
            remote_path: Optional[str] = getattr(response_obj.content, "remote_file_path", None)

            try:
                file_resource = getattr(client, "files", None)
                get_method = getattr(file_resource, "get", None) if file_resource else None
                if callable(get_method):
                    file_info = get_method(response_obj.content.file_uuid)  # type: ignore[misc]
                    video_url = getattr(file_info, "file_url", None)
                    remote_path = getattr(file_info, "remote_file_path", remote_path)
                    if not remote_path:
                        remote_path = getattr(file_info, "original_file_url", remote_path)
                    if not remote_path:
                        remote_path = getattr(file_info, "file_url", remote_path)

                if not video_url and file_resource is not None:
                    status_method = getattr(file_resource, "get_status", None)
                    if callable(status_method):
                        status_info = status_method(response_obj.content.file_uuid)  # type: ignore[misc]
                        remote_path = getattr(status_info, "remote_file_path", remote_path)
            except Exception as exc:
                logger.info(f"Could not fetch video metadata: {exc}")

            if not video_url and remote_path is not None:
                if remote_path.startswith(("http://", "https://")):
                    video_url = remote_path
                else:
                    candidate_uri: Optional[str] = None
                    if remote_path.startswith("s3://"):
                        candidate_uri = remote_path
                    elif fallback_s3_bucket:
                        candidate_uri = f"s3://{fallback_s3_bucket.rstrip('/')}/{remote_path.lstrip('/')}"

                    if candidate_uri:
                        try:
                            video_url = generate_presigned_url_from_s3_uri(candidate_uri)
                        except Exception as exc:
                            logger.info(f"Could not generate presigned URL: {exc}")

            if video_url and ipy_html is not None and ipy_video is not None and display_fn is not None:
                rendered = False
                embed_url = f"{video_url}#t=0.001" if "#" not in video_url else video_url

                data_url: Optional[str] = None
                if video_url:
                    try:
                        resp = requests.get(video_url, timeout=60)
                        resp.raise_for_status()
                        data_url = "data:video/mp4;base64," + base64.b64encode(resp.content).decode("ascii")
                    except Exception as exc:
                        logger.info(f"Could not inline video data: {exc}")

                if ipy_video is not None:
                    try:
                        source = data_url or embed_url
                        display_fn(ipy_video(source, width=640, height=360))
                        rendered = True
                    except Exception:
                        rendered = False

                if not rendered:
                    source = data_url or embed_url
                    html = f"""
                    <div style="margin: 20px 0; padding: 10px; border: 1px solid #ddd; border-radius: 5px;">
                        <video width="640" controls>
                            <source src="{source}" type="video/mp4">
                            Your browser does not support the video tag.
                        </video>
                        <p><a href="{video_url}" target="_blank" rel="noopener">Open video in new tab</a></p>
                        <p><strong>Passed:</strong> {response_obj.is_passed}</p>
                        <p><strong>Explanation:</strong> {getattr(response_obj, 'explanation', None) or 'N/A'}</p>
                    </div>
                    """
                    display_fn(ipy_html(html))

            else:
                if remote_path:
                    logger.info(f"Video content not available (remote path: {remote_path})")
                else:
                    logger.info("Video content not available")
        elif getattr(response_obj, "ai_refused", False):
            logger.info("AI refused to generate content.")
