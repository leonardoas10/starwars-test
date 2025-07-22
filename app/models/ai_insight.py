from pydantic import BaseModel, Field

class AIInsightRequest(BaseModel):
    type: str = Field(..., pattern="^(person|planet)$")
    name: str

class AIInsightResponse(BaseModel):
    insight: str