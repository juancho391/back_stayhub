from sqlmodel import SQLModel
from ..users.models import UserResponse
from typing import Optional
class LodgingResponse(SQLModel):
    _id: Optional[str] = None
    title:str
    description:str
    no_rooms:int
    no_bathrooms:int
    price_night:int
    images:list[str]
    city:str
    propietario:UserResponse
    contact:str
    characteristics:list[str]
    nearby_areas:list[str]

    

    