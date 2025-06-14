from .repository import booking_repository_dependency
from ..exceptions import BookingError, BookingNotFoundError
from datetime import datetime
from typing import Annotated
from .models import Booking
from fastapi import Depends


class ReservaService:
    def __init__(self, booking_repository: booking_repository_dependency):
        self.booking_repository = booking_repository

    def get_user_bookings(self, user_id: int):
        bookings = self.booking_repository.get_user_bookings(user_id=user_id)
        return bookings

    def create_booking(self, new_booking: Booking):
        current_date = datetime.today()
        if new_booking.fecha_reserva < current_date.date():
            raise BookingError()
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
        return self.booking_repository.get_bookings_by_alojamientoid_from_today(
            id_alojamiento
        )

    def delete_booking(self, booking_id: str):
        result = self.booking_repository.delete_booking(booking_id=booking_id)
        if result.deleted_count > 0:
            return True
        raise BookingNotFoundError()


def get_booking_service(booking_repository: booking_repository_dependency):
    return ReservaService(booking_repository)


booking_service_dependency = Annotated[ReservaService, Depends(get_booking_service)]
