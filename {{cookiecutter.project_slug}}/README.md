# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Quick Start

```bash
# Install dependencies
just install

# Run tests
just test

# Start development server
just dev

# Run CLI
just cli --help
```

## Architecture

This project follows a **three-layer architecture** inspired by Palantir's ontology patterns:

```
src/{{ cookiecutter.project_slug|replace('-', '_') }}/
├── domain/           # Semantic Layer - "What the world is"
│   ├── entities.py   # Domain entities with business rules
│   └── ...
├── adapters/         # Kinetic Layer - "Connecting to reality"
│   └── repositories/ # Data access implementations
├── services/         # Dynamic Layer - "Making it come alive"
│   └── __init__.py   # Business logic services
├── api/              # REST API presentation (FastAPI)
│   └── main.py
├── cli/              # CLI presentation (Typer)
│   └── main.py
└── infrastructure/   # Cross-cutting concerns
    └── config.py     # Configuration management
```

### Layers

| Layer | Purpose | Location |
|-------|---------|----------|
| **Domain** | Pure business entities and rules | `domain/` |
| **Adapters** | External system integrations | `adapters/` |
| **Services** | Business logic orchestration | `services/` |
| **API** | REST endpoints | `api/` |
| **CLI** | Command-line interface | `cli/` |

## Development

### Prerequisites

- Python {{ cookiecutter.python_version }}+
- [uv](https://docs.astral.sh/uv/) package manager
- [just](https://github.com/casey/just) command runner
- Docker (for containerized services)

### Common Commands

```bash
just --list          # Show all available commands

# Development
just install         # Install all dependencies
just dev             # Start dev server with hot reload
just serve           # Start production server
just cli <command>   # Run CLI commands

# Code Quality
just check           # Run all checks (lint, typecheck, test)
just lint            # Run linter
just lint-fix        # Fix linting issues
just format          # Format code
just typecheck       # Run mypy

# Testing
just test            # Run all tests
just test-cov        # Run tests with coverage
just test-unit       # Run unit tests only
just test-integration # Run integration tests only

# Build
just build           # Build the package
just clean           # Clean build artifacts

# Docker
just up              # Start all services
just down            # Stop all services
just docker-build    # Build Docker image
```

### Project Structure

```
{{ cookiecutter.project_slug }}/
├── src/{{ cookiecutter.project_slug|replace('-', '_') }}/  # Python package
├── tests/                   # Test suite
│   ├── unit/               # Unit tests
│   └── integration/        # Integration tests
├── project-management/      # BEACON framework
│   ├── ADRs/               # Architecture decisions
│   ├── Background/         # Problem statement & requirements
│   ├── Roadmap/            # Development roadmap
│   └── Work/               # Transient work files
├── .claude/                 # Claude agent configurations
│   ├── agents/             # Specialized agents
│   └── reference/          # Architecture guidance
├── .devcontainer/          # VS Code Dev Container
├── pyproject.toml          # Project configuration
├── justfile                # Development commands
├── Dockerfile              # Container image
└── docker-compose.yml      # Services orchestration
```

## Testing

Tests are organized by layer:

```bash
tests/
├── unit/
│   ├── domain/         # Entity and business rule tests
│   └── services/       # Service layer tests
└── integration/        # API and end-to-end tests
```

Run tests:

```bash
just test              # All tests
just test-unit         # Fast unit tests
just test-integration  # API tests
just test-cov          # With coverage report
```

## Documentation

Full project documentation is available via MkDocs:

```bash
just docs-serve      # Serve docs locally at http://localhost:8000
just docs-build      # Build static site to site/
just docs-deploy     # Deploy to GitHub Pages
```

### API Documentation

When the server is running, interactive API docs are available at:

- **Swagger UI**: http://localhost:{{ cookiecutter.app_port }}/docs
- **ReDoc**: http://localhost:{{ cookiecutter.app_port }}/redoc
- **OpenAPI JSON**: http://localhost:{{ cookiecutter.app_port }}/openapi.json

## CLI Usage

```bash
# Show version
just cli version

# Show configuration
just cli config

# Create an entity
just cli create "My Entity" --description "Description"

# Start the server via CLI
just cli serve --port 8000
```

## Configuration

Configuration is managed via environment variables and `.env` files:

| Variable | Description | Default |
|----------|-------------|---------|
| `DEBUG` | Enable debug mode | `false` |
| `LOG_LEVEL` | Logging level | `INFO` |
| `DATABASE_URL` | Database connection string | - |
| `HOST` | Server host | `0.0.0.0` |
| `PORT` | Server port | `{{ cookiecutter.app_port }}` |

## Docker

### Build and Run

```bash
just docker-build    # Build image
just docker-run      # Run container

# Or use docker-compose
just up              # Start all services
just down            # Stop all services
just logs            # View logs
```

### Services

| Service | Port | Description |
|---------|------|-------------|
| app | {{ cookiecutter.app_port }} | Application API |
| postgres | 5432 (internal) | PostgreSQL database |

## Development Environment

This project includes a **VS Code Dev Container** configuration:

1. Open in VS Code
2. Click "Reopen in Container" when prompted
3. All dependencies and tools are pre-configured

### Available MCP Services

{% if cookiecutter.enable_mcp_services == 'yes' %}
| Service | Purpose |
|---------|---------|
{% if cookiecutter.enable_searxng == 'yes' %}| SearxNG | Private web search |
{% endif %}{% if cookiecutter.enable_crawl4ai == 'yes' %}| Crawl4AI | AI-powered web crawling |
{% endif %}{% if cookiecutter.enable_context7 == 'yes' %}| Context7 | Documentation lookup |
{% endif %}| Serena | Code-aware IDE assistant |
| Sequential Thinking | Structured reasoning |
{% endif %}

## BEACON Framework

This project follows the **BEACON methodology** for development:

- **Tracer Bullets**: Build end-to-end features incrementally
- **Project Management**: Track progress in `project-management/Roadmap/`
- **ADRs**: Document decisions in `project-management/ADRs/`
- **Sessions**: Track work in `project-management/Work/sessions/`

See `project-management/Roadmap/README.md` for current status.

## Contributing

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Make changes following the three-layer architecture
3. Run checks: `just check`
4. Commit with clear messages
5. Push and create a pull request

## License

MIT License - See LICENSE file for details.

---

Generated with [devenv](https://github.com/{{ cookiecutter.github_username }}/devenv) cookiecutter template.
