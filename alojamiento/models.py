from sqlmodel import SQLModel
from ..users.models import UserResponse

class LodgingResponse(SQLModel):
    id:str
    title:str
    description:str
    no_rooms:int
    no_bathrooms:int
    price_night:int
    images:list[str]
    city:str
    propietario:int
    contact:str
    characteristics:list[str]
    nearby_areas:list[str]
    type:str
    