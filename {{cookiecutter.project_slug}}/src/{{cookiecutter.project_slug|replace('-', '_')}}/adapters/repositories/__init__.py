"""Repository implementations - Data access layer.

Repositories handle persistence of domain entities, translating between
domain objects and storage formats.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Protocol
from uuid import UUID

if TYPE_CHECKING:
    from ..domain.entities import ExampleEntity


class ExampleRepository(Protocol):
    """Protocol defining the repository contract for ExampleEntity.

    Implementations should handle actual persistence (database, file, memory).
    """

    async def get_by_id(self, entity_id: UUID) -> Optional[ExampleEntity]:
        """Retrieve an entity by its unique identifier."""
        ...

    async def save(self, entity: ExampleEntity) -> ExampleEntity:
        """Persist an entity, creating or updating as needed."""
        ...

    async def delete(self, entity_id: UUID) -> bool:
        """Remove an entity by its identifier. Returns True if deleted."""
        ...


class InMemoryExampleRepository:
    """In-memory implementation of ExampleRepository for development/testing."""

    def __init__(self) -> None:
        self._storage: dict[UUID, ExampleEntity] = {}

    async def get_by_id(self, entity_id: UUID) -> Optional[ExampleEntity]:
        """Retrieve entity from memory."""
        return self._storage.get(entity_id)

    async def save(self, entity: ExampleEntity) -> ExampleEntity:
        """Store entity in memory."""
        self._storage[entity.id] = entity
        return entity

    async def delete(self, entity_id: UUID) -> bool:
        """Remove entity from memory."""
        if entity_id in self._storage:
            del self._storage[entity_id]
            return True
        return False
