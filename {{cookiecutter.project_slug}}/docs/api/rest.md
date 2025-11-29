# REST API

{{ cookiecutter.project_name }} provides a RESTful HTTP API built with FastAPI.

## Overview

The API is available at `http://localhost:8000` when running locally.

### Interactive Documentation

FastAPI generates interactive API documentation automatically:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Starting the Server

=== "Just"

    ```bash
    just serve
    ```

=== "Development (with reload)"

    ```bash
    just dev
    ```

=== "Direct"

    ```bash
    uv run uvicorn {{ cookiecutter.project_slug|replace('-', '_') }}.api.main:app --host 0.0.0.0 --port 8000
    ```

## Endpoints

### Health Check

Check if the service is running:

```http
GET /health
```

**Response:**

```json
{
  "status": "ok",
  "app_name": "{{ cookiecutter.project_name }}",
  "database": "not configured"
}
```

### Root

```http
GET /
```

**Response:**

```json
{
  "message": "Hello from {{ cookiecutter.project_name }}!"
}
```

### Create Entity

```http
POST /entities
Content-Type: application/json

{
  "name": "My Entity",
  "description": "Optional description"
}
```

**Response (201 Created):**

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "My Entity",
  "description": "Optional description"
}
```

**Error Response (400 Bad Request):**

```json
{
  "detail": "Name cannot be empty"
}
```

### Get Entity

```http
GET /entities/{entity_id}
```

**Response (200 OK):**

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "My Entity",
  "description": "Optional description"
}
```

**Error Response (404 Not Found):**

```json
{
  "detail": "Entity not found"
}
```

### Delete Entity

```http
DELETE /entities/{entity_id}
```

**Response:** `204 No Content`

**Error Response (404 Not Found):**

```json
{
  "detail": "Entity not found"
}
```

## Request/Response Schemas

### CreateEntityRequest

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Entity name |
| `description` | string | No | Entity description |

### EntityResponse

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Unique identifier |
| `name` | string | Entity name |
| `description` | string | Entity description |

## Error Handling

All errors follow a consistent format:

```json
{
  "detail": "Error message here"
}
```

| Status Code | Meaning |
|-------------|---------|
| 400 | Bad Request - Invalid input |
| 404 | Not Found - Resource doesn't exist |
| 422 | Validation Error - Schema mismatch |
| 500 | Internal Server Error |

## Authentication

!!! note "Not Implemented"
    Authentication is not included by default. Add your preferred auth mechanism (JWT, OAuth, API keys) as needed.

## CORS

CORS is not configured by default. To enable:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Examples

### cURL

```bash
# Create entity
curl -X POST http://localhost:8000/entities \
  -H "Content-Type: application/json" \
  -d '{"name": "Test", "description": "A test entity"}'

# Get entity
curl http://localhost:8000/entities/550e8400-e29b-41d4-a716-446655440000

# Delete entity
curl -X DELETE http://localhost:8000/entities/550e8400-e29b-41d4-a716-446655440000
```

### Python (httpx)

```python
import httpx

async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
    # Create
    response = await client.post("/entities", json={"name": "Test"})
    entity = response.json()

    # Get
    response = await client.get(f"/entities/{entity['id']}")

    # Delete
    await client.delete(f"/entities/{entity['id']}")
```

## Next Steps

- [CLI Reference](cli.md) - Command-line interface
- [API Reference](../reference/api.md) - Code documentation
