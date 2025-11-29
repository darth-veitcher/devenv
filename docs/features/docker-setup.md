# Docker Setup

Generated projects include comprehensive Docker configuration for development and production.

## Files Overview

| File | Purpose |
|------|---------|
| `Dockerfile` | Production-ready multi-stage build |
| `docker-compose.yml` | Service orchestration |
| `.devcontainer/compose.yml` | Dev container services |
| `.devcontainer/compose-mcp.yml` | MCP server services |

## Dockerfile

Multi-stage build optimized for size and security:

```dockerfile
# Build stage
FROM python:3.12-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev
COPY src/ src/

# Runtime stage
FROM python:3.12-slim AS runtime
RUN useradd --create-home --shell /bin/bash app
WORKDIR /app
COPY --from=builder --chown=app:app /app/.venv /app/.venv
COPY --from=builder --chown=app:app /app/src /app/src
USER app
ENV PATH="/app/.venv/bin:$PATH"
EXPOSE 8000
CMD ["python", "-m", "my_project.api.main"]
```

### Key Features

- **Multi-stage** - Small final image (~150MB vs ~1GB)
- **Non-root user** - Security best practice
- **uv for speed** - Fast dependency installation
- **Locked dependencies** - Reproducible builds

## Building Images

```bash
# Build production image
just docker-build
# or
docker build -t my-project:latest .

# Run container
just docker-run
# or
docker run -p 8000:8000 my-project:latest
```

## Docker Compose

### Production Services

`docker-compose.yml`:

```yaml
services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/app
    depends_on:
      - db

  db:
    image: postgres:16-alpine
    environment:
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=app
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### Commands

```bash
# Start all services
just up
# or
docker compose up -d

# View logs
just logs
# or
docker compose logs -f

# Stop services
just down
# or
docker compose down
```

## Dev Container Setup

### Main Container

`.devcontainer/compose.yml`:

```yaml
services:
  dev:
    build:
      context: ..
      dockerfile: .devcontainer/Dockerfile
    volumes:
      - ..:/workspace:cached
    command: sleep infinity
```

### MCP Services

`.devcontainer/compose-mcp.yml`:

```yaml
services:
  searxng:
    image: searxng/searxng:latest

  memgraph:
    image: memgraph/memgraph-platform

  # ... other MCP servers
```

## Environment Variables

### In docker-compose.yml

```yaml
services:
  app:
    environment:
      - DEBUG=false
      - DATABASE_URL=${DATABASE_URL}
```

### Using .env File

```bash
# .env
DATABASE_URL=postgresql://user:pass@db:5432/app
DEBUG=true
```

```yaml
services:
  app:
    env_file:
      - .env
```

## Networking

### Service Discovery

Services can reach each other by name:

```python
# From app container
DATABASE_URL = "postgresql://db:5432/app"  # 'db' is the service name
```

### Port Mapping

```yaml
ports:
  - "8000:8000"  # host:container
```

## Volumes

### Named Volumes

Persist data between container restarts:

```yaml
volumes:
  postgres_data:

services:
  db:
    volumes:
      - postgres_data:/var/lib/postgresql/data
```

### Bind Mounts

Mount local directories:

```yaml
services:
  dev:
    volumes:
      - ./src:/app/src  # Local changes reflected immediately
```

## Health Checks

```yaml
services:
  app:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
```

## Production Considerations

### Security

- Use secrets management, not environment variables for sensitive data
- Run as non-root user
- Keep base images updated

### Performance

- Use multi-stage builds
- Leverage build cache
- Consider Alpine-based images

### Scaling

```bash
docker compose up --scale app=3
```

## Next Steps

- [Dev Containers](../getting-started/dev-containers.md) - Full development environment
- [MCP Servers](mcp-servers.md) - AI integrations
