from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

class DataProvider(ABC):
    @abstractmethod
    async def get_people(self, page: int, search: Optional[str] = None, sort_by: Optional[str] = None) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    async def get_planets(self, page: int, search: Optional[str] = None, sort_by: Optional[str] = None) -> Dict[str, Any]:
        pass

class InsightProvider(ABC):
    @abstractmethod
    def generate_insight(self, type: str, name: str) -> str:
        pass