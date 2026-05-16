from fastapi import APIRouter, Query

from ...models.memory_models import MemoryRecord, MemorySearchResponse, MemoryStoreRequest
from ...services.memory_service import MemoryService

router = APIRouter(prefix="/memory", tags=["memory"])
memory_service = MemoryService()


@router.get("/search", response_model=MemorySearchResponse)
def search_memory(q: str = Query(..., min_length=1)):
    results = memory_service.search_memory(q)
    return MemorySearchResponse(query=q, results=results)


@router.post("/store", response_model=MemoryRecord)
def store_memory(payload: MemoryStoreRequest):
    memory_service.store_memory(
        payload.content,
        memory_type=payload.memory_type,
        importance_score=payload.importance_score,
    )
    return MemoryRecord(
        content=payload.content,
        memory_type=payload.memory_type,
        score=payload.importance_score,
    )
