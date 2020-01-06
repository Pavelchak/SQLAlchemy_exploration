from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from . import Base


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    students = relationship("Student", back_populates="students")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Student('%s', '%s')>" % (self.id, self.name)

