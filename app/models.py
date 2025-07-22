from pydantic import BaseModel
from typing import List, Optional, Any

class Person(BaseModel):
    name: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    homeworld: str
    films: List[str]
    species: List[str]
    vehicles: List[str]
    starships: List[str]
    created: str
    edited: str
    url: str

class Planet(BaseModel):
    name: str
    rotation_period: str
    orbital_period: str
    diameter: str
    climate: str
    gravity: str
    terrain: str
    surface_water: str
    population: str
    residents: List[str]
    films: List[str]
    created: str
    edited: str
    url: str

class PeopleResponse(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[Any]

class PlanetsResponse(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[Any]