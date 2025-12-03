"""Tests for domain entities."""

from __future__ import annotations

from {{ cookiecutter.project_slug|replace('-', '_') }}.domain.entities import User


class TestUser:
    """Tests for User entity."""

    def test_create_user(self) -> None:
        """User can be created with valid data."""
        user = User(username="alice", email="alice@example.com", display_name="Alice")

        assert user.username == "alice"
        assert user.email == "alice@example.com"
        assert user.display_name == "Alice"
        assert user.id is not None
        assert user.created_at is not None

    def test_user_is_immutable(self) -> None:
        """User should be immutable (frozen dataclass)."""
        import pytest

        user = User(username="alice", email="alice@example.com")

        # Should raise FrozenInstanceError
        with pytest.raises(AttributeError):
            user.username = "bob"  # type: ignore

    def test_is_valid_with_valid_data(self) -> None:
        """User with valid username and email should be valid."""
        user = User(username="alice", email="alice@example.com")
        assert user.is_valid() is True

    def test_is_invalid_with_short_username(self) -> None:
        """User with short username should be invalid."""
        user = User(username="ab", email="ab@example.com")
        assert user.is_valid() is False

    def test_is_invalid_without_email_at(self) -> None:
        """User with invalid email should be invalid."""
        user = User(username="alice", email="alice-at-example.com")
        assert user.is_valid() is False

    def test_with_display_name_returns_new_user(self) -> None:
        """with_display_name returns a new User with updated display name."""
        user = User(username="alice", email="alice@example.com")
        updated = user.with_display_name("Alice Smith")

        assert updated.display_name == "Alice Smith"
        assert updated.id == user.id
        assert updated.username == user.username
        assert updated.updated_at is not None
