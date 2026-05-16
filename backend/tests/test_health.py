import os

from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_health_response_shape():
    response = client.get("/health")
    assert response.status_code == 200

    payload = response.json()
    assert "status" in payload
    assert "ollama" in payload
    assert "model" in payload


def test_health_ollama_connected_if_enabled():
    if os.getenv("OLLAMA_INTEGRATION") != "1":
        return

    response = client.get("/health")
    payload = response.json()

    assert payload["ollama"] == "connected"
    assert payload["status"] in {"healthy", "degraded"}
