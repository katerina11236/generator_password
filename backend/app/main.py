from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import test

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
)

app.include_router(test.router)

@app.get("/")
async def root():
    return {"status": "ok"}
