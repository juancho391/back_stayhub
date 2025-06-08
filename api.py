from fastapi import FastAPI
from .users.router import users_router


def register_routers(app: FastAPI):
    app.include_router(users_router, prefix="/users")