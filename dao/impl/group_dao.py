from dao.i_group_dao import IGroupDAO
from domain.db_connection import SessionManager
from domain.group import Group


class GroupDAO(IGroupDAO):

    def find_all(self):
        session = SessionManager.get_session()
        return session.query(Group).all()

    def find_by_id(self, key):
        session = SessionManager.get_session()
        return session.query(Group).filter_by(id=key).all()

    def create(self, obj):
        session = SessionManager.get_session()
        session.add(obj)
        session.commit()

    def update(self, obj):
        pass

    def delete(self, key):
        pass
