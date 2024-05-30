from app.core.process import Process


class Handler:
    @staticmethod
    def create_application_handler(applicaction: dict, db):
        return Process.create_application_process(applicaction, db)

    @staticmethod
    def update_application_handler(id: int, applicaction, db):
        return Process.update_application_process(id, applicaction, db)

    @staticmethod
    def update_application_status_handler(id: int, status, db):
        return Process.update_application_status_process(id, status, db)

    @staticmethod
    def read_application_handler(skip: int, limit: int, db):
        return Process.read_application_process(skip, limit, db)

    @staticmethod
    def read_assignments_handler(db):
        return Process.read_assignments_process(db)

    @staticmethod
    def delete_application_handler(id, db):
        return Process.delete_application_process(id, db)
