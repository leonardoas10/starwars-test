from fastapi import FastAPI, Query
from typing import Optional, Dict, Any
import httpx
import os
import logging
from datetime import datetime

app = FastAPI(title="Star Wars API", version="1.0.0")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SWAPI_BASE_URL = os.getenv("SWAPI_BASE_URL", "https://swapi.dev/api")

@app.get("/people")
async def get_people(
    page: int = Query(1, ge=1),
    search: Optional[str] = None,
    sort_by: Optional[str] = Query(None, regex="^(name|created|edited)$")
) -> Dict[str, Any]:
    # Log request
    logger.info(f"People request - page: {page}, search: {search}, sort_by: {sort_by} at {datetime.now()}")
    
    async with httpx.AsyncClient(verify=False) as client:
        url = f"{SWAPI_BASE_URL}/people/"
        params = {"page": page}
        if search:
            params["search"] = search
        
        response = await client.get(url, params=params)
        data = response.json()
        
        if sort_by and "results" in data:
            reverse = sort_by.startswith("-")
            sort_key = sort_by.lstrip("-")
            data["results"] = sorted(data["results"], key=lambda x: x.get(sort_key, ""), reverse=reverse)
        
        return data

@app.get("/planets")
async def get_planets(
    page: int = Query(1, ge=1),
    search: Optional[str] = None,
    sort_by: Optional[str] = Query(None, regex="^(name|created|edited)$")
) -> Dict[str, Any]:
    # Log request
    logger.info(f"Planets request - page: {page}, search: {search}, sort_by: {sort_by} at {datetime.now()}")
    
    async with httpx.AsyncClient(verify=False) as client:
        url = f"{SWAPI_BASE_URL}/planets/"
        params = {"page": page}
        if search:
            params["search"] = search
        
        response = await client.get(url, params=params)
        data = response.json()
        
        if sort_by and "results" in data:
            reverse = sort_by.startswith("-")
            sort_key = sort_by.lstrip("-")
            data["results"] = sorted(data["results"], key=lambda x: x.get(sort_key, ""), reverse=reverse)
        
        return data

@app.get("/simulate-ai-insight")
async def simulate_ai_insight(
    type: str = Query(..., regex="^(person|planet)$"),
    name: str = Query(...)
):
    insights = {
        "person": f"{name} is a fascinating character in the Star Wars universe with unique abilities and compelling storylines.",
        "planet": f"{name} is a remarkable world with diverse ecosystems and rich cultural heritage in the galaxy."
    }
    return {"insight": insights[type]}