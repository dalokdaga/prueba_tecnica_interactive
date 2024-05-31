import unittest
from app.core.handler import Handler
from app.core.models import Base
from app.core.schemas import SolicitudCreate, SolicitudEstatusUpdate
from config.database import session_local_test
from config.database import engine_test
from sqlalchemy.orm import Session
from tests.base_test import BaseTest

Base.metadata.create_all(bind=engine_test)


class CaseTest(BaseTest):
    application = SolicitudCreate(**{
        "nombre": "kqWJXdPVsCknXBcFLFVg",
        "apellido": "afgSHUBLekXfDvyIqyQO",
        "identificacion": "Iel96QxlAn",
        "edad": 12,
        "afinidad_magica": "Oscuridad"
    })
    test_final = False
    id = None

    def test_case_1_create_application(self):
        self.db: Session = session_local_test()
        result = Handler.create_application_handler(self.application, self.db)

        if result:
            CaseTest.id = result.id
            self.assertEqual(result.estatus, 'recibido')
            self.assertEqual(result.nombre, self.application.nombre)
            print("--- Registro de solicitud ok")

    def test_case_2_solicitud_id(self):        
        self.application.apellido = "Uscanga"
        result = Handler.update_application_handler(CaseTest.id, self.application, self.db)
        if result:
            self.assertEqual(result.apellido, self.application.apellido)
            print("--- Busqueda solicitud por id ok")

    def test_case_3_solicitud_status(self):
        status = SolicitudEstatusUpdate(estatus="aceptado")             
        result = Handler.update_application_status_handler(CaseTest.id, status, self.db)
        if result:
            self.assertEqual("aceptado", status.estatus)
            print("--- Actualizacion de estatus ok")

    def test_case_4_solicitudes(self):        
        result = Handler.read_application_handler(0, 10, self.db)
        if result:
            self.assertEqual(1, len(result))
            print("--- Listar todas las solicitudes ok")

    def test_case_5_assignments(self):        
        result = Handler.read_assignments_handler(self.db)
        if result:
            self.assertEqual(1, len(result))
            print("--- Listar asignaciones ok")

    def test_case_6_delete(self):
        self.test_final = True            
        result = Handler.delete_application_handler(CaseTest.id, self.db)
        if result:
            self.assertEqual(CaseTest.id, result.id)
            print("--- Elimninar registro ok")

    def run_test(self):
        unittest.main()
