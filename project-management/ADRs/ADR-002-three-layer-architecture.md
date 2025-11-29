# ADR-002: Three-Layer Architecture Pattern

## Status

Accepted

## Context

Generated projects need a consistent, maintainable code structure. Options considered:

- **Flat structure**: Simple but doesn't scale
- **MVC**: Web-centric, doesn't fit all use cases
- **Hexagonal/Ports & Adapters**: Good but complex terminology
- **Three-layer (Domain/Adapters/Services)**: Clean separation, intuitive naming

The pattern is inspired by Palantir's ontology approach:
- **Semantic Layer** (Domain): What the world looks like
- **Kinetic Layer** (Adapters): How we connect to reality
- **Dynamic Layer** (Services): How we make things happen

## Decision

Adopt a **three-layer architecture** for all generated Python projects:

```
src/package_name/
├── domain/           # Pure business entities and rules
├── adapters/         # External system interfaces
├── services/         # Business logic orchestration
├── api/              # REST presentation layer
├── cli/              # CLI presentation layer
└── infrastructure/   # Cross-cutting concerns
```

### Layer Rules

1. **Domain** has no dependencies (pure Python)
2. **Adapters** depend only on Domain
3. **Services** depend on Domain and Adapters (via interfaces)
4. **API/CLI** depend on Services (presentation only)
5. **Infrastructure** can be used by any layer

## Consequences

### Positive

- Clear separation of concerns
- Domain logic is testable in isolation
- Easy to swap adapters (e.g., in-memory → database)
- Scales well as project grows
- Familiar to developers (similar to Clean Architecture)

### Negative

- More files/directories than flat structure
- May feel over-engineered for tiny projects
- Requires discipline to maintain layer boundaries

### Neutral

- Learning curve for developers unfamiliar with layered architecture
- Some flexibility in how strictly layers are enforced

## Escape Hatch

For simple scripts or prototypes:
1. Domain entities can be used directly
2. Services layer can be skipped for simple CRUD
3. Structure can be flattened by moving files
4. No framework lock-in - it's just directory organization

---

_Created: 2025-11-29_
_Last Updated: 2025-11-29_
