import sqlalchemy as db
from sqlalchemy.orm import mapper
from domain.user import User


print("vers SQLAlchemy :", db.__version__)

engine = db.create_engine('sqlite:///:memory:', echo=True)
# metadata = db.MetaData()
# users_table = db.Table('users', metadata,
#     db.Column('id', db.Integer, primary_key=True),
#     db.Column('name', db.String),
#     db.Column('fullname', db.String),
#     db.Column('password', db.String)
# )

metadata.create_all(engine)


print(mapper(User, users_table))
user = User("John", "John first", "qweasdzxc")

print(user)
print(user.id)
