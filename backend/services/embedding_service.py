from typing import List

from sentence_transformers import SentenceTransformer

from ..core.config import get_settings


class EmbeddingService:
    def __init__(self):
        settings = get_settings()
        self._model = SentenceTransformer(settings.embedding_model)

    def embed_text(self, text: str) -> List[float]:
        return self._model.encode([text])[0].tolist()
