from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.core import models, schemas
from app.core.enums.status import StatusType


class SolicitudRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_solicitud(self, solicitud: schemas.SolicitudCreate):
        try:                     
            db_solicitud = models.Solicitud(**solicitud.model_dump())
            self.db.add(db_solicitud)
            self.db.commit()
            self.db.refresh(db_solicitud)
            return db_solicitud
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"db error {str(e)}")

    def update_solicitud(self, id: int, solicitud: schemas.SolicitudUpdate):
        try:
            db_solicitud = self.db.query(models.Solicitud).filter(
                models.Solicitud.id == id).first()
            if db_solicitud is None:
                return None
            for key, value in solicitud.model_dump().items():
                setattr(db_solicitud, key, value)
            self.db.commit()
            self.db.refresh(db_solicitud)
            return db_solicitud
        except Exception as e:
            raise HTTPException(status_code=404, detail=f"db error {str(e)}")    

    def update_solicitud_estatus(self, id: int,
                                 estatus: schemas.SolicitudEstatusUpdate):
        try:        
            db_solicitud = self.db.query(models.Solicitud).filter(
                models.Solicitud.id == id).first()
            if db_solicitud is None:
                return None
            db_solicitud.estatus = estatus.estatus.lower()
            if estatus.estatus.lower() == StatusType.aceptado:
                db_solicitud.grimorio_asignado = self.asignar_grimorio()
            self.db.commit()
            self.db.refresh(db_solicitud)
            return db_solicitud
        except Exception as e:
            raise HTTPException(status_code=404, detail=f"db error {str(e)}")

    def get_solicitudes(self, skip: int = 0, limit: int = 10):
        try:
            return self.db.query(models.Solicitud).offset(skip).limit(limit).all()
        except Exception as e:
            raise HTTPException(status_code=404, detail=f"db error {str(e)}")        

    def get_asignaciones(self):
        try:
            return self.db.query(models.Solicitud).filter(
                models.Solicitud.grimorio_asignado is not None).all()
        except Exception as e:
            raise HTTPException(status_code=404, detail=f"db error {str(e)}")

    def delete_solicitud(self, id: int):
        try:
            db_solicitud = self.db.query(models.Solicitud).filter(
                models.Solicitud.id == id).first()
            if db_solicitud is None:
                return None
            self.db.delete(db_solicitud)
            self.db.commit()
            return db_solicitud
        except Exception as e:
            raise HTTPException(status_code=404, detail=f"db error {str(e)}")

    def asignar_grimorio(self):
        try:
            from random import choices
            grimorios = ["Trébol de 1 hoja", "Trébol de 2 hojas",
                         "Trébol de 3 hojas", "Trébol de 4 hojas",
                         "Trébol de 5 hojas"]
            probabilidades = [0.4, 0.3, 0.2, 0.09, 0.01]
            return choices(grimorios, probabilidades)[0]
        except Exception as e:
            raise HTTPException(status_code=404, detail=f"db error {str(e)}")        
