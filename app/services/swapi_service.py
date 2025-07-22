from typing import Dict, Any, Optional
from ..providers.container import container

class SWAPIService:
    def __init__(self):
        self.data_provider = container.data_provider
    
    async def get_people(self, page: int, search: Optional[str] = None, sort_by: Optional[str] = None) -> Dict[str, Any]:
        return await self.data_provider.get_people(page, search, sort_by)
    
    async def get_planets(self, page: int, search: Optional[str] = None, sort_by: Optional[str] = None) -> Dict[str, Any]:
        return await self.data_provider.get_planets(page, search, sort_by)

class AIService:
    def __init__(self):
        self.insight_provider = container.insight_provider
    
    def generate_insight(self, type: str, name: str) -> str:
        return self.insight_provider.generate_insight(type, name)