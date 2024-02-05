import unittest
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        """
        Set up a new State instance before each test.
        """
        self.state = State()

    def test_state_name_default(self):
        """
        Test the default value of State.name.
        """
        self.assertEqual(self.state.name, "")
