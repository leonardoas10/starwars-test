from fastapi import FastAPI
import logging
from .routes.api import router

# Configure logging
logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Star Wars API",
    version="1.0.0",
    description="A FastAPI service for exploring the Star Wars API (SWAPI)"
)

app.include_router(router)