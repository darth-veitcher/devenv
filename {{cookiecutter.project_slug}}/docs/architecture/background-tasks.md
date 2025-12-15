{%- if cookiecutter.cache_backend in ['redis', 'falkordb'] -%}
# Background Tasks

This project uses [ARQ](https://arq-docs.helpmanual.io/) for async background task processing with Redis as the job queue backend.

## Overview

Background tasks enable you to:

- Offload long-running operations from request handlers
- Schedule periodic/cron jobs
- Retry failed operations automatically
- Distribute work across multiple workers

## Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│    FastAPI      │     │     Redis       │     │   ARQ Worker    │
│   (enqueue)     │────▶│   (job queue)   │────▶│   (execute)     │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

1. **Producer**: Your API or CLI enqueues tasks via `enqueue_task()`
2. **Queue**: Redis stores the job queue with persistence
3. **Consumer**: ARQ workers poll for jobs and execute them

## Quick Start

### Running the Worker

```bash
# Start the worker
just worker

# Or with verbose logging
just worker-verbose

# Or directly
uv run arq {{ cookiecutter.project_slug|replace('-', '_') }}.infrastructure.tasks.WorkerSettings
```

### Enqueuing Tasks

```python
from {{ cookiecutter.project_slug|replace('-', '_') }}.infrastructure.tasks import enqueue_task

# Simple task
job_id = await enqueue_task("example_task", message="Hello!")

# Delayed task (run in 5 minutes)
from datetime import timedelta
job_id = await enqueue_task(
    "example_task",
    message="Delayed hello!",
    _defer_by=timedelta(minutes=5)
)

# Task with custom job ID (for deduplication)
job_id = await enqueue_task(
    "send_email",
    to="user@example.com",
    _job_id="email-user-123"
)
```

## Creating Tasks

Tasks are async functions defined in `infrastructure/tasks.py`:

```python
async def my_task(ctx: dict[str, Any], param1: str, param2: int) -> str:
    """My background task.

    Args:
        ctx: ARQ context (contains redis connection, job info)
        param1: First parameter
        param2: Second parameter

    Returns:
        Result string
    """
    # Your async task logic here
    result = await some_async_operation(param1, param2)
    return f"Completed: {result}"
```

Then register it in `WorkerSettings.functions`:

```python
@dataclass
class WorkerSettings:
    functions = [
        example_task,
        cleanup_expired_sessions,
        my_task,  # Add your task here
    ]
```

## Task Context

The `ctx` parameter provides:

- `ctx['redis']`: Redis connection for direct access
- `ctx['job_id']`: Current job ID
- `ctx['job_try']`: Retry attempt number (starts at 1)

## Scheduling Cron Jobs

For periodic tasks, use ARQ's cron scheduling:

```python
from arq import cron

@dataclass
class WorkerSettings:
    functions = [example_task, cleanup_expired_sessions]

    cron_jobs = [
        # Run cleanup at 3 AM daily
        cron(cleanup_expired_sessions, hour=3, minute=0),

        # Run every 30 minutes
        cron(some_periodic_task, minute={0, 30}),

        # Run every weekday at 9 AM
        cron(weekday_task, weekday={0, 1, 2, 3, 4}, hour=9),
    ]
```

## Retry Configuration

ARQ automatically retries failed tasks:

```python
@dataclass
class WorkerSettings:
    max_tries = 3  # Retry up to 3 times
    retry_delay = timedelta(seconds=10)  # Wait 10s between retries
```

For per-task retry control:

```python
from arq import Retry

async def flaky_task(ctx: dict[str, Any]) -> str:
    try:
        result = await unreliable_service()
        return result
    except ServiceUnavailable:
        # Retry after 60 seconds
        raise Retry(defer=60)
```

## Docker Compose

The worker runs as a separate container:

```yaml
services:
  worker:
    build: .
    command: uv run arq {{ cookiecutter.project_slug|replace('-', '_') }}.infrastructure.tasks.WorkerSettings
    depends_on:
      cache:
        condition: service_healthy
    environment:
      REDIS_URL: redis://cache:6379/0
```

Scale workers for higher throughput:

```bash
docker compose up -d --scale worker=3
```

## Monitoring

### Check Worker Status

```bash
just worker-check
```

### View Job Results

```python
from {{ cookiecutter.project_slug|replace('-', '_') }}.infrastructure.tasks import get_task_pool

async def check_job(job_id: str):
    pool = await get_task_pool()
    job = await pool.job(job_id)
    if job:
        info = await job.info()
        print(f"Status: {info.status}")
        print(f"Result: {info.result}")
```

## Best Practices

### 1. Keep Tasks Idempotent

Tasks may be retried, so ensure they can safely run multiple times:

```python
async def process_order(ctx: dict[str, Any], order_id: str) -> str:
    # Check if already processed (idempotent)
    if await is_order_processed(order_id):
        return "Already processed"

    await do_processing(order_id)
    await mark_order_processed(order_id)
    return "Processed"
```

### 2. Use Job IDs for Deduplication

Prevent duplicate jobs with custom IDs:

```python
await enqueue_task(
    "send_welcome_email",
    user_id=user.id,
    _job_id=f"welcome-{user.id}"  # Only one per user
)
```

### 3. Set Appropriate Timeouts

```python
@dataclass
class WorkerSettings:
    job_timeout = 300  # 5 minute default
```

For long-running tasks:

```python
async def long_task(ctx: dict[str, Any]) -> str:
    ctx['job_timeout'] = 3600  # 1 hour for this job
    await lengthy_operation()
```

### 4. Handle Graceful Shutdown

The worker handles SIGTERM gracefully, completing current jobs before exiting.

## Configuration Reference

| Setting | Default | Description |
|---------|---------|-------------|
| `max_jobs` | 10 | Max concurrent jobs per worker |
| `job_timeout` | 300 | Default job timeout (seconds) |
| `keep_result` | 3600 | Result retention time (seconds) |
| `poll_delay` | 0.5 | Queue polling interval (seconds) |
| `max_tries` | 3 | Max retry attempts |
| `retry_delay` | 10s | Delay between retries |

## See Also

- [ARQ Documentation](https://arq-docs.helpmanual.io/)
- [Cache Infrastructure](cache-graph.md)
- [Services Layer](services.md)
{%- else -%}
# Background Tasks

Background tasks are not enabled in this project.

To enable ARQ-based background task processing, regenerate the project with:

```bash
cookiecutter /path/to/devenv \
    --no-input \
    cache_backend="redis"
```

ARQ requires Redis as its job queue backend.
{%- endif %}
