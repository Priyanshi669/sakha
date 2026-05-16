import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    environment: str = os.getenv("PAIOS_ENV", "local")
    llm_model: str = os.getenv("PAIOS_LLM_MODEL", "phi4")
    ollama_host: str = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    sqlite_url: str = os.getenv("PAIOS_SQLITE_URL", "sqlite:///./data/paios.db")
    chroma_collection: str = os.getenv("PAIOS_CHROMA_COLLECTION", "memories")
    embedding_model: str = os.getenv(
        "PAIOS_EMBEDDING_MODEL",
        "all-MiniLM-L6-v2",
    )
    chroma_path: str = os.getenv("PAIOS_CHROMA_PATH", "./data/chroma")


_settings = None


def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings
