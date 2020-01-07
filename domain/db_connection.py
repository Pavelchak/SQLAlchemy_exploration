from orm_config import OrmConfig as Cnf
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base
from .group import Group
from .student import Student
from .address import Address
from .subject import Subject

# Singleton
class SessionManager:
    # Here will be the instance stored.
    __engine = None
    __session = None

    def __init__(self):
        raise RuntimeError("Call get_session() instead!")

    @classmethod
    def get_engine(cls):
        if cls.__engine is None:
            if Cnf.IS_DEL_DB_FILE and os.path.exists(Cnf.DB_FILE):
                os.remove(Cnf.DB_FILE)
            cls.__engine = create_engine(Cnf.DB_CONNECT_STR, echo=Cnf.ECHO)
        return cls.__engine

    @classmethod
    def get_session(cls):
        if cls.__session is None:
            cls.get_engine()
            Base.metadata.create_all(cls.__engine)
            Session = sessionmaker(bind=cls.__engine)
            cls.__session = Session()
        return cls.__session

