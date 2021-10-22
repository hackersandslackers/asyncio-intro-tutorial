"""Interact with a running event loop."""
import asyncio

from logger import LOGGER


def inspect_event_loop():
    """Inspect current running event loop."""
    loop = asyncio.get_event_loop()
    thread_id = loop.__dict__.get("_thread_id")
    if loop.is_running():
        LOGGER.info(
            f"Loop has been running {loop.time()} seconds. (Thread ID #{thread_id})"
        )
