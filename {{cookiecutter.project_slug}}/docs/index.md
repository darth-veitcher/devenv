# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Overview

{{ cookiecutter.project_name }} is a Python application built with a clean 3-layer architecture:

- **Domain Layer** - Core business logic and entities
- **Adapters Layer** - Interface implementations (repositories, external services)
- **Services Layer** - Application orchestration and use cases

## Features

- **REST API** - FastAPI-powered HTTP endpoints
- **CLI** - Typer-based command-line interface
- **Modern Python** - Python {{ cookiecutter.python_version }}+ with type hints
- **Well Tested** - Comprehensive test suite with pytest

## Quick Start

```bash
# Install dependencies
uv sync

# Run the CLI
uv run {{ cookiecutter.project_slug|replace('-', '_') }} --help

# Start the API server
uv run {{ cookiecutter.project_slug|replace('-', '_') }} serve

# Run tests
uv run pytest
```

## Installation

=== "Using uv (recommended)"

    ```bash
    uv sync --all-extras
    ```

=== "Using pip"

    ```bash
    pip install -e ".[dev]"
    ```

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── src/
│   └── {{ cookiecutter.project_slug|replace('-', '_') }}/
│       ├── domain/          # Core business entities
│       ├── adapters/        # Repository implementations
│       ├── services/        # Business logic orchestration
│       ├── api/             # FastAPI REST endpoints
│       ├── cli/             # Typer CLI commands
│       └── infrastructure/  # Configuration, logging
├── tests/
│   ├── unit/               # Unit tests
│   └── integration/        # Integration tests
├── docs/                   # Documentation (you are here)
└── project-management/     # BEACON framework artifacts
```

## Documentation

- [Getting Started](getting-started/installation.md) - Installation and setup
- [Architecture](architecture/overview.md) - System design and patterns
- [API Reference](reference/index.md) - Auto-generated code documentation
- [Development](development/contributing.md) - Contributing guidelines

## License

This project is licensed under the MIT License.
