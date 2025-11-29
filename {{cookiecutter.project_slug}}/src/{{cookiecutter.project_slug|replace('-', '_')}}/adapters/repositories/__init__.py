"""Repository implementations - Data access layer.

Repositories handle persistence of domain entities, translating between
domain objects and storage formats.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol
from uuid import UUID
{%- if cookiecutter.database_backend in ['sqlite', 'postgresql'] %}

from sqlalchemy import select

from ...infrastructure.database import get_session
from ..models import ExampleEntityModel
{%- endif %}

if TYPE_CHECKING:
    from ...domain.entities import ExampleEntity


class ExampleRepository(Protocol):
    """Protocol defining the repository contract for ExampleEntity.

    Implementations should handle actual persistence (database, file, memory).
    """

    async def get_by_id(self, entity_id: UUID) -> ExampleEntity | None:
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

    async def get_by_id(self, entity_id: UUID) -> ExampleEntity | None:
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
{% if cookiecutter.database_backend in ['sqlite', 'postgresql'] %}


class SQLAlchemyExampleRepository:
    """SQLAlchemy implementation of ExampleRepository for database persistence."""

    async def get_by_id(self, entity_id: UUID) -> ExampleEntity | None:
        """Retrieve entity from database."""
        from ...domain.entities import ExampleEntity

        async with get_session() as session:
            result = await session.execute(
                select(ExampleEntityModel).where(ExampleEntityModel.id == str(entity_id))
            )
            model = result.scalar_one_or_none()
            if model is None:
                return None
            return ExampleEntity(
                id=UUID(model.id),
                name=model.name,
                description=model.description,
            )

    async def save(self, entity: ExampleEntity) -> ExampleEntity:
        """Persist entity to database."""
        async with get_session() as session:
            # Check if exists
            result = await session.execute(
                select(ExampleEntityModel).where(ExampleEntityModel.id == str(entity.id))
            )
            existing = result.scalar_one_or_none()

            if existing:
                # Update
                existing.name = entity.name
                existing.description = entity.description
            else:
                # Create
                model = ExampleEntityModel(
                    id=str(entity.id),
                    name=entity.name,
                    description=entity.description,
                )
                session.add(model)

            return entity

    async def delete(self, entity_id: UUID) -> bool:
        """Remove entity from database."""
        async with get_session() as session:
            result = await session.execute(
                select(ExampleEntityModel).where(ExampleEntityModel.id == str(entity_id))
            )
            model = result.scalar_one_or_none()
            if model is None:
                return False
            await session.delete(model)
            return True
{% endif %}
