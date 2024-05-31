import os
import unittest
from sqlalchemy.orm import Session
from config.database import session_local_test
from config.database import engine_test


class BaseTest(unittest.TestCase):
    def setUp(self):        
        self.db: Session = session_local_test()

    def tearDown(self):        
        self.db.close()
        engine_test.dispose()
        if self.test_final:
            try:
                self.db = None
                os.remove("test.db")           
            except FileNotFoundError:
                pass
