"""CLI application entry point.

Command-line interface using Typer that delegates to services.
"""

from __future__ import annotations

import asyncio
from typing import Annotated
from uuid import UUID

import typer
from rich.console import Console
from rich.table import Table

from ..adapters.repositories import InMemoryUserRepository
from ..infrastructure.config import get_settings
from ..services import UserService

app = typer.Typer(
    name="{{ cookiecutter.project_slug }}",
    help="{{ cookiecutter.project_description }}",
    add_completion=False,
)
console = Console()

# Service instance (in real app, use proper dependency injection)
_repository = InMemoryUserRepository()
_service = UserService(_repository)


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
    username: str = typer.Argument(..., help="Username (unique, min 3 characters)"),
    email: str = typer.Argument(..., help="Email address"),
    display_name: str = typer.Option("", "--display-name", "-n", help="Display name"),
) -> None:
    """Create a new user."""
    try:
        user = run_async(_service.create(username, email, display_name))
        console.print(f"[green]Created user:[/green] {user.id}")
        console.print(f"  Username: {user.username}")
        console.print(f"  Email: {user.email}")
        if user.display_name:
            console.print(f"  Display Name: {user.display_name}")
    except ValueError as e:
        console.print(f"[red]Error:[/red] {e}")
        raise typer.Exit(1) from None


@app.command()
def get(
    user_id: Annotated[UUID, typer.Argument(help="User UUID")],
) -> None:
    """Get a user by ID."""
    user = run_async(_service.get_by_id(user_id))
    if not user:
        console.print(f"[red]User not found:[/red] {user_id}")
        raise typer.Exit(1)

    table = Table(title="User Details")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("ID", str(user.id))
    table.add_row("Username", user.username)
    table.add_row("Email", user.email)
    table.add_row("Display Name", user.display_name or "-")
    table.add_row("Created", str(user.created_at))

    console.print(table)


@app.command("list")
def list_users() -> None:
    """List all users."""
    users = run_async(_service.list_all())

    if not users:
        console.print("[yellow]No users found.[/yellow]")
        return

    table = Table(title=f"Users ({len(users)} total)")
    table.add_column("ID", style="dim")
    table.add_column("Username", style="cyan")
    table.add_column("Email", style="green")
    table.add_column("Display Name")
    table.add_column("Created", style="dim")

    for user in users:
        table.add_row(
            str(user.id)[:8] + "...",
            user.username,
            user.email,
            user.display_name or "-",
            str(user.created_at.date()),
        )

    console.print(table)


@app.command()
def delete(
    user_id: Annotated[UUID, typer.Argument(help="User UUID to delete")],
    force: bool = typer.Option(False, "--force", "-f", help="Skip confirmation"),
) -> None:
    """Delete a user by ID."""
    user = run_async(_service.get_by_id(user_id))
    if not user:
        console.print(f"[red]User not found:[/red] {user_id}")
        raise typer.Exit(1)

    if not force:
        typer.confirm(
            f"Delete user '{user.username}' ({user_id})?",
            abort=True,
        )

    deleted = run_async(_service.delete(user_id))
    if deleted:
        console.print(f"[green]Deleted user:[/green] {user.username}")
    else:
        console.print(f"[red]Failed to delete user:[/red] {user_id}")
        raise typer.Exit(1)

{%- if cookiecutter.api_framework == 'fastapi' %}


@app.command()
def serve(
    host: str | None = typer.Option(None, "--host", "-h", help="Host to bind to"),
    port: int | None = typer.Option(None, "--port", "-p", help="Port to bind to"),
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
{%- endif %}


def main() -> None:
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
