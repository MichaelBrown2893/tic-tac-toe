import unittest
from typing import TypeVar, Callable
from parameterized import parameterized
from unittest.mock import *

from console_app_tools import user_input


class UserInputTests(unittest.TestCase):

    T = TypeVar('T')

    # region get input
    @parameterized.expand([
        [int, "12"],
        [float, "12.1"],
        [bool, "True"],
        [bool, "False"],
    ])
    def test_get_input_with_type_argument_returns_correct_type(self, input_type: T, return_value):
        user_input._get_string = MagicMock()
        user_input._get_string.return_value = return_value
        self.assertIs(type(user_input.get_input(return_type=input_type)), input_type)

    @parameterized.expand([
        [lambda x: len(x) == 2, "12"],
        [lambda x: x == "4", "4"],
        [lambda x: int(x) == 12, "12"],
        [lambda x: int(x) % 2 == 0, "2"],
    ])
    def test_get_input_with_condition_argument_checks_condition(self, condition: Callable, return_value: str):
        user_input._get_string = MagicMock()
        user_input._get_string.return_value = return_value
        self.assertEqual(user_input.get_input(condition=condition), return_value)
    # endregion


if __name__ == '__main__':
    unittest.main()
