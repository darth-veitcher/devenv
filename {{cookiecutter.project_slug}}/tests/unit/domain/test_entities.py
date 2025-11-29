"""Tests for domain entities."""

from __future__ import annotations

from {{ cookiecutter.project_slug|replace('-', '_') }}.domain.entities import ExampleEntity


class TestExampleEntity:
    """Tests for ExampleEntity."""

    def test_create_entity(self) -> None:
        """Entity can be created with valid data."""
        entity = ExampleEntity(name="Test", description="A test entity")

        assert entity.name == "Test"
        assert entity.description == "A test entity"
        assert entity.id is not None
        assert entity.created_at is not None

    def test_entity_is_immutable(self) -> None:
        """Entity should be immutable (frozen dataclass)."""
        import pytest

        entity = ExampleEntity(name="Test")

        # Should raise FrozenInstanceError
        with pytest.raises(AttributeError):
            entity.name = "Changed"  # type: ignore

    def test_is_valid_with_name(self) -> None:
        """Entity with name should be valid."""
        entity = ExampleEntity(name="Valid Name")
        assert entity.is_valid() is True

    def test_is_invalid_without_name(self) -> None:
        """Entity without name should be invalid."""
        entity = ExampleEntity(name="")
        assert entity.is_valid() is False
