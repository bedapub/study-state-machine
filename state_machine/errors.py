"""Collection of state machine errors"""


class GenericStateMachineException(Exception):
    """Generic state machine error"""
    pass


class StatelessException(GenericStateMachineException):
    """Exception if state is not defined"""
    pass


class CurrentStateNotDefined(GenericStateMachineException):
    """Exception if current """
    pass


class NextStateNotDefined(GenericStateMachineException):
    """Error if no next state is defined"""
    pass
