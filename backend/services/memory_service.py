from typing import List

from ..models.memory_models import MemoryRecord


class MemoryService:
    def store_memory(self, content: str, memory_type: str) -> MemoryRecord:
        return MemoryRecord(content=content, memory_type=memory_type, score=1.0)

    def search_memory(self, query: str) -> List[MemoryRecord]:
        return []
