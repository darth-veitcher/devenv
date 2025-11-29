# devenv

A [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for creating sophisticated Python projects with containerized development environments and AI-powered development support.

> **[Full Documentation](https://jamesveitch.github.io/devenv/)** | **[Quick Start](#quick-start)** | **[Features](#features)**

## Features

- **Modern Python Stack**: 3-layer architecture (domain/adapters/services), src-layout, type hints
- **Zero Config Tooling**: uv package manager, hatch-vcs versioning, ruff linting
- **Complete Dev Environment**: VS Code Dev Containers with Docker isolation
- **AI-Powered Development**: Claude AI integration with MCP servers
- **Documentation Ready**: MkDocs with Material theme, auto-generated API docs
- **BEACON Framework**: Project management artifacts for structured development

## Quick Start

### Prerequisites

- Python 3.12+ (or [uv](https://docs.astral.sh/uv/))
- Docker Desktop
- VS Code with Dev Containers extension

### Generate a Project

```bash
# Install cookiecutter (if needed)
pip install cookiecutter

# Generate project
cookiecutter gh:JAMESVEITCH/devenv

# Or with uv
uvx cookiecutter gh:JAMESVEITCH/devenv
```

### Answer the Prompts

| Variable | Description | Default |
|----------|-------------|---------|
| `project_name` | Human-readable name | My Project |
| `project_slug` | Package name (auto-generated) | my_project |
| `project_description` | Short description | A Python project |
| `author_name` | Your name | Your Name |
| `author_email` | Your email | you@example.com |
| `github_username` | GitHub username | yourusername |
| `python_version` | Python version | 3.12 |
| `app_port` | Application port | 8000 |

### Start Developing

```bash
cd my-project
code .
# VS Code will prompt to "Reopen in Container" - click yes!

# Or without Dev Containers:
uv sync --all-extras
uv run pytest
```

## What You Get

```
my-project/
├── src/my_project/        # Python package (3-layer architecture)
│   ├── domain/            # Business entities and logic
│   ├── adapters/          # External interfaces (repositories)
│   ├── services/          # Application services
│   ├── api/               # FastAPI REST endpoints
│   └── cli/               # Typer CLI commands
├── tests/                 # pytest test suite
├── docs/                  # MkDocs documentation
├── .devcontainer/         # VS Code Dev Container config
├── .claude/               # Claude AI configuration
├── project-management/    # BEACON Framework artifacts
├── pyproject.toml         # Package config (uv, hatch-vcs)
├── justfile               # Development commands
└── Dockerfile             # Production container
```

## Common Commands

Generated projects include a `justfile` with useful commands:

```bash
just install          # Install all dependencies
just dev              # Start dev server with reload
just test             # Run tests
just check            # Run all quality checks
just docs-serve       # Serve documentation locally
just cli --help       # Run CLI commands
```

## Documentation

- **[Full Documentation](https://jamesveitch.github.io/devenv/)** - Complete guide
- **[Getting Started](https://jamesveitch.github.io/devenv/getting-started/quickstart/)** - Step-by-step setup
- **[Features](https://jamesveitch.github.io/devenv/features/python-scaffold/)** - What's included
- **[Configuration](https://jamesveitch.github.io/devenv/configuration/cookiecutter-options/)** - All options
- **[Reference](https://jamesveitch.github.io/devenv/reference/directory-structure/)** - Complete reference

## Development

To work on the template itself:

```bash
git clone https://github.com/JAMESVEITCH/devenv.git
cd devenv

# Build and serve documentation
just docs-serve

# Test template generation
just test
```

## Contributing

See [Contributing Guide](https://jamesveitch.github.io/devenv/contributing/) for details.

## License

MIT License - see [LICENSE](LICENSE) for details.
