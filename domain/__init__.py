from address import Address
from group import Group
from student import Student
from subject import Subject
from base import Session, engine, Base

Base.metadata.create_all(engine)
session = Session()
