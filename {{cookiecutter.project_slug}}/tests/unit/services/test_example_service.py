"""Tests for ExampleService."""

from __future__ import annotations

import pytest

from {{ cookiecutter.project_slug|replace('-', '_') }}.services import ExampleService


class TestExampleService:
    """Tests for ExampleService."""

    async def test_create_entity(self, service: ExampleService) -> None:
        """Service can create a valid entity."""
        entity = await service.create("Test Entity", "A description")

        assert entity.name == "Test Entity"
        assert entity.description == "A description"
        assert entity.id is not None

    async def test_create_entity_trims_whitespace(self, service: ExampleService) -> None:
        """Service trims whitespace from name."""
        entity = await service.create("  Trimmed  ", "")

        assert entity.name == "Trimmed"

    async def test_create_entity_empty_name_raises(self, service: ExampleService) -> None:
        """Service raises ValueError for empty name."""
        with pytest.raises(ValueError, match="cannot be empty"):
            await service.create("", "")

    async def test_create_entity_whitespace_name_raises(self, service: ExampleService) -> None:
        """Service raises ValueError for whitespace-only name."""
        with pytest.raises(ValueError, match="cannot be empty"):
            await service.create("   ", "")

    async def test_get_by_id_returns_entity(self, service: ExampleService) -> None:
        """Service retrieves created entity by ID."""
        created = await service.create("Test", "")
        retrieved = await service.get_by_id(created.id)

        assert retrieved is not None
        assert retrieved.id == created.id
        assert retrieved.name == created.name

    async def test_get_by_id_returns_none_for_unknown(self, service: ExampleService) -> None:
        """Service returns None for unknown ID."""
        from uuid import uuid4

        result = await service.get_by_id(uuid4())
        assert result is None

    async def test_delete_returns_true_for_existing(self, service: ExampleService) -> None:
        """Service returns True when deleting existing entity."""
        entity = await service.create("To Delete", "")
        result = await service.delete(entity.id)

        assert result is True
        assert await service.get_by_id(entity.id) is None

    async def test_delete_returns_false_for_unknown(self, service: ExampleService) -> None:
        """Service returns False when deleting unknown entity."""
        from uuid import uuid4

        result = await service.delete(uuid4())
        assert result is False
