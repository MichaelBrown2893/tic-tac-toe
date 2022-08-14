"""Tests for text_model.py"""
import unittest

from parameterized import parameterized

from .text_model import TextModel


class ContentTests(unittest.TestCase):

    @parameterized.expand([
        [" "],
        [""],
        ["Test Content"]
    ])
    def test_content_getter_returns_content(self, expected_result: str) -> None:
        model = TextModel()
        self.assertEqual(model.content, "")
        model.content = expected_result
        self.assertEqual(model.content, expected_result)

    @parameterized.expand([
        [" "],
        [""],
        ["Test Content"]
    ])
    def test_content_setter_sets_content(self, expected_results: str) -> None:
        model = TextModel(content=expected_results)
        model.content = expected_results
        self.assertEqual(model.content, expected_results)

    @parameterized.expand([
        [" "],
        [""],
        ["Test Content"]
    ])
    def test_content_setter_passed_string_doesnt_raise_type_error(self, content: str) -> None:
        model = TextModel()
        try:
            model.content = content
        except TypeError as err:
            self.fail(err)

    @parameterized.expand([
        [1],
        [1.2],
        [["List", "Of", "Strings"]],
        [[1, 2, 3]],
        [(1, 2, 3)],
        [("Tuple", "Of", "Strings")],
        [{1, 2, 3}],
        [{"Set", "Of", "Strings"}]
    ])
    def test_content_setter_passed_invalid_content_raises_type_error(self, invalid_content: str) -> None:
        model = TextModel()
        with self.assertRaises(TypeError):
            model.content = invalid_content


class AddContentOnNewLineTests(unittest.TestCase):
    @parameterized.expand([
        ["TestContent"],
        ["Multi\nLine\nText\nContent"]
    ])
    def test_add_content_on_new_line_adds_content_on_new_line(self, content: str):
        initial_content = "Starting Content"
        model = TextModel(initial_content)
        model.add_content_on_new_line(content)
        self.assertEqual(model.content, "{0}\n{1}".format(initial_content,content))

    @parameterized.expand([
        ["TestContent"],
        ["Multi\nLine\nText\nContent"]
    ])
    def test_add_content_on_new_line_string_passed_doesnt_raise(self, content: str):
        model = TextModel()
        try:
            model.add_content_on_new_line(content)
        except TypeError as err:
            self.fail(err)

    @parameterized.expand([
        [1],
        [1.2],
        [["List", "Of", "Strings"]],
        [[1, 2, 3]],
        [(1, 2, 3)],
        [("Tuple", "Of", "Strings")],
        [{1, 2, 3}],
        [{"Set", "Of", "Strings"}]
    ])
    def test_add_content_on_new_line_invalid_type_raises_type_error(self, invalid_content: str):
        model = TextModel()
        with self.assertRaises(TypeError):
            model.add_content_on_new_line(invalid_content)


class AddNewLinesTests(unittest.TestCase):
    @parameterized.expand([
        [[]],
        [["List"]],
        [["List", "Of"]],
        [["List", "Of", "Strings"]],

    ])
    def test_add_new_lines_adds_new_lines(self, new_lines: list[str]) -> None:
        initial_content = "initial\ncontent"
        model = TextModel(initial_content)
        self.assertEqual(model.content, initial_content)
        model.add_new_lines(new_lines)
        self.assertEqual(model.content, "{0}\n{1}".format(initial_content, "\n".join(new_lines)))

    @parameterized.expand([
        [[]],
        [["List"]],
        [["List", "Of"]],
        [["List", "Of", "Strings"]],
        [("Tuple", "Of", "Strings")],
        [{"Set", "Of", "Strings"}]

    ])
    def test_add_new_lines_passed_list_string_doesnt_raise(self, new_lines: list[str]) -> None:
        model = TextModel()
        try:
            model.add_new_lines(new_lines)
        except TypeError as err:
            self.fail(err)

    @parameterized.expand([
        [1],
        [1.2],
        [[1, 2, 3]],
        [(1, 2, 3)],
        [{1, 2, 3}],
    ])
    def test_add_new_lines_passed_invalid_type_raises_type_error(self, invalid_content) -> None:
        model = TextModel()
        with self.assertRaises(TypeError):
            model.add_new_lines(invalid_content)


class ClearTests(unittest.TestCase):
    @parameterized.expand([
        ["Some"],
        ["Test\nContent"]
    ])
    def test_clear_clears_content(self, initial_content: str) -> None:
        model = TextModel(initial_content)
        self.assertEqual(model.content, initial_content)
        model.clear()
        self.assertEqual(model.content, "")


if __name__ == "__main__":
    unittest.main()
