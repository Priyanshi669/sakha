from typing import List

from pydantic import BaseModel, Field


class MemoryRecord(BaseModel):
    content: str
    memory_type: str
    score: float


class MemoryStoreRequest(BaseModel):
    content: str = Field(..., min_length=1)
    memory_type: str = "semantic"
    importance_score: float = Field(1.0, ge=0.0, le=1.0)


class MemorySearchResponse(BaseModel):
    query: str
    results: List[MemoryRecord]
