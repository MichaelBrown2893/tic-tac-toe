import unittest
from typing import TypeVar, Callable
from parameterized import parameterized
from unittest.mock import *

from console_app_tools.Input import input_handler

T = TypeVar('T')


class GetInputTests(unittest.TestCase):
    @parameterized.expand([
        ["12"],
        ["12.1"],
        ["True"],
        ["False"],
        ["Hello World"],
    ])
    def test_get_input_without_type_or_condition_returns_input_string(self, return_value):
        user_input._get_string = MagicMock()
        user_input._get_string.return_value = return_value
        self.assertEquals(user_input.get_input(), return_value)

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

    @parameterized.expand([
        [str, lambda x: len(x) == 2, "12"],
        [float, lambda x: x == 4.5, "4.5"],
        [int, lambda x: x == 12, "12"],
        [int, lambda x: int(x) % 2 == 0, "2"],
    ])
    def test_get_input_with_condition_and_type_checks_both(self, return_type: T, condition: Callable, return_value: T):
        user_input._get_string = MagicMock()
        user_input._get_string.return_value = return_value
        self.assertEqual(user_input.get_input(return_type=return_type, condition=condition), return_type(return_value))


class GetYesOrNoTests(unittest.TestCase):
    @parameterized.expand([
        ['y', True],
        ['Y', True],
        ['n', False],
        ['N', False],
    ])
    def test_get_yes_or_no_returns_correct_bool(self, mock_input: str, expected_result: bool):
        user_input._get_string = MagicMock()
        user_input._get_string.return_value = mock_input
        self.assertEqual(user_input.get_yes_or_no(), expected_result)


class CheckConditionTests(unittest.TestCase):
    @parameterized.expand([
        ["Hello", lambda x: x == "Hello"],
        ["String", lambda x: len(x) == len("String")],
        [12, lambda x: x < 13],
        [14.5, lambda x: x * 10 == 145]
    ])
    def test__check_condition_pass_condition_doesnt_raise(self, value: T, condition: Callable):
        try:
            user_input._check_condition(value=value, condition=condition)
        except BaseException as err:
            self.fail(err)

    @parameterized.expand([
        ["Hello", lambda x: x == "Hello"],
        ["String", lambda x: len(x) == len("String")],
        [12, lambda x: x < 13],
        [14.5, lambda x: x * 10 == 145]
    ])
    def test__check_condition_pass_condition_returns_true(self, value: T, condition: Callable):
        self.assertEqual(user_input._check_condition(value=value, condition=condition), True)

    @parameterized.expand([
        ["Hello", lambda x: x == "Hello world"],
        ["String", lambda x: len(x) == len("float")],
        [12, lambda x: x < 12],
        [14.5, lambda x: x * 10 == 150]
    ])
    def test__check_condition_fail_condition_returns_false(self, value: T, condition: Callable):
        self.assertEqual(user_input._check_condition(value=value, condition=condition), False)

    @parameterized.expand([
        ["Hello", lambda x: x == x / 0],
        ["String", lambda x: x == x / 0],
        [12, lambda x: x == x / 0],
        [14.5, lambda x: x == x / 0]
    ])
    def test__condition_error_raises_Exception(self, value: T, condition: Callable):
        with self.assertRaises(BaseException):
            user_input._check_condition(value=value, condition=condition)


class CastValueTests(unittest.TestCase):
    @parameterized.expand([
        ["12", int],
        ["12", float],
        ["true", bool],
        ["", bool],
        ["Letters", list],
        ["12", tuple],
        ["Letters", set]
    ])
    def test_cast_value_casts_returns_expected_type(self, value: str, return_type: T):
        self.assertIs(type(user_input._cast_value(value=value, return_type=return_type)), return_type)

    @parameterized.expand([
        ["12", int, 12],
        ["12", float, 12.0],
        ["true", bool, True],
        ["", bool, False],
        ["Letters", list, ['L', 'e', 't', 't', 'e', 'r', 's']],
        ["12", tuple, ('1', '2')],
        ["Letters", set, {'L', 'e', 't', 'r', 's'}]
    ])
    def test_cast_value_casts_returns_expected_value(self, value: str, return_type: T, expected_value: T):
        self.assertEqual(user_input._cast_value(value=value, return_type=return_type), expected_value)

    @parameterized.expand([
        ["hello", int],
        ["hello", float],
        ["hello", complex],
        ["", int],
        ["", float],
        ["", complex],
    ])
    def test_cast_value_cant_cast_raises_value_error(self, value: str, return_type: T):
        with self.assertRaises(ValueError):
            user_input._cast_value(value=value, return_type=return_type)


if __name__ == '__main__':
    unittest.main()
