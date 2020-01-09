from sqlalchemy import Column, Integer, String
from base import Base


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    city = Column(String(35))
    street = Column(String(35))
    apartment = Column(String(15))

    def __init__(self, city, street, apartment):
        self.city = city
        self.street = street
        self.apartment = apartment

    def __repr__(self):
        return "Address('%s', '%s', '%s', '%s')" % (self.id, self.city, self.street, self.apartment)
