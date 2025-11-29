# Services Layer

The Services Layer orchestrates business operations, coordinating between domain entities and adapters.

## Overview

The services layer represents the **Dynamic Layer** - it coordinates *when* and *in what order* things happen.

```
src/{{ cookiecutter.project_slug|replace('-', '_') }}/services/
└── __init__.py
```

## Application Services

Services implement use cases by coordinating domain objects:

```python
class ExampleService:
    """Service for managing example entities."""

    def __init__(self, repository: ExampleRepository) -> None:
        self._repository = repository

    async def create(self, name: str, description: str = "") -> ExampleEntity:
        """Create a new entity.

        Args:
            name: The entity name (required, non-empty).
            description: Optional description.

        Returns:
            The created entity.

        Raises:
            ValueError: If name is empty or whitespace-only.
        """
        if not name.strip():
            raise ValueError("Name cannot be empty")

        entity = ExampleEntity(
            name=name.strip(),
            description=description
        )
        return await self._repository.save(entity)

    async def get_by_id(self, entity_id: UUID) -> ExampleEntity | None:
        """Retrieve an entity by its ID."""
        return await self._repository.get_by_id(entity_id)

    async def delete(self, entity_id: UUID) -> bool:
        """Delete an entity by its ID."""
        return await self._repository.delete(entity_id)
```

## Service Responsibilities

Services should:

1. **Validate input** - Check parameters before processing
2. **Coordinate work** - Call domain methods and repositories
3. **Handle transactions** - Ensure data consistency
4. **Raise business exceptions** - Communicate failures clearly

## Complex Operations

For operations spanning multiple entities:

```python
class OrderService:
    def __init__(
        self,
        order_repo: OrderRepository,
        product_repo: ProductRepository,
        payment_adapter: PaymentAdapter,
    ) -> None:
        self._orders = order_repo
        self._products = product_repo
        self._payments = payment_adapter

    async def place_order(
        self,
        customer_id: UUID,
        items: list[OrderItem],
        payment_token: str,
    ) -> Order:
        # 1. Validate products exist and are available
        for item in items:
            product = await self._products.get_by_id(item.product_id)
            if not product or not product.is_available():
                raise ValueError(f"Product {item.product_id} unavailable")

        # 2. Calculate total
        total = sum(item.price * item.quantity for item in items)

        # 3. Process payment
        payment = await self._payments.charge(total, payment_token)
        if not payment.success:
            raise PaymentError(payment.error)

        # 4. Create and save order
        order = Order(
            customer_id=customer_id,
            items=tuple(items),
            total=total,
            payment_id=payment.transaction_id,
            status=OrderStatus.CONFIRMED,
        )
        return await self._orders.save(order)
```

## Error Handling

Define domain-specific exceptions:

```python
class DomainError(Exception):
    """Base exception for domain errors."""
    pass

class EntityNotFoundError(DomainError):
    """Raised when an entity cannot be found."""
    pass

class ValidationError(DomainError):
    """Raised when validation fails."""
    pass


# In service
async def get_by_id(self, entity_id: UUID) -> ExampleEntity:
    entity = await self._repository.get_by_id(entity_id)
    if not entity:
        raise EntityNotFoundError(f"Entity {entity_id} not found")
    return entity
```

## Transaction Management

For database transactions:

```python
class OrderService:
    def __init__(self, session: AsyncSession, ...):
        self._session = session

    async def place_order(self, ...):
        async with self._session.begin():
            # All operations in single transaction
            order = await self._create_order(...)
            await self._update_inventory(...)
            await self._send_notification(...)
            return order
```

## Testing Services

Services are tested with mock adapters:

```python
@pytest.fixture
def repository():
    return InMemoryExampleRepository()

@pytest.fixture
def service(repository):
    return ExampleService(repository)


class TestExampleService:
    async def test_create_entity(self, service):
        entity = await service.create("Test", "Description")

        assert entity.name == "Test"
        assert entity.description == "Description"
        assert entity.id is not None

    async def test_create_empty_name_raises(self, service):
        with pytest.raises(ValueError, match="cannot be empty"):
            await service.create("")

    async def test_create_whitespace_name_raises(self, service):
        with pytest.raises(ValueError, match="cannot be empty"):
            await service.create("   ")

    async def test_get_by_id_returns_entity(self, service):
        created = await service.create("Test")
        retrieved = await service.get_by_id(created.id)

        assert retrieved == created

    async def test_get_by_id_returns_none(self, service):
        result = await service.get_by_id(uuid4())
        assert result is None
```

## Best Practices

### Do

- [x] Keep services focused on coordination
- [x] Inject dependencies through constructor
- [x] Validate inputs at service boundary
- [x] Use meaningful exception types
- [x] Document public methods with docstrings

### Don't

- [ ] Put domain logic in services
- [ ] Access infrastructure directly
- [ ] Create services with too many responsibilities
- [ ] Catch and swallow exceptions silently

## Service Patterns

| Pattern | Use Case |
|---------|----------|
| **CRUD Service** | Basic entity management |
| **Workflow Service** | Multi-step operations |
| **Query Service** | Complex read operations |
| **Integration Service** | External system coordination |

## Next Steps

- [REST API](../api/rest.md) - Exposing services via HTTP
- [CLI](../api/cli.md) - Exposing services via command line
- [API Reference](../reference/services.md) - Full service documentation
