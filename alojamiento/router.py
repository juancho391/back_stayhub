from fastapi import APIRouter
from .models import LodgingResponse
from typing import Annotated
from fastapi import Depends
from .service import lodging_service_dependency

lodging_router = APIRouter(tags=["lodging"])

@lodging_router.get("",response_model=list[LodgingResponse])
def obtain_all_lodging(lodging_service:lodging_service_dependency):
    return lodging_service.obtain_lodgings()

@lodging_router.delete("/{lodging_id}")
def delete_lodging(lodging_service:lodging_service_dependency, lodging_id:int):
    return lodging_service.delete_lodging(lodging_id=lodging_id)