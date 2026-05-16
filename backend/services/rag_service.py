from typing import List

from ..models.memory_models import MemoryRecord
from .memory_service import MemoryService


class RAGService:
    def __init__(self):
        self._memory_service = MemoryService()

    def build_context(self, query: str, limit: int = 5) -> str:
        memories = self._memory_service.search_memory(query, limit=limit)
        return self._format_context(memories)

    def _format_context(self, memories: List[MemoryRecord]) -> str:
        if not memories:
            return ""

        lines = ["RELEVANT MEMORIES:"]
        for memory in memories:
            lines.append(f"- {memory.content}")
        return "\n".join(lines)
