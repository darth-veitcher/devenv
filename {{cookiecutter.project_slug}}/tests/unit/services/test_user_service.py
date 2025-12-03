"""Tests for UserService."""

from __future__ import annotations

import pytest

from {{ cookiecutter.project_slug|replace('-', '_') }}.services import UserService


class TestUserService:
    """Tests for UserService."""

    async def test_create_user(self, service: UserService) -> None:
        """Service can create a valid user."""
        user = await service.create("alice", "alice@example.com", "Alice Smith")

        assert user.username == "alice"
        assert user.email == "alice@example.com"
        assert user.display_name == "Alice Smith"
        assert user.id is not None

    async def test_create_user_normalizes_case(self, service: UserService) -> None:
        """Service normalizes username and email to lowercase."""
        user = await service.create("ALICE", "Alice@Example.COM")

        assert user.username == "alice"
        assert user.email == "alice@example.com"

    async def test_create_user_trims_whitespace(self, service: UserService) -> None:
        """Service trims whitespace from username and email."""
        user = await service.create("  alice  ", "  alice@example.com  ")

        assert user.username == "alice"
        assert user.email == "alice@example.com"

    async def test_create_user_short_username_raises(self, service: UserService) -> None:
        """Service raises ValueError for short username."""
        with pytest.raises(ValueError, match="at least 3 characters"):
            await service.create("ab", "ab@example.com")

    async def test_create_user_invalid_email_raises(self, service: UserService) -> None:
        """Service raises ValueError for invalid email."""
        with pytest.raises(ValueError, match="Invalid email"):
            await service.create("alice", "not-an-email")

    async def test_create_user_duplicate_username_raises(self, service: UserService) -> None:
        """Service raises ValueError for duplicate username."""
        await service.create("alice", "alice@example.com")

        with pytest.raises(ValueError, match="already exists"):
            await service.create("alice", "other@example.com")

    async def test_get_by_id_returns_user(self, service: UserService) -> None:
        """Service retrieves created user by ID."""
        created = await service.create("alice", "alice@example.com")
        retrieved = await service.get_by_id(created.id)

        assert retrieved is not None
        assert retrieved.id == created.id
        assert retrieved.username == created.username

    async def test_get_by_id_returns_none_for_unknown(self, service: UserService) -> None:
        """Service returns None for unknown ID."""
        from uuid import uuid4

        result = await service.get_by_id(uuid4())
        assert result is None

    async def test_get_by_username_returns_user(self, service: UserService) -> None:
        """Service retrieves user by username."""
        await service.create("alice", "alice@example.com")
        retrieved = await service.get_by_username("alice")

        assert retrieved is not None
        assert retrieved.username == "alice"

    async def test_get_by_username_case_insensitive(self, service: UserService) -> None:
        """Service finds user regardless of case."""
        await service.create("alice", "alice@example.com")
        retrieved = await service.get_by_username("ALICE")

        assert retrieved is not None
        assert retrieved.username == "alice"

    async def test_delete_returns_true_for_existing(self, service: UserService) -> None:
        """Service returns True when deleting existing user."""
        user = await service.create("todelete", "todelete@example.com")
        result = await service.delete(user.id)

        assert result is True
        assert await service.get_by_id(user.id) is None

    async def test_delete_returns_false_for_unknown(self, service: UserService) -> None:
        """Service returns False when deleting unknown user."""
        from uuid import uuid4

        result = await service.delete(uuid4())
        assert result is False
