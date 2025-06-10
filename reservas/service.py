from .repository import booking_repository_dependency
from fastapi import Depends
from typing import Annotated
from .models import Booking
from ..exceptions import BookingError
import pprint


class ReservaService:
    def __init__(self, booking_repository: booking_repository_dependency):
        self.booking_repository = booking_repository

    def get_user_bookings(self, user_id: int):
        bookings = self.booking_repository.get_user_bookings(user_id=user_id)
        return bookings

    def create_booking(self, new_booking: Booking):
        bookings = self.get_bookings_by_alojamientoid_from_today(
            new_booking.id_alojamiento
        )
        date_bookings = [
            (booking.fecha_reserva, booking.fecha_fin) for booking in bookings
        ]
        for date in date_bookings:
            if not (
                new_booking.fecha_fin <= date[0] or new_booking.fecha_reserva >= date[1]
            ):
                raise BookingError()

        return self.booking_repository.create_booking(new_booking)

    def get_bookings_by_alojamientoid_from_today(self, id_alojamiento: str):
        return self.booking_repository.get_booking_by_alojamientoid_from_today(
            id_alojamiento
        )


def get_booking_service(booking_repository: booking_repository_dependency):
    return ReservaService(booking_repository)


booking_service_dependency = Annotated[ReservaService, Depends(get_booking_service)]
