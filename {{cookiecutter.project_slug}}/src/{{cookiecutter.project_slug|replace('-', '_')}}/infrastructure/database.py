"""Database infrastructure using SQLAlchemy async.

Provides database engine, session management, and base model for ORM.
"""
{%- if cookiecutter.database_backend in ['sqlite', 'postgresql'] %}
from __future__ import annotations

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
{%- if cookiecutter.database_backend == 'sqlite' %}
from pathlib import Path
{%- endif %}

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from .config import get_settings

# Naming convention for constraints (helps with migrations)
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models."""

    metadata = MetaData(naming_convention=convention)


# Engine and session factory (initialized lazily)
_engine = None
_session_factory = None


def get_engine():
    """Get or create the database engine."""
    global _engine
    if _engine is None:
        settings = get_settings()
        if settings.database_url is None:
            raise ValueError("DATABASE_URL is not configured")
{% if cookiecutter.database_backend == 'sqlite' %}

        # Ensure data directory exists for SQLite
        db_path = settings.database_url.replace("sqlite+aiosqlite:///", "")
        if db_path.startswith("./"):
            Path(db_path).parent.mkdir(parents=True, exist_ok=True)
{% endif %}

        _engine = create_async_engine(
            settings.database_url,
            echo=settings.debug,
{% if cookiecutter.database_backend == 'sqlite' %}
            connect_args={"check_same_thread": False},
{% endif %}
        )
    return _engine


def get_session_factory():
    """Get or create the session factory."""
    global _session_factory
    if _session_factory is None:
        _session_factory = async_sessionmaker(
            get_engine(),
            class_=AsyncSession,
            expire_on_commit=False,
        )
    return _session_factory


@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Get a database session as an async context manager."""
    factory = get_session_factory()
    async with factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise


async def init_db() -> None:
    """Initialize the database, creating all tables."""
    # Import models to register them with Base.metadata
    from ..adapters import models  # noqa: F401

    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def close_db() -> None:
    """Close the database connection."""
    global _engine, _session_factory
    if _engine is not None:
        await _engine.dispose()
        _engine = None
        _session_factory = None
{% else %}
# Database backend is 'none' - no database infrastructure needed
{% endif %}
