from typing import List, Optional
from uuid import uuid4

from ..core.config import get_settings
from ..db.chroma import get_client, get_collection
from ..db.sqlite import SessionLocal
from ..models.db_models import Conversation, Memory
from ..models.memory_models import MemoryRecord


class MemoryService:
    def __init__(self):
        settings = get_settings()
        client = get_client(settings.chroma_path)
        self._collection = get_collection(client, settings.chroma_collection)

    def store_conversation(
        self,
        user_message: str,
        assistant_response: str,
        session_id: Optional[str] = None,
    ) -> None:
        db = SessionLocal()
        try:
            record = Conversation(
                session_id=session_id or "default",
                user_message=user_message,
                assistant_response=assistant_response,
            )
            db.add(record)
            db.commit()
        finally:
            db.close()

    def store_memory(
        self,
        content: str,
        memory_type: str = "semantic",
        importance_score: float = 1.0,
    ) -> None:
        chroma_id = f"mem-{uuid4()}"
        self._collection.add(
            documents=[content],
            ids=[chroma_id],
            metadatas=[{"memory_type": memory_type, "importance_score": importance_score}],
        )

        db = SessionLocal()
        try:
            record = Memory(
                content=content,
                memory_type=memory_type,
                importance_score=importance_score,
                chroma_id=chroma_id,
            )
            db.add(record)
            db.commit()
        finally:
            db.close()

    def store_memory_if_relevant(self, content: str, memory_type: str = "semantic") -> None:
        if not self._should_store_memory(content):
            return

        self.store_memory(content, memory_type=memory_type, importance_score=1.0)

    def search_memory(self, query: str, limit: int = 5) -> List[MemoryRecord]:
        results = self._collection.query(query_texts=[query], n_results=limit)
        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        memories: List[MemoryRecord] = []
        for content, metadata, distance in zip(documents, metadatas, distances):
            score = 1.0 - float(distance) if distance is not None else 0.0
            memory_type = (metadata or {}).get("memory_type", "semantic")
            memories.append(
                MemoryRecord(content=content, memory_type=memory_type, score=round(score, 4))
            )

        return memories

    def _should_store_memory(self, content: str) -> bool:
        lowered = content.lower()
        keywords = [
            "goal",
            "prefer",
            "preference",
            "struggle",
            "weak",
            "improve",
            "project",
            "interest",
            "avoid",
        ]
        return any(keyword in lowered for keyword in keywords)
