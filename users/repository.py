from ..db.postgresql.conexion import session_dependency
from ..db.postgresql.entities import Users
from typing import Annotated
from sqlmodel import select
from fastapi import Depends

class UserRepository:
    def __init__(self, session: session_dependency):
        self.session = session

    def search_user_by_email(self, email: str):
        return self.session.exec(select(Users).where(Users.email == email)).first()


    


def get_user_repository(session: session_dependency):
    return UserRepository(session=session)


user_repository_dependency = Annotated[UserRepository, Depends(get_user_repository)]
