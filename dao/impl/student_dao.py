from ..i_student_dao import IStudentDAO
from domain import Student, session


class StudentDAO(IStudentDAO):
    def find_all(self):
        return session.query(Student).all()

    def find_by_id(self, key):
        return session.query(Student).get(key)

    def create(self, obj):
        session.add(obj)
        session.commit()

    def update(self, key, obj):
        student = session.query(Student).get(key)
        student.full_update(obj)
        session.commit()

    def patch(self, key, field_name, value):
        student = session.query(Student).get(key)
        setattr(student, field_name, value)
        session.commit()

    def delete(self, key):
        student = session.query(Student).get(key)
        session.delete(student)
