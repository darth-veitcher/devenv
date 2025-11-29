"""Pytest configuration and fixtures.

Shared fixtures for all tests.
"""

from __future__ import annotations

from collections.abc import AsyncGenerator

import pytest
from httpx import ASGITransport, AsyncClient

from {{ cookiecutter.project_slug|replace('-', '_') }}.adapters.repositories import InMemoryExampleRepository
from {{ cookiecutter.project_slug|replace('-', '_') }}.api.main import app
{% if cookiecutter.database_backend in ['sqlite', 'postgresql'] -%}
from {{ cookiecutter.project_slug|replace('-', '_') }}.infrastructure.database import close_db, init_db
{% endif -%}
from {{ cookiecutter.project_slug|replace('-', '_') }}.services import ExampleService


@pytest.fixture
def repository() -> InMemoryExampleRepository:
    """Provide a fresh in-memory repository for each test."""
    return InMemoryExampleRepository()


@pytest.fixture
def service(repository: InMemoryExampleRepository) -> ExampleService:
    """Provide a service instance with the test repository."""
    return ExampleService(repository)


@pytest.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    """Provide an async HTTP client for API tests."""
{% if cookiecutter.database_backend in ['sqlite', 'postgresql'] %}
    # Initialize database tables before tests
    await init_db()
{% endif %}
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client
{% if cookiecutter.database_backend in ['sqlite', 'postgresql'] %}
    # Clean up database connection after tests
    await close_db()
{% endif %}
