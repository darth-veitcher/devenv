"""CLI application entry point.

Command-line interface using Typer that delegates to services.
"""

from __future__ import annotations

import asyncio
from typing import Optional
from uuid import UUID

import typer
from rich.console import Console
from rich.table import Table

from ..adapters.repositories import InMemoryExampleRepository
from ..infrastructure.config import get_settings
from ..services import ExampleService

app = typer.Typer(
    name="{{ cookiecutter.project_slug }}",
    help="{{ cookiecutter.project_description }}",
    add_completion=False,
)
console = Console()

# Service instance (in real app, use proper dependency injection)
_repository = InMemoryExampleRepository()
_service = ExampleService(_repository)


def run_async(coro):
    """Helper to run async functions from sync CLI."""
    return asyncio.get_event_loop().run_until_complete(coro)


@app.command()
def version() -> None:
    """Show version information."""
    from .. import __version__

    console.print(f"{{ cookiecutter.project_name }} v{__version__}")


@app.command()
def config() -> None:
    """Show current configuration."""
    settings = get_settings()

    table = Table(title="Configuration")
    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("App Name", settings.app_name)
    table.add_row("Debug", str(settings.debug))
    table.add_row("Host", settings.host)
    table.add_row("Port", str(settings.port))
    table.add_row("Database", settings.database_url or "Not configured")

    console.print(table)


@app.command()
def create(
    name: str = typer.Argument(..., help="Entity name"),
    description: str = typer.Option("", "--description", "-d", help="Entity description"),
) -> None:
    """Create a new entity."""
    try:
        entity = run_async(_service.create(name, description))
        console.print(f"[green]Created entity:[/green] {entity.id}")
        console.print(f"  Name: {entity.name}")
        if entity.description:
            console.print(f"  Description: {entity.description}")
    except ValueError as e:
        console.print(f"[red]Error:[/red] {e}")
        raise typer.Exit(1)


@app.command()
def get(
    entity_id: UUID = typer.Argument(..., help="Entity UUID"),
) -> None:
    """Get an entity by ID."""
    entity = run_async(_service.get_by_id(entity_id))
    if not entity:
        console.print(f"[red]Entity not found:[/red] {entity_id}")
        raise typer.Exit(1)

    table = Table(title="Entity Details")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("ID", str(entity.id))
    table.add_row("Name", entity.name)
    table.add_row("Description", entity.description or "-")
    table.add_row("Created", str(entity.created_at))

    console.print(table)


@app.command()
def serve(
    host: Optional[str] = typer.Option(None, "--host", "-h", help="Host to bind to"),
    port: Optional[int] = typer.Option(None, "--port", "-p", help="Port to bind to"),
) -> None:
    """Start the API server."""
    import uvicorn

    from ..api.main import app as api_app

    settings = get_settings()
    uvicorn.run(
        api_app,
        host=host or settings.host,
        port=port or settings.port,
    )


def main() -> None:
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
