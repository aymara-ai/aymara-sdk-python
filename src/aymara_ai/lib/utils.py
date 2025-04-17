import os
import time
import asyncio
from typing import Any, Union, TypeVar, Callable, Optional, Awaitable

T = TypeVar("T")


def wait_until_complete(
    get_fn: Callable[[str], T],
    resource_id: str,
    status_path: str = "status",
    success_status: str = "finished",
    failure_status: Optional[str] = "failed",
    timeout: int = 300,
    interval: int = 2,
    backoff: bool = False,
) -> T:
    """
    Generic polling helper for long-running resources.

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

    def get_status(resource: Any) -> str:
        keys = status_path.split(".")
        for k in keys:
            resource = resource.get(k, {}) if isinstance(resource, dict) else getattr(resource, k, {})  # type: ignore
        return resource if isinstance(resource, str) else ""

    start_time = time.time()
    current_interval = interval

    while time.time() - start_time < timeout:
        resource = get_fn(resource_id)
        status = get_status(resource)
        if status == success_status:
            return resource
        if failure_status and status == failure_status:
            raise RuntimeError(f"Resource {resource_id} failed with status '{status}'")

        time.sleep(current_interval)
        if backoff:
            current_interval = min(current_interval * 2, 30)

    raise TimeoutError(f"Resource {resource_id} did not complete in time.")


async def async_wait_until(
    operation: Callable[..., Awaitable[Any]],
    predicate: Union[Callable[[Any], bool], Callable[[Any], Awaitable[bool]]],
    interval: Optional[float] = 1.0,
    timeout: Optional[int] = 30,
    *args: Any,
    **kwargs: Any,
) -> Any:
    """
    Asynchronously calls `operation` with provided args/kwargs until `predicate` returns True for the result,
    or until timeout is reached.

    Args:
        operation: Async callable to invoke (e.g., await client.evals.retrieve).
        predicate: Callable (sync or async) that takes the operation result and returns True if done.
        interval: Polling interval in seconds (default: from AYMR_WAIT_INTERVAL or 1.0).
        timeout: Maximum time to wait in seconds (default: from AYMR_WAIT_TIMEOUT or 60.0).
        *args: Positional arguments for operation.
        **kwargs: Keyword arguments for operation.

    Returns:
        The result from `operation` for which `predicate(result)` is True.

    Raises:
        WaitTimeoutError: If timeout is reached before predicate is satisfied.
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
