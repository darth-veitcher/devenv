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
from ..models import UserModel
{%- endif %}

if TYPE_CHECKING:
    from ...domain.entities import User


class UserRepository(Protocol):
    """Protocol defining the repository contract for User.

    Implementations should handle actual persistence (database, file, memory).
    All implementations (InMemory, SQLite, PostgreSQL) must support the same interface.
    """

    async def get_by_id(self, user_id: UUID) -> User | None:
        """Retrieve a user by their unique identifier."""
        ...

    async def get_by_username(self, username: str) -> User | None:
        """Retrieve a user by their username."""
        ...

    async def list_all(self) -> list[User]:
        """Retrieve all users."""
        ...

    async def save(self, user: User) -> User:
        """Persist a user, creating or updating as needed."""
        ...

    async def delete(self, user_id: UUID) -> bool:
        """Remove a user by their identifier. Returns True if deleted."""
        ...


class InMemoryUserRepository:
    """In-memory implementation of UserRepository for development/testing."""

    def __init__(self) -> None:
        self._storage: dict[UUID, User] = {}
        self._username_index: dict[str, UUID] = {}

    async def get_by_id(self, user_id: UUID) -> User | None:
        """Retrieve user from memory."""
        return self._storage.get(user_id)

    async def get_by_username(self, username: str) -> User | None:
        """Retrieve user by username from memory."""
        user_id = self._username_index.get(username)
        return self._storage.get(user_id) if user_id else None

    async def list_all(self) -> list[User]:
        """Retrieve all users from memory."""
        return list(self._storage.values())

    async def save(self, user: User) -> User:
        """Store user in memory."""
        # Update username index
        self._username_index[user.username] = user.id
        self._storage[user.id] = user
        return user

    async def delete(self, user_id: UUID) -> bool:
        """Remove user from memory."""
        if user_id in self._storage:
            user = self._storage[user_id]
            del self._username_index[user.username]
            del self._storage[user_id]
            return True
        return False
{% if cookiecutter.database_backend in ['sqlite', 'postgresql'] %}


class SQLAlchemyUserRepository:
    """SQLAlchemy implementation of UserRepository.

    Provides feature parity between SQLite and PostgreSQL via the SQLAlchemy ORM.
    """

    async def get_by_id(self, user_id: UUID) -> User | None:
        """Retrieve user from database."""
        from ...domain.entities import User

        async with get_session() as session:
            result = await session.execute(
                select(UserModel).where(UserModel.id == str(user_id))
            )
            model = result.scalar_one_or_none()
            if model is None:
                return None
            return User(
                id=UUID(model.id),
                created_at=model.created_at,
                updated_at=model.updated_at,
                username=model.username,
                email=model.email,
                display_name=model.display_name or "",
            )

    async def get_by_username(self, username: str) -> User | None:
        """Retrieve user by username from database."""
        from ...domain.entities import User

        async with get_session() as session:
            result = await session.execute(
                select(UserModel).where(UserModel.username == username)
            )
            model = result.scalar_one_or_none()
            if model is None:
                return None
            return User(
                id=UUID(model.id),
                created_at=model.created_at,
                updated_at=model.updated_at,
                username=model.username,
                email=model.email,
                display_name=model.display_name or "",
            )

    async def list_all(self) -> list[User]:
        """Retrieve all users from database."""
        from ...domain.entities import User

        async with get_session() as session:
            result = await session.execute(select(UserModel))
            models = result.scalars().all()
            return [
                User(
                    id=UUID(model.id),
                    created_at=model.created_at,
                    updated_at=model.updated_at,
                    username=model.username,
                    email=model.email,
                    display_name=model.display_name or "",
                )
                for model in models
            ]

    async def save(self, user: User) -> User:
        """Persist user to database."""
        async with get_session() as session:
            result = await session.execute(
                select(UserModel).where(UserModel.id == str(user.id))
            )
            existing = result.scalar_one_or_none()

            if existing:
                # Update
                existing.username = user.username
                existing.email = user.email
                existing.display_name = user.display_name or None
                existing.updated_at = user.updated_at
            else:
                # Create
                model = UserModel(
                    id=str(user.id),
                    username=user.username,
                    email=user.email,
                    display_name=user.display_name or None,
                    created_at=user.created_at,
                    updated_at=user.updated_at,
                )
                session.add(model)

            return user

    async def delete(self, user_id: UUID) -> bool:
        """Remove user from database."""
        async with get_session() as session:
            result = await session.execute(
                select(UserModel).where(UserModel.id == str(user_id))
            )
            model = result.scalar_one_or_none()
            if model is None:
                return False
            await session.delete(model)
            return True
{% endif %}
