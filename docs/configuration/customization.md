# Customization

How to modify and extend your generated project.

## After Generation

Generated projects are fully yours to modify. There's no "magic" - everything is standard Python.

## Common Customizations

### Change the Architecture

The 3-layer architecture is a starting point. You can:

**Add more layers:**

```
src/my_project/
├── domain/
├── adapters/
├── services/
├── api/
├── cli/
├── jobs/          # Add background jobs
└── integrations/  # Add external integrations
```

**Simplify for small projects:**

```
src/my_project/
├── models.py      # Combined domain
├── db.py          # Combined adapters
├── api.py         # Combined presentation
└── main.py
```

### Add a Database

1. Add dependencies to `pyproject.toml`:

```toml
dependencies = [
    # ... existing deps
    "sqlalchemy>=2.0.0",
    "asyncpg>=0.29.0",  # For PostgreSQL
]
```

2. Create a database adapter:

```python
# src/my_project/adapters/repositories/postgres.py
from sqlalchemy.ext.asyncio import AsyncSession

class PostgresExampleRepository(ExampleRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def save(self, entity: ExampleEntity) -> ExampleEntity:
        # ... implementation
```

3. Update dependency injection in `api/main.py`

### Add Authentication

1. Add dependencies:

```toml
dependencies = [
    # ... existing deps
    "python-jose[cryptography]>=3.3.0",
    "passlib[bcrypt]>=1.7.4",
]
```

2. Create auth module:

```python
# src/my_project/infrastructure/auth.py
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Verify token and return user
    ...
```

3. Add to routes:

```python
@app.get("/protected")
async def protected_route(user = Depends(get_current_user)):
    return {"user": user.email}
```

### Add Background Tasks

1. Add Celery or similar:

```toml
dependencies = [
    "celery>=5.3.0",
    "redis>=5.0.0",
]
```

2. Create tasks module:

```python
# src/my_project/jobs/tasks.py
from celery import Celery

app = Celery("my_project")

@app.task
def process_entity(entity_id: str):
    # ... background processing
```

### Customize the CLI

Add new commands to `cli/main.py`:

```python
@app.command()
def export(
    format: str = typer.Option("json", help="Export format"),
    output: Path = typer.Option("export.json", help="Output file"),
) -> None:
    """Export all entities."""
    entities = run_async(service.list_all())
    # ... export logic
```

### Add API Endpoints

Extend `api/main.py`:

```python
@app.get("/entities", response_model=list[EntityResponse])
async def list_entities(
    skip: int = 0,
    limit: int = 100,
    service: ExampleService = Depends(get_example_service),
) -> list[Any]:
    """List all entities with pagination."""
    return await service.list_all(skip=skip, limit=limit)
```

### Modify Documentation

Edit files in `docs/`:

- Add new pages
- Modify mkdocs.yml navigation
- Customize the theme

### Change the CI/CD

Add GitHub Actions workflow:

```yaml
# .github/workflows/ci.yml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v4
      - run: uv sync --all-extras
      - run: uv run pytest
```

## Removing Features

### Remove the CLI

1. Delete `src/my_project/cli/`
2. Remove from `pyproject.toml`:
   - `typer` and `rich` dependencies
   - `[project.scripts]` section
3. Delete CLI tests

### Remove the API

1. Delete `src/my_project/api/`
2. Remove from `pyproject.toml`:
   - `fastapi` and `uvicorn` dependencies
3. Delete API tests
4. Update Dockerfile if needed

### Simplify Dependencies

Edit `pyproject.toml` to remove unused packages.

## Keeping in Sync

If the template updates, you can manually apply changes:

1. Generate a fresh project with same options
2. Compare with your project
3. Cherry-pick desired changes

Or use [cruft](https://cruft.github.io/cruft/) for template updates.

## Next Steps

- [Directory Structure](../reference/directory-structure.md) - Full file listing
- [Dependencies](../reference/dependencies.md) - Package details
