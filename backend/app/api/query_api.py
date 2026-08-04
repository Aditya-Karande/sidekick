from fastapi import APIRouter
from routers.query_route import query_process
from models.schemas import ChatRequest, ChatResponse
from services.chatbot import chatbot
import uuid
from langchain.messages import HumanMessage

query_router = APIRouter(prefix="/chat",tags=["Chat"])

@query_router.post("/", response_model=ChatResponse)
def chat(req:ChatRequest):

    thread_id = req.thread_id or str(uuid.uuid4())
    CONFIG = {"configurable":{"thread_id":thread_id}}

    res = chatbot.invoke(
        {"messages":[HumanMessage(content=req.req)]},
        config=CONFIG
    )

    reply = res['messages'][-1].content
    
    return ChatResponse(res=reply, thread_id=thread_id)

@query_router.get("/{thread_id}/history")
def get_history(thread_id:str):

    CONFIG = {"configurable":{"thread_id":thread_id}}

    state = chatbot.get_state(config=CONFIG)

    messages = state.values.get("messages",[])

    return {
        "thread_id": thread_id,
        "messages": [
            {"role": m.type, "content": m.content} for m in messages
        ],
    }
