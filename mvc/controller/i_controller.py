from abc import abstractmethod, ABCMeta


class IController:
    __metaclass__ = ABCMeta

    @abstractmethod
    def action1(self):
        pass

    @abstractmethod
    def action2(self):
        pass
