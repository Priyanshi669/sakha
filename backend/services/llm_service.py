from typing import Optional

import ollama

from ..core.config import get_settings
from ..core.prompts import SYSTEM_PROMPT


class LLMService:
    def __init__(self):
        settings = get_settings()
        self._model = settings.llm_model
        self._client = ollama.Client(host=settings.ollama_host)

    def generate_response(
        self,
        message: str,
        system_prompt: Optional[str] = None,
        context_block: str = "",
    ) -> str:
        prompt = system_prompt or SYSTEM_PROMPT
        context_section = f"\n\n{context_block}" if context_block else ""
        full_prompt = f"{prompt}{context_section}\n\nUser: {message}\nAssistant:"

        try:
            result = self._client.generate(model=self._model, prompt=full_prompt)
        except Exception as exc:
            raise RuntimeError("LLM request failed") from exc

        return result.get("response", "").strip()
