# Domain Layer

The Domain Layer is the heart of {{ cookiecutter.project_name }} - containing pure business logic with no external dependencies.

## Overview

The domain layer represents the **Semantic Layer** in our architecture - it defines *what* the business concepts are, not *how* they're stored or presented.

```
src/{{ cookiecutter.project_slug|replace('-', '_') }}/domain/
├── __init__.py
└── entities.py
```

## Entities

Entities are objects with identity that persist over time.

### Base Entity

All entities inherit from `EntityBase`:

```python
@dataclass(frozen=True, kw_only=True)
class EntityBase:
    """Base class for domain entities with identity tracking."""

    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime | None = None
```

Key characteristics:

- **Immutable** (`frozen=True`) - State changes create new instances
- **Identified** - Every entity has a unique UUID
- **Timestamped** - Creation and update tracking built-in

### Creating Domain Entities

```python
from dataclasses import dataclass
from {{ cookiecutter.project_slug|replace('-', '_') }}.domain.entities import EntityBase

@dataclass(frozen=True)
class Product(EntityBase):
    """A product in our catalog."""

    name: str
    price: Decimal
    sku: str
    description: str = ""

    def is_available(self) -> bool:
        """Check if product can be sold."""
        return self.price > 0

    def apply_discount(self, percentage: Decimal) -> "Product":
        """Return new product with discounted price."""
        new_price = self.price * (1 - percentage / 100)
        return Product(
            id=self.id,
            name=self.name,
            price=new_price,
            sku=self.sku,
            description=self.description,
        )
```

## Value Objects

Value objects are immutable objects defined by their attributes, not identity.

```python
@dataclass(frozen=True)
class Money:
    """A monetary value."""

    amount: Decimal
    currency: str = "USD"

    def add(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(amount=self.amount + other.amount, currency=self.currency)
```

## Repository Interfaces

The domain layer defines repository **interfaces** (not implementations):

```python
from abc import ABC, abstractmethod
from typing import Protocol
from uuid import UUID

class ExampleRepository(Protocol):
    """Repository interface for ExampleEntity persistence."""

    async def save(self, entity: ExampleEntity) -> ExampleEntity:
        """Persist an entity."""
        ...

    async def get_by_id(self, entity_id: UUID) -> ExampleEntity | None:
        """Retrieve an entity by ID."""
        ...

    async def delete(self, entity_id: UUID) -> bool:
        """Delete an entity by ID."""
        ...
```

!!! note "Why Interfaces?"
    By defining interfaces in the domain, we ensure the domain has no dependency on infrastructure. The adapters layer provides implementations.

## Domain Rules

Encode business rules in entity methods:

```python
@dataclass(frozen=True)
class Order(EntityBase):
    items: tuple[OrderItem, ...]
    status: OrderStatus

    def can_cancel(self) -> bool:
        """Only pending orders can be cancelled."""
        return self.status == OrderStatus.PENDING

    def cancel(self) -> "Order":
        if not self.can_cancel():
            raise DomainError("Cannot cancel non-pending order")
        return Order(
            id=self.id,
            items=self.items,
            status=OrderStatus.CANCELLED,
        )
```

## Best Practices

### Do

- [x] Keep entities immutable
- [x] Put business logic in entity methods
- [x] Use value objects for complex attributes
- [x] Define repository interfaces here
- [x] Validate invariants in entity creation

### Don't

- [ ] Import from adapters or infrastructure
- [ ] Include database or ORM code
- [ ] Add HTTP/API concerns
- [ ] Use mutable state
- [ ] Depend on external services

## Testing Domain Logic

Domain tests are fast and isolated:

```python
def test_product_discount():
    product = Product(
        name="Widget",
        price=Decimal("100.00"),
        sku="WID-001"
    )

    discounted = product.apply_discount(Decimal("10"))

    assert discounted.price == Decimal("90.00")
    assert discounted.id == product.id  # Same identity
```

## Next Steps

- [Adapters Layer](adapters.md) - Implementing repositories
- [Services Layer](services.md) - Using domain entities
- [API Reference](../reference/domain.md) - Full API documentation
