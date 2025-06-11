from sqlmodel import SQLModel
from pydantic import EmailStr
from ..reservas.models import Booking
from ..alojamiento.models import LodgingResponse


class UserCreate(SQLModel):
    name: str
    cedula: str
    password: str
    email: EmailStr
    age: int


class UserLogin(SQLModel):
    email: EmailStr
    password: str


class UserResponse(SQLModel):
    id: int
    name: str
    cedula: str
    email: EmailStr
    age: int


class UserProfile(UserResponse):
    bookings: list[Booking] | None = []
    lodgings: list[LodgingResponse] | None = []


class Token(SQLModel):
    access_token: str
    token_type: str


class TokenData(SQLModel):
    user_id: int | None = None
