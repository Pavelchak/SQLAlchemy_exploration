from abc import ABCMeta, abstractmethod
from .i_general_service import IGeneralService


class IGroupService(IGeneralService):
    __metaclass__ = ABCMeta
