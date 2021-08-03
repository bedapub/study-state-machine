import sys
import inspect

from study_state_machine.study_states.generic import GenericState, RegisteredState, \
    DatasetState, ProcessedState, AnalyzedState, LockedState

"""
Store all above imported states in dict <name, class>
"""
available_states = {}

for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass):
    available_states[name] = obj

__all__ = ["GenericState", "RegisteredState", "DatasetState", "ProcessedState",
    "AnalyzedState", "LockedState"]
