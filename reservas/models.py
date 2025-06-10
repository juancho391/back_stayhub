from sqlmodel import SQLModel
from datetime import date


class Booking(SQLModel):
    id: str
    id_usuario: int
    id_alojamiento: str
    fecha_reserva: date
    fecha_fin: date


class BookingCreate(SQLModel):
    id_usuario: int
    id_alojamiento: str
    fecha_reserva: date
    fecha_fin: date
