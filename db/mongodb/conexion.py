from pymongo import MongoClient
from fastapi import Depends
from typing import Annotated

def get_db():
    client = MongoClient("mongodb://localhost:30000")
    db = client["StayHubTest"]
    return db


mongo_db_dependency = Annotated[MongoClient, Depends(get_db)]


