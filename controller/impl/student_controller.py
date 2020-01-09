from service import StudentService
from ..i_group_controller import IGroupController


class StudentController(IGroupController):

    def find_all(self):
        return StudentService().find_all()

    def find_by_id(self, key):
        return StudentService().find_by_id(key)

    def create(self, obj):
        StudentService().create(obj)

    def update(self, key, obj):
        StudentService().update(key, obj)

    def patch(self, key, field_name, value):
        StudentService().patch(key, field_name, value)

    def delete(self, key):
        StudentService().delete(key)