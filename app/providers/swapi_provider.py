import httpx
import os
from typing import Dict, Any, Optional
import logging
from datetime import datetime
from .interfaces import DataProvider

logger = logging.getLogger(__name__)

class SWAPIProvider(DataProvider):
    def __init__(self):
        self.base_url = os.getenv("SWAPI_BASE_URL", "https://swapi.dev/api")
    
    async def get_people(self, page: int, search: Optional[str] = None, sort_by: Optional[str] = None) -> Dict[str, Any]:
        logger.info(f"People request - page: {page}, search: {search}, sort_by: {sort_by} at {datetime.now()}")
        
        async with httpx.AsyncClient(verify=False) as client:
            url = f"{self.base_url}/people/"
            params = {"page": page}
            if search:
                params["search"] = search
            
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            if sort_by and "results" in data:
                reverse = sort_by.startswith("-")
                sort_key = sort_by.lstrip("-")
                data["results"] = sorted(data["results"], key=lambda x: x.get(sort_key, ""), reverse=reverse)
            
            return data
    
    async def get_planets(self, page: int, search: Optional[str] = None, sort_by: Optional[str] = None) -> Dict[str, Any]:
        logger.info(f"Planets request - page: {page}, search: {search}, sort_by: {sort_by} at {datetime.now()}")
        
        async with httpx.AsyncClient(verify=False) as client:
            url = f"{self.base_url}/planets/"
            params = {"page": page}
            if search:
                params["search"] = search
            
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            if sort_by and "results" in data:
                reverse = sort_by.startswith("-")
                sort_key = sort_by.lstrip("-")
                data["results"] = sorted(data["results"], key=lambda x: x.get(sort_key, ""), reverse=reverse)
            
            return data