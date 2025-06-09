from ..exceptions import UserLoginError, AuthenticationError, UserRegisterError
from .repository import user_repository_dependency
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from .models import Token, TokenData, UserCreate, UserLogin
from dotenv import load_dotenv
from typing import Annotated
from fastapi import Depends
from jwt import PyJWTError
import jwt
import os


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCES_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/token")

class UserService:
    def __init__(self, user_repository: user_repository_dependency):
        self.user_repository = user_repository

    
    def create_acces_token(self, email:str, user_id : int, expires_delta: timedelta):
        encode = {
            "sub" : email,
            "id": user_id,
            "exp" : datetime.now(timezone.utc) + expires_delta
        }
        return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


    #funcion para verificar la contraseña    
    def verify_password(self,password:str, password_hash:str):
        return pwd_context.verify(password, password_hash)
    
    #funcion para loguear el usuario
    def login(self, user:UserLogin):
        user_db = self.user_repository.search_user_by_email(email=user.email)
        if not user_db or not self.verify_password(password=user.password, password_hash=user_db.password):
            raise UserLoginError(status_code=404, detail="user credentials invalid")
        token = self.create_acces_token(email=user_db.email, user_id=user_db.id, expires_delta=timedelta(minutes=ACCES_TOKEN_EXPIRE_MINUTES))
        return Token(access_token=token, token_type="bearer")
    

    def register(self, new_user: UserCreate):
        new_user.password = pwd_context.hash(new_user.password)
        return self.user_repository.insert_user(new_user=new_user)
        




def get_user_service(user_repository: user_repository_dependency):
    return UserService(user_repository=user_repository)

#Funcion para verificar el token 
def verify_token(token:str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        id_user = payload.get("id")
        return TokenData(user_id=id_user)
    except PyJWTError:
        raise AuthenticationError()
    
#Funcion para solicitar token en las requests 
def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    return verify_token(token=token)


usuario_actual = Annotated[TokenData, Depends(get_current_user)]
user_service_dependency = Annotated[UserService, Depends(get_user_service)]