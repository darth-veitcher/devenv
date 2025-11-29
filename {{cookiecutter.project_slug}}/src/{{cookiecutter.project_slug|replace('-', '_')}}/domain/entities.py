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


# Example entity - replace with your domain entities
@dataclass(frozen=True)
class ExampleEntity(EntityBase):
    """Example domain entity.

    Replace this with your actual domain entities. Each entity should:
    - Be immutable (frozen=True)
    - Have a unique identity (id)
    - Contain business logic methods
    - Be independent of infrastructure

    Example:
        >>> entity = ExampleEntity(name="Test", description="A test entity")
        >>> entity.name
        'Test'
    """

    name: str
    description: str = ""

    def is_valid(self) -> bool:
        """Check if entity meets business rules."""
        return len(self.name) > 0
