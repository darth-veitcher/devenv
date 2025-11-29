# ADR-004: Docker-Based Dev Containers

## Status

Accepted

## Context

Development environment consistency is crucial for:
- Eliminating "works on my machine" issues
- Onboarding new developers quickly
- Providing pre-configured tooling and services
- Isolating project dependencies from host system

Options considered:

- **Local setup**: Simple but inconsistent across machines
- **Vagrant**: Heavy, slow to start
- **Docker Compose only**: Good for services, not full dev environment
- **VS Code Dev Containers**: Full IDE integration, Docker-based

## Decision

Use **VS Code Dev Containers** for development environments.

Structure:
```
.devcontainer/
├── devcontainer.json    # VS Code configuration
├── Dockerfile           # Dev container image
├── compose.yml          # Development services
├── compose-mcp.yml      # MCP server services
└── mcp/                 # MCP server configs
    ├── searxng/
    ├── context7/
    └── crawl4ai/
```

Key features:
- Automatic environment setup on "Reopen in Container"
- Pre-installed tools (uv, just, git)
- Pre-configured extensions
- Integrated services (PostgreSQL, Redis, MCP servers)

## Consequences

### Positive

- Zero setup for developers (just open in VS Code)
- Consistent environment across all machines
- Services pre-configured and running
- Host machine stays clean
- Easy to add new services

### Negative

- Requires Docker Desktop
- Resource overhead (RAM, disk)
- Initial container build takes time
- Some developers prefer local setup

### Neutral

- VS Code required (but alternatives like Cursor work too)
- Network isolation may complicate some debugging
- Learning curve for Docker concepts

## Escape Hatch

For developers who prefer local setup:
1. pyproject.toml works with local uv/pip
2. justfile commands work locally
3. Services can be run via docker-compose alone
4. Dev container is optional, not required

Migration path:
```bash
# Skip dev container, use local environment
uv sync --all-extras
just dev
```

---

_Created: 2025-11-29_
_Last Updated: 2025-11-29_
