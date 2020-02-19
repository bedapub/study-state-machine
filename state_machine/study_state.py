"""Implementation of a finite state machine for studies

The :func:`~.StudyStateMachine` controls the state of the study. First, one has to evaluate the next state. This is
done with the :func:`~StudyStateMachine.eval_next_state` which uses passed keyword arguments to determine the next
state. Second, :func:`~StudyStateMachine.change` makes the transition to the next state. It is necessary to
always evaluate the next state before changing to it.

>>> state_machine = StudyStateMachine()
... state_machine.eval_next_state({"platform": "expression"})
... state_machine.change()
... state_machine.current_state
StudyStateMachine(current state: StudyExpressionState, next state: None)

"""
from abc import ABC, abstractmethod

from state_machine.errors import NextStateNotDefined, StatelessException


class StudyStateMachine:
    """State Machine controller for study data"""

    def __init__(self):
        """ """
        self.current_state = None

    def __repr__(self):
        return f"{self.__class__.__name__}" \
               f"(current state: {self.current_state}, next state: {self.current_state.next_state})"

    def eval_next_state(self, **kwargs):
        """Set the next state based on the passed data.

        The next state is chosen based on the passed data.

        :returns name of the next state
        """
        if not self.current_state:
            raise StatelessException(f"{self.current_state.__name__} not defined. "
                                     f"Call {self.load_initial_state.__name__} to set the initial state")

        return self.current_state.eval_next_state(**kwargs)

    def change(self, *args, **kwargs):
        """Make the transition from the current to the next state"""
        if not self.current_state.next_state:
            raise StatelessException(f"{self.current_state.next_state.__name__} not defined."
                                     f" Call {self.eval_next_state.__name__} to determine the next state.")

        self.current_state = self.current_state.change(*args, **kwargs)

    def load_state(self, name, *args, **kwargs):

        study_states = {
            "generic_study": StudyGenericState,
            "immunogenicity": StudyImmunogenicityState,
            "retroperspective_insert": StudyRetroperspectiveInsertState,
            "rna_sequencing_biokit": StudyRNA_SeqState
        }

        state_cls = study_states[name]
        self.current_state = state_cls(*args, **kwargs)

    def load_initial_state(self, name, *args, **kwargs):

        study_state = {
            "generic_study": StudyGenericState,
            "rna_sequencing_biokit": StudyRNA_SeqState,
        }

        state_cls = study_state[name]
        self.current_state = state_cls(*args, **kwargs)


class AbstractStudyState(ABC):

    def __init__(self):
        self.next_state = None

    def __repr__(self):
        return f"{self.__class__.__name__}"

    def change(self, *args, **kwargs):
        return self.next_state(*args, **kwargs)

    @abstractmethod
    def eval_next_state(self, **kwargs):
        """Evaluate the state in which the study will transition based on the passed input"""
        raise NotImplementedError


class StudyGenericState(AbstractStudyState):

    def eval_next_state(self, **kwargs):

        if "platform" not in kwargs.keys():
            raise AttributeError("Expected platform in submitted data")

        platform_name = kwargs["platform"]

        supported_platforms = {
            "expression": StudyExpressionState,
            "immunogenicity": StudyImmunogenicityState
        }

        if platform_name not in supported_platforms.keys():
            raise AttributeError(f"Could not find platform. Supported platforms are {supported_platforms.keys()}")

        self.next_state = supported_platforms[platform_name]

        return platform_name


class StudyExpressionState(AbstractStudyState):

    def eval_next_state(self, **kwargs):
        raise NotImplementedError


class StudyImmunogenicityState(AbstractStudyState):

    def eval_next_state(self, **kwargs):
        raise NotImplementedError

class StudyRNA_SeqState(AbstractStudyState):

    def eval_next_state(self, **kwargs):
        self.next_state = StudyRNA_SeqState
        return "rna_sequencing_biokit"


class StudyRetroperspectiveInsertState(AbstractStudyState):

    def eval_next_state(self, **kwargs):
        raise NotImplementedError

if __name__ == '__main__':
    print("Hello")
