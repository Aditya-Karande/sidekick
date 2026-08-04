from pydantic import BaseModel

class ChatRequest(BaseModel):
    req: str
    thread_id: str | None = None

class ChatResponse(BaseModel):
    res: str
    thread_id: str