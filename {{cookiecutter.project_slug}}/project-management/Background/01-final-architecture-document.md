# Architecture Document

## Overview

{{ cookiecutter.project_name }} follows a **three-layer architecture** for clean separation of concerns.

## System Components

### Package Structure

```
src/{{ cookiecutter.project_slug | replace('-', '_') }}/
├── domain/           # Semantic Layer - Business entities
│   └── entities.py   # Domain models with validation
├── adapters/         # Kinetic Layer - External interfaces
│   └── repositories/ # Data access implementations
├── services/         # Dynamic Layer - Business logic
│   └── __init__.py   # Service orchestration
├── api/              # REST API (FastAPI)
│   └── main.py       # Endpoints
├── cli/              # CLI (Typer)
│   └── main.py       # Commands
└── infrastructure/   # Cross-cutting concerns
    └── config.py     # Configuration management
```

## Technology Stack

| Layer | Technology | Rationale | ADR Reference |
|-------|------------|-----------|---------------|
| Package Manager | uv | Fast, modern Python tooling | - |
| Architecture | 3-Layer | Clean separation of concerns | - |
| API Framework | FastAPI | Modern async Python API | - |
| CLI Framework | Typer | Type-safe CLI building | - |
| Testing | pytest | Industry standard, async support | - |
| Linting | Ruff | Fast, comprehensive | - |

## Three-Layer Architecture

### Domain Layer (Semantic)

**Purpose:** Define business entities and rules
**Location:** `src/{{ cookiecutter.project_slug | replace('-', '_') }}/domain/`
**Dependencies:** None (pure Python)

### Adapters Layer (Kinetic)

**Purpose:** Connect domain to external systems
**Location:** `src/{{ cookiecutter.project_slug | replace('-', '_') }}/adapters/`
**Dependencies:** Domain layer only

### Services Layer (Dynamic)

**Purpose:** Orchestrate business operations
**Location:** `src/{{ cookiecutter.project_slug | replace('-', '_') }}/services/`
**Dependencies:** Domain and Adapters

## Interface Contracts

### CLI Interface

```bash
just cli --help          # Show commands
just cli version         # Show version
just cli serve           # Start server
```

### REST API Interface

```
GET  /health             # Health check
GET  /                   # Root endpoint
POST /entities           # Create entity
GET  /entities/{id}      # Get entity
DELETE /entities/{id}    # Delete entity
```

## Key Architectural Decisions

Document major decisions in `project-management/ADRs/`:

1. **[Decision Name]** - See ADR-001
2. **[Decision Name]** - See ADR-002

## Non-Functional Requirements

- **Performance:** [Define targets]
- **Security:** [Define requirements]
- **Scalability:** [Define approach]

---

_Created: [Date]_
_Last Updated: [Date]_
_Status: Living Document - Update when architecture evolves_
