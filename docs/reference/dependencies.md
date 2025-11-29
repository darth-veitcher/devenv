# Dependencies

Python packages included in generated projects.

## Core Dependencies

Installed by default in all projects.

| Package | Version | Purpose |
|---------|---------|---------|
| **pydantic** | >=2.9.0 | Data validation and settings |
| **pydantic-settings** | >=2.5.0 | Environment-based configuration |
| **fastapi** | >=0.115.0 | REST API framework |
| **uvicorn** | >=0.32.0 | ASGI server |
| **typer** | >=0.12.0 | CLI framework |
| **rich** | >=13.0.0 | Beautiful terminal output |
| **structlog** | >=24.4.0 | Structured logging |

## Development Dependencies

Installed with `uv sync --all-extras`.

### Testing

| Package | Version | Purpose |
|---------|---------|---------|
| **pytest** | >=8.3.0 | Test framework |
| **pytest-asyncio** | >=0.24.0 | Async test support |
| **pytest-cov** | >=5.0.0 | Coverage reporting |
| **httpx** | >=0.27.0 | HTTP client for API tests |

### Type Checking

| Package | Version | Purpose |
|---------|---------|---------|
| **mypy** | >=1.11.0 | Static type checker |

### Linting & Formatting

| Package | Version | Purpose |
|---------|---------|---------|
| **ruff** | >=0.6.0 | Linter and formatter |

### Security

| Package | Version | Purpose |
|---------|---------|---------|
| **bandit** | >=1.7.0 | Security scanner |

## Documentation Dependencies

Installed with `[docs]` extra.

| Package | Version | Purpose |
|---------|---------|---------|
| **mkdocs** | >=1.6.0 | Documentation generator |
| **mkdocstrings** | >=0.25.0 | Auto-generate from docstrings |
| **mkdocs-material** | >=9.5.0 | Material theme |

## Versioning

| Package | Version | Purpose |
|---------|---------|---------|
| **hatchling** | (build) | Build backend |
| **hatch-vcs** | (build) | Git-based versioning |

## pyproject.toml

```toml
[project]
dependencies = [
    "pydantic>=2.9.0",
    "pydantic-settings>=2.5.0",
    "fastapi>=0.115.0",
    "uvicorn[standard]>=0.32.0",
    "typer>=0.12.0",
    "rich>=13.0.0",
    "structlog>=24.4.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.3.0",
    "pytest-asyncio>=0.24.0",
    "pytest-cov>=5.0.0",
    "httpx>=0.27.0",
    "mypy>=1.11.0",
    "ruff>=0.6.0",
    "bandit>=1.7.0",
]

docs = [
    "mkdocs>=1.6.0",
    "mkdocstrings[python]>=0.25.0",
    "mkdocs-material>=9.5.0",
]
```

## Adding Dependencies

### Runtime Dependency

```bash
uv add requests
```

Or manually edit `pyproject.toml`:

```toml
dependencies = [
    # ... existing
    "requests>=2.31.0",
]
```

### Development Dependency

```bash
uv add --dev hypothesis
```

Or:

```toml
[project.optional-dependencies]
dev = [
    # ... existing
    "hypothesis>=6.0.0",
]
```

## Updating Dependencies

### Update All

```bash
uv sync --upgrade
```

### Update Specific Package

```bash
uv add package-name@latest
```

## Lock File

`uv.lock` contains exact versions for reproducibility.

- Committed to git
- Used for CI/CD
- Ensures consistent builds

## Version Constraints

| Syntax | Meaning |
|--------|---------|
| `>=2.0.0` | Minimum version |
| `>=2.0.0,<3.0.0` | Version range |
| `~=2.0.0` | Compatible release |
| `==2.0.0` | Exact version |

## Common Additions

### Database

```toml
"sqlalchemy>=2.0.0",
"asyncpg>=0.29.0",  # PostgreSQL
"aiosqlite>=0.20.0",  # SQLite
```

### Authentication

```toml
"python-jose[cryptography]>=3.3.0",
"passlib[bcrypt]>=1.7.4",
```

### Background Tasks

```toml
"celery>=5.3.0",
"redis>=5.0.0",
```

### HTTP Client

```toml
"httpx>=0.27.0",
"aiohttp>=3.9.0",
```
