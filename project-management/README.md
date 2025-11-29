# Project Management: devenv Cookiecutter Template

This folder contains all project management documentation for the devenv cookiecutter template, following the BEACON Framework methodology.

## Structure

```
project-management/
├── ADRs/                    # Architectural Decision Records
│   ├── ADR-001-use-uv-package-manager.md
│   ├── ADR-002-three-layer-architecture.md
│   ├── ADR-003-mkdocs-documentation.md
│   └── ADR-004-dev-containers.md
│
├── Background/              # Product Requirements & Context
│   ├── 00-problem-statement.md      # Why we're building this
│   ├── 01-final-architecture-document.md  # How it's architected
│   └── archive/             # Historical planning documents
│
├── Roadmap/                 # Development Plan
│   ├── README.md            # Current roadmap and status
│   └── archive/             # Completed roadmaps
│
└── Work/                    # Transient Workspace
    ├── sessions/            # Session notes (delete after merge)
    ├── planning/            # Feature planning (delete after implementation)
    └── analysis/            # Code analysis (delete after ADR created)
```

## Quick Reference

| Task | Location |
|------|----------|
| Document a major decision | `ADRs/ADR-###-name.md` |
| Understand the problem | `Background/00-problem-statement.md` |
| See the architecture | `Background/01-final-architecture-document.md` |
| Check current progress | `Roadmap/README.md` |
| Plan a new feature | `Work/planning/feature-name.md` |

## Key Documents

### Background (Permanent)

- **[Problem Statement](Background/00-problem-statement.md)** - Why devenv exists and what problem it solves
- **[Architecture Document](Background/01-final-architecture-document.md)** - How the template and generated projects are structured

### ADRs (Permanent)

- **[ADR-001: uv Package Manager](ADRs/ADR-001-use-uv-package-manager.md)** - Why we use uv over pip/poetry
- **[ADR-002: Three-Layer Architecture](ADRs/ADR-002-three-layer-architecture.md)** - Domain/Adapters/Services pattern
- **[ADR-003: MkDocs Documentation](ADRs/ADR-003-mkdocs-documentation.md)** - Why MkDocs over Sphinx
- **[ADR-004: Dev Containers](ADRs/ADR-004-dev-containers.md)** - Docker-based development environments

### Roadmap (Living)

- **[Current Roadmap](Roadmap/README.md)** - Active milestones and tracer bullets

## Historical Context

The `Background/archive/` directory contains original planning documents from before the BEACON framework was adopted. These include:

- Original PRD and implementation plans
- Agent implementation guides
- MCP server analysis
- Various "Solo Dev" vision documents

These are preserved for historical reference but are superseded by the current BEACON-structured documents.

## BEACON Framework

This project follows the BEACON methodology:

- **B**uild working software daily
- **E**valuate ideas before building
- **A**rchitect with reversibility
- **C**ode in tracer bullets
- **O**perate with simplicity
- **N**avigate with clear documentation

See `CLAUDE.md` in the project root for full framework details.
