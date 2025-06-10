from typing import Annotated
from bson import ObjectId
from fastapi import Depends
from .repository import lodging_repository_dependency
from ..users.repository import UserRepository
from ..db.postgresql.conexion import session_dependency 
from .models import LodgingResponse
import pprint as pp


class LodgingService:
    def __init__(
        self,
        lodging_repository: lodging_repository_dependency,
        session: session_dependency,
    ):
        self.lodging_repository = lodging_repository
        self.session = session
    
    def obtain_lodgings(self)->list[LodgingResponse]:
        list_lodgings = list(self.lodging_repository.get_lodgins())
        for lodging in list_lodgings:
            lodging["id"] = str(lodging["_id"])
        return list_lodgings
    
    def delete_loging(self, lodging_id: str)->bool:
        lodging_id = ObjectId(lodging_id)
        try:
            self.lodging_repository.delete_lodging(lodging_id=lodging_id)
            return True
        except Exception as e:
            print(e)
            return False
    
    def create_lodging(self, lodging)->LodgingResponse | bool:
        try:
            result = self.lodging_repository.insert_lodging(lodging)
            data = lodging.model_dump()
            data['id'] = str(result.inserted_id)
            return data
        except Exception as e:
            print(e)
            return False

def get_lodging_service(lodging_repository:lodging_repository_dependency, session: session_dependency):
    return LodgingService(lodging_repository=lodging_repository, session=session)


lodging_service_dependency = Annotated[LodgingService, Depends(get_lodging_service)]
