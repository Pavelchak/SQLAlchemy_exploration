from sqlalchemy.ext.declarative import declarative_base

# class Base:
#     __base = None
#
#     @classmethod
#     def get_base(cls):
#         if cls.__base is None:
#             cls.__base = declarative_base()
#         return cls.__base

Base = declarative_base()
