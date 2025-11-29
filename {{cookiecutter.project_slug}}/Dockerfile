# {{ cookiecutter.project_name }}
# Multi-stage Dockerfile using uv for fast, reliable builds

# ============================================================================
# Stage 1: Build dependencies
# ============================================================================
FROM python:{{ cookiecutter.python_version }}-slim AS builder

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Set up working directory
WORKDIR /app

# Copy project files needed for dependency resolution
COPY pyproject.toml ./
COPY README.md ./

# Create source directory structure for editable install
COPY src/ ./src/

# Install dependencies (no dev dependencies in production)
RUN uv sync --frozen --no-dev

# ============================================================================
# Stage 2: Runtime
# ============================================================================
FROM python:{{ cookiecutter.python_version }}-slim AS runtime

# Don't run as root
RUN useradd --create-home --shell /bin/bash app
USER app

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder --chown=app:app /app/.venv /app/.venv

# Copy source code
COPY --chown=app:app src/ ./src/
COPY --chown=app:app pyproject.toml README.md ./

# Add venv to path
ENV PATH="/app/.venv/bin:$PATH"

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT={{ cookiecutter.app_port }}
{% if cookiecutter.api_framework == 'fastapi' %}
# Expose the application port
EXPOSE {{ cookiecutter.app_port }}

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:{{ cookiecutter.app_port }}/health')" || exit 1

# Default command: run the API server
CMD ["python", "-m", "uvicorn", "{{ cookiecutter.project_slug|replace('-', '_') }}.api.main:app", "--host", "0.0.0.0", "--port", "{{ cookiecutter.app_port }}"]
{% else %}
# Default command: run the CLI help
CMD ["{{ cookiecutter.project_slug|replace('-', '_') }}", "--help"]
{% endif %}
