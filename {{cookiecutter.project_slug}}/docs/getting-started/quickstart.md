# Quickstart

Get up and running with {{ cookiecutter.project_name }} in minutes.

## Your First Steps

### 1. Start the Development Server

Launch the API server in development mode with auto-reload:

```bash
just dev
```

Or without just:

```bash
uv run uvicorn {{ cookiecutter.project_slug|replace('-', '_') }}.api.main:app --reload
```

The API will be available at [http://localhost:8000](http://localhost:8000).

### 2. Explore the API

Open your browser to view the interactive API documentation:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### 3. Try the CLI

The CLI provides the same functionality as the API:

```bash
# Show available commands
uv run {{ cookiecutter.project_slug|replace('-', '_') }} --help

# Show configuration
uv run {{ cookiecutter.project_slug|replace('-', '_') }} config

# Create an entity
uv run {{ cookiecutter.project_slug|replace('-', '_') }} create "My Entity" --description "A test entity"
```

## Basic Usage

### Creating Entities

=== "CLI"

    ```bash
    uv run {{ cookiecutter.project_slug|replace('-', '_') }} create "Product A" -d "First product"
    ```

=== "API"

    ```bash
    curl -X POST http://localhost:8000/entities \
      -H "Content-Type: application/json" \
      -d '{"name": "Product A", "description": "First product"}'
    ```

=== "Python"

    ```python
    from {{ cookiecutter.project_slug|replace('-', '_') }}.services import ExampleService
    from {{ cookiecutter.project_slug|replace('-', '_') }}.adapters.repositories import InMemoryExampleRepository

    repo = InMemoryExampleRepository()
    service = ExampleService(repo)

    entity = await service.create("Product A", "First product")
    print(f"Created: {entity.id}")
    ```

### Retrieving Entities

=== "CLI"

    ```bash
    uv run {{ cookiecutter.project_slug|replace('-', '_') }} get <entity-uuid>
    ```

=== "API"

    ```bash
    curl http://localhost:8000/entities/<entity-uuid>
    ```

## Running Tests

Execute the test suite to ensure everything works:

```bash
# Run all tests
just test

# Run with coverage
just test-cov

# Run specific test file
uv run pytest tests/unit/domain/test_entities.py -v
```

## Development Workflow

A typical development session looks like:

```bash
# 1. Start fresh
just install

# 2. Run tests to verify setup
just test

# 3. Start development server
just dev

# 4. Make changes and run linting
just lint

# 5. Run tests again
just test

# 6. Commit your changes
git add -A && git commit -m "feat: your feature"
```

## Next Steps

- [Configuration](configuration.md) - Customize settings
- [Architecture Overview](../architecture/overview.md) - Understand the codebase
- [API Reference](../reference/index.md) - Detailed code documentation
