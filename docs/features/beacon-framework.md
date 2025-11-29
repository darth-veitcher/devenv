# BEACON Framework

Generated projects include the BEACON Framework - a pragmatic, artifact-driven development methodology.

## What is BEACON?

BEACON helps solo developers and small teams build software methodically:

- **B**uild working software daily
- **E**valuate ideas before building
- **A**rchitect with reversibility
- **C**ode in tracer bullets
- **O**perate with simplicity
- **N**avigate with clear documentation

## Core Principles

### 1. Tracer Bullets

Build complete, minimal paths through your system that work end-to-end.

```
Day 1: Hardcoded response (proves plumbing)
Day 2: In-memory storage (proves logic)
Day 3: File storage (proves persistence)
Day 4: Database (production ready)
```

Each step delivers working software.

### 2. DRY (Don't Repeat Yourself)

Every piece of knowledge has a single, authoritative representation.

### 3. Orthogonality

Design independent components with minimal coupling.

### 4. Reversibility

Make decisions that can be changed. Always have an escape hatch.

### 5. Simplicity

The simplest thing that could possibly work. Complexity must earn its keep.

## Project Management Structure

Generated projects include:

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

Define **why** before **how**:

```markdown
# Problem Statement

## Core Problem
Users cannot track their daily tasks efficiently.

## Target User
Solo developers managing personal projects.

## Success Criteria
- [ ] Create tasks in < 5 seconds
- [ ] View all tasks on single screen
```

### Roadmap

Track progress with tracer bullets:

```markdown
## Tracer Bullet Progress

### Phase 1: Foundation
- [x] Bullet #1: Hardcoded response
- [x] Bullet #2: In-memory storage
- [ ] Bullet #3: File persistence
```

## Daily Workflow

### Morning

1. Fix any broken windows (< 15 min)
2. Review today's bullet goal
3. Write acceptance test first

### During Session

1. Focus on ONE bullet only
2. Write test → See fail → Make pass
3. Verify previous bullets still work
4. Commit with meaningful message

### End of Session

1. Update Roadmap with progress
2. Note tomorrow's bullet
3. Ask: "Would I sign this?"

## The Prime Directive

> "Would I proudly sign my name to this?"

Every commit, every function, every decision should pass this test.

## Working with BEACON

### Starting a New Feature

1. Create a bullet in the Roadmap
2. Write the acceptance test
3. Implement minimally
4. Verify and commit

### Making Architectural Decisions

1. Document in an ADR
2. Include context, decision, consequences
3. Link from Roadmap

### Handling Technical Debt

Fix immediately if < 15 minutes, otherwise:

1. Create an issue with deadline
2. Add to Roadmap as a bullet
3. Don't let it fester

## Integration with Claude

The `.claude/` directory includes:

- **CLAUDE.md** - Agent system prompt with BEACON instructions
- **agents/** - Specialized agent prompts
- **reference/** - Architecture documentation

Claude understands BEACON and can help:

- Decompose features into tracer bullets
- Write ADRs
- Update Roadmaps
- Follow the daily workflow

## Next Steps

- [Claude Agents](claude-agents.md) - AI pair programming
- [Directory Structure](../reference/directory-structure.md) - Full file listing
