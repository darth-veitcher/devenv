{%- if cookiecutter.api_framework == 'fastapi' -%}
"""API layer - REST API presentation interface.

FastAPI application exposing business logic as RESTful endpoints.
"""
{%- else -%}
"""API layer - Not enabled.

To enable the API layer, set api_framework to 'fastapi' when generating the project.
"""
{%- endif %}
