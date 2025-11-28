"""Services layer - Dynamic layer implementing business logic and workflows.

Contains business rules, workflows, and orchestration logic that operates
on domain entities through repository interfaces.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional
from uuid import UUID

if TYPE_CHECKING:
    from ..adapters.repositories import ExampleRepository
    from ..domain.entities import ExampleEntity


class ExampleService:
    """Service implementing business logic for ExampleEntity.

    Services orchestrate domain operations through repositories and apply
    business rules. They are reused across all presentation interfaces
    (CLI, REST API, MCP).

    Example:
        >>> repo = InMemoryExampleRepository()
        >>> service = ExampleService(repo)
        >>> entity = await service.create("My Entity", "Description")
    """

    def __init__(self, repository: ExampleRepository) -> None:
        self._repository = repository

    async def create(self, name: str, description: str = "") -> ExampleEntity:
        """Create a new entity with validation.

        Args:
            name: The entity name (required, non-empty)
            description: Optional description

        Returns:
            The created entity

        Raises:
            ValueError: If name is empty
        """
        from ..domain.entities import ExampleEntity

        if not name.strip():
            raise ValueError("Name cannot be empty")

        entity = ExampleEntity(name=name.strip(), description=description)
        return await self._repository.save(entity)

    async def get_by_id(self, entity_id: UUID) -> Optional[ExampleEntity]:
        """Retrieve an entity by ID."""
        return await self._repository.get_by_id(entity_id)

    async def delete(self, entity_id: UUID) -> bool:
        """Delete an entity by ID."""
        return await self._repository.delete(entity_id)
