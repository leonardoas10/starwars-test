import typer
from .commands import people, planets

app = typer.Typer()
app.command()(people)
app.command()(planets)