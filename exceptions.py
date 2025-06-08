from fastapi import HTTPException

class UserError(HTTPException):
    pass


class UserLoginError(UserError):
    def __init__(self, status_code, detail = None):
        super().__init__(status_code, detail)


# Excepcion de autenticacion de usuario
class AuthenticationError(HTTPException):
    def __init__(self, mensaje: str = "No se pudo validar el usuario"):
        super().__init__(status_code=401, detail=mensaje)

