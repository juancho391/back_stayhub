from sqlmodel import Session, SQLModel, create_engine
from dotenv import load_dotenv
from typing import Annotated
from fastapi import Depends
import os

load_dotenv()

db_url = os.getenv("DATABASE_URL")

engine = create_engine(db_url)

#Funcion para crear las tablas
def create_tables_and_db():
    SQLModel.metadata.create_all(engine)

#Funcion para obtener la session de la base de datos
def get_session():
    with Session(engine) as session:
        yield session

session_dependency = Annotated[Session, Depends(get_session)]

