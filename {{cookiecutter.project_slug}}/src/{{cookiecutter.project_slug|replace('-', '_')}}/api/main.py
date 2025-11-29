"""FastAPI application entry point.

REST API presentation layer that delegates to services.
"""

from __future__ import annotations

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Annotated, Any
from uuid import UUID

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict
{%- if cookiecutter.database_backend == 'none' %}

from ..adapters.repositories import InMemoryExampleRepository
from ..infrastructure.config import Settings, get_settings
from ..services import ExampleService
{%- else %}

from ..adapters.repositories import SQLAlchemyExampleRepository
from ..infrastructure.config import Settings, get_settings
from ..infrastructure.database import close_db, init_db
from ..services import ExampleService
{%- endif %}


# Request/Response schemas
class CreateEntityRequest(BaseModel):
    """Request schema for creating an entity."""

    name: str
    description: str = ""


class EntityResponse(BaseModel):
    """Response schema for entity data."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    description: str


class HealthResponse(BaseModel):
    """Health check response."""

    status: str
    app_name: str
    database: str | None


# Dependency injection
{% if cookiecutter.database_backend == 'none' %}
_repository = InMemoryExampleRepository()
{% else %}
_repository = SQLAlchemyExampleRepository()
{% endif %}


def get_example_service() -> ExampleService:
    """Dependency for ExampleService."""
    return ExampleService(_repository)


# Type aliases for dependency injection (B008 fix)
SettingsDep = Annotated[Settings, Depends(get_settings)]
ServiceDep = Annotated[ExampleService, Depends(get_example_service)]


# Application lifecycle
@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan manager."""
    # Startup
{% if cookiecutter.database_backend in ['sqlite', 'postgresql'] %}
    await init_db()
{% endif %}
    yield
    # Shutdown
{% if cookiecutter.database_backend in ['sqlite', 'postgresql'] %}
    await close_db()
{% endif %}


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
    )


@app.post("/entities", response_model=EntityResponse, status_code=201)
async def create_entity(
    request: CreateEntityRequest,
    service: ServiceDep,
) -> Any:
    """Create a new entity."""
    try:
        entity = await service.create(request.name, request.description)
        return EntityResponse(
            id=entity.id,
            name=entity.name,
            description=entity.description,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@app.get("/entities/{entity_id}", response_model=EntityResponse)
async def get_entity(
    entity_id: UUID,
    service: ServiceDep,
) -> Any:
    """Get an entity by ID."""
    entity = await service.get_by_id(entity_id)
    if not entity:
        raise HTTPException(status_code=404, detail="Entity not found")
    return EntityResponse(
        id=entity.id,
        name=entity.name,
        description=entity.description,
    )


@app.delete("/entities/{entity_id}", status_code=204)
async def delete_entity(
    entity_id: UUID,
    service: ServiceDep,
) -> None:
    """Delete an entity by ID."""
    deleted = await service.delete(entity_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Entity not found")


if __name__ == "__main__":
    import uvicorn

    settings = get_settings()
    uvicorn.run(app, host=settings.host, port=settings.port)
