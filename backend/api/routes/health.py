from fastapi import APIRouter
import ollama

from ...core.config import get_settings

router = APIRouter(tags=["health"])


@router.get("/health")
def health_check():
    settings = get_settings()
    status = "healthy"
    ollama_status = "connected"

    try:
        client = ollama.Client(host=settings.ollama_host)
        models = client.list().get("models", [])
        model_names = {model.get("name") for model in models}
        if settings.llm_model not in model_names:
            status = "degraded"
    except Exception:
        status = "degraded"
        ollama_status = "disconnected"

    return {
        "status": status,
        "ollama": ollama_status,
        "model": settings.llm_model,
    }
