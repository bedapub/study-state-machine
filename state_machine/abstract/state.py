from abc import ABC, abstractmethod


class AbstractState(ABC):

    # data_obj = None

    def __init__(self):
        pass

    @abstractmethod
    def change(self):
        pass

    @property
    @abstractmethod
    def data_obj(self, data_obj):
        pass

    @data_obj.setter
    @abstractmethod
    def data_obj(self):
        pass

    @abstractmethod
    def get_view(self):
        """ Return view to render """
        pass


