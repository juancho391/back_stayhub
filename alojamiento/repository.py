from ..db.mongodb.conexion import mongo_db_dependency
from bson import ObjectId
from .models import LodgingResponse
from typing import Annotated
from fastapi import Depends


class LodgingRepository:
    def __init__(self, mongodb: mongo_db_dependency):
        self.bd = mongodb
        self.collection = self.bd["alojamiento"]

    # Obtener todos los user 
    def get_lodgins(self, limit=10):
        lodgins = self.collection.find({}).limit(limit)
        return lodgins
    
    # Eliminar el alojamiento
    def delete_lodging(self, lodging_id: ObjectId):
        return self.collection.delete_one({"_id": lodging_id})
    
    # Insertar el alojamiento
    def insert_lodging(self, lodging)->LodgingResponse:
        format_js = lodging.model_dump()
        return self.collection.insert_one(format_js)
    
    #Buscar el alojamiento por propietario
    def lodging_for_user(self, user_id: int)->list[LodgingResponse]:
        return self.collection.find({"propietario": user_id}).limit(10)

def get_lodging_repository(mongodb: mongo_db_dependency):
    return LodgingRepository(mongodb=mongodb)


lodging_repository_dependency = Annotated[
    LodgingRepository, Depends(get_lodging_repository)
]
