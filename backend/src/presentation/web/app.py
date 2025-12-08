import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.presentation.web.routes.api import router

app = FastAPI(title="Telegram Birthday Calendar API")

# CORS для Telegram Mini App
allowed_origins = os.getenv("ALLOWED_ORIGINS", "*")
# Если указано несколько доменов через запятую, разбиваем на список
if allowed_origins != "*" and "," in allowed_origins:
    allowed_origins = [origin.strip() for origin in allowed_origins.split(",")]
elif allowed_origins == "*":
    allowed_origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Telegram Birthday Calendar API"}

