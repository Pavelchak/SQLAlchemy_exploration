from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base, IGeneral


class Student(Base, IGeneral):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    surname = Column(String(50))
    name = Column(String(50))
    birthday = Column(Date)
    group_id = Column(Integer, ForeignKey('group.id'))
    group = relationship("Group", back_populates="students")

    def __init__(self, surname, name, birthday, group_id):
        # type: (str, str, date, int) -> None
        self.surname = surname
        self.name = name
        self.birthday = birthday
        self.group_id = group_id

    def __repr__(self):
        return "Student('%s', '%s', '%s', '%s', '%s')" % (
            self.id, self.surname, self.name, self.birthday, self.group.name)

    def full_update(self, obj):
        self.surname = obj.surname
        self.name = obj.name
        self.birthday = obj.birthday
        self.group_id = obj.group_id
