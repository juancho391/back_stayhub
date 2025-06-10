from fastapi import FastAPI
from .users.router import users_router
from .reservas.router import booking_router


def register_routers(app: FastAPI):
    app.include_router(users_router, prefix="/users")
    app.include_router(booking_router, prefix="/reservas")
