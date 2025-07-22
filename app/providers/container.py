from .interfaces import DataProvider, InsightProvider
from .swapi_provider import SWAPIProvider
from .ai_provider import MockAIProvider

class Container:
    def __init__(self):
        self._data_provider = None
        self._insight_provider = None
    
    @property
    def data_provider(self) -> DataProvider:
        if self._data_provider is None:
            self._data_provider = SWAPIProvider()
        return self._data_provider
    
    @property
    def insight_provider(self) -> InsightProvider:
        if self._insight_provider is None:
            self._insight_provider = MockAIProvider()
        return self._insight_provider

# Global container instance
container = Container()