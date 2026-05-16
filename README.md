# Sakha - Personal AI OS (Phase 1)

Sakha is a local, production-minded AI assistant with persistent memory. It exposes a FastAPI backend for chat, memory storage, and retrieval, backed by Ollama for local LLM inference and ChromaDB for vector search. This repo also includes a legacy analytics module for activity insights.

## What this project does

- Local LLM chat via Ollama
- Persistent memory storage (SQLite + ChromaDB)
- Memory retrieval and context injection (RAG)
- Health checks for model availability
- Legacy activity insights endpoint

## Tech stack

- FastAPI + Uvicorn
- SQLAlchemy + SQLite
- ChromaDB (persistent vector store)
- Ollama (local LLM runtime)
- Sentence-Transformers (embeddings)
- Pytest (tests)

## Architecture (Phase 1)

The backend is split into services:

- `LLMService`: builds prompts and calls Ollama
- `MemoryService`: stores conversations in SQLite and memories in ChromaDB
- `RAGService`: retrieves top memories and formats context
- `EmbeddingService`: sentence-transformers embeddings (used by ChromaDB)

## API endpoints

Base URL: `http://localhost:8000`

- `GET /health` - Checks API and Ollama connectivity
- `POST /chat` - Chat with context injection and memory writes
- `GET /memory/search?q=...` - Search stored memories
- `POST /memory/store` - Store a memory record
- `GET /insights` - Legacy activity insights (reads from `sakha.db`)

### Example requests

```bash
curl http://localhost:8000/health
```

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Help me improve networking"}'
```

```bash
curl "http://localhost:8000/memory/search?q=focus+time"
```

```bash
curl -X POST http://localhost:8000/memory/store \
  -H "Content-Type: application/json" \
  -d '{"content":"User prefers concise answers","memory_type":"semantic","importance_score":0.8}'
```

## Project structure

```
.
├── app/                       # Legacy analytics module
│   ├── analyzer.py
│   ├── crud.py
│   ├── database.py            # SQLite database: sakha.db
│   ├── models.py
│   ├── routes/insights.py
│   └── schemas.py
├── backend/                   # FastAPI backend
│   ├── api/routes/            # /chat, /memory, /health
│   ├── core/                  # settings, prompts, security
│   ├── db/                    # sqlite + chroma clients
│   ├── models/                # pydantic + sqlalchemy models
│   ├── services/              # llm, memory, rag
│   └── main.py                # FastAPI app
├── data/                      # ChromaDB persistence
├── requirements.txt
└── plan.md                    # Phase 1 architecture notes
```

## Setup

### 1) Install Ollama and pull a model

Install Ollama from https://ollama.com and pull a model that matches the config (default is `phi4`).

```bash
ollama pull phi4
```

### 2) Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

- Windows PowerShell:
  ```bash
  .\.venv\Scripts\Activate.ps1
  ```
- macOS/Linux:
  ```bash
  source .venv/bin/activate
  ```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Run the API

```bash
uvicorn backend.main:app --reload
```

The API will be available at http://localhost:8000

## Configuration

Environment variables (defaults shown):

- `PAIOS_ENV=local`
- `PAIOS_LLM_MODEL=phi4`
- `OLLAMA_HOST=http://localhost:11434`
- `PAIOS_SQLITE_URL=sqlite:///./data/paios.db`
- `PAIOS_CHROMA_COLLECTION=memories`
- `PAIOS_EMBEDDING_MODEL=all-MiniLM-L6-v2`
- `PAIOS_CHROMA_PATH=./data/chroma`

## Persistence

- Conversations + memory metadata are stored in SQLite (`./data/paios.db`)
- Vector embeddings are stored in ChromaDB (`./data/chroma/`)
- Legacy analytics uses `./sakha.db`

## Tests

```bash
pytest
```

## Notes

- The legacy `app/` module exposes `/insights` and is mounted into the main API.
- Memory writes are keyword-triggered; adjust logic in `MemoryService._should_store_memory` if needed.

## License

Add a license if you plan to open source this repository.
