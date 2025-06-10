from fastapi import APIRouter
from .models import LodgingResponse
from typing import Annotated
from fastapi import Depends
from .service import lodging_service_dependency

lodging_router = APIRouter(tags=["lodging"])

@lodging_router.get("",response_model=list[LodgingResponse])
def obtain_all_lodging(lodging_service:lodging_service_dependency):
    return lodging_service.obtain_lodgings()

@lodging_router.post("",response_model=LodgingResponse)
def create_lodging(lodging_service:lodging_service_dependency,lodging:LodgingResponse):
    return lodging_service.create_lodging(lodging=lodging)