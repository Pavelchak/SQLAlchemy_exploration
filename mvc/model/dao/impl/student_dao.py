from mvc.model.dao.i_student_dao import IStudentDAO
from mvc.model.domain.db_connection import SessionManager
from mvc.model.domain.student import Student


class StudentDAO(IStudentDAO):

    def find_all(self):
        session = SessionManager.get_session()
        return session.query(Student).all()

    def find_by_id(self, key):
        session = SessionManager.get_session()
        return session.query(Student).filter_by(id=key).all()

    def create(self, obj):
        session = SessionManager.get_session()
        session.add(obj)
        session.commit()

    def update(self, obj):
        pass

    def delete(self, key):
        pass
