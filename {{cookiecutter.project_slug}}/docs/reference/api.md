# API Reference

Auto-generated documentation for the API layer.

## FastAPI Application

::: {{ cookiecutter.project_slug|replace('-', '_') }}.api.main
    options:
      show_root_heading: true
      show_source: true
      members:
        - app
        - CreateEntityRequest
        - EntityResponse
        - HealthResponse
        - root
        - health
        - create_entity
        - get_entity
        - delete_entity

## CLI Application

::: {{ cookiecutter.project_slug|replace('-', '_') }}.cli.main
    options:
      show_root_heading: true
      show_source: true
      members:
        - app
        - version
        - config
        - create
        - get
        - serve
        - main
