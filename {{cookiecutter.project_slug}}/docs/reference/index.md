# API Reference

This section contains auto-generated documentation from the source code.

## Modules

| Module | Description |
|--------|-------------|
| [Domain](domain.md) | Core business entities and interfaces |
| [Services](services.md) | Application services and use cases |
| [Adapters](adapters.md) | Repository and external service implementations |
| [API](api.md) | FastAPI REST endpoints |
| [Infrastructure](infrastructure.md) | Configuration and cross-cutting concerns |

## Code Style

This project follows:

- **Type hints** on all public functions
- **Google-style docstrings** for documentation
- **Async/await** for I/O operations
- **Immutable data** where possible

## Example Docstring

```python
async def create(self, name: str, description: str = "") -> ExampleEntity:
    """Create a new entity.

    Creates and persists a new ExampleEntity with the given name
    and optional description.

    Args:
        name: The entity name. Must be non-empty after stripping whitespace.
        description: Optional description text. Defaults to empty string.

    Returns:
        The newly created and persisted entity.

    Raises:
        ValueError: If name is empty or contains only whitespace.

    Example:
        >>> service = ExampleService(repository)
        >>> entity = await service.create("My Entity", "Description")
        >>> print(entity.name)
        'My Entity'
    """
```

## Navigation

Use the sidebar to browse individual modules, or:

- [:material-domain: Domain Layer](domain.md)
- [:material-cog: Services Layer](services.md)
- [:material-connection: Adapters Layer](adapters.md)
- [:material-api: API Layer](api.md)
- [:material-wrench: Infrastructure](infrastructure.md)
