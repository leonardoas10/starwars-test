import pytest
from typer.testing import CliRunner
from cli import app

runner = CliRunner()

def test_people_command():
    result = runner.invoke(app, ["people", "--help"])
    assert result.exit_code == 0
    assert "List Star Wars people" in result.stdout

def test_planets_command():
    result = runner.invoke(app, ["planets", "--help"])
    assert result.exit_code == 0
    assert "List Star Wars planets" in result.stdout

def test_people_with_page():
    result = runner.invoke(app, ["people", "--page", "1"])
    assert result.exit_code == 0

def test_people_with_search():
    result = runner.invoke(app, ["people", "--search", "luke"])
    assert result.exit_code == 0

def test_people_with_sort():
    result = runner.invoke(app, ["people", "--sort-by", "name"])
    assert result.exit_code == 0