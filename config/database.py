from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False, bind=engine)

# Variables para Tests #########################
SQLALCHEMY_DATABASE_URL_TEST = "sqlite:///./test.db"    
engine_test = create_engine(SQLALCHEMY_DATABASE_URL_TEST,
                            connect_args={"check_same_thread": False})
session_local_test = sessionmaker(autocommit=False,
                                  autoflush=False, bind=engine_test)
# end
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
