from enum import Enum


class StatusType(str, Enum):
    received = 'recibido'
    rejected = 'rechazado'
    accepted = 'aceptado'


class AfinidadMagica(str, Enum):
    oscuridad = "Oscuridad"
    luz = "Luz"
    fuego = "Fuego"
    agua = "Agua"
    viento = "Viento"
    tierra = "Tierra"
