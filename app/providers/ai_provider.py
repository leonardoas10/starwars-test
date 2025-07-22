from .interfaces import InsightProvider

class MockAIProvider(InsightProvider):
    def generate_insight(self, type: str, name: str) -> str:
        insights = {
            "person": f"{name} is a fascinating character in the Star Wars universe with unique abilities and compelling storylines.",
            "planet": f"{name} is a remarkable world with diverse ecosystems and rich cultural heritage in the galaxy."
        }
        return insights[type]