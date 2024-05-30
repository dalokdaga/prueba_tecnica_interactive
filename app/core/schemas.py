from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum


class AfinidadMagica(str, Enum):
    oscuridad = "Oscuridad"
    luz = "Luz"
    fuego = "Fuego"
    agua = "Agua"
    viento = "Viento"
    tierra = "Tierra"


class SolicitudBase(BaseModel):
    nombre: str = Field(..., max_length=20, pattern="^[a-zA-Z]+$")
    apellido: str = Field(..., max_length=20, pattern="^[a-zA-Z]+$")
    identificacion: str = Field(..., max_length=10, pattern="^[a-zA-Z0-9]+$")
    edad: int = Field(..., ge=10, le=99)
    afinidad_magica: AfinidadMagica


class SolicitudCreate(SolicitudBase):
    pass


class SolicitudUpdate(SolicitudBase):
    pass


class SolicitudEstatusUpdate(BaseModel):
    estatus: str


class Solicitud(SolicitudBase):
    id: int
    estatus: str
    grimorio_asignado: Optional[str] = None

    class Config:
        from_attributes = True
