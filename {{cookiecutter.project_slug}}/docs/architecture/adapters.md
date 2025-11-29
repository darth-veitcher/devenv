# Adapters Layer

The Adapters Layer provides concrete implementations of domain interfaces, connecting your business logic to external systems.

## Overview

The adapters layer represents the **Kinetic Layer** - it defines *how* things happen (database access, API calls, etc.).

```
src/{{ cookiecutter.project_slug|replace('-', '_') }}/adapters/
├── __init__.py
└── repositories/
    └── __init__.py
```

## Repository Pattern

Repositories abstract data persistence, allowing the domain to remain infrastructure-agnostic.

### In-Memory Repository

The default implementation for development and testing:

```python
class InMemoryExampleRepository(ExampleRepository):
    """In-memory repository for development and testing."""

    def __init__(self) -> None:
        self._storage: dict[UUID, ExampleEntity] = {}

    async def save(self, entity: ExampleEntity) -> ExampleEntity:
        self._storage[entity.id] = entity
        return entity

    async def get_by_id(self, entity_id: UUID) -> ExampleEntity | None:
        return self._storage.get(entity_id)

    async def delete(self, entity_id: UUID) -> bool:
        if entity_id in self._storage:
            del self._storage[entity_id]
            return True
        return False
```

### Database Repository

For production with SQLAlchemy or similar:

```python
class SQLAlchemyExampleRepository(ExampleRepository):
    """PostgreSQL repository using SQLAlchemy."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def save(self, entity: ExampleEntity) -> ExampleEntity:
        model = ExampleModel(
            id=entity.id,
            name=entity.name,
            description=entity.description,
            created_at=entity.created_at,
        )
        self._session.add(model)
        await self._session.commit()
        return entity

    async def get_by_id(self, entity_id: UUID) -> ExampleEntity | None:
        result = await self._session.get(ExampleModel, entity_id)
        if result:
            return ExampleEntity(
                id=result.id,
                name=result.name,
                description=result.description,
            )
        return None
```

## External Service Adapters

Adapters also wrap external APIs:

```python
class StripePaymentAdapter:
    """Adapter for Stripe payment processing."""

    def __init__(self, api_key: str) -> None:
        self._client = stripe.Client(api_key)

    async def charge(self, amount: Money, token: str) -> PaymentResult:
        try:
            charge = await self._client.charges.create(
                amount=int(amount.amount * 100),
                currency=amount.currency.lower(),
                source=token,
            )
            return PaymentResult(success=True, transaction_id=charge.id)
        except stripe.CardError as e:
            return PaymentResult(success=False, error=str(e))
```

## Dependency Injection

Adapters are injected into services:

```python
# In application setup
def create_service(settings: Settings) -> ExampleService:
    if settings.database_url:
        repository = SQLAlchemyExampleRepository(get_session())
    else:
        repository = InMemoryExampleRepository()

    return ExampleService(repository)
```

In FastAPI:

```python
def get_repository() -> ExampleRepository:
    return InMemoryExampleRepository()

def get_service(repo: ExampleRepository = Depends(get_repository)) -> ExampleService:
    return ExampleService(repo)

@app.post("/entities")
async def create(request: Request, service: ExampleService = Depends(get_service)):
    return await service.create(request.name)
```

## Testing with Adapters

### Using In-Memory for Tests

```python
@pytest.fixture
def repository():
    return InMemoryExampleRepository()

@pytest.fixture
def service(repository):
    return ExampleService(repository)

async def test_create_entity(service):
    entity = await service.create("Test")
    assert entity.name == "Test"
```

### Mocking External Services

```python
@pytest.fixture
def mock_payment_adapter():
    adapter = Mock(spec=PaymentAdapter)
    adapter.charge.return_value = PaymentResult(success=True)
    return adapter
```

## Best Practices

### Do

- [x] Implement domain interfaces
- [x] Handle infrastructure errors gracefully
- [x] Map between domain entities and persistence models
- [x] Keep adapter logic minimal
- [x] Use async where appropriate

### Don't

- [ ] Put business logic in adapters
- [ ] Expose infrastructure details to domain
- [ ] Create circular dependencies
- [ ] Hardcode configuration

## Common Adapters

| Adapter Type | Purpose | Example |
|-------------|---------|---------|
| Repository | Data persistence | `SQLAlchemyRepository` |
| HTTP Client | External APIs | `StripeAdapter` |
| Message Queue | Async messaging | `RabbitMQAdapter` |
| Cache | Caching layer | `RedisAdapter` |
| File Storage | File operations | `S3Adapter` |

## Next Steps

- [Services Layer](services.md) - Using adapters in services
- [API Reference](../reference/adapters.md) - Full adapter documentation
