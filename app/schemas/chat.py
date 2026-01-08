from typing import Optional
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    language: Optional[str] = "en"

class ChatResponse(BaseModel):
    answer: str
