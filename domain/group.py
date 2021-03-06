from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from base import Base, IGeneral


class Group(Base, IGeneral):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    students = relationship("Student", back_populates="group")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Group('%s', '%s')" % (self.id, self.name)

    def full_update(self, obj):
        self.name = obj.name
