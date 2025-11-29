# Architecture Document: devenv Cookiecutter Template

## Overview

devenv is a Cookiecutter template that generates production-ready Python projects with containerized development environments, AI assistance, and BEACON framework scaffolding.

## System Components

### Template Architecture

```
devenv/                              # Cookiecutter template repository
├── {{cookiecutter.project_slug}}/   # Generated project template
│   ├── src/                         # Python package (3-layer architecture)
│   ├── tests/                       # Pytest test suite
│   ├── docs/                        # MkDocs documentation
│   ├── .devcontainer/               # VS Code Dev Container
│   ├── .claude/                     # Claude AI configuration
│   └── project-management/          # BEACON framework
├── hooks/                           # Cookiecutter hooks
├── docs/                            # Template documentation
└── cookiecutter.json                # Template variables
```

### Generated Project Architecture

```
my-project/
├── src/my_project/          # Python Package
│   ├── domain/              # Semantic Layer - Business entities
│   │   └── entities.py      # Domain models with validation
│   ├── adapters/            # Kinetic Layer - External interfaces
│   │   └── repositories/    # Data access implementations
│   ├── services/            # Dynamic Layer - Business logic
│   │   └── __init__.py      # Service orchestration
│   ├── api/                 # REST API (FastAPI)
│   │   └── main.py          # Endpoints
│   ├── cli/                 # CLI (Typer)
│   │   └── main.py          # Commands
│   └── infrastructure/      # Cross-cutting concerns
│       └── config.py        # Configuration management
├── tests/                   # Test Suite
│   ├── unit/                # Unit tests by layer
│   └── integration/         # API and integration tests
├── docs/                    # MkDocs Documentation
├── .devcontainer/           # Dev Container Configuration
│   ├── compose.yml          # Development services
│   ├── compose-mcp.yml      # MCP servers
│   └── devcontainer.json    # VS Code settings
├── .claude/                 # Claude AI Configuration
│   ├── agents/              # Specialized agents
│   └── reference/           # Architecture guidance
└── project-management/      # BEACON Framework
    ├── ADRs/                # Architectural Decision Records
    ├── Background/          # Problem statement, context
    ├── Roadmap/             # Development plan
    └── Work/                # Transient workspace
```

## Technology Stack

| Layer | Technology | Rationale | ADR Reference |
|-------|------------|-----------|---------------|
| Package Manager | uv | Fast, modern Python tooling | ADR-001 |
| Architecture | 3-Layer | Clean separation of concerns | ADR-002 |
| Documentation | MkDocs + Material | Modern, searchable docs | ADR-003 |
| Development | Dev Containers | Reproducible environments | ADR-004 |
| Versioning | hatch-vcs | Git-based semantic versioning | ADR-001 |
| Linting | Ruff | Fast, comprehensive Python linting | ADR-001 |
| Testing | pytest | Industry standard, async support | ADR-001 |
| API Framework | FastAPI | Modern async Python API | - |
| CLI Framework | Typer | Type-safe CLI building | - |

## Three-Layer Architecture

### Semantic Layer (Domain)

**Purpose:** Define what the business world looks like
**Contents:** Entities, value objects, domain rules
**Dependencies:** None (pure Python)

```python
# domain/entities.py
@dataclass(frozen=True)
class ExampleEntity:
    id: str
    name: str
    created_at: datetime
```

### Kinetic Layer (Adapters)

**Purpose:** Connect domain to external systems
**Contents:** Repositories, API clients, file handlers
**Dependencies:** Domain layer only

```python
# adapters/repositories/__init__.py
class ExampleRepository(Protocol):
    async def save(self, entity: ExampleEntity) -> ExampleEntity: ...
    async def get_by_id(self, id: str) -> ExampleEntity | None: ...
```

### Dynamic Layer (Services)

**Purpose:** Orchestrate business operations
**Contents:** Use cases, workflows, business logic
**Dependencies:** Domain and Adapters

```python
# services/__init__.py
class ExampleService:
    def __init__(self, repository: ExampleRepository):
        self._repository = repository

    async def create(self, name: str) -> ExampleEntity: ...
```

## Development Environment

### MCP Servers (AI Assistance)

| Server | Purpose |
|--------|---------|
| Serena | Code-aware IDE assistant |
| Context7 | Documentation lookup |
| SearxNG | Private web search |
| Crawl4AI | AI-powered web crawling |
| Memgraph | Graph database |
| Sequential Thinking | Structured reasoning |

### Dev Container Services

| Service | Port | Purpose |
|---------|------|---------|
| App | 8000 | FastAPI application |
| PostgreSQL | 5432 | Database (internal) |
| Redis | 6379 | Caching (internal) |
| SearxNG | 8080 | Web search |
| Memgraph Lab | 3000 | Graph visualization |

## Key Design Decisions

1. **uv over pip/poetry** - See ADR-001
2. **3-layer architecture** - See ADR-002
3. **MkDocs over Sphinx** - See ADR-003
4. **Dev Containers over local setup** - See ADR-004

## Interface Contracts

### CLI Interface

```bash
just cli --help          # Show commands
just cli version         # Show version
just cli serve           # Start server
just cli create "name"   # Create entity
```

### REST API Interface

```
GET  /health             # Health check
GET  /                   # Root endpoint
POST /entities           # Create entity
GET  /entities/{id}      # Get entity
DELETE /entities/{id}    # Delete entity
```

## Non-Functional Requirements

- **Performance:** API response < 100ms for simple operations
- **Security:** No secrets in code, environment-based configuration
- **Scalability:** Stateless design, horizontal scaling ready
- **Maintainability:** Type hints, comprehensive tests, auto-docs

---

_Created: 2025-11-29_
_Last Updated: 2025-11-29_
_Status: Living Document - Update when architecture evolves_
