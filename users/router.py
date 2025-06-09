from .models import Token, UserLogin, UserResponse, UserCreate
from .service import user_service_dependency
from fastapi import APIRouter

users_router = APIRouter(tags=["users"])


@users_router.post("/login", response_model=Token)
def login(user_service : user_service_dependency, user: UserLogin):
    return user_service.login(user)

@users_router.post("/register", response_model=UserResponse)
def register(user_service: user_service_dependency, new_user: UserCreate):
    return user_service.register(new_user=new_user)