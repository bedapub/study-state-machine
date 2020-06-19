from study_state_machine.interfaces import IStudyState
from study_state_machine.errors import BehaviorNotAllowedException


class ExpressionRegisteredState(IStudyState):
    """An expression study has just been registered"""

    def create_study(self, *args, **kwargs):
        pass

    def change_state(self, *args, **kwargs):
        if kwargs.get("datasets", []) != []:
            self.context.transition_to(ExpressionDatasetState())


class ExpressionDatasetState(IStudyState):
    """At least one dataset has been uploaded"""

    def change_state(self, *args, **kwargs):
        pass

class ExpressionLockedState(IStudyState):
    """The study has been finalized, it can't be edited anymore"""

    def change_state(self, *args, **kwargs):
        message = f"Not allowed to change to another state in state {self.__class__.__name__}."
        message += f" This is a final state where modifications are not allowed anymore"
        raise BehaviorNotAllowedException(message)




