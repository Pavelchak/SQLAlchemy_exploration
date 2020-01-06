from sqlalchemy import Column, Integer, String, Date
from . import Base


class Subject(Base):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True)
    name = Column(String(35))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Student('%s', '%s')>" % (self.id, self.name)

