"""Tests for the classes and methods in text_presenter.py"""

import unittest
from unittest.mock import MagicMock, patch

from parameterized import parameterized

from console_app_tools.ModelViewPresenter.Models.text_model import ITextModel
from console_app_tools.ModelViewPresenter.Presenters.text_presenter import ConsoleTextPresenter


class MockTextModel(ITextModel):
    @property
    def content(self) -> str:
        return "Mock content"

    def add_content_on_new_line(self, content: str) -> None:
        pass

    def add_new_lines(self, new_lines: list[str]) -> None:
        pass

    def clear(self) -> None:
        pass


class DisplayTextTests(unittest.TestCase):
    def setUp(self) -> None:
        self._presenter = ConsoleTextPresenter()

    @parameterized.expand([
        [" "],
        [""],
        ["Test Content"]
    ])
    def test_display_text_passed_string_doesnt_raise(self, valid_text: str) -> None:
        try:
            self._presenter.display_text(valid_text)
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
        [{"Set", "Of", "Strings"}],
        [MockTextModel()]
    ])
    def test_display_text_passed_invalid_type_raises_type_error(self, invalid_text) -> None:
        with self.assertRaises(TypeError):
            self._presenter.display_text(invalid_text)


class UpdateTests(unittest.TestCase):
    def setUp(self) -> None:
        self._model = MockTextModel()
        self._presenter = ConsoleTextPresenter()

    def mock_display_text(self, text: str):
        pass

    def test_update_tests_valid_model_passed_doesnt_raise(self) -> None:
        try:
            self._presenter.update(self._model)
        except TypeError as err:
            self.fail(err)

    def test_update_tests_valid_model_calls_display_text(self) -> None:
        with patch.object(ConsoleTextPresenter, 'display_text', MagicMock(side_effect=self.mock_display_text)):
            self._presenter.update(self._model)
            self.assertTrue(self._presenter.display_text.called)

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
    def test_update_tests_invalid_type_raises_type_error(self, invalid_model) -> None:
        with self.assertRaises(TypeError):
            self._presenter.update(invalid_model)


if __name__ == '__main__':
    unittest.main()
