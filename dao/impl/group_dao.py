from dao.i_group_dao import IGroupDAO
from domain import Group, session


class GroupDAO(IGroupDAO):

    def find_all(self):
        return session.query(Group).all()

    def find_by_id(self, key):
        return session.query(Group).get(key)

    def create(self, obj):
        session.add(obj)
        session.commit()

    def update(self, key, obj):
        group = session.query(Group).get(key)
        group.full_update(obj)
        session.commit()

    def patch(self, key, field_name, value):
        group = session.query(Group).get(key)
        setattr(group, field_name, value)
        session.commit()

    def delete(self, key):
        group = session.query(Group).get(key)
        session.delete(group)
        session.commit()
