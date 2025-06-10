from typing import Annotated
from fastapi import Depends
from .repository import lodging_repository_dependency
class LodgingService:
    def __init__(self, lodging_repository: lodging_repository_dependency):
        self.lodging_repository = lodging_repository
    
    def obtain_lodgings(self):
        return self.lodging_repository.get_lodgins()
    
    
def get_lodging_service(lodging_repository:lodging_repository_dependency):
    return LodgingService(lodging_repository=lodging_repository)

lodging_service_dependency = Annotated[LodgingService, Depends(get_lodging_service)]

