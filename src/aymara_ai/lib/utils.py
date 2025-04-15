import os
import time
import asyncio
from typing import Any, Union, Callable, Optional, Awaitable


class WaitTimeoutError(Exception):
    """Raised when wait_for_predicate times out before predicate is satisfied."""
    pass


def wait_until(
    operation: Callable[..., Any],
    predicate: Callable[[Any], bool],
    interval: Optional[float] = 1.0,
    timeout: Optional[int] = 30,
    *args: Any,
    **kwargs: Any
) -> Any:
    """
    Repeatedly calls `operation` with provided args/kwargs until `predicate` returns True for the result,
    or until timeout is reached.

    Args:
        operation: Callable to invoke (e.g., client.evals.retrieve).
        predicate: Callable that takes the operation result and returns True if done.
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

    start_time = time.monotonic()
    while True:
        result = operation(*args, **kwargs)
        if predicate(result):
            return result
        if (time.monotonic() - start_time) >= max_timeout:
            raise WaitTimeoutError(
                f"Timeout after {max_timeout} seconds waiting for predicate to be satisfied."
            )
        time.sleep(poll_interval)


async def async_wait_until(
    operation: Callable[..., Awaitable[Any]],
    predicate: Union[Callable[[Any], bool], Callable[[Any], Awaitable[bool]]],
    interval: Optional[float] = 1.0,
    timeout: Optional[int] = 30,
    *args: Any,
    **kwargs: Any
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
            raise WaitTimeoutError(
                f"Timeout after {max_timeout} seconds waiting for predicate to be satisfied."
            )
        await asyncio.sleep(poll_interval)