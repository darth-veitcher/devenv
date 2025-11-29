# Problem Statement

## Core Problem

Solo developers waste significant time on boilerplate setup, environment configuration, and deployment friction instead of building features that matter.

## Target User

**Who:** Solo developers and small teams building web applications
**Context:** Working from home, often on evenings/weekends, with limited time and patience for DevOps
**Current Pain:**
- Hours lost to environment setup and "works on my machine" issues
- Repeated boilerplate for each new project (auth, testing, CI/CD)
- Context switching between coding, debugging, deploying, documenting
- Complex deployment steps that kill momentum

## Success Criteria

- [ ] New project setup in < 5 minutes (cookiecutter → coding)
- [ ] Zero "works on my machine" issues via containerized development
- [ ] Production-ready Python scaffold with tests, docs, and CI from day one
- [ ] AI-assisted development with Claude agents and MCP servers pre-configured
- [ ] BEACON framework artifacts for structured, disciplined development

## Non-Goals (What We're NOT Solving)

1. NOT a full application framework (we generate scaffolds, not apps)
2. NOT production deployment automation (projects handle their own deployment)
3. NOT a replacement for learning fundamentals (we scaffold best practices)
4. NOT multi-language support initially (Python-first, others later)

## Why This Matters

The gap between "idea" and "working software" should be measured in hours, not weeks. By eliminating setup friction and embedding best practices into the project scaffold, solo developers can focus on what matters: building features and shipping to users.

Every project generated should feel like it was set up by a senior engineer who cares about:
- Clean architecture (3-layer: domain/adapters/services)
- Modern tooling (uv, hatch-vcs, ruff, pytest)
- Documentation (MkDocs with auto-generated API docs)
- Development experience (justfile, pre-commit, Dev Containers)
- AI assistance (Claude agents, MCP servers)

---

_Created: 2025-11-29_
_Last Updated: 2025-11-29_
_Status: Living Document - Update as requirements evolve_
