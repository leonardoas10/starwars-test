from pydantic import BaseModel, Field
from typing import List, Optional, Any

class PaginationParams(BaseModel):
    page: int = Field(1, ge=1, description="Page number")
    search: Optional[str] = Field(None, description="Search term")
    sort_by: Optional[str] = Field(None, pattern="^(name|created|edited)$", description="Sort field")

class APIResponse(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[Any]