from study_state_machine.interfaces import IStudyState

class GenericState(IStudyState):
    """A generic state for conveniance, it is final and unlocked"""

    def create_study(self, *args, **kwargs):
        pass

    def change_state(self, *args, **kwargs):
        pass