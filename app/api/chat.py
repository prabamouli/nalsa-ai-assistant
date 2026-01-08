from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # Placeholder — RAG comes later
    return ChatResponse(
        answer="This is a placeholder response from NALSA AI."
    )
