from abc import ABCMeta, abstractmethod

from .i_general_controller import IGeneralController


class IStudentController(IGeneralController):
    __metaclass__ = ABCMeta
