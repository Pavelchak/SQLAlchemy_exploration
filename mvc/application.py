from mvc.model.domain.db_connection import SessionManager as sm


def main():
    # MyView().show()
    sm.get_session()


main()
