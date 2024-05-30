from fastapi import FastAPI
from app.core.models import Base
from config.database import engine
import importlib


Base.metadata.create_all(bind=engine)


app = FastAPI()

"""
Initialize URL
"""
urls = importlib.import_module('app.api.urls')
