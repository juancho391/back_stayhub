from .service import booking_service_dependency
from fastapi import APIRouter
from .models import BookingCreate, Booking
from fastapi.responses import JSONResponse


booking_router = APIRouter(tags=["reservas"])


@booking_router.post("/")
def create_booking(booking_service: booking_service_dependency, booking: BookingCreate):
    booking_service.create_booking(booking)
    return JSONResponse(
        content={"message": "Reserva creada con exito"}, status_code=201
    )


@booking_router.get("/alojamiento/{alojamiento_id}")
def get_bookings_by_alojamiento_from_today(
    booking_service: booking_service_dependency, alojamiento_id: str
):
    return booking_service.get_bookings_by_alojamientoid_from_today(
        id_alojamiento=alojamiento_id
    )


@booking_router.delete("/{booking_id}")
def delete_booking(booking_service: booking_service_dependency, booking_id: str):
    booking_service.delete_booking(booking_id=booking_id)
    return JSONResponse(content={"message": "Reserva eliminada con exito"})
