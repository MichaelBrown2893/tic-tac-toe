"""Unit tests for the ConsoleView class in console_view.py"""

import unittest
from type_checking.type_check_tests import type_check_doesnt_raise, type_check_raises
import console_view
from parameterized import parameterized


class ConsoleViewTests(unittest.TestCase):

    @parameterized.expand([
        [1], [1.0], [-4],
        [["", "", ""]], [(1, 2, 3)], [{"type": "dictionary"}],
        [False], [True], [None]
    ])
    def test_add_line_wrong_type_raises(self, value: str):
        view = console_view.ConsoleView()
        type_check_raises(self, view.add_line, value, error_type=TypeError)

    @parameterized.expand([["Test string"]])
    def test_add_line_correct_type_does_not_raise(self, value: str):
        view = console_view.ConsoleView()
        type_check_doesnt_raise(self, view.add_line, value)

    @parameterized.expand([
        [1], [1.0], [-4],
        ["Test String"], [(1, 2, 3)], [{"type": "dictionary"}],
        [False], [True], [None]
    ])
    def test_add_lines_wrong_type_raises(self, value: list[str]):
        view = console_view.ConsoleView()
        type_check_raises(self, view.add_lines, value, error_type=TypeError)

    @parameterized.expand([[["Test string 1", "Test string 2"]]])
    def test_add_lines_correct_type_does_not_raise(self, value: list[str]):
        view = console_view.ConsoleView()
        type_check_doesnt_raise(self, view.add_lines, value)


if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()
