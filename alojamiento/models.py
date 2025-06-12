from sqlmodel import SQLModel
from typing import Optional
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

class LodgingCreate(SQLModel):
    title:str
    description:str
    no_rooms:Optional[int] = 1
    no_bathrooms:Optional[int] = 1
    price_night:int
    images:Optional[list[str]] = []
    city:str
    propietario:int
    contact:Optional[str] = "xxxxxxxx"
    characteristics:list[str]
    nearby_areas:list[str]
    type:str
    