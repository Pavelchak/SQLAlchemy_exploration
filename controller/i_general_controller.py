from abc import abstractmethod, ABCMeta


class IGeneralController:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, key):
        pass

    @abstractmethod
    def create(self, obj):
        pass

    @abstractmethod
    def update(self, obj):
        pass

    @abstractmethod
    def delete(self, key):
        pass
