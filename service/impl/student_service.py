from dao import StudentDAO
from ..i_student_service import IStudentService


class StudentService(IStudentService):

    def find_all(self):
        return StudentDAO().find_all()

    def find_by_id(self, key):
        return StudentDAO().find_by_id(key)

    def create(self, obj):
        StudentDAO().create(obj)

    def update(self, obj):
        StudentDAO().update(obj)

    def delete(self, key):
        StudentDAO().delete(key)
