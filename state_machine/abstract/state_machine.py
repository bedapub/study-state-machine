from abc import ABC, abstractmethod
from functools import wraps


class StatelessException(Exception):
    pass


def is_stateful(func):
    """ Decorator which ensures that `func` is only called if a current state is not None """
    @wraps(func)
    def wrapped(self, *args, **kwargs):
        if not self.current_state:
            raise StatelessException("the function {}() can only be called if the state is defined. Define a state by "
                                     "either calling `set_data_obj()` or `set_initial_state()".format(func.__name__))

        return func(args, kwargs)

    return wrapped


class StateMachine(ABC):

    def __init__(self, initial_state_cls=None):
        """
        :param initial_state_cls: The class of the initial state
        """
        if not callable(initial_state_cls):
            raise AttributeError("initial_state_cls is not callable")

        self._init_state_cls = initial_state_cls

    # @abstractmethod
    # def set_data_obj(self, data_obj, *args, **kwargs):
    #     """ Pass data_obj to the current state """
    #     pass
    #
    # def init_state(self, *args, **kwargs):
    #     """ Set the initial state """
    #     if not self.initial_state_cls:
    #         raise AttributeError("initial_state_cls is undefined")
    #
    #     self.current_state = self._initial_state_cls(*args, **kwargs)

    @is_stateful
    def change(self, *args, **kwargs):
        """ Delegate state change to the current state"""
        self.current_state = self.current_state.change(*args, **kwargs)

    # @is_stateful
    # def get_view(self):
    #     """ Return view from current state """
    #     return self.current_state.get_view()
