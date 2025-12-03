{%- if cookiecutter.api_framework == 'fastapi' -%}
"""Integration tests for the REST API."""

from __future__ import annotations

from httpx import AsyncClient


class TestHealthEndpoint:
    """Tests for health check endpoint."""

    async def test_health_returns_ok(self, client: AsyncClient) -> None:
        """Health endpoint returns OK status."""
        response = await client.get("/health")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert "app_name" in data


class TestRootEndpoint:
    """Tests for root endpoint."""

    async def test_root_returns_message(self, client: AsyncClient) -> None:
        """Root endpoint returns welcome message."""
        response = await client.get("/")

        assert response.status_code == 200
        data = response.json()
        assert "message" in data


class TestUserEndpoints:
    """Tests for user CRUD endpoints."""

    async def test_create_user(self, client: AsyncClient) -> None:
        """Can create user via POST."""
        response = await client.post(
            "/users",
            json={"username": "alice", "email": "alice@example.com", "display_name": "Alice"},
        )

        assert response.status_code == 201
        data = response.json()
        assert data["username"] == "alice"
        assert data["email"] == "alice@example.com"
        assert "id" in data
        assert "created_at" in data

    async def test_create_user_short_username_fails(self, client: AsyncClient) -> None:
        """Creating user with short username returns 400."""
        response = await client.post(
            "/users",
            json={"username": "ab", "email": "ab@example.com"},
        )

        assert response.status_code == 400

    async def test_create_user_invalid_email_fails(self, client: AsyncClient) -> None:
        """Creating user with invalid email returns 400."""
        response = await client.post(
            "/users",
            json={"username": "alice", "email": "not-an-email"},
        )

        assert response.status_code == 422  # Pydantic validation error

    async def test_get_user_not_found(self, client: AsyncClient) -> None:
        """Getting unknown user returns 404."""
        from uuid import uuid4

        response = await client.get(f"/users/{uuid4()}")
        assert response.status_code == 404

    async def test_get_user_by_username(self, client: AsyncClient) -> None:
        """Can get user by username."""
        # First create a user
        await client.post(
            "/users",
            json={"username": "findme", "email": "findme@example.com"},
        )

        # Then find by username
        response = await client.get("/users/by-username/findme")
        assert response.status_code == 200
        data = response.json()
        assert data["username"] == "findme"

    async def test_delete_user_not_found(self, client: AsyncClient) -> None:
        """Deleting unknown user returns 404."""
        from uuid import uuid4

        response = await client.delete(f"/users/{uuid4()}")
        assert response.status_code == 404

    async def test_create_duplicate_username_fails(self, client: AsyncClient) -> None:
        """Creating user with duplicate username returns 400."""
        await client.post(
            "/users",
            json={"username": "duplicate", "email": "first@example.com"},
        )

        response = await client.post(
            "/users",
            json={"username": "duplicate", "email": "second@example.com"},
        )
        assert response.status_code == 400
{%- else -%}
"""Integration tests - API not enabled.

This project was generated without an API framework.
Add API tests here if you enable FastAPI later.
"""
{%- endif %}
