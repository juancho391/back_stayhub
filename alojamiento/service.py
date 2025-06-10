from typing import Annotated
from fastapi import Depends
from .repository import lodging_repository_dependency
from ..users.repository import UserRepository
from ..db.postgresql.conexion import session_dependency 
import pprint as pp

class LodgingService:
    def __init__(self, lodging_repository: lodging_repository_dependency, session: session_dependency):
        self.lodging_repository = lodging_repository
        self.session = session
    
    def obtain_lodgings(self):
        list_lodgings = list(self.lodging_repository.get_lodgins())
        user_repository = UserRepository(session=self.session)
        for lodgings in list_lodgings:
            lodgings['propietario'] = user_repository.search_user_id(lodgings['propietario']).model_dump()
        return list_lodgings
    
    
def get_lodging_service(lodging_repository:lodging_repository_dependency, session: session_dependency):
    return LodgingService(lodging_repository=lodging_repository, session=session)

lodging_service_dependency = Annotated[LodgingService, Depends(get_lodging_service)]

