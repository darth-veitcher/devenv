# ADR-001: Use uv as Package Manager

## Status

Accepted

## Context

Python projects need a package manager for dependency management, virtual environments, and package building. Traditional options include:

- **pip + venv**: Standard but slow, no lock file by default
- **poetry**: Popular but slow resolver, complex configuration
- **pipenv**: Falling out of favor, slow
- **uv**: New Rust-based tool from Astral (ruff creators), extremely fast

We need a tool that:
1. Is fast (developer experience matters)
2. Handles virtual environments
3. Supports lock files for reproducibility
4. Works with pyproject.toml
5. Supports building and publishing packages

## Decision

Use **uv** as the primary package manager for all generated projects.

Key features used:
- `uv sync` - Install dependencies from lock file
- `uv add` - Add new dependencies
- `uv run` - Run commands in virtual environment
- `uv build` - Build packages for distribution
- Dependency groups (dev, docs, test)

Combined with:
- **hatch-vcs** for git-based versioning (no manual version bumps)
- **ruff** for linting and formatting (also from Astral, same philosophy)

## Consequences

### Positive

- 10-100x faster than pip/poetry for dependency resolution
- Lock file (`uv.lock`) ensures reproducible builds
- Single tool for venv, deps, and building
- Excellent pyproject.toml support
- Same company as ruff (consistent tooling philosophy)
- Active development with rapid improvements

### Negative

- Newer tool, less ecosystem familiarity
- Some edge cases may not be handled yet
- Developers need to learn new commands

### Neutral

- Replaces both pip and venv
- Works alongside existing tools if needed

## Escape Hatch

If uv proves problematic:
1. Lock file can be converted to requirements.txt
2. pyproject.toml remains compatible with pip/poetry
3. Virtual environments are standard Python venvs
4. Migration path: `uv export > requirements.txt`

---

_Created: 2025-11-29_
_Last Updated: 2025-11-29_
