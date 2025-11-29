# Justfile Commands

All available commands in generated projects.

## Quick Reference

```bash
just --list  # Show all commands
```

## Development Setup

### install

Install all dependencies including dev tools.

```bash
just install
# Runs: uv sync --all-extras
```

### install-prod

Install only production dependencies.

```bash
just install-prod
# Runs: uv sync
```

## Running

### serve

Start the API server.

```bash
just serve
just serve --port 3000  # With arguments
```

### dev

Start development server with auto-reload.

```bash
just dev
# Runs: uvicorn my_project.api.main:app --reload
```

### cli

Run CLI commands.

```bash
just cli --help
just cli version
just cli create "My Entity" -d "Description"
```

## Code Quality

### check

Run all quality checks (lint, typecheck, test).

```bash
just check
```

### lint

Run Ruff linter.

```bash
just lint
# Runs: uv run ruff check src/ tests/
```

### lint-fix

Fix linting issues automatically.

```bash
just lint-fix
# Runs: uv run ruff check src/ tests/ --fix
```

### format

Format code with Ruff.

```bash
just format
# Runs: uv run ruff format src/ tests/
```

### format-check

Check formatting without changes.

```bash
just format-check
```

### typecheck

Run MyPy type checker.

```bash
just typecheck
# Runs: uv run mypy src/
```

### security

Run Bandit security scanner.

```bash
just security
# Runs: uv run bandit -r src/
```

## Testing

### test

Run all tests.

```bash
just test
just test -v              # Verbose
just test tests/unit/     # Specific directory
```

### test-cov

Run tests with coverage report.

```bash
just test-cov
# Generates terminal and HTML reports
```

### test-watch

Run tests in watch mode.

```bash
just test-watch
# Requires pytest-watch
```

### test-unit

Run only unit tests.

```bash
just test-unit
```

### test-integration

Run only integration tests.

```bash
just test-integration
```

## Documentation

### docs-serve

Serve documentation locally.

```bash
just docs-serve
# Opens http://localhost:8000
```

### docs-build

Build static documentation.

```bash
just docs-build
# Output in site/
```

### docs-deploy

Deploy to GitHub Pages.

```bash
just docs-deploy
# Runs: mkdocs gh-deploy --force
```

### docs-check

Build with strict mode to catch errors.

```bash
just docs-check
```

## Build & Release

### build

Build the package.

```bash
just build
# Runs: uv build
# Output in dist/
```

### clean

Remove build artifacts.

```bash
just clean
# Removes: build/, dist/, __pycache__, etc.
```

### version

Show current version.

```bash
just version
# From hatch-vcs (git tags)
```

## Docker

### docker-build

Build Docker image.

```bash
just docker-build
```

### docker-run

Run Docker container.

```bash
just docker-run
```

### up

Start all services with Docker Compose.

```bash
just up
```

### down

Stop all services.

```bash
just down
```

### logs

View container logs.

```bash
just logs
just logs app -f  # Follow specific service
```

## Database

### db-up

Start database services.

```bash
just db-up
```

### db-down

Stop database services.

```bash
just db-down
```

## Git Shortcuts

### save

Quick commit all changes.

```bash
just save "commit message"
# Runs: git add -A && git commit -m "message"
```

### undo

Undo last commit (keep changes).

```bash
just undo
# Runs: git reset --soft HEAD~1
```

## Customizing

Edit `justfile` to add your own commands:

```just
# My custom command
deploy:
    ssh server "cd /app && git pull && docker compose up -d"
```
