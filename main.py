from fastapi import FastAPI
from api.route.apimain import api_router

description = """
API for managing Todo items.
"""

app = FastAPI(title="Todo API", version="1.0.0")

app.include_router(api_router)