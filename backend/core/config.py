import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    environment: str = os.getenv("PAIOS_ENV", "local")
    llm_model: str = os.getenv("PAIOS_LLM_MODEL", "phi4")
    chroma_path: str = os.getenv("PAIOS_CHROMA_PATH", "./data/chroma")


_settings = None


def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings
