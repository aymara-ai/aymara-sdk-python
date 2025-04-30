import os
import time
import asyncio
from typing import Any, Union, TypeVar, Callable, Optional, Awaitable

from aymara_ai.types.shared.status import Status

T = TypeVar("T")


def _get_status(resource: Any, status_path: str) -> str:
    """
    Helper to extract status from a resource using a dot-path.
    """
    keys = status_path.split(".")
    for k in keys:
        resource = resource.get(k, {}) if isinstance(resource, dict) else getattr(resource, k, {})  # type: ignore
    return resource if isinstance(resource, str) else "failed"


def wait_until(
    operation: Callable[..., T],
    predicate: Callable[[Any], bool],
    interval: float = 1.0,
    timeout: int = 60,
    *args: Any,
    **kwargs: Any,
) -> T:
    """
    Synchronously calls `operation` with provided args/kwargs until `predicate` returns True for the result,
    or until timeout is reached.

    Args:
        operation: Callable to invoke.
        predicate: Callable that takes the operation result and returns True if done.
        interval: Polling interval in seconds.
        timeout: Maximum time to wait in seconds.
        *args: Positional arguments for operation.
        **kwargs: Keyword arguments for operation.

    Returns:
        The result from `operation` for which `predicate(result)` is True.

    Raises:
        TimeoutError: If timeout is reached before predicate is satisfied.
    """
    start_time = time.time()
    while True:
        result = operation(*args, **kwargs)
        if predicate(result):
            return result
        if (time.time() - start_time) >= timeout:
            raise TimeoutError(f"Timeout after {timeout} seconds waiting for predicate to be satisfied.")
        time.sleep(interval)


def wait_until_complete(
    get_fn: Callable[[str], T],
    resource_id: str,
    status_path: str = "status",
    success_status: Status = "finished",
    failure_status: Optional[Status] = "failed",
    timeout: int = 300,
    interval: int = 2,
    backoff: bool = False,
) -> T:
    """
    Generic polling helper for long-running resources (sync version).

    Args:
        get_fn: A function that takes resource_id and returns resource dict.
        resource_id: The ID of the resource to poll.
        status_path: Dot-path to status field (e.g. "status" or "metadata.status").
        success_status: Status value that indicates completion.
        failure_status: Status value that indicates failure (optional).
        timeout: Max time to wait, in seconds.
        interval: Poll interval in seconds.
        backoff: If True, exponentially increase interval (max 30s).

    Returns:
        The completed resource dict.

    Raises:
        TimeoutError or RuntimeError on failure.
    """

    def predicate(resource: Any) -> bool:
        status = _get_status(resource, status_path)
        if failure_status and status == failure_status:
            raise RuntimeError(f"Resource {resource_id} failed with status '{status}'")
        return status == success_status

    current_interval = interval

    def operation(resource_id: str) -> T:
        return get_fn(resource_id)

    if not backoff:
        return wait_until(
            operation,
            predicate,
            interval=interval,
            timeout=timeout,
            resource_id=resource_id,
        )
    else:
        # Handle backoff manually since wait_until does not support it natively
        start_time = time.time()
        while True:
            resource = get_fn(resource_id)
            try:
                if predicate(resource):
                    return resource
            except RuntimeError:
                raise
            if (time.time() - start_time) >= timeout:
                raise TimeoutError(f"Resource {resource_id} did not complete in time.")
            time.sleep(current_interval)
            current_interval = min(current_interval * 2, 30)


async def async_wait_until(
    operation: Callable[..., Awaitable[T]],
    predicate: Union[Callable[[Any], bool], Callable[[Any], Awaitable[bool]]],
    interval: Optional[float] = 1.0,
    timeout: Optional[int] = 30,
    *args: Any,
    **kwargs: Any,
) -> T:
    """
    Asynchronously calls `operation` with provided args/kwargs until `predicate` returns True for the result,
    or until timeout is reached.

    Args:
        operation: Async callable to invoke (e.g., await client.evals.get).
        predicate: Callable (sync or async) that takes the operation result and returns True if done.
        interval: Polling interval in seconds (default: from AYMR_WAIT_INTERVAL or 1.0).
        timeout: Maximum time to wait in seconds (default: from AYMR_WAIT_TIMEOUT or 60.0).
        *args: Positional arguments for operation.
        **kwargs: Keyword arguments for operation.

    Returns:
        The result from `operation` for which `predicate(result)` is True.

    Raises:
        TimeoutError: If timeout is reached before predicate is satisfied.
    """
    poll_interval = interval if interval is not None else float(os.getenv("AYMR_WAIT_INTERVAL", "1.0"))
    max_timeout = timeout if timeout is not None else float(os.getenv("AYMR_WAIT_TIMEOUT", "60.0"))

    start_time = asyncio.get_event_loop().time()
    while True:
        result = await operation(*args, **kwargs)
        pred_result = predicate(result)
        if asyncio.iscoroutine(pred_result):
            pred_result = await pred_result
        if pred_result:
            return result
        if (asyncio.get_event_loop().time() - start_time) >= max_timeout:
            raise TimeoutError(f"Timeout after {max_timeout} seconds waiting for predicate to be satisfied.")
        await asyncio.sleep(poll_interval)


async def async_wait_until_complete(
    get_fn: Callable[[str], Awaitable[T]],
    resource_id: str,
    status_path: str = "status",
    success_status: Status = "finished",
    failure_status: Optional[Status] = "failed",
    timeout: int = 300,
    interval: int = 2,
    backoff: bool = False,
) -> T:
    """
    Async polling helper for long-running resources.

    Args:
        get_fn: An async function that takes resource_id and returns resource dict.
        resource_id: The ID of the resource to poll.
        status_path: Dot-path to status field (e.g. "status" or "metadata.status").
        success_status: Status value that indicates completion.
        failure_status: Status value that indicates failure (optional).
        timeout: Max time to wait, in seconds.
        interval: Poll interval in seconds.
        backoff: If True, exponentially increase interval (max 30s).

    Returns:
        The completed resource dict.

    Raises:
        TimeoutError or RuntimeError on failure.
    """

    def predicate(resource: Any) -> bool:
        status = _get_status(resource, status_path)
        if failure_status and status == failure_status:
            raise RuntimeError(f"Resource {resource_id} failed with status '{status}'")
        return status == success_status

    current_interval = interval

    async def operation(resource_id: str) -> T:
        return await get_fn(resource_id)

    if not backoff:
        return await async_wait_until(
            operation,
            predicate,
            interval=interval,
            timeout=timeout,
            resource_id=resource_id,
        )
    else:
        # Handle backoff manually since async_wait_until does not support it natively
        start_time = asyncio.get_event_loop().time()
        while True:
            resource = await get_fn(resource_id)
            try:
                pred_result = predicate(resource)
                if pred_result:
                    return resource
            except RuntimeError:
                raise
            if (asyncio.get_event_loop().time() - start_time) >= timeout:
                raise TimeoutError(f"Resource {resource_id} did not complete in time.")
            await asyncio.sleep(current_interval)
            current_interval = min(current_interval * 2, 30)
