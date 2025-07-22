import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_people_endpoint():
    response = client.get("/people")
    assert response.status_code == 200
    data = response.json()
    assert "results" in data

def test_people_pagination():
    response = client.get("/people?page=2")
    assert response.status_code == 200

def test_people_search():
    response = client.get("/people?search=luke")
    assert response.status_code == 200

def test_people_sort():
    response = client.get("/people?sort_by=name")
    assert response.status_code == 200

def test_planets_endpoint():
    response = client.get("/planets")
    assert response.status_code == 200
    data = response.json()
    assert "results" in data

def test_ai_insight():
    response = client.get("/simulate-ai-insight?type=person&name=Luke")
    assert response.status_code == 200
    data = response.json()
    assert "insight" in data