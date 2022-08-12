"""Tests for classes in model_view_presenter.py"""

from parameterized import parameterized
from type_checking.type_check_tests import *
from model_view_presenter import *


class ConsoleModelTests(unittest.TestCase):

    # region content tests
    @parameterized.expand([
        [1], [1.0], [-4],
        [["", "", ""]], [(1, 2, 3)], [{"type": "dictionary"}],
        [False], [True], [None]
    ])
    def test_set_content_wrong_type_raises(self, value: str):
        model = ConsoleModel()
        with self.assertRaises(TypeError):
            model.content = value

    @parameterized.expand(["Test string"])
    def test_set_content_correct_type_does_not_raise(self, value: str):
        model = ConsoleModel()
        try:
            model.content = value
        except Exception as err:
            self.fail(f"{model.content} setter raised {type(err)}: {err}")

    def test_content_getter_returns_content(self):
        expected_result = "Test"
        model = ConsoleModel(expected_result)
        self.assertEqual(expected_result, model.content)

    def test_content_setter_sets_content(self):
        initial_content = "original"
        expected_result = "altered_text"
        model = ConsoleModel(initial_content)
        model.content = expected_result
        self.assertEqual(expected_result, model.content)

    # endregion

    # region add_line tests
    @parameterized.expand([
        [1], [1.0], [-4],
        [["", "", ""]], [(1, 2, 3)], [{"type": "dictionary"}],
        [False], [True], [None]
    ])
    def test_add_line_wrong_type_raises(self, value: str):
        model = ConsoleModel()
        type_check_raises(self, model.add_line, value, error_type=TypeError)

    @parameterized.expand([["Test string"]])
    def test_add_line_correct_type_does_not_raise(self, value: str):
        model = ConsoleModel()
        type_check_doesnt_raise(self, model.add_line, value)

    @parameterized.expand([
        ["", "line"],
        ["initial_value", "line"]
    ])
    def test_add_line_adds_line_to_content(self, initial_value: str, line: str):
        model = ConsoleModel(initial_value)
        model.add_line(line)
        self.assertEqual(model.content, f"{initial_value}\n{line}")

    # endregion

    # region add_lines tests
    @parameterized.expand([
        [1], [1.0], [-4],
        ["Test String"], [(1, 2, 3)], [{"type": "dictionary"}],
        [False], [True], [None]
    ])
    def test_add_lines_wrong_type_raises(self, value: list[str]):
        model = ConsoleModel()
        type_check_raises(self, model.add_lines, value, error_type=TypeError)

    @parameterized.expand([[["Test string 1", "Test string 2"]]])
    def test_add_lines_correct_type_does_not_raise(self, value: list[str]):
        model = ConsoleModel()
        type_check_doesnt_raise(self, model.add_lines, value)

    @parameterized.expand([
        ["", ["line1", "line2", "line3"]],
        ["initial_value", ["line1", "line2", "line3"]]
    ])
    def test_add_lines_adds_lines_to_content(self, initial_value: str, lines: list[str]):
        model = ConsoleModel(initial_value)
        model.add_lines(lines)
        self.assertEqual(initial_value + "\n" + "\n".join(lines), model.content)

    # endregion

    # region clear_content tests
    @parameterized.expand([
        [""],
        ["initial content"],
        ["initial\nmulti\nline\ncontent"]
    ])
    def test_clear_content_clears_content(self, initial_value: str):
        expected_case = ""
        model = ConsoleModel(initial_value)
        model.clear_content()
        self.assertEqual(expected_case, model.content)

    # endregion


class ConsoleViewTests(unittest.TestCase):

    # region add_line tests
    @parameterized.expand([
        [1], [1.0], [-4],
        [["", "", ""]], [(1, 2, 3)], [{"type": "dictionary"}],
        [False], [True], [None]
    ])
    def test_add_line_wrong_type_raises(self, value: str):
        view = ConsoleView()
        type_check_raises(self, view.add_line, value, error_type=TypeError)

    @parameterized.expand([["Test string"]])
    def test_add_line_correct_type_does_not_raise(self, value: str):
        view = ConsoleView()
        type_check_doesnt_raise(self, view.add_line, value)

    # endregion

    # region add_lines tests
    @parameterized.expand([
        [1], [1.0], [-4],
        ["Test String"], [(1, 2, 3)], [{"type": "dictionary"}],
        [False], [True], [None]
    ])
    def test_add_lines_wrong_type_raises(self, value: list[str]):
        view = ConsoleView()
        type_check_raises(self, view.add_lines, value, error_type=TypeError)

    @parameterized.expand([[["Test string 1", "Test string 2"]]])
    def test_add_lines_correct_type_does_not_raise(self, value: list[str]):
        view = ConsoleView()
        type_check_doesnt_raise(self, view.add_lines, value)
    # endregion

    # region set_output tests
    @parameterized.expand([
        [1], [1.0], [-4],
        [(1, 2, 3)], [{"type": "dictionary"}], [["Test string 1", "Test string 2"]],
        [False], [True], [None]
    ])
    def test_set_output_lines_wrong_type_raises(self, value: list[str]):
        view = ConsoleView()
        type_check_raises(self, view.set_output, value, error_type=TypeError)

    @parameterized.expand([
        ["Test string 1"]
    ])
    def test_set_output_correct_type_does_not_raise(self, value: list[str]):
        view = ConsoleView()
        type_check_doesnt_raise(self, view.set_output, value)
    # endregion

    # region set_output_from_list tests
    @parameterized.expand([
        [1], [1.0], [-4],
        [(1, 2, 3)], [{"type": "dictionary"}], ["Test string 1"],
        [False], [True], [None]
    ])
    def test_set_output_from_list_wrong_type_raises(self, value: list[str]):
        view = ConsoleView()
        type_check_raises(self, view.set_output_from_list, value, error_type=TypeError)

    @parameterized.expand([
        [["Test string 1", "Test string 2"]]
    ])
    def test_set_output_from_list_correct_type_does_not_raise(self, value: list[str]):
        view = ConsoleView()
        type_check_doesnt_raise(self, view.set_output_from_list, value)

    # endregion


if __name__ == '__main__':
    unittest.main()
