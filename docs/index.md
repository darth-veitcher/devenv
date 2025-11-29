# devenv

A sophisticated containerized development environment template with Claude AI integration.

## What is devenv?

**devenv** is a [cookiecutter](https://cookiecutter.readthedocs.io/) template that generates production-ready Python projects with:

- **3-Layer Architecture** - Clean separation of domain, adapters, and services
- **Dual Interfaces** - REST API (FastAPI) and CLI (Typer) out of the box
- **Modern Python Tooling** - uv package manager, hatch-vcs versioning
- **VS Code Dev Containers** - Fully containerized development environment
- **Claude AI Integration** - Pre-configured agents and MCP servers
- **BEACON Framework** - Pragmatic, artifact-driven development methodology

## Quick Start

```bash
# Install cookiecutter
pip install cookiecutter

# Generate a new project
cookiecutter gh:darth-veitcher/devenv

# Follow the prompts...
```

That's it! You'll have a fully configured Python project ready for development.

## What You Get

When you generate a project, you receive:

```
my-project/
├── src/my_project/          # 3-layer Python package
│   ├── domain/              # Business entities
│   ├── adapters/            # Repository implementations
│   ├── services/            # Application logic
│   ├── api/                 # FastAPI REST API
│   └── cli/                 # Typer CLI
├── tests/                   # pytest test suite
├── docs/                    # MkDocs documentation
├── .devcontainer/           # VS Code Dev Container
├── .claude/                 # Claude AI agent configs
├── project-management/      # BEACON framework artifacts
├── justfile                 # Development commands
├── pyproject.toml           # Modern Python packaging
└── docker-compose.yml       # Container orchestration
```

## Features at a Glance

| Feature | Description |
|---------|-------------|
| **Python {{ python_version }}+** | Modern Python with type hints |
| **uv** | Fast, reliable package management |
| **FastAPI** | High-performance REST API |
| **Typer** | Beautiful CLI applications |
| **pytest** | Comprehensive testing |
| **MkDocs** | Auto-generated documentation |
| **Docker** | Containerized everything |
| **Claude AI** | AI pair programming ready |

## Why devenv?

### For Solo Developers

- Start coding immediately, not configuring
- Best practices baked in from day one
- AI assistance pre-configured

### For Teams

- Consistent project structure across all projects
- Shared development environment via containers
- Documentation generated automatically

### For Learning

- See how modern Python projects are structured
- Learn clean architecture patterns
- Understand professional tooling

## Next Steps

<div class="grid cards" markdown>

-   :material-download:{ .lg .middle } **Getting Started**

    ---

    Install prerequisites and create your first project

    [:octicons-arrow-right-24: Prerequisites](getting-started/prerequisites.md)

-   :material-folder-open:{ .lg .middle } **Features**

    ---

    Explore what's included in generated projects

    [:octicons-arrow-right-24: Python Scaffold](features/python-scaffold.md)

-   :material-cog:{ .lg .middle } **Configuration**

    ---

    Customize the template to your needs

    [:octicons-arrow-right-24: Options](configuration/cookiecutter-options.md)

-   :material-file-tree:{ .lg .middle } **Reference**

    ---

    Detailed documentation of generated files

    [:octicons-arrow-right-24: Directory Structure](reference/directory-structure.md)

</div>

## License

MIT License - Use freely in your projects.
