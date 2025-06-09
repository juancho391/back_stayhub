from sqlmodel import SQLModel, Field
from pydantic import EmailStr


class Users(SQLModel, table=True):
    __tablename__= "users"

    id : int | None = Field(default=None, primary_key=True)
    name : str 
    cedula : str 
    password : str
    email : EmailStr = Field(unique=True)
    age : int 
