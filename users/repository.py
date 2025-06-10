from ..db.postgresql.conexion import session_dependency
from ..db.postgresql.entities import Users
from typing import Annotated
from sqlmodel import select
from fastapi import Depends
from .models import UserCreate, UserResponse
from ..db.postgresql.entities import Users

class UserRepository:
    def __init__(self, session: session_dependency):
        self.session = session

    # Buscar el usuario por email
    def search_user_by_email(self, email: str):
        return self.session.exec(select(Users).where(Users.email == email)).first()

    # Buscar por el id del usuario
    def search_user_id(self, id:int)->UserResponse:
        return self.session.exec(select(Users).where(Users.id == id)).first()

    # Obtener todas las contraseñas
    def get_passwords(self)-> list[str]:
        return self.session.exec(select(Users.password)).all()

    # Ingresar un nuevo usuario en la base de datos
    def insert_user(self, new_user: UserCreate):
        new_user = Users(**new_user.model_dump())
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user
def get_user_repository(session: session_dependency):
    return UserRepository(session=session)


user_repository_dependency = Annotated[UserRepository, Depends(get_user_repository)]
