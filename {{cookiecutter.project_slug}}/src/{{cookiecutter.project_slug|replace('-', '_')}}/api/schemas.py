{%- if cookiecutter.api_framework == 'fastapi' -%}
"""Pydantic schemas for API request/response validation.

These DTOs (Data Transfer Objects) define the contract between the API
and its clients. They are separate from domain entities to allow the API
contract to evolve independently from business logic.
"""

from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CreateEntityRequest(BaseModel):
    """Request schema for creating an entity."""

    name: str
    description: str = ""


class UpdateEntityRequest(BaseModel):
    """Request schema for updating an entity."""

    name: str | None = None
    description: str | None = None


class EntityResponse(BaseModel):
    """Response schema for entity data."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    description: str


class EntityListResponse(BaseModel):
    """Response schema for a list of entities."""

    items: list[EntityResponse]
    total: int


class HealthResponse(BaseModel):
    """Health check response."""

    status: str
    app_name: str
    database: str | None


class ErrorResponse(BaseModel):
    """Standard error response."""

    detail: str
    code: str | None = None
{%- else -%}
"""API schemas - Not enabled.

This project was generated without an API framework.
To enable Pydantic schemas, regenerate with api_framework='fastapi'.
"""
{%- endif %}
