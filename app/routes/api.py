from fastapi import APIRouter, Query, HTTPException, Depends
from typing import Optional, Dict, Any
from ..services.swapi_service import SWAPIService, AIService
from ..models.common import APIResponse
from ..models.ai_insight import AIInsightResponse

router = APIRouter()

def get_swapi_service() -> SWAPIService:
    return SWAPIService()

def get_ai_service() -> AIService:
    return AIService()

@router.get("/people", response_model=Dict[str, Any])
async def get_people(
    page: int = Query(1, ge=1, description="Page number"),
    search: Optional[str] = Query(None, description="Search by name"),
    sort_by: Optional[str] = Query(None, pattern="^(name|created|edited)$", description="Sort field"),
    service: SWAPIService = Depends(get_swapi_service)
):
    """Get Star Wars people with pagination, search, and sorting."""
    try:
        return await service.get_people(page, search, sort_by)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/planets", response_model=Dict[str, Any])
async def get_planets(
    page: int = Query(1, ge=1, description="Page number"),
    search: Optional[str] = Query(None, description="Search by name"),
    sort_by: Optional[str] = Query(None, pattern="^(name|created|edited)$", description="Sort field"),
    service: SWAPIService = Depends(get_swapi_service)
):
    """Get Star Wars planets with pagination, search, and sorting."""
    try:
        return await service.get_planets(page, search, sort_by)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/simulate-ai-insight", response_model=AIInsightResponse)
async def simulate_ai_insight(
    type: str = Query(..., pattern="^(person|planet)$", description="Type of insight"),
    name: str = Query(..., description="Name for insight generation"),
    service: AIService = Depends(get_ai_service)
):
    """Generate AI insights for Star Wars characters or planets."""
    try:
        insight = service.generate_insight(type, name)
        return AIInsightResponse(insight=insight)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))