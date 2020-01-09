class OrmConfig:
    DB_FILE = 'cy_xml_db.sqlite'
    DB_PATH = ''
    IS_DEL_DB_FILE = True
    DB_CONNECT_STR = 'sqlite:///' + DB_PATH + DB_FILE
    # DB_CONNECT_STR = 'sqlite:///:memory:'
    ECHO = False
    LOAD_DATA_TO_DB = True
