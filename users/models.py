from sqlmodel import SQLModel 
from pydantic import EmailStr


class UserLogin(SQLModel):
    email : EmailStr
    password : str


class UserResponse(SQLModel):
    id : int 
    name : str 
    cedula : str 
    email : EmailStr
    edad : int 


class Token(SQLModel):
    access_token: str
    token_type : str 


class TokenData(SQLModel):
    user_id: int | None = None