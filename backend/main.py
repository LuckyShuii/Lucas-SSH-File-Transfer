from fastapi import FastAPI
from db.models import *
from database import Database
from routers import tag, api
from fastapi.middleware.cors import CORSMiddleware
from config import Config
from db.schemas.base_schema import BaseSchema

app = FastAPI()

origins = [
    Config.FRONTEND_URL,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tag.router)
app.include_router(api.router)

@app.on_event("startup")
async def startup():
    Database.init()
    BaseSchema.forward_all()