from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    surname = Column(String(50))
    name = Column(String(50))
    birthday = Column(Date)
    group_id = Column(Integer, ForeignKey('group.id'))
    group = relationship("Group", back_populates="students")

    def __init__(self, surname, name, birthday):
        self.surname = surname
        self.name = name
        self.birthday = birthday

    def __repr__(self):
        return "Student('%s', '%s','%s', '%s', '%s')" % (
            self.id, self.surname, self.name, self.birthday, self.group.name)
