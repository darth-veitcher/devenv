{%- if cookiecutter.api_framework == 'fastapi' -%}
"""FastAPI application entry point.

REST API presentation layer that delegates to services.
"""

from __future__ import annotations

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Annotated, Any
from uuid import UUID

from fastapi import Depends, FastAPI, HTTPException
{%- if cookiecutter.database_backend == 'none' %}

from ..adapters.repositories import InMemoryUserRepository
from ..infrastructure.config import Settings, get_settings
from ..services import UserService
from .schemas import CreateUserRequest, HealthResponse, UserListResponse, UserResponse
{%- else %}

from ..adapters.repositories import SQLAlchemyUserRepository
from ..infrastructure.config import Settings, get_settings
from ..infrastructure.database import close_db, init_db
from ..services import UserService
from .schemas import CreateUserRequest, HealthResponse, UserListResponse, UserResponse
{%- endif %}
{%- if cookiecutter.cache_backend in ['redis', 'falkordb'] %}
from ..infrastructure.cache import close_cache, init_cache
{%- endif %}
{%- if cookiecutter.cache_backend == 'falkordb' %}
from ..infrastructure.graph import close_graph, init_graph
from .schemas import FollowRequest
{%- endif %}

# Dependency injection
{% if cookiecutter.database_backend == 'none' %}
_repository = InMemoryUserRepository()
{% else %}
_repository = SQLAlchemyUserRepository()
{% endif %}


def get_user_service() -> UserService:
    """Dependency for UserService."""
    return UserService(_repository)


# Type aliases for dependency injection (B008 fix)
SettingsDep = Annotated[Settings, Depends(get_settings)]
ServiceDep = Annotated[UserService, Depends(get_user_service)]


# Application lifecycle
@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan manager."""
    # Startup
{%- if cookiecutter.database_backend in ['sqlite', 'postgresql'] %}
    await init_db()
{%- endif %}
{%- if cookiecutter.cache_backend in ['redis', 'falkordb'] %}
    await init_cache()
{%- endif %}
{%- if cookiecutter.cache_backend == 'falkordb' %}
    await init_graph()
{%- endif %}
    yield
    # Shutdown
{%- if cookiecutter.cache_backend == 'falkordb' %}
    await close_graph()
{%- endif %}
{%- if cookiecutter.cache_backend in ['redis', 'falkordb'] %}
    await close_cache()
{%- endif %}
{%- if cookiecutter.database_backend in ['sqlite', 'postgresql'] %}
    await close_db()
{%- endif %}


# FastAPI app
app = FastAPI(
    title="{{ cookiecutter.project_name }}",
    description="{{ cookiecutter.project_description }}",
    version="0.1.0",
    lifespan=lifespan,
)


# Routes
@app.get("/", response_model=dict[str, str])
def root() -> dict[str, str]:
    """Root endpoint."""
    return {"message": "Hello from {{ cookiecutter.project_name }}!"}


@app.get("/health", response_model=HealthResponse)
def health(settings: SettingsDep) -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(
        status="ok",
        app_name=settings.app_name,
        database=settings.database_url or "not configured",
{%- if cookiecutter.cache_backend in ['redis', 'falkordb'] %}
        cache=settings.redis_url or "not configured",
{%- endif %}
    )


# User CRUD endpoints
@app.post("/users", response_model=UserResponse, status_code=201)
async def create_user(
    request: CreateUserRequest,
    service: ServiceDep,
) -> Any:
    """Create a new user."""
    try:
        user = await service.create(
            username=request.username,
            email=request.email,
            display_name=request.display_name,
        )
        return UserResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            display_name=user.display_name,
            created_at=user.created_at,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: UUID,
    service: ServiceDep,
) -> Any:
    """Get a user by ID."""
    user = await service.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        display_name=user.display_name,
        created_at=user.created_at,
    )


@app.get("/users/by-username/{username}", response_model=UserResponse)
async def get_user_by_username(
    username: str,
    service: ServiceDep,
) -> Any:
    """Get a user by username."""
    user = await service.get_by_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        display_name=user.display_name,
        created_at=user.created_at,
    )


@app.delete("/users/{user_id}", status_code=204)
async def delete_user(
    user_id: UUID,
    service: ServiceDep,
) -> None:
    """Delete a user by ID."""
    deleted = await service.delete(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
{%- if cookiecutter.cache_backend == 'falkordb' %}


# Social graph endpoints (FalkorDB)
@app.post("/users/{user_id}/follow", status_code=201)
async def follow_user(
    user_id: UUID,
    request: FollowRequest,
    service: ServiceDep,
) -> dict[str, str]:
    """Follow another user.

    Creates a FOLLOWS relationship in the graph database.
    """
    try:
        await service.follow(user_id, request.target_user_id)
        return {"status": "following"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@app.delete("/users/{user_id}/follow/{target_user_id}", status_code=204)
async def unfollow_user(
    user_id: UUID,
    target_user_id: UUID,
    service: ServiceDep,
) -> None:
    """Unfollow a user.

    Removes the FOLLOWS relationship from the graph database.
    """
    await service.unfollow(user_id, target_user_id)


@app.get("/users/{user_id}/followers", response_model=UserListResponse)
async def get_followers(
    user_id: UUID,
    service: ServiceDep,
) -> Any:
    """Get all users who follow this user."""
    user = await service.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    followers = await service.get_followers(user_id)
    return UserListResponse(
        items=[
            UserResponse(
                id=u.id,
                username=u.username,
                email=u.email,
                display_name=u.display_name,
                created_at=u.created_at,
            )
            for u in followers
        ],
        total=len(followers),
    )


@app.get("/users/{user_id}/following", response_model=UserListResponse)
async def get_following(
    user_id: UUID,
    service: ServiceDep,
) -> Any:
    """Get all users this user follows."""
    user = await service.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    following = await service.get_following(user_id)
    return UserListResponse(
        items=[
            UserResponse(
                id=u.id,
                username=u.username,
                email=u.email,
                display_name=u.display_name,
                created_at=u.created_at,
            )
            for u in following
        ],
        total=len(following),
    )


@app.get("/users/{user_id}/friends", response_model=UserListResponse)
async def get_friends(
    user_id: UUID,
    service: ServiceDep,
) -> Any:
    """Get mutual follows (friends) - users who follow each other."""
    user = await service.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    friends = await service.get_mutual_follows(user_id)
    return UserListResponse(
        items=[
            UserResponse(
                id=u.id,
                username=u.username,
                email=u.email,
                display_name=u.display_name,
                created_at=u.created_at,
            )
            for u in friends
        ],
        total=len(friends),
    )
{%- endif %}


if __name__ == "__main__":
    import uvicorn

    settings = get_settings()
    uvicorn.run(app, host=settings.host, port=settings.port)
{%- else -%}
"""API module - Not enabled.

This project was generated without an API framework.
To enable FastAPI, regenerate with api_framework='fastapi'.
"""
{%- endif %}
