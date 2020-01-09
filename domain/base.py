from abc import abstractmethod, ABCMeta
from orm_config import OrmConfig as Cnf
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class IGeneral():
    @abstractmethod
    def full_update(self, obj):
        pass


if Cnf.IS_DEL_DB_FILE and os.path.exists(Cnf.DB_FILE):
    os.remove(Cnf.DB_FILE)
engine = create_engine(Cnf.DB_CONNECT_STR, echo=Cnf.ECHO)
Session = sessionmaker(bind=engine)
Base = declarative_base()
