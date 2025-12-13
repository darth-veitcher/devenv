{%- if cookiecutter.database_backend in ['sqlite', 'postgresql'] -%}
"""Alembic migration environment configuration.

This file configures how Alembic runs migrations.
It uses the same database configuration as the main application.
"""

from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from {{ cookiecutter.project_slug|replace('-', '_') }}.infrastructure.config import get_settings
from {{ cookiecutter.project_slug|replace('-', '_') }}.infrastructure.database import Base

# Import all models so Alembic can detect them
from {{ cookiecutter.project_slug|replace('-', '_') }}.adapters import models  # noqa: F401

# This is the Alembic Config object
config = context.config

# Interpret the config file for Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Add your model's MetaData object here for 'autogenerate' support
target_metadata = Base.metadata


def get_url() -> str:
    """Get database URL from application settings.

    Converts async URLs to sync URLs for Alembic compatibility.
    """
    settings = get_settings()
    url = settings.database_url
    if url is None:
        raise ValueError("DATABASE_URL environment variable is not set")
{%- if cookiecutter.database_backend == 'sqlite' %}
    # Convert async SQLite URL to sync for Alembic
    return url.replace("sqlite+aiosqlite", "sqlite")
{%- elif cookiecutter.database_backend == 'postgresql' %}
    # Convert async PostgreSQL URL to sync for Alembic
    return url.replace("postgresql+asyncpg", "postgresql+psycopg2")
{%- endif %}


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL and not an Engine,
    though an Engine is also acceptable here. By skipping the Engine
    creation we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.
    """
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine and associate a
    connection with the context.
    """
    configuration = config.get_section(config.config_ini_section, {})
    configuration["sqlalchemy.url"] = get_url()

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
{%- else -%}
# Migrations not configured - database backend is 'none'
{%- endif %}
