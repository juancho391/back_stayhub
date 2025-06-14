from fastapi import APIRouter
from .models import LodgingResponse,LodgingCreate
from typing import Annotated
from fastapi import Depends
from .service import lodging_service_dependency

lodging_router = APIRouter(tags=["lodging"])

@lodging_router.get("",response_model=list[LodgingResponse])
def obtain_all_lodging(lodging_service:lodging_service_dependency):
    return lodging_service.obtain_lodgings()

@lodging_router.delete("/{lodging_id}")
def delete_lodging(lodging_service:lodging_service_dependency, lodging_id:str):
    return lodging_service.delete_loging(lodging_id=lodging_id)

@lodging_router.post("",response_model=LodgingResponse)
def create_lodging(lodging_service:lodging_service_dependency,lodging:LodgingCreate):
    return lodging_service.create_lodging(lodging=lodging)


@lodging_router.get("/{title_post}", response_model=LodgingResponse)
def get_lodging(lodging_service:lodging_service_dependency,title_post:str):
    return lodging_service.get_lodging(title_post)