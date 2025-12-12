{%- if cookiecutter.cache_backend in ['redis', 'falkordb'] -%}
{% raw %}
# Cache & Graph Patterns

This project includes cache infrastructure{% endraw %}{% if cookiecutter.cache_backend == 'falkordb' %} and graph database support{% endif %}{% raw %} for session management{% endraw %}{% if cookiecutter.cache_backend == 'falkordb' %}, relationship modeling, and graph traversals{% endif %}{% raw %}.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     Presentation Layer                       │
│                    (FastAPI / CLI / MCP)                     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      Service Layer                           │
│                      (UserService)                           │
│  ┌─────────────────┐  ┌─────────────────┐                   │
│  │ Business Logic  │  │   Graph Sync    │                   │
│  │  (Validation)   │  │ (Best Effort)   │                   │
│  └────────┬────────┘  └────────┬────────┘                   │
└───────────┼────────────────────┼────────────────────────────┘
            │                    │
            ▼                    ▼
┌───────────────────┐  ┌───────────────────┐
│   SQL Repository  │  │  Graph Database   │
│  (Source of Truth)│  │   (FalkorDB)      │
│  SQLite/PostgreSQL│  │   Relationships   │
└───────────────────┘  └───────────────────┘
```

## Session Management (Redis)

The `SessionManager` provides simple key-value session storage.

### Basic Usage

```python
{% endraw %}from {{ cookiecutter.project_slug|replace('-', '_') }}.infrastructure.cache import get_session_manager{% raw %}

# Get session manager
sessions = get_session_manager()

# Store session data
await sessions.set("user:123:session", {
    "user_id": "123",
    "authenticated": True,
    "permissions": ["read", "write"]
})

# Retrieve session
data = await sessions.get("user:123:session")

# Delete session (logout)
await sessions.delete("user:123:session")
```

### With Custom TTL

```python
# Session expires in 1 hour
await sessions.set("user:123:session", data, ttl=3600)
```

### Raw Redis Access

For advanced use cases:

```python
{% endraw %}from {{ cookiecutter.project_slug|replace('-', '_') }}.infrastructure.cache import get_redis{% raw %}

redis = get_redis()
await redis.set("custom:key", "value")
await redis.incr("counter")
await redis.expire("custom:key", 300)
```
{% endraw %}
{%- if cookiecutter.cache_backend == 'falkordb' %}
{% raw %}
## Graph Database (FalkorDB)

FalkorDB provides graph capabilities on top of Redis, enabling relationship modeling and traversals using Cypher queries.

### Sync Pattern

**SQL is the source of truth.** Graph data is synced for relationship queries:

```python
class UserService:
    async def create(self, username: str, email: str) -> User:
        # 1. Validate and save to SQL (source of truth)
        user = await self._repository.save(user)

        # 2. Sync to graph (best-effort, for relationships)
        await self._sync_user_to_graph(user)

        return user
```

If FalkorDB is unavailable, operations succeed (graceful degradation).

### Graph Operations

#### Creating Relationships

```python
{% endraw %}from {{ cookiecutter.project_slug|replace('-', '_') }}.infrastructure.graph import get_graph{% raw %}

graph = get_graph()

# Create FOLLOWS relationship
graph.query("""
    MATCH (a:User {id: $follower_id})
    MATCH (b:User {id: $followed_id})
    MERGE (a)-[r:FOLLOWS]->(b)
""", {"follower_id": "123", "followed_id": "456"})
```

#### Querying Relationships

```python
# Get all followers
result = graph.query("""
    MATCH (follower:User)-[:FOLLOWS]->(u:User {id: $user_id})
    RETURN follower.id, follower.username
""", {"user_id": "123"})

for row in result.result_set:
    print(f"Follower: {row[1]}")
```

#### Common Patterns

**Mutual Follows (Friends):**
```python
result = graph.query("""
    MATCH (u:User {id: $user_id})-[:FOLLOWS]->(friend:User)-[:FOLLOWS]->(u)
    RETURN friend.id, friend.username
""", {"user_id": "123"})
```

**Friends of Friends:**
```python
result = graph.query("""
    MATCH (u:User {id: $user_id})-[:FOLLOWS]->(:User)-[:FOLLOWS]->(fof:User)
    WHERE fof.id <> $user_id
    AND NOT (u)-[:FOLLOWS]->(fof)
    RETURN DISTINCT fof.id, fof.username
    LIMIT 10
""", {"user_id": "123"})
```

**Shortest Path:**
```python
result = graph.query("""
    MATCH path = shortestPath(
        (a:User {id: $from_id})-[:FOLLOWS*]-(b:User {id: $to_id})
    )
    RETURN [n IN nodes(path) | n.username] as usernames
""", {"from_id": "123", "to_id": "789"})
```

### Using GraphRepository

For common operations, use the `GraphRepository` base class:

```python
{% endraw %}from {{ cookiecutter.project_slug|replace('-', '_') }}.infrastructure.graph import GraphRepository{% raw %}

repo = GraphRepository()

# Create a node
repo.create_node("Product", {"id": "prod-1", "name": "Widget"})

# Create a relationship
repo.create_edge("User", "user-1", "PURCHASED", "Product", "prod-1", {
    "quantity": 2,
    "date": "2024-01-15"
})

# Custom query
results = repo.query("""
    MATCH (u:User)-[p:PURCHASED]->(prod:Product)
    WHERE u.id = $user_id
    RETURN prod.name, p.quantity
""", {"user_id": "user-1"})
```
{% endraw %}
{%- endif %}
{% raw %}
## Extending with New Entities

### Step 1: Create Domain Entity

```python
# domain/entities.py
@dataclass(frozen=True)
class Product(EntityBase):
    name: str
    price: Decimal

    def is_valid(self) -> bool:
        return len(self.name) > 0 and self.price > 0
```

### Step 2: Add SQL Model

```python
# adapters/models.py
class ProductModel(Base):
    __tablename__ = "products"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
```

### Step 3: Create Repository

```python
# adapters/repositories/__init__.py
class ProductRepository(Protocol):
    async def get_by_id(self, product_id: UUID) -> Product | None: ...
    async def save(self, product: Product) -> Product: ...
    async def delete(self, product_id: UUID) -> bool: ...

class SQLAlchemyProductRepository:
    # Implementation following UserRepository pattern
    ...
```

### Step 4: Create Service with Graph Sync

```python
# services/__init__.py
class ProductService:
    def __init__(self, repository: ProductRepository) -> None:
        self._repository = repository

    async def create(self, name: str, price: Decimal) -> Product:
        product = Product(name=name, price=price)
        saved = await self._repository.save(product)

        # Sync to graph for relationship queries
        await self._sync_to_graph(saved)

        return saved

    async def _sync_to_graph(self, product: Product) -> None:
        try:
            graph = get_graph()
            graph.query("""
                MERGE (p:Product {id: $id})
                SET p.name = $name, p.price = $price
            """, {
                "id": str(product.id),
                "name": product.name,
                "price": float(product.price),
            })
        except Exception:
            pass  # Best-effort sync
```

## Best Practices

### 1. SQL is Source of Truth

Always write to SQL first, then sync to graph:

```python
# Correct
user = await sql_repository.save(user)
await sync_to_graph(user)

# Wrong - graph should not be source of truth
graph.create_node("User", user_data)
await sql_repository.save(user)  # What if this fails?
```

### 2. Graceful Degradation

Handle graph unavailability:

```python
async def _sync_to_graph(self, entity) -> None:
    try:
        graph = get_graph()
        graph.query(...)
    except Exception:
        # Log warning, but don't fail the operation
        pass
```

### 3. Index Graph Properties

Create indexes for frequently queried properties:

```python
async def init_graph() -> None:
    graph = get_graph()
    try:
        graph.query("CREATE INDEX FOR (u:User) ON (u.id)")
        graph.query("CREATE INDEX FOR (p:Product) ON (p.id)")
    except Exception:
        pass  # Indexes may already exist
```

### 4. Use Parameterized Queries

Always use parameters to prevent injection:

```python
# Safe - uses parameters
graph.query("MATCH (u:User {id: $id}) RETURN u", {"id": user_id})

# Unsafe - string interpolation
# Never do this!
```

## Testing

### Unit Tests (No External Services)

Unit tests use `InMemoryUserRepository` and skip graph sync:

```python
@pytest.fixture
def service(repository: InMemoryUserRepository) -> UserService:
    return UserService(repository)

async def test_create_user(service: UserService) -> None:
    user = await service.create("alice", "alice@example.com")
    assert user.username == "alice"
    # Graph sync fails silently (graceful degradation)
```

### Integration Tests (With Services)

Run inside devcontainer with docker-compose:

```bash
just test-integration
```

This starts Redis/FalkorDB and runs full integration tests.
{% endraw %}
{%- else -%}
# Cache & Graph Patterns

This project was generated without cache/graph support.

To enable these features, regenerate with:

```bash
cookiecutter . cache_backend=redis    # For session caching
cookiecutter . cache_backend=falkordb  # For caching + graph database
```

See the [devenv documentation](https://your-docs-url) for more information.
{%- endif %}
