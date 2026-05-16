from fastapi import APIRouter

from ...models.chat_models import ChatRequest, ChatResponse
from ...services.llm_service import LLMService

router = APIRouter(prefix="/chat", tags=["chat"])
llm_service = LLMService()


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):
    response_text = llm_service.generate_response(request.message)
    return ChatResponse(response=response_text)
