from ..db.mongodb.conexion import mongo_db_dependency
from datetime import datetime, date
from typing import Annotated
from .models import Booking
from fastapi import Depends
from ..utils.mapBookin import mapBooking
from bson import ObjectId


class BookingsRepository:
    def __init__(self, mongodb: mongo_db_dependency):
        self.bd = mongodb
        self.booking = self.bd["reserva"]

    def create_booking(self, booking: Booking):
        new_booking = booking.model_dump()
        if isinstance(new_booking["fecha_reserva"], date):
            new_booking["fecha_reserva"] = datetime.combine(
                new_booking["fecha_reserva"], datetime.min.time()
            )
        if isinstance(new_booking["fecha_fin"], date):
            new_booking["fecha_fin"] = datetime.combine(
                new_booking["fecha_fin"], datetime.min.time()
            )
        booking_created = self.booking.insert_one(new_booking)
        return booking_created

    def     get_user_bookings_by_user_id(self, user_id: int):
        bookings_cursor = self.booking.find({"id_usuario": user_id})
        bookings = mapBooking(bookings_cursor)
        return bookings

    def get_bookings_by_alojamientoid_from_today(self, id_alojamiento: str):
        bookings_cursor = self.booking.find(
            {
                "id_alojamiento": id_alojamiento,
                "fecha_reserva": {"$gte": datetime.now()},
            }
        )
        bookings = mapBooking(bookings_cursor)
        return bookings

    def get_booking_by_id(self, booking_id: str):
        return self.booking.find_one({"_id": ObjectId(booking_id)})

    def delete_booking(self, booking_id: str):
        return self.booking.delete_one({"_id": ObjectId(booking_id)})


def get_bookings_repository(mongodb: mongo_db_dependency):
    return BookingsRepository(mongodb)


booking_repository_dependency = Annotated[
    BookingsRepository, Depends(get_bookings_repository)
]

# Json de prueba para hacer un post
# {
#   "id_usuario": 1,
#   "id_alojamiento": "68472baf0f2b14dd03afef45",
#   "fecha_reserva": "2025-06-09",
#   "fecha_fin": "2025-07-09"
# }
