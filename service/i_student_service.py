from abc import ABCMeta, abstractmethod
from .i_general_service import IGeneralService


class IStudentService(IGeneralService):
    __metaclass__ = ABCMeta
