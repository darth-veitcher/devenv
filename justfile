# devenv Template Development Commands
# Run `just --list` to see available commands

# Default: show available commands
default:
    @just --list

# Build documentation
docs-build:
    uv run --group docs mkdocs build

# Serve documentation locally
docs-serve:
    uv run --group docs mkdocs serve

# Deploy docs to GitHub Pages
docs-deploy:
    uv run --group docs mkdocs gh-deploy --force

# Build docs with strict mode (catches errors)
docs-check:
    uv run --group docs mkdocs build --strict

# Test template generation
test-generate:
    #!/usr/bin/env bash
    set -euo pipefail
    rm -rf /tmp/test-devenv-project
    cookiecutter . --no-input -o /tmp project_name="test-devenv-project"
    echo "Generated project at /tmp/test-devenv-project"

# Test generated project works
test-project:
    #!/usr/bin/env bash
    set -euo pipefail
    cd /tmp/test-devenv-project
    uv sync --all-extras
    uv run pytest

# Full test: generate and verify
test: test-generate test-project
    @echo "All tests passed!"

# Clean generated test artifacts
clean:
    rm -rf /tmp/test-devenv-project site/
