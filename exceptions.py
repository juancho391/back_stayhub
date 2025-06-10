from fastapi import HTTPException


class UserError(HTTPException):
    pass


class UserLoginError(UserError):
    def __init__(self, status_code, detail=None):
        super().__init__(status_code, detail)


class UserRegisterError(UserError):
    def __init__(self, message: str = "Ya existe un usuario registrado con este email"):
        super().__init__(status_code=401, detail=message)


# Excepcion de autenticacion de usuario
class AuthenticationError(HTTPException):
    def __init__(self, message: str = "No se pudo validar el usuario"):
        super().__init__(status_code=401, detail=message)


class BookingError(HTTPException):
    def __init__(
        self, status_code=400, detail="No se puede realizar la reserva en esas fechas"
    ):
        super().__init__(status_code, detail)
