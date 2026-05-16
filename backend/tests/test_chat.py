import os

import pytest
from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_chat_handles_llm_failure(monkeypatch):
    from backend.api.routes import chat as chat_route

    class FakeLLM:
        def generate_response(self, *args, **kwargs):
            raise RuntimeError("timeout")

    chat_route.llm_service = FakeLLM()

    response = client.post("/chat", json={"message": "hello"})
    assert response.status_code == 503


def test_chat_integration_with_ollama():
    if os.getenv("OLLAMA_INTEGRATION") != "1":
        pytest.skip("Set OLLAMA_INTEGRATION=1 to run integration test")

    response = client.post("/chat", json={"message": "Hello"})
    assert response.status_code == 200

    payload = response.json()
    assert payload["response"]
    assert len(payload["response"]) > 0
