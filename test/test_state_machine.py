import unittest

from study_state_machine.interfaces import IStudyState
from study_state_machine.errors import StateNotFoundException, BehaviorNotAllowedException
from study_state_machine.study_states import RegisteredState, DatasetState
from study_state_machine.context import Context


class ContextTestCase(unittest.TestCase):

    def test_none_initial_state(self):
        context = Context()
        self.assertIsNone(context.current_state)

    def test_set_current_state(self):
        context = Context()
        context.current_state = RegisteredState()
        self.assertEqual(context.current_state, RegisteredState(context))

    def test_load_unknown_state(self):
        context = Context()
        with self.assertRaises(StateNotFoundException):
            context.load_state("unknown")

    def test_same_state_w_different_context_not_equal(self):
        context = Context(RegisteredState())
        self.assertNotEqual(context.current_state, DatasetState())

    def test_get_available_states(self):
        context = Context()
        name, cls = context.available_states

        self.assertEqual(len(name), 2)

    def test_behavior_create_study(self):
        context = Context(IStudyState)

        for func in [context.create_study, context.change_state, context.add_sample]:
            with self.assertRaises(BehaviorNotAllowedException):
                func(context)


class IStudyStateTestCase(unittest.TestCase):

    def test_study_state_create_study(self):
        state = IStudyState()
        with self.assertRaises(BehaviorNotAllowedException):
            state.create_study()

    def test_study_state_add_sample(self):
        state = IStudyState()
        with self.assertRaises(BehaviorNotAllowedException):
            state.add_sample(None)

    def test_study_state_change_state(self):
        state = IStudyState()
        with self.assertRaises(BehaviorNotAllowedException):
            state.change_state()

