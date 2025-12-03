"""Services layer - Dynamic layer implementing business logic and workflows.

Contains business rules, workflows, and orchestration logic that operates
on domain entities through repository interfaces.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID
{%- if cookiecutter.cache_backend == 'falkordb' %}

from ..infrastructure.graph import get_graph
{%- endif %}

if TYPE_CHECKING:
    from ..adapters.repositories import UserRepository
    from ..domain.entities import User


class UserService:
    """Service implementing business logic for User.

    Services orchestrate domain operations through repositories and apply
    business rules. They are reused across all presentation interfaces
    (CLI, REST API, MCP).

    When FalkorDB is enabled, user operations automatically sync to the graph
    for relationship queries.

    Example:
        >>> repo = InMemoryUserRepository()
        >>> service = UserService(repo)
        >>> user = await service.create("alice", "alice@example.com")
    """

    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    async def create(self, username: str, email: str, display_name: str = "") -> User:
        """Create a new user with validation.

        Args:
            username: Unique username (min 3 characters)
            email: Valid email address
            display_name: Optional display name

        Returns:
            The created user

        Raises:
            ValueError: If username or email is invalid
        """
        from ..domain.entities import User

        username = username.strip().lower()
        email = email.strip().lower()

        if len(username) < 3:
            raise ValueError("Username must be at least 3 characters")
        if "@" not in email:
            raise ValueError("Invalid email address")

        # Check for existing username
        existing = await self._repository.get_by_username(username)
        if existing:
            raise ValueError(f"Username '{username}' already exists")

        user = User(username=username, email=email, display_name=display_name)
        saved = await self._repository.save(user)
{%- if cookiecutter.cache_backend == 'falkordb' %}

        # Sync to graph database
        await self._sync_user_to_graph(saved)
{%- endif %}

        return saved

    async def get_by_id(self, user_id: UUID) -> User | None:
        """Retrieve a user by ID."""
        return await self._repository.get_by_id(user_id)

    async def get_by_username(self, username: str) -> User | None:
        """Retrieve a user by username."""
        return await self._repository.get_by_username(username.strip().lower())

    async def delete(self, user_id: UUID) -> bool:
        """Delete a user by ID."""
        user = await self._repository.get_by_id(user_id)
        if not user:
            return False

        deleted = await self._repository.delete(user_id)
{%- if cookiecutter.cache_backend == 'falkordb' %}

        if deleted:
            # Remove from graph database
            await self._remove_user_from_graph(user_id)
{%- endif %}

        return deleted
{%- if cookiecutter.cache_backend == 'falkordb' %}

    # Graph sync methods (FalkorDB)
    async def _sync_user_to_graph(self, user: User) -> None:
        """Sync user to FalkorDB graph.

        Creates a :User node with the user's properties.
        PostgreSQL/SQLite remains the source of truth.

        Note: Gracefully handles connection failures to allow operation
        without FalkorDB (e.g., in tests or degraded mode).
        """
        try:
            graph = get_graph()
            query = """
                MERGE (u:User {id: $id})
                SET u.username = $username,
                    u.email = $email,
                    u.display_name = $display_name
            """
            graph.query(query, {
                "id": str(user.id),
                "username": user.username,
                "email": user.email,
                "display_name": user.display_name,
            })
        except Exception:
            # Graph sync is best-effort; primary data is in SQL
            pass

    async def _remove_user_from_graph(self, user_id: UUID) -> None:
        """Remove user and their relationships from FalkorDB."""
        try:
            graph = get_graph()
            query = "MATCH (u:User {id: $id}) DETACH DELETE u"
            graph.query(query, {"id": str(user_id)})
        except Exception:
            # Graph sync is best-effort; primary data is in SQL
            pass

    async def follow(self, follower_id: UUID, followed_id: UUID) -> bool:
        """Create a FOLLOWS relationship between users.

        Args:
            follower_id: The user who is following
            followed_id: The user being followed

        Returns:
            True if relationship was created

        Raises:
            ValueError: If either user doesn't exist or self-follow attempt
        """
        if follower_id == followed_id:
            raise ValueError("Cannot follow yourself")

        follower = await self._repository.get_by_id(follower_id)
        followed = await self._repository.get_by_id(followed_id)

        if not follower:
            raise ValueError(f"Follower user {follower_id} not found")
        if not followed:
            raise ValueError(f"Followed user {followed_id} not found")

        graph = get_graph()
        query = """
            MATCH (a:User {id: $follower_id})
            MATCH (b:User {id: $followed_id})
            MERGE (a)-[r:FOLLOWS]->(b)
            RETURN r
        """
        result = graph.query(query, {
            "follower_id": str(follower_id),
            "followed_id": str(followed_id),
        })
        return len(result.result_set) > 0

    async def unfollow(self, follower_id: UUID, followed_id: UUID) -> bool:
        """Remove a FOLLOWS relationship between users.

        Returns:
            True if relationship was removed
        """
        graph = get_graph()
        query = """
            MATCH (a:User {id: $follower_id})-[r:FOLLOWS]->(b:User {id: $followed_id})
            DELETE r
            RETURN count(r) as deleted
        """
        result = graph.query(query, {
            "follower_id": str(follower_id),
            "followed_id": str(followed_id),
        })
        return len(result.result_set) > 0

    async def get_followers(self, user_id: UUID) -> list[User]:
        """Get all users who follow the given user."""
        graph = get_graph()
        query = """
            MATCH (follower:User)-[:FOLLOWS]->(u:User {id: $user_id})
            RETURN follower.id as id
        """
        result = graph.query(query, {"user_id": str(user_id)})

        followers = []
        for row in result.result_set:
            user = await self._repository.get_by_id(UUID(row[0]))
            if user:
                followers.append(user)
        return followers

    async def get_following(self, user_id: UUID) -> list[User]:
        """Get all users that the given user follows."""
        graph = get_graph()
        query = """
            MATCH (u:User {id: $user_id})-[:FOLLOWS]->(followed:User)
            RETURN followed.id as id
        """
        result = graph.query(query, {"user_id": str(user_id)})

        following = []
        for row in result.result_set:
            user = await self._repository.get_by_id(UUID(row[0]))
            if user:
                following.append(user)
        return following

    async def get_mutual_follows(self, user_id: UUID) -> list[User]:
        """Get users who mutually follow (friends).

        Example graph query for social features.
        """
        graph = get_graph()
        query = """
            MATCH (u:User {id: $user_id})-[:FOLLOWS]->(friend:User)-[:FOLLOWS]->(u)
            RETURN friend.id as id
        """
        result = graph.query(query, {"user_id": str(user_id)})

        mutuals = []
        for row in result.result_set:
            user = await self._repository.get_by_id(UUID(row[0]))
            if user:
                mutuals.append(user)
        return mutuals
{%- endif %}
