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


class TestEntityEndpoints:
    """Tests for entity CRUD endpoints."""

    async def test_create_entity(self, client: AsyncClient) -> None:
        """Can create entity via POST."""
        response = await client.post(
            "/entities",
            json={"name": "Test Entity", "description": "A test"},
        )

        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Test Entity"
        assert "id" in data

    async def test_create_entity_empty_name_fails(self, client: AsyncClient) -> None:
        """Creating entity with empty name returns 400."""
        response = await client.post(
            "/entities",
            json={"name": "", "description": ""},
        )

        assert response.status_code == 400

    async def test_get_entity_not_found(self, client: AsyncClient) -> None:
        """Getting unknown entity returns 404."""
        from uuid import uuid4

        response = await client.get(f"/entities/{uuid4()}")
        assert response.status_code == 404

    async def test_delete_entity_not_found(self, client: AsyncClient) -> None:
        """Deleting unknown entity returns 404."""
        from uuid import uuid4

        response = await client.delete(f"/entities/{uuid4()}")
        assert response.status_code == 404
