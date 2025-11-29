"""Application configuration using pydantic-settings.

Environment variables and configuration management following 12-factor app principles.
"""

from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables.

    All settings can be overridden via environment variables.
    Prefix: none (direct mapping)

    Example:
        DATABASE_URL=postgresql://... sets settings.database_url
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Application
    app_name: str = "{{ cookiecutter.project_name }}"
    debug: bool = False
    log_level: str = "INFO"

    # Server
    host: str = "0.0.0.0"
    port: int = {{ cookiecutter.app_port }}
{% if cookiecutter.database_backend == 'none' %}

    # Database (in-memory, no persistence)
    database_url: str | None = None
{% elif cookiecutter.database_backend == 'sqlite' %}

    # Database (SQLite)
    database_url: str = "sqlite+aiosqlite:///./data/{{ cookiecutter.project_slug }}.db"
{% elif cookiecutter.database_backend == 'postgresql' %}

    # Database (PostgreSQL)
    database_url: str = "postgresql+asyncpg://{{ cookiecutter.postgres_user }}:{{ cookiecutter.postgres_password }}@postgres:5432/{{ cookiecutter.postgres_db }}"
{% endif %}

    @property
    def is_production(self) -> bool:
        """Check if running in production mode."""
        return not self.debug


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance.

    Uses lru_cache to ensure settings are only loaded once.
    """
    return Settings()
