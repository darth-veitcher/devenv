{%- if cookiecutter.database_backend in ['sqlite', 'postgresql'] -%}
"""SQLAlchemy ORM models - Database table definitions.

ORM models map domain entities to database tables. They are separate from
domain entities to maintain clean architecture boundaries.
"""

from __future__ import annotations

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from ..infrastructure.database import Base


class ExampleEntityModel(Base):
    """SQLAlchemy model for ExampleEntity persistence.

    Maps to the 'example_entities' database table.
    """

    __tablename__ = "example_entities"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
{%- else -%}
"""ORM models - Not enabled.

This project was generated without a database backend.
To enable SQLAlchemy models, regenerate with database_backend='sqlite' or 'postgresql'.
"""
{%- endif %}
