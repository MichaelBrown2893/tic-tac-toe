import unittest
from typing import TypeVar
from parameterized import parameterized
from unittest.mock import *

from console_app_tools import user_input


class UserInputTests(unittest.TestCase):
    T = TypeVar('T')

    @parameterized.expand([
        [int, "str"],
        [float, "str"],
    ])
    def test_get_input_of_type_incorrect_type_raises(self, expected_type: T, return_value):
        user_input.get_input = MagicMock(name="user_input.get_input")
        user_input.get_input.return_value = return_value
        # user_input.get_input_of_type = unittest.mock.(name="user_input.get_input_of_type")
        with self.assertRaises(ValueError):
            user_input.get_input_of_type(expected_type)

    @parameterized.expand([
        [int, "12"],
        [float, "12.1"],
        [bool, "True"],
        [bool, "False"],
    ])
    def test_get_input_of_type_correct_type_doesnt_raise(self, expected_type: T, return_value):
        user_input.get_input = MagicMock(name="user_input.get_input")
        user_input.get_input.return_value = return_value
        try:
            user_input.get_input_of_type(expected_type)
        except Exception as err:
            self.fail(f"{user_input.get_input_of_type.__name__} raised {type(err)}: {err}")

    @parameterized.expand([
        [int, "12"],
        [float, "12.1"],
        [bool, "True"],
        [bool, "False"],
    ])
    def test_get_input_of_type_correct_type_returns_correct_type(self, input_type: T, return_value):
        user_input.get_input = MagicMock(name="user_input.get_input")
        user_input.get_input.return_value = return_value
        self.assertIs(type(user_input.get_input_of_type(input_type)), input_type)


if __name__ == '__main__':
    unittest.main()
