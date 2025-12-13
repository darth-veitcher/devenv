{%- if cookiecutter.database_backend in ['sqlite', 'postgresql'] -%}
# Database Migrations

This directory contains Alembic database migrations for {{ cookiecutter.project_name }}.

## Quick Start

```bash
# Apply all pending migrations
just migrate

# Create a new migration (auto-detect changes)
just migrate-create "description of changes"

# Downgrade one version
just migrate-down

# Show current version
just migrate-status
```

## Manual Commands

If you prefer using Alembic directly:

```bash
# Apply all migrations
uv run alembic upgrade head

# Create auto-generated migration
uv run alembic revision --autogenerate -m "description"

# Create empty migration
uv run alembic revision -m "description"

# Downgrade one version
uv run alembic downgrade -1

# Show current version
uv run alembic current

# Show migration history
uv run alembic history
```

## Directory Structure

```
migrations/
├── env.py              # Alembic environment configuration
├── script.py.mako      # Template for new migrations
├── README.md           # This file
└── versions/           # Migration scripts
    └── *.py            # Individual migrations
```

## Best Practices

1. **Always review auto-generated migrations** before applying
2. **Test migrations both up and down** in development
3. **Keep migrations small and focused** - one logical change per migration
4. **Never modify migrations** that have been applied to production
5. **Include both upgrade() and downgrade()** functions

## Environment Variables

Migrations use `DATABASE_URL` from environment:

```bash
{%- if cookiecutter.database_backend == 'sqlite' %}
# SQLite (default for development)
export DATABASE_URL="sqlite+aiosqlite:///./data/app.db"
{%- elif cookiecutter.database_backend == 'postgresql' %}
# PostgreSQL
export DATABASE_URL="postgresql+asyncpg://user:pass@localhost:5432/dbname"
{%- endif %}
```

## Troubleshooting

### "Target database is not up to date"

Run `just migrate` to apply pending migrations.

### "Can't locate revision"

The database may have been created with a different migration history.
Try `uv run alembic stamp head` to mark current state as up-to-date.

### "No changes detected"

Alembic couldn't detect schema changes. Either:
- Your models match the database schema
- You need to import models in `env.py`
{%- else -%}
# Database Migrations - Not Enabled

This project was generated without a database backend.
Regenerate with `database_backend='sqlite'` or `'postgresql'` to enable migrations.
{%- endif %}
