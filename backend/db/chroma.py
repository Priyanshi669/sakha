from chromadb import PersistentClient
from chromadb.utils import embedding_functions

from ..core.config import get_settings


def get_client(path: str):
    return PersistentClient(path=path)


def get_collection(client: PersistentClient, name: str):
    settings = get_settings()
    embedder = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=settings.embedding_model
    )
    return client.get_or_create_collection(name=name, embedding_function=embedder)
