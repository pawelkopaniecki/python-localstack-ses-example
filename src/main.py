from fastapi import APIRouter, FastAPI

from .modules.email.controller import router as email_router
from .modules.ping.controller import router as ping_router

app = FastAPI()

api_router = APIRouter(prefix="/api")
api_router.include_router(email_router)
api_router.include_router(ping_router)

app.include_router(api_router)
