{%- if cookiecutter.cache_backend in ['redis', 'falkordb'] -%}
"""Redis cache infrastructure.

Provides async Redis client for caching, sessions, and pub/sub.
Compatible with both Redis and FalkorDB (Redis-compatible).
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import Any

import redis.asyncio as redis

from .config import get_settings

# Redis client (initialized lazily)
_redis_client: redis.Redis | None = None


def get_redis() -> redis.Redis:
    """Get or create the Redis client."""
    global _redis_client
    if _redis_client is None:
        settings = get_settings()
        if settings.redis_url is None:
            raise ValueError("REDIS_URL is not configured")
        _redis_client = redis.from_url(
            settings.redis_url,
            encoding="utf-8",
            decode_responses=True,
        )
    return _redis_client


async def init_cache() -> None:
    """Initialize the cache connection and verify connectivity."""
    client = get_redis()
    await client.ping()


async def close_cache() -> None:
    """Close the Redis connection."""
    global _redis_client
    if _redis_client is not None:
        await _redis_client.close()
        _redis_client = None


@asynccontextmanager
async def get_cache():
    """Get Redis client as async context manager."""
    client = get_redis()
    try:
        yield client
    finally:
        pass  # Connection pooling handles cleanup


# Session helpers
class SessionManager:
    """Simple session management using Redis."""

    def __init__(self, prefix: str = "session:", ttl: int = 3600):
        self.prefix = prefix
        self.ttl = ttl

    async def get(self, session_id: str) -> dict[str, Any] | None:
        """Get session data by ID."""
        import json

        client = get_redis()
        data = await client.get(f"{self.prefix}{session_id}")
        if data:
            return json.loads(data)
        return None

    async def set(self, session_id: str, data: dict[str, Any]) -> None:
        """Set session data with TTL."""
        import json

        client = get_redis()
        await client.setex(
            f"{self.prefix}{session_id}",
            self.ttl,
            json.dumps(data),
        )

    async def delete(self, session_id: str) -> None:
        """Delete a session."""
        client = get_redis()
        await client.delete(f"{self.prefix}{session_id}")

    async def extend(self, session_id: str) -> None:
        """Extend session TTL."""
        client = get_redis()
        await client.expire(f"{self.prefix}{session_id}", self.ttl)


# Default session manager
session_manager = SessionManager()
{%- else -%}
"""Cache infrastructure - Not enabled.

This project was generated without a cache backend.
To enable Redis/FalkorDB, regenerate with cache_backend='redis' or 'falkordb'.
"""
{%- endif %}
