# Configuration

{{ cookiecutter.project_name }} uses environment variables and Pydantic Settings for configuration.

## Environment Variables

All configuration can be set via environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_NAME` | `{{ cookiecutter.project_name }}` | Application name |
| `DEBUG` | `false` | Enable debug mode |
| `HOST` | `0.0.0.0` | Server bind host |
| `PORT` | `8000` | Server bind port |
| `DATABASE_URL` | `None` | Database connection string |
| `LOG_LEVEL` | `INFO` | Logging level |

## Configuration File

Create a `.env` file in the project root:

```ini
# .env
APP_NAME={{ cookiecutter.project_name }}
DEBUG=true
HOST=0.0.0.0
PORT=8000
DATABASE_URL=postgresql://user:pass@localhost:5432/db
LOG_LEVEL=DEBUG
```

!!! warning "Security"
    Never commit `.env` files to version control. The `.gitignore` excludes them by default.

## Settings Class

Configuration is managed by Pydantic Settings in `infrastructure/config.py`:

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings loaded from environment."""

    app_name: str = "{{ cookiecutter.project_name }}"
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000
    database_url: str | None = None
    log_level: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
```

## Accessing Configuration

### In Application Code

```python
from {{ cookiecutter.project_slug|replace('-', '_') }}.infrastructure.config import get_settings

settings = get_settings()
print(settings.app_name)
print(settings.database_url)
```

### In Tests

Override settings for testing:

```python
import pytest
from {{ cookiecutter.project_slug|replace('-', '_') }}.infrastructure.config import Settings

@pytest.fixture
def test_settings():
    return Settings(
        app_name="test-app",
        debug=True,
        database_url="sqlite:///:memory:"
    )
```

## Environment-Specific Configuration

### Development

```bash
# .env.development
DEBUG=true
LOG_LEVEL=DEBUG
DATABASE_URL=sqlite:///dev.db
```

### Production

```bash
# Set via environment or secrets manager
export DEBUG=false
export LOG_LEVEL=WARNING
export DATABASE_URL=postgresql://...
```

### Docker

Environment variables in `docker-compose.yml`:

```yaml
services:
  app:
    environment:
      - DEBUG=false
      - DATABASE_URL=postgresql://db:5432/app
```

## Validation

Pydantic validates all configuration at startup:

```python
# This will fail if DATABASE_URL is invalid
settings = Settings(database_url="not-a-url")
# ValidationError: 1 validation error for Settings
```

## Next Steps

- [Architecture Overview](../architecture/overview.md) - Understand the system design
- [API Reference](../reference/infrastructure.md) - Configuration API details
