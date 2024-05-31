from sqlalchemy import Column, Integer, String, Enum as SQLAEnum
from sqlalchemy.ext.declarative import declarative_base
from app.core.enums.status import StatusType
from app.core.schemas import AfinidadMagica

Base = declarative_base()


class Solicitud(Base):
    __tablename__ = 'solicitudes'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20), nullable=False)
    apellido = Column(String(20), nullable=False)
    identificacion = Column(String(10), nullable=False, unique=True)
    edad = Column(Integer, nullable=False)
    afinidad_magica = Column(SQLAEnum(AfinidadMagica), nullable=False)
    estatus = Column(SQLAEnum(StatusType), default="recibido")
    grimorio_asignado = Column(String(50), nullable=True)
