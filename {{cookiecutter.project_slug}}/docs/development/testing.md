# Testing Guide

{{ cookiecutter.project_name }} uses pytest for testing with a comprehensive test suite.

## Quick Start

```bash
# Run all tests
just test

# Run with coverage
just test-cov

# Run with verbose output
uv run pytest -v
```

## Test Structure

```
tests/
├── __init__.py
├── conftest.py              # Shared fixtures
├── unit/                    # Fast, isolated tests
│   ├── __init__.py
│   ├── domain/
│   │   ├── __init__.py
│   │   └── test_entities.py
│   └── services/
│       ├── __init__.py
│       └── test_example_service.py
└── integration/             # Slower, realistic tests
    ├── __init__.py
    └── test_api.py
```

## Fixtures

Common fixtures in `conftest.py`:

```python
import pytest
from {{ cookiecutter.project_slug|replace('-', '_') }}.adapters.repositories import InMemoryExampleRepository
from {{ cookiecutter.project_slug|replace('-', '_') }}.services import ExampleService

@pytest.fixture
def repository():
    """Fresh in-memory repository for each test."""
    return InMemoryExampleRepository()

@pytest.fixture
def service(repository):
    """Service with injected repository."""
    return ExampleService(repository)
```

## Unit Tests

### Testing Entities

```python
from {{ cookiecutter.project_slug|replace('-', '_') }}.domain.entities import ExampleEntity

class TestExampleEntity:
    def test_create_entity(self):
        entity = ExampleEntity(name="Test", description="Desc")

        assert entity.name == "Test"
        assert entity.description == "Desc"
        assert entity.id is not None

    def test_entity_is_immutable(self):
        entity = ExampleEntity(name="Test")

        with pytest.raises(FrozenInstanceError):
            entity.name = "New Name"

    def test_is_valid_with_name(self):
        entity = ExampleEntity(name="Valid")
        assert entity.is_valid() is True

    def test_is_invalid_without_name(self):
        entity = ExampleEntity(name="")
        assert entity.is_valid() is False
```

### Testing Services

```python
import pytest
from uuid import uuid4

class TestExampleService:
    async def test_create_entity(self, service):
        entity = await service.create("Test", "Description")

        assert entity.name == "Test"
        assert entity.description == "Description"

    async def test_create_empty_name_raises(self, service):
        with pytest.raises(ValueError, match="cannot be empty"):
            await service.create("")

    async def test_get_by_id_returns_entity(self, service):
        created = await service.create("Test")

        retrieved = await service.get_by_id(created.id)

        assert retrieved == created

    async def test_get_by_id_returns_none_for_unknown(self, service):
        result = await service.get_by_id(uuid4())
        assert result is None
```

## Integration Tests

### Testing API Endpoints

```python
import pytest
from httpx import AsyncClient, ASGITransport
from {{ cookiecutter.project_slug|replace('-', '_') }}.api.main import app

@pytest.fixture
async def client():
    """Async HTTP client for testing."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client

class TestHealthEndpoint:
    async def test_health_returns_ok(self, client):
        response = await client.get("/health")

        assert response.status_code == 200
        assert response.json()["status"] == "ok"

class TestEntityEndpoints:
    async def test_create_entity(self, client):
        response = await client.post(
            "/entities",
            json={"name": "Test", "description": "Desc"}
        )

        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Test"
        assert "id" in data

    async def test_create_empty_name_fails(self, client):
        response = await client.post(
            "/entities",
            json={"name": ""}
        )

        assert response.status_code == 400
```

## Async Testing

pytest-asyncio handles async tests automatically:

```python
# pyproject.toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
```

All `async def test_*` functions run as coroutines.

## Coverage

### Generate Coverage Report

```bash
# Terminal report
just test-cov

# HTML report
uv run pytest --cov=src --cov-report=html
open htmlcov/index.html
```

### Coverage Configuration

```toml
# pyproject.toml
[tool.coverage.run]
source = ["src"]
branch = true

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "if TYPE_CHECKING:",
    "raise NotImplementedError",
]
```

## Test Markers

Use markers for test categorization:

```python
@pytest.mark.slow
async def test_heavy_computation():
    ...

@pytest.mark.integration
async def test_database_connection():
    ...
```

Run specific markers:

```bash
uv run pytest -m "not slow"
uv run pytest -m integration
```

## Best Practices

### Do

- [x] Write tests before or alongside code
- [x] Use descriptive test names
- [x] Follow Arrange-Act-Assert pattern
- [x] Keep tests independent
- [x] Use fixtures for setup

### Don't

- [ ] Share state between tests
- [ ] Test implementation details
- [ ] Write flaky tests
- [ ] Skip error path testing
- [ ] Leave debug code in tests

## Debugging Tests

```bash
# Stop on first failure
uv run pytest -x

# Show print statements
uv run pytest -s

# Drop into debugger on failure
uv run pytest --pdb

# Run specific test
uv run pytest tests/unit/services/test_example_service.py::TestExampleService::test_create_entity -v
```
