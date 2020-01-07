from service.impl.group_service import GroupService
from ..i_group_controller import IGroupController


class StudentController(IGroupController):

    def find_all(self):
        return GroupService().find_all()

    def find_by_id(self, key):
        return GroupService().find_by_id(key)

    def create(self, obj):
        GroupService().create(obj)

    def update(self, obj):
        GroupService().update(obj)

    def delete(self, key):
        GroupService().delete(key)
