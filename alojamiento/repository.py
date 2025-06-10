from ..db.mongodb.conexion import mongo_db_dependency
from typing import Annotated
from fastapi import Depends


class LodgingRepository:
    def __init__(self, mongodb: mongo_db_dependency):
        self.bd = mongodb
        self.collection = self.bd["alojamiento"]

    def get_lodgins(self, limit=10):
        lodgins = self.collection.find({}).limit(limit)
        return lodgins


def get_lodging_repository(mongodb: mongo_db_dependency):
    return LodgingRepository(mongodb=mongodb)


lodging_repository_dependency = Annotated[
    LodgingRepository, Depends(get_lodging_repository)
]
