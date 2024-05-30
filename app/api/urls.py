from config.main import app
from fastapi import APIRouter
from app.api.v1 import views as api


urls = APIRouter()
urls.include_router(api.router, prefix="/api/v1")
app.include_router(urls)
