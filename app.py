from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from chat import chat

app = FastAPI(
    title="SHL Assessment Recommender",
    version="1.0.0"
)


# -----------------------------
# Request / Response Models
# -----------------------------

class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    message: str
    history: List[Message] = []


class ChatResponse(BaseModel):
    response: str


# -----------------------------
# Health Endpoint
# -----------------------------

@app.get("/health")
def health():
    return {
        "status": "ok"
    }


# -----------------------------
# Chat Endpoint
# -----------------------------

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):

    history = [
        {
            "role": msg.role,
            "content": msg.content
        }
        for msg in request.history
    ]

    answer = chat(request.message)

    return ChatResponse(
        response=answer
    )