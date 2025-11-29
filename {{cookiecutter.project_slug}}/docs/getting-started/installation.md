# Installation

This guide covers how to install and set up {{ cookiecutter.project_name }}.

## Prerequisites

Before you begin, ensure you have the following installed:

| Tool | Version | Purpose |
|------|---------|---------|
| Python | {{ cookiecutter.python_version }}+ | Runtime |
| uv | Latest | Package management |
| Git | Latest | Version control |

### Installing uv

=== "macOS/Linux"

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== "Windows"

    ```powershell
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

=== "pipx"

    ```bash
    pipx install uv
    ```

## Installation Methods

### Development Installation

Clone the repository and install in development mode:

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}

# Install all dependencies including dev tools
uv sync --all-extras
```

### Production Installation

For production use without dev dependencies:

```bash
uv sync
```

### Global CLI Installation

To install the CLI tool globally:

```bash
uv tool install .
```

This makes the `{{ cookiecutter.project_slug|replace('-', '_') }}` command available system-wide.

## Verify Installation

After installation, verify everything is working:

```bash
# Check CLI is available
uv run {{ cookiecutter.project_slug|replace('-', '_') }} --help

# Check version
uv run {{ cookiecutter.project_slug|replace('-', '_') }} version

# Run tests
uv run pytest
```

## Docker Installation

If you prefer using Docker:

```bash
# Build the image
docker build -t {{ cookiecutter.project_slug }} .

# Run the container
docker run -p 8000:8000 {{ cookiecutter.project_slug }}
```

Or using Docker Compose:

```bash
docker compose up -d
```

## Next Steps

- [Quickstart Guide](quickstart.md) - Get up and running quickly
- [Configuration](configuration.md) - Configure the application
