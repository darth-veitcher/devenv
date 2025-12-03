{%- if cookiecutter.api_framework == 'fastapi' -%}
"""Pydantic schemas for API request/response validation.

These DTOs (Data Transfer Objects) define the contract between the API
and its clients. They are separate from domain entities to allow the API
contract to evolve independently from business logic.
"""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr


class CreateUserRequest(BaseModel):
    """Request schema for creating a user."""

    username: str
    email: EmailStr
    display_name: str = ""


class UpdateUserRequest(BaseModel):
    """Request schema for updating a user."""

    display_name: str | None = None


class UserResponse(BaseModel):
    """Response schema for user data."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    username: str
    email: str
    display_name: str
    created_at: datetime


class UserListResponse(BaseModel):
    """Response schema for a list of users."""

    items: list[UserResponse]
    total: int
{%- if cookiecutter.cache_backend == 'falkordb' %}


class FollowRequest(BaseModel):
    """Request schema for follow/unfollow operations."""

    target_user_id: UUID
{%- endif %}


class HealthResponse(BaseModel):
    """Health check response."""

    status: str
    app_name: str
    database: str | None
{%- if cookiecutter.cache_backend in ['redis', 'falkordb'] %}
    cache: str | None
{%- endif %}


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
