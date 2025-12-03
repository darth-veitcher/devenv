"""Domain entities - Core business objects with identity and lifecycle.

Following the Semantic Layer pattern, entities here represent the conceptual
domain model, independent of persistence or presentation concerns.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4


@dataclass(frozen=True, kw_only=True)
class EntityBase:
    """Base class for domain entities with identity tracking."""

    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime | None = None


@dataclass(frozen=True)
class User(EntityBase):
    """User domain entity.

    Core user entity for authentication and social features.
    Works across all database backends (in-memory, SQLite, PostgreSQL).

    Example:
        >>> user = User(username="alice", email="alice@example.com")
        >>> user.is_valid()
        True
    """

    username: str
    email: str
    display_name: str = ""

    def is_valid(self) -> bool:
        """Check if user meets business rules."""
        return len(self.username) >= 3 and "@" in self.email

    def with_display_name(self, display_name: str) -> User:
        """Return a new User with updated display name (immutable update)."""
        return User(
            id=self.id,
            created_at=self.created_at,
            updated_at=datetime.now(UTC),
            username=self.username,
            email=self.email,
            display_name=display_name,
        )
