from abc import ABCMeta, abstractmethod

from .i_general_controller import IGeneralController


class IGroupController(IGeneralController):
    __metaclass__ = ABCMeta
