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

Create a new user.

```bash
uv run {{ cookiecutter.project_slug|replace('-', '_') }} create USERNAME EMAIL [OPTIONS]
```

**Arguments:**

| Argument | Required | Description |
|----------|----------|-------------|
| `USERNAME` | Yes | Unique username (min 3 characters) |
| `EMAIL` | Yes | Email address |

**Options:**

| Option | Short | Description |
|--------|-------|-------------|
| `--display-name` | `-n` | Display name |

**Examples:**

```bash
# Create with username and email
uv run {{ cookiecutter.project_slug|replace('-', '_') }} create alice alice@example.com

# Create with display name
uv run {{ cookiecutter.project_slug|replace('-', '_') }} create alice alice@example.com -n "Alice Smith"
```

**Output:**

```
Created user: 550e8400-e29b-41d4-a716-446655440000
  Username: alice
  Email: alice@example.com
  Display Name: Alice Smith
```

### get

Retrieve a user by ID.

```bash
uv run {{ cookiecutter.project_slug|replace('-', '_') }} get USER_ID
```

**Arguments:**

| Argument | Required | Description |
|----------|----------|-------------|
| `USER_ID` | Yes | User UUID |

**Example:**

```bash
uv run {{ cookiecutter.project_slug|replace('-', '_') }} get 550e8400-e29b-41d4-a716-446655440000
```

**Output:**

```
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Field         ┃ Value                                  ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ID            │ 550e8400-e29b-41d4-a716-446655440000   │
│ Username      │ alice                                  │
│ Email         │ alice@example.com                      │
│ Display Name  │ Alice Smith                            │
│ Created       │ 2024-01-15 10:30:00                    │
└───────────────┴────────────────────────────────────────┘
```

### list

List all users.

```bash
uv run {{ cookiecutter.project_slug|replace('-', '_') }} list
```

**Example:**

```bash
uv run {{ cookiecutter.project_slug|replace('-', '_') }} list
```

**Output:**

```
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ ID          ┃ Username   ┃ Email             ┃ Display Name ┃ Created    ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ 550e8400... │ alice      │ alice@example.com │ Alice Smith  │ 2024-01-15 │
│ 6ba7b810... │ bob        │ bob@example.com   │ -            │ 2024-01-16 │
└─────────────┴────────────┴───────────────────┴──────────────┴────────────┘
```

### delete

Delete a user by ID.

```bash
uv run {{ cookiecutter.project_slug|replace('-', '_') }} delete USER_ID [OPTIONS]
```

**Arguments:**

| Argument | Required | Description |
|----------|----------|-------------|
| `USER_ID` | Yes | User UUID to delete |

**Options:**

| Option | Short | Description |
|--------|-------|-------------|
| `--force` | `-f` | Skip confirmation prompt |

**Examples:**

```bash
# Delete with confirmation
uv run {{ cookiecutter.project_slug|replace('-', '_') }} delete 550e8400-e29b-41d4-a716-446655440000

# Delete without confirmation
uv run {{ cookiecutter.project_slug|replace('-', '_') }} delete 550e8400-e29b-41d4-a716-446655440000 -f
```

**Output:**

```
Deleted user: alice
```
{%- if cookiecutter.api_framework == 'fastapi' %}

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
{%- endif %}

## Using Just

The justfile provides shortcuts:

```bash
# Run any CLI command
just cli --help
just cli version
just cli create alice alice@example.com

# List all users
just cli list
{%- if cookiecutter.api_framework == 'fastapi' %}

# Start server
just serve
just dev  # with auto-reload
{%- endif %}
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
