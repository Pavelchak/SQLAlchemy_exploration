from dao import GroupDAO
from ..i_group_service import IGroupService


class GroupService(IGroupService):

    def find_all(self):
        return GroupDAO().find_all()

    def find_by_id(self, key):
        return GroupDAO().find_by_id(key)

    def create(self, obj):
        GroupDAO().create(obj)

    def update(self, key, obj):
        GroupDAO().update(key, obj)

    def patch(self, key, field_name, value):
        GroupDAO().patch(key, field_name, value)

    def delete(self, key):
        GroupDAO().delete(key)
