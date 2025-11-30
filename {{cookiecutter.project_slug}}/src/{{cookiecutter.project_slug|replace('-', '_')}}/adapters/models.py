{%- if cookiecutter.database_backend in ['sqlite', 'postgresql'] -%}
"""SQLAlchemy ORM models - Database table definitions.

ORM models map domain entities to database tables. They are separate from
domain entities to maintain clean architecture boundaries.
"""

from __future__ import annotations
{%- if cookiecutter.database_backend == 'postgresql' %}

from pgvector.sqlalchemy import Vector
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
{%- else %}

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
{%- endif %}

from ..infrastructure.database import Base

{%- if cookiecutter.database_backend == 'postgresql' %}

# Default embedding dimension (adjust based on your model)
# Common sizes: 384 (MiniLM), 768 (BERT), 1536 (OpenAI), 3072 (Cohere)
EMBEDDING_DIM = 384
{%- endif %}


class ExampleEntityModel(Base):
    """SQLAlchemy model for ExampleEntity persistence.

    Maps to the 'example_entities' database table.
    """

    __tablename__ = "example_entities"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
{%- if cookiecutter.database_backend == 'postgresql' %}

    # Vector embedding for similarity search (optional)
    # Use with: SELECT * FROM example_entities ORDER BY embedding <-> :query_vector LIMIT 10
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
