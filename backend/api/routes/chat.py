from fastapi import APIRouter, HTTPException

from ...models.chat_models import ChatRequest, ChatResponse
from ...services.llm_service import LLMService
from ...services.memory_service import MemoryService
from ...services.rag_service import RAGService

router = APIRouter(prefix="/chat", tags=["chat"])
llm_service = LLMService()
memory_service = MemoryService()
rag_service = RAGService()


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):
    context_block = rag_service.build_context(request.message)
    try:
        response_text = llm_service.generate_response(
            request.message,
            context_block=context_block,
        )
    except RuntimeError:
        raise HTTPException(status_code=503, detail="LLM unavailable")

    memory_service.store_conversation(request.message, response_text)
    memory_service.store_memory_if_relevant(request.message)
    memory_service.store_memory_if_relevant(response_text, memory_type="assistant")

    return ChatResponse(response=response_text)
