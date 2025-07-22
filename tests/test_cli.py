from typer.testing import CliRunner
from unittest.mock import patch, Mock
from cli import app

runner = CliRunner()

def test_people_help():
    result = runner.invoke(app, ["people", "--help"])
    assert result.exit_code == 0
    assert "List Star Wars people" in result.stdout

def test_planets_help():
    result = runner.invoke(app, ["planets", "--help"])
    assert result.exit_code == 0
    assert "List Star Wars planets" in result.stdout

@patch('httpx.get')
def test_people_command(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "results": [{"name": "Luke", "height": "172", "mass": "77", "birth_year": "19BBY"}],
        "count": 1
    }
    mock_get.return_value = mock_response
    
    result = runner.invoke(app, ["people"])
    assert result.exit_code == 0
    mock_get.assert_called_once()

@patch('httpx.get')
def test_planets_command(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "results": [{"name": "Tatooine", "climate": "arid", "terrain": "desert", "population": "200000"}],
        "count": 1
    }
    mock_get.return_value = mock_response
    
    result = runner.invoke(app, ["planets"])
    assert result.exit_code == 0
    mock_get.assert_called_once()

@patch('httpx.get')
def test_people_with_search(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"results": [], "count": 0}
    mock_get.return_value = mock_response
    
    result = runner.invoke(app, ["people", "--search", "luke"])
    assert result.exit_code == 0
    mock_get.assert_called_with("http://localhost:8000/people", params={"page": 1, "search": "luke"})