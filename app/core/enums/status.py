from enum import Enum


class StatusType(str, Enum):
    recibido = 'recibido'
    rechazado = 'rechazado'
    aprobado = 'aprobado'


class AfinidadMagica(str, Enum):
    oscuridad = "Oscuridad"
    luz = "Luz"
    fuego = "Fuego"
    agua = "Agua"
    viento = "Viento"
    tierra = "Tierra"
