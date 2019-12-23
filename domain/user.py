# class User(object):
#     def __init__(self, name, fullname, password):
#         self.name = name
#         self.fullname = fullname
#         self.password = password
#
#     def __repr__(self):
#         return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s', '%s','%s', '%s')>" % (self.id, self.name, self.fullname, self.password)


Base.metadata.create_all(engine)

user = User("John", "John first", "qweasdzxc")

# Session = sessionmaker(bind=engine)
session = sessionmaker(bind=engine)()

session.add(user)
session.commit()

print(user)

ourUser = session.query(User).filter_by(name="John").all()
print ourUser


