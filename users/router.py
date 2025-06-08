from .models import Token, UserLogin
from .service import user_service_dependency
from fastapi import APIRouter

users_router = APIRouter(tags=["users"])



@users_router.post("/login", response_model=Token)
def login(user_service : user_service_dependency, user: UserLogin):
    return user_service.login(user)