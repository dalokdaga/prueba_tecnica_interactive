from fastapi import HTTPException
from app.core.repositories.solitude_repository import SolicitudRepository
from app.core.utilities import is_valid_enum
from app.core.enums.status import StatusType


class Process:
    @staticmethod
    def create_application_process(applicaction: dict, db):
        repository = SolicitudRepository(db)
        return repository.create_solicitud(applicaction)

    @staticmethod
    def update_application_process(id: int, applicaction: dict, db):
        repository = SolicitudRepository(db)
        updated_solicitud = repository.update_solicitud(id, applicaction)
        if updated_solicitud is None:
            raise HTTPException(status_code=404, detail="Solicitud not found")
        return updated_solicitud

    @staticmethod
    def update_application_status_process(id: int, status, db):        
        repository = SolicitudRepository(db)
        updated_solicitud = repository.update_solicitud_estatus(id, status)
        if updated_solicitud is None:
            raise HTTPException(status_code=404, detail="Solicitud not found")
        return updated_solicitud

    @staticmethod
    def read_application_process(skip, limit, db):
        repository = SolicitudRepository(db)
        return repository.get_solicitudes(skip, limit)

    @staticmethod
    def read_assignments_process(db):
        repository = SolicitudRepository(db)
        return repository.get_asignaciones()

    @staticmethod
    def delete_application_process(id, db):
        repository = SolicitudRepository(db)
        deleted_solicitud = repository.delete_solicitud(id)
        if deleted_solicitud is None:
            raise HTTPException(status_code=404, detail="Solicitud not found")
        return deleted_solicitud
