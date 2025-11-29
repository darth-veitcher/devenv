# Quickstart

Create your first project in under 5 minutes.

## Generate a Project

### From GitHub

```bash
cookiecutter gh:darth-veitcher/devenv
```

### From Local Clone

```bash
git clone https://github.com/darth-veitcher/devenv.git
cookiecutter devenv/
```

## Answer the Prompts

Cookiecutter will ask you a series of questions:

```
project_name [My Project]: My Awesome App
project_slug [my-awesome-app]:
project_description [A sophisticated multi-layer containerized development environment]: My app description
author_name [Your Name]: Jane Developer
author_email [your.email@example.com]: jane@example.com
github_username [yourusername]: janedeveloper
python_version [3.12]:
fastapi_version [0.115.0]:
uvicorn_version [0.32.0]:
app_port [8000]:
```

!!! tip "Defaults"
    Press Enter to accept defaults shown in brackets.

## What Gets Created

```
my-awesome-app/
├── .claude/                 # Claude AI configuration
│   ├── agents/             # AI agent prompts
│   └── reference/          # Architecture docs
├── .devcontainer/          # VS Code Dev Container
├── src/my_awesome_app/     # Your Python package
│   ├── domain/             # Business entities
│   ├── adapters/           # Repository implementations
│   ├── services/           # Application logic
│   ├── api/                # FastAPI REST API
│   └── cli/                # Typer CLI
├── tests/                  # Test suite
├── docs/                   # MkDocs documentation
├── project-management/     # BEACON framework
├── justfile                # Development commands
├── pyproject.toml          # Package configuration
└── docker-compose.yml      # Container setup
```

## Start Developing

### 1. Enter the Project

```bash
cd my-awesome-app
```

### 2. Install Dependencies

```bash
uv sync --all-extras
```

### 3. Run Tests

```bash
uv run pytest
```

You should see all 18 tests pass:

```
======================== 18 passed in 0.03s ========================
```

### 4. Start the API Server

```bash
uv run my_awesome_app serve
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for the API documentation.

### 5. Try the CLI

```bash
# Show help
uv run my_awesome_app --help

# Show version
uv run my_awesome_app version

# Create an entity
uv run my_awesome_app create "Hello World" -d "My first entity"
```

## Using justfile Commands

If you have `just` installed:

```bash
# Install dependencies
just install

# Run tests
just test

# Start development server with auto-reload
just dev

# Run linting and type checking
just check

# See all commands
just --list
```

## Using Dev Containers

For the full containerized experience:

1. Open the project in VS Code
2. Click "Reopen in Container" when prompted
3. Wait for the container to build
4. Start coding!

See [Dev Containers](dev-containers.md) for details.

## Next Steps

- [Dev Containers](dev-containers.md) - Full containerized development
- [Python Scaffold](../features/python-scaffold.md) - Understanding the architecture
- [Cookiecutter Options](../configuration/cookiecutter-options.md) - Customization options
