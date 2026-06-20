from fastapi import FastAPI, APIRouter, Depends
import os
from helpers.config import get_settings, Settings
from time import sleep
import logging

logger = logging.getLogger('uvicorn.error')

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@base_router.get("/")
async def welcome(app_settings: Settings = Depends(get_settings)):
    # Simple Hello World response for quick testing
    return {"message": "Hello World"}
