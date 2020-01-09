from service.impl.group_service import GroupService
from ..i_group_controller import IGroupController


class GroupController(IGroupController):

    def find_all(self):
        return GroupService().find_all()

    def find_by_id(self, key):
        return GroupService().find_by_id(key)

    def create(self, obj):
        GroupService().create(obj)

    def update(self, key, obj):
        GroupService().update(key, obj)

    def patch(self, key, field_name, value):
        GroupService().patch(key, field_name, value)

    def delete(self, key):
        GroupService().delete(key)
