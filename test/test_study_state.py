import unittest

from state_machine.abstract.state_machine import StatelessException
from state_machine.study_state import StudyGenericState


class MyTestCase(unittest.TestCase):
    def test_error_thrown(self):
        ssm = StudyGenericState()

        with self.assertRaises(StatelessException):
            ssm.change()

        with self.assertRaises(StatelessException):
            ssm.get_view()

    def test_initial_state(self):
        ssm = StudyGenericState()
        ssm.init_state()

        self.assertEqual(ssm.current_state.__class__.__name__, "StudyInitialState")


if __name__ == '__main__':
    unittest.main()
