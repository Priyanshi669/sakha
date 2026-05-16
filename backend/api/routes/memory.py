from fastapi import APIRouter, Query

from ...models.memory_models import MemorySearchResponse
from ...services.memory_service import MemoryService

router = APIRouter(prefix="/memory", tags=["memory"])
memory_service = MemoryService()


@router.get("/search", response_model=MemorySearchResponse)
def search_memory(q: str = Query(..., min_length=1)):
    results = memory_service.search_memory(q)
    return MemorySearchResponse(query=q, results=results)
