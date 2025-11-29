# CLI Reference

{{ cookiecutter.project_name }} includes a command-line interface built with Typer.

## Overview

The CLI provides the same functionality as the REST API but from your terminal.

```bash
uv run {{ cookiecutter.project_slug|replace('-', '_') }} --help
```

## Commands

### version

Show version information.

```bash
uv run {{ cookiecutter.project_slug|replace('-', '_') }} version
```

**Output:**

```
{{ cookiecutter.project_name }} v0.1.0
```

### config

Display current configuration.

```bash
uv run {{ cookiecutter.project_slug|replace('-', '_') }} config
```

**Output:**

```
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Setting     ┃ Value                          ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ App Name    │ {{ cookiecutter.project_name }}│
│ Debug       │ False                          │
│ Host        │ 0.0.0.0                        │
│ Port        │ 8000                           │
│ Database    │ Not configured                 │
└─────────────┴────────────────────────────────┘
```

### create

Create a new entity.

```bash
uv run {{ cookiecutter.project_slug|replace('-', '_') }} create NAME [OPTIONS]
```

**Arguments:**

| Argument | Required | Description |
|----------|----------|-------------|
| `NAME` | Yes | Entity name |

**Options:**

| Option | Short | Description |
|--------|-------|-------------|
| `--description` | `-d` | Entity description |

**Examples:**

```bash
# Create with name only
uv run {{ cookiecutter.project_slug|replace('-', '_') }} create "My Entity"

# Create with description
uv run {{ cookiecutter.project_slug|replace('-', '_') }} create "My Entity" -d "A detailed description"
```

**Output:**

```
Created entity: 550e8400-e29b-41d4-a716-446655440000
  Name: My Entity
  Description: A detailed description
```

### get

Retrieve an entity by ID.

```bash
uv run {{ cookiecutter.project_slug|replace('-', '_') }} get ENTITY_ID
```

**Arguments:**

| Argument | Required | Description |
|----------|----------|-------------|
| `ENTITY_ID` | Yes | Entity UUID |

**Example:**

```bash
uv run {{ cookiecutter.project_slug|replace('-', '_') }} get 550e8400-e29b-41d4-a716-446655440000
```

**Output:**

```
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Field       ┃ Value                                  ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ID          │ 550e8400-e29b-41d4-a716-446655440000   │
│ Name        │ My Entity                              │
│ Description │ A detailed description                 │
│ Created     │ 2024-01-15 10:30:00                   │
└─────────────┴────────────────────────────────────────┘
```

### serve

Start the API server.

```bash
uv run {{ cookiecutter.project_slug|replace('-', '_') }} serve [OPTIONS]
```

**Options:**

| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--host` | `-h` | `0.0.0.0` | Host to bind to |
| `--port` | `-p` | `8000` | Port to bind to |

**Examples:**

```bash
# Default settings
uv run {{ cookiecutter.project_slug|replace('-', '_') }} serve

# Custom port
uv run {{ cookiecutter.project_slug|replace('-', '_') }} serve -p 3000

# Custom host and port
uv run {{ cookiecutter.project_slug|replace('-', '_') }} serve -h 127.0.0.1 -p 8080
```

## Using Just

The justfile provides shortcuts:

```bash
# Run any CLI command
just cli --help
just cli version
just cli create "Test"

# Start server
just serve
just dev  # with auto-reload
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Error (invalid input, not found, etc.) |

## Environment Variables

The CLI respects the same environment variables as the API:

```bash
export APP_NAME="My App"
export DEBUG=true
uv run {{ cookiecutter.project_slug|replace('-', '_') }} config
```

## Shell Completion

Typer supports shell completion:

=== "Bash"

    ```bash
    {{ cookiecutter.project_slug|replace('-', '_') }} --install-completion bash
    ```

=== "Zsh"

    ```bash
    {{ cookiecutter.project_slug|replace('-', '_') }} --install-completion zsh
    ```

=== "Fish"

    ```bash
    {{ cookiecutter.project_slug|replace('-', '_') }} --install-completion fish
    ```

## Global Installation

Install the CLI globally:

```bash
uv tool install .
```

Then use without `uv run`:

```bash
{{ cookiecutter.project_slug|replace('-', '_') }} --help
{{ cookiecutter.project_slug|replace('-', '_') }} version
```

## Next Steps

- [REST API](rest.md) - HTTP API reference
- [API Reference](../reference/api.md) - Code documentation
