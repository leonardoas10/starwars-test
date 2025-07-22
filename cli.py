import typer
import httpx
from rich.console import Console
from rich.table import Table
from typing import Optional
import os

app = typer.Typer()
console = Console()

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

@app.command()
def people(
    page: int = typer.Option(1, "--page", "-p", help="Page number"),
    search: Optional[str] = typer.Option(None, "--search", "-s", help="Search by name"),
    sort_by: Optional[str] = typer.Option(None, "--sort-by", help="Sort by field (name, created, edited)"),
    order: str = typer.Option("asc", "--order", "-o", help="Sort order (asc, desc)")
):
    """List Star Wars people"""
    params = {"page": page}
    if search:
        params["search"] = search
    if sort_by:
        params["sort_by"] = f"-{sort_by}" if order == "desc" else sort_by
    
    try:
        with console.status("[bold green]Fetching people data...", spinner="dots"):
            response = httpx.get(f"{API_BASE_URL}/people", params=params)
            data = response.json()
        
        table = Table(title="Star Wars People")
        table.add_column("Name", style="cyan")
        table.add_column("Height", style="magenta")
        table.add_column("Mass", style="green")
        table.add_column("Birth Year", style="yellow")
        
        for person in data.get("results", []):
            table.add_row(
                person.get("name", ""),
                person.get("height", ""),
                person.get("mass", ""),
                person.get("birth_year", "")
            )
        
        console.print(table)
        console.print(f"Page {page} of {(data.get('count', 0) + 9) // 10}")
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@app.command()
def planets(
    page: int = typer.Option(1, "--page", "-p", help="Page number"),
    search: Optional[str] = typer.Option(None, "--search", "-s", help="Search by name"),
    sort_by: Optional[str] = typer.Option(None, "--sort-by", help="Sort by field (name, created, edited)"),
    order: str = typer.Option("asc", "--order", "-o", help="Sort order (asc, desc)")
):
    """List Star Wars planets"""
    params = {"page": page}
    if search:
        params["search"] = search
    if sort_by:
        params["sort_by"] = f"-{sort_by}" if order == "desc" else sort_by
    
    try:
        with console.status("[bold green]Fetching planets data...", spinner="dots"):
            response = httpx.get(f"{API_BASE_URL}/planets", params=params)
            data = response.json()
        
        table = Table(title="Star Wars Planets")
        table.add_column("Name", style="cyan")
        table.add_column("Climate", style="magenta")
        table.add_column("Terrain", style="green")
        table.add_column("Population", style="yellow")
        
        for planet in data.get("results", []):
            table.add_row(
                planet.get("name", ""),
                planet.get("climate", ""),
                planet.get("terrain", ""),
                planet.get("population", "")
            )
        
        console.print(table)
        console.print(f"Page {page} of {(data.get('count', 0) + 9) // 10}")
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

if __name__ == "__main__":
    app()