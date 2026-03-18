from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from app.database import fetch_message

router = APIRouter(prefix="/api", tags=["test"])

@router.get("/message", response_class=PlainTextResponse)
async def get_message():
    message = await fetch_message()
    return message
