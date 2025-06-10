from ..reservas.models import Booking


def mapBooking(bookings):
    bookings = [
        Booking(
            id=str(booking["_id"]),
            id_usuario=booking["id_usuario"],
            id_alojamiento=booking["id_alojamiento"],
            fecha_reserva=booking["fecha_reserva"],
            fecha_fin=booking["fecha_fin"],
        )
        for booking in bookings
    ]

    return bookings
