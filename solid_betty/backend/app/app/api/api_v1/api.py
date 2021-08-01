from fastapi import APIRouter

from app.api.api_v1.endpoints import fighters, login, users, utils

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(fighters.router, prefix="/fighters", tags=["fighters"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
