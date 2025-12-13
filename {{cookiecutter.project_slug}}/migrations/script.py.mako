{%- if cookiecutter.database_backend in ['sqlite', 'postgresql'] -%}
<%!
"""Alembic migration script template.

This Mako template is used to generate new migration scripts when running
'alembic revision' or 'alembic revision --autogenerate'.
"""
%>"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}
"""

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# Revision identifiers, used by Alembic.
revision: str = ${repr(up_revision)}
down_revision: str | None = ${repr(down_revision)}
branch_labels: str | Sequence[str] | None = ${repr(branch_labels)}
depends_on: str | Sequence[str] | None = ${repr(depends_on)}


def upgrade() -> None:
    """Apply migration."""
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    """Reverse migration."""
    ${downgrades if downgrades else "pass"}
{%- else -%}
# Migrations not configured - database backend is 'none'
{%- endif %}
