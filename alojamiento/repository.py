from ..db.mongodb.conexion import mongo_db_dependency
from .models import LodgingResponse
from typing import Annotated
from fastapi import Depends
class LodgingRepository:
    def __init__(self, mongodb: mongo_db_dependency):
        self.bd = mongodb
        self.collection = self.bd['alojamiento']

    # Funcion para obtener la lista de alojamientos
    def get_lodgins(self, limit=10)->list[LodgingResponse]:
        lodgins = self.collection.find({}).limit(limit)
        return lodgins
    
    def insert_lodging(self, lodging)->LodgingResponse:
        format_js = lodging.model_dump()
        return self.collection.insert_one(format_js)
    

def get_lodging_repository(mongodb:mongo_db_dependency)->LodgingRepository:
    return LodgingRepository(mongodb=mongodb)

lodging_repository_dependency = Annotated[LodgingRepository,Depends(get_lodging_repository)]