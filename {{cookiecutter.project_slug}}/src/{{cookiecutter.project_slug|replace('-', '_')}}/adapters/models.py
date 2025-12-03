{%- if cookiecutter.database_backend in ['sqlite', 'postgresql'] -%}
"""SQLAlchemy ORM models - Database table definitions.

ORM models map domain entities to database tables. They are separate from
domain entities to maintain clean architecture boundaries.
"""

from __future__ import annotations

from datetime import datetime
{%- if cookiecutter.database_backend == 'postgresql' %}

from pgvector.sqlalchemy import Vector
from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column
{%- else %}

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column
{%- endif %}

from ..infrastructure.database import Base

{%- if cookiecutter.database_backend == 'postgresql' %}

# Default embedding dimension (adjust based on your model)
# Common sizes: 384 (MiniLM), 768 (BERT), 1536 (OpenAI), 3072 (Cohere)
EMBEDDING_DIM = 384
{%- endif %}


class UserModel(Base):
    """SQLAlchemy model for User persistence.

    Maps to the 'users' database table. Works with both SQLite and PostgreSQL
    via the repository pattern.
    """

    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    display_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
{%- if cookiecutter.database_backend == 'postgresql' %}

    # Vector embedding for user profile similarity (optional)
    # Use with: SELECT * FROM users ORDER BY embedding <-> :query_vector LIMIT 10
    embedding: Mapped[list[float] | None] = mapped_column(
        Vector(EMBEDDING_DIM), nullable=True
    )
{%- endif %}
{%- else -%}
"""ORM models - Not enabled.

This project was generated without a database backend.
To enable SQLAlchemy models, regenerate with database_backend='sqlite' or 'postgresql'.
"""
{%- endif %}
