from domain.db_connection import SessionManager as SM
from view.my_view import MyView


def main():
    MyView().show()
    # SM.get_session()


main()
