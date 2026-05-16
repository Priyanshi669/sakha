from typing import List

from pydantic import BaseModel


class MemoryRecord(BaseModel):
    content: str
    memory_type: str
    score: float


class MemorySearchResponse(BaseModel):
    query: str
    results: List[MemoryRecord]
