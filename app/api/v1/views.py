from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.schemas import (Solicitud, SolicitudCreate,
                              SolicitudEstatusUpdate, SolicitudUpdate)
from config.database import get_db
from app.core.handler import Handler

router = APIRouter()


@router.post("/solicitud", response_model=Solicitud)
def create_application(application: SolicitudCreate,
                       db: Session = Depends(get_db)):
    return Handler.create_application_handler(application, db)


@router.put("/solicitud/{id}", response_model=Solicitud)
def update_application(id: int, application: SolicitudUpdate,
                       db: Session = Depends(get_db)):
    return Handler.update_application_handler(id, application, db)


@router.patch("/solicitud/{id}/estatus", response_model=Solicitud)
def update_solicitud_estatus(id: int, status: SolicitudEstatusUpdate,
                             db: Session = Depends(get_db)):
    return Handler.update_application_status_handler(id, status, db)


@router.get("/solicitudes", response_model=List[Solicitud])
def read_application(skip: int = 0, limit: int = 10,
                     db: Session = Depends(get_db)):
    return Handler.read_application_handler(skip, limit, db)


@router.get("/asignaciones", response_model=List[Solicitud])
def read_assignments(db: Session = Depends(get_db)):
    return Handler.read_assignments_handler(db)


@router.delete("/solicitud/{id}", response_model=Solicitud)
def delete_solicitud(id: int, db: Session = Depends(get_db)):
    return Handler.delete_application_handler(id, db)
