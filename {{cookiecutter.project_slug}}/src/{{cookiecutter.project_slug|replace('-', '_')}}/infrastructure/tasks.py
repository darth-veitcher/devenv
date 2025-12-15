{%- if cookiecutter.cache_backend in ['redis', 'falkordb'] -%}
"""Background task infrastructure using ARQ.

ARQ is an async Redis-based job queue built for Python.
Tasks are defined here and executed by a worker process.

Usage:
    # Enqueue a task from anywhere in the app
    from {{ cookiecutter.project_slug|replace('-', '_') }}.infrastructure.tasks import enqueue_task

    await enqueue_task("example_task", message="Hello!")

    # Run the worker (separate process)
    uv run arq {{ cookiecutter.project_slug|replace('-', '_') }}.infrastructure.tasks.WorkerSettings
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import timedelta
from typing import Any

from arq import create_pool
from arq.connections import ArqRedis, RedisSettings

from .config import get_settings

logger = logging.getLogger(__name__)

# Connection pool (initialized lazily)
_arq_pool: ArqRedis | None = None


def get_redis_settings() -> RedisSettings:
    """Get ARQ Redis settings from app configuration."""
    settings = get_settings()
    if settings.redis_url is None:
        raise ValueError("REDIS_URL is not configured")

    # Parse redis URL for ARQ RedisSettings
    # redis://host:port/db or redis://user:pass@host:port/db
    url = settings.redis_url
    if url.startswith("redis://"):
        url = url[8:]

    # Handle auth
    if "@" in url:
        auth, hostpart = url.rsplit("@", 1)
        password = auth.split(":")[-1] if ":" in auth else auth
    else:
        password = None
        hostpart = url

    # Handle host:port/db
    if "/" in hostpart:
        hostport, db = hostpart.rsplit("/", 1)
        database = int(db) if db else 0
    else:
        hostport = hostpart
        database = 0

    if ":" in hostport:
        host, port_str = hostport.rsplit(":", 1)
        port = int(port_str)
    else:
        host = hostport
        port = 6379

    return RedisSettings(
        host=host,
        port=port,
        database=database,
        password=password,
    )


async def get_task_pool() -> ArqRedis:
    """Get or create the ARQ connection pool."""
    global _arq_pool
    if _arq_pool is None:
        _arq_pool = await create_pool(get_redis_settings())
    return _arq_pool


async def close_task_pool() -> None:
    """Close the ARQ connection pool."""
    global _arq_pool
    if _arq_pool is not None:
        await _arq_pool.close()
        _arq_pool = None


async def enqueue_task(
    task_name: str,
    *args: Any,
    _defer_by: timedelta | None = None,
    _job_id: str | None = None,
    **kwargs: Any,
) -> str | None:
    """Enqueue a background task.

    Args:
        task_name: Name of the task function to execute
        *args: Positional arguments for the task
        _defer_by: Optional delay before task execution
        _job_id: Optional custom job ID (for deduplication)
        **kwargs: Keyword arguments for the task

    Returns:
        Job ID if successfully enqueued, None if deduplicated

    Example:
        job_id = await enqueue_task("example_task", message="Hello!")
        job_id = await enqueue_task("send_email", to="user@example.com", _defer_by=timedelta(minutes=5))
    """
    pool = await get_task_pool()
    job = await pool.enqueue_job(
        task_name,
        *args,
        _defer_by=_defer_by,
        _job_id=_job_id,
        **kwargs,
    )
    return job.job_id if job else None


# =============================================================================
# Task Definitions
# =============================================================================
# Define your background tasks below. Each task should be an async function.
# Tasks are automatically discovered by the WorkerSettings.functions list.


async def example_task(ctx: dict[str, Any], message: str) -> str:
    """Example background task.

    Args:
        ctx: ARQ context dict (contains redis connection, job info)
        message: A message to process

    Returns:
        Result string
    """
    logger.info(f"Processing example task with message: {message}")

    # Simulate some async work
    import asyncio

    await asyncio.sleep(1)

    result = f"Processed: {message}"
    logger.info(f"Task complete: {result}")
    return result


async def cleanup_expired_sessions(ctx: dict[str, Any]) -> int:
    """Periodic task to clean up expired sessions.

    This is an example of a cron-scheduled task.

    Returns:
        Number of sessions cleaned up
    """
    logger.info("Running session cleanup task")

    # In a real implementation, you'd scan Redis for expired sessions
    # This is a placeholder showing the pattern
    cleaned = 0

    logger.info(f"Cleaned up {cleaned} expired sessions")
    return cleaned


# =============================================================================
# Worker Settings
# =============================================================================


@dataclass
class WorkerSettings:
    """ARQ worker settings.

    Run the worker with:
        uv run arq {{ cookiecutter.project_slug|replace('-', '_') }}.infrastructure.tasks.WorkerSettings
    """

    # Task functions to register
    functions = [
        example_task,
        cleanup_expired_sessions,
    ]

    # Redis connection
    redis_settings = get_redis_settings()

    # Cron jobs (scheduled tasks)
    # Uncomment to enable periodic session cleanup
    # cron_jobs = [
    #     cron(cleanup_expired_sessions, hour=3, minute=0),  # Run at 3 AM daily
    # ]

    # Worker configuration
    max_jobs = 10  # Max concurrent jobs
    job_timeout = 300  # 5 minute timeout per job
    keep_result = 3600  # Keep results for 1 hour
    poll_delay = 0.5  # Polling interval in seconds

    # Retry configuration
    max_tries = 3
    retry_delay = timedelta(seconds=10)

    # Logging
    @staticmethod
    async def on_startup(ctx: dict[str, Any]) -> None:
        """Called when worker starts."""
        logger.info("ARQ worker starting up")

    @staticmethod
    async def on_shutdown(ctx: dict[str, Any]) -> None:
        """Called when worker shuts down."""
        logger.info("ARQ worker shutting down")

    @staticmethod
    async def on_job_start(ctx: dict[str, Any]) -> None:
        """Called before each job starts."""
        logger.debug(f"Starting job: {ctx.get('job_id')}")

    @staticmethod
    async def on_job_end(ctx: dict[str, Any]) -> None:
        """Called after each job completes."""
        logger.debug(f"Completed job: {ctx.get('job_id')}")
{%- else -%}
"""Background tasks infrastructure - Not enabled.

This project was generated without a cache backend.
ARQ requires Redis for its job queue.
To enable background tasks, regenerate with cache_backend='redis' or 'falkordb'.
"""
{%- endif %}
