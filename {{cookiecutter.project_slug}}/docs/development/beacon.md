# BEACON Framework

{{ cookiecutter.project_name }} follows the BEACON Framework for pragmatic, artifact-driven development.

## What is BEACON?

BEACON is a methodology that emphasizes:

- **B**uild working software daily
- **E**valuate ideas before building
- **A**rchitect with reversibility
- **C**ode in tracer bullets
- **O**perate with simplicity
- **N**avigate with clear documentation

## Core Principles

### 1. Tracer Bullets

Build complete, minimal paths through the system that work end-to-end.

```
Day 1: Hardcoded UI → API → Response (proves plumbing)
Day 2: In-memory storage (proves logic)
Day 3: File storage (proves persistence)
Day 4: Database (production ready)
```

Each step delivers working software that could go to production.

### 2. DRY (Don't Repeat Yourself)

Every piece of knowledge has a single, authoritative representation.

```python
# Bad: Duplicated validation
def create_user(name):
    if not name.strip():
        raise ValueError("Name cannot be empty")

def update_user(user, name):
    if not name.strip():
        raise ValueError("Name cannot be empty")

# Good: Single source of truth
def validate_name(name: str) -> str:
    name = name.strip()
    if not name:
        raise ValueError("Name cannot be empty")
    return name
```

### 3. Orthogonality

Design independent components with minimal coupling.

```
UI → Service → Repository → Database

Each layer can change independently.
```

### 4. Reversibility

Make decisions that can be changed. Always have an escape hatch.

```python
# Good: Interface allows swapping implementations
class ExampleRepository(Protocol):
    async def save(self, entity: Entity) -> Entity: ...

# Can easily swap:
# - InMemoryExampleRepository (testing)
# - SQLAlchemyExampleRepository (production)
# - RedisExampleRepository (caching)
```

### 5. Simplicity

The simplest thing that could possibly work. Complexity must earn its keep.

!!! tip "Ask yourself"
    "Is this the simplest solution? What can I remove?"

## Project Structure

BEACON projects include a `project-management/` directory:

```
project-management/
├── ADRs/                    # Architectural Decision Records
│   └── ADR-000-template.md
├── Background/              # Problem context
│   └── 00-problem-statement.md
├── Roadmap/                 # Development plan
│   └── README.md
└── Work/                    # Transient workspace
    └── README.md
```

### ADRs (Architectural Decision Records)

Document significant technical decisions:

```markdown
# ADR-001: Use PostgreSQL for persistence

## Status
Accepted

## Context
We need a database for production data storage.

## Decision
Use PostgreSQL via SQLAlchemy.

## Consequences
- Proven, reliable database
- Requires PostgreSQL installation
- Team familiar with SQL
```

### Problem Statement

Define the problem before building:

```markdown
# Problem Statement

## Core Problem
Users cannot track their daily tasks efficiently.

## Target User
Solo developers managing personal projects.

## Success Criteria
- [ ] Create tasks in < 5 seconds
- [ ] View all tasks on single screen
- [ ] Mark tasks complete with one click
```

### Roadmap

Track progress with tracer bullets:

```markdown
## Tracer Bullets

- [x] Bullet #1: Hardcoded task list
- [x] Bullet #2: In-memory task storage
- [ ] Bullet #3: File-based persistence
- [ ] Bullet #4: Database integration
```

## Daily Workflow

### Morning

1. Fix any broken windows (< 15 min)
2. Review today's bullet goal
3. Write acceptance test first

### During Session

1. Focus on ONE bullet only
2. Write test → See it fail → Make it pass
3. Verify previous bullets still work
4. Commit with meaningful message

### End of Session

1. Update roadmap with progress
2. Note tomorrow's bullet
3. Ask: "Would I sign this?"

## The Prime Directive

> "Would I proudly sign my name to this?"

Every commit, every function, every decision should pass this test.

## Resources

- [The Pragmatic Programmer](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/)
- [Architecture Overview](../architecture/overview.md)
- [Project Roadmap](../../project-management/Roadmap/README.md)
