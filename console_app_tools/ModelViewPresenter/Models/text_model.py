"""Model containing text information"""
from abc import ABC, abstractmethod
from typing import TypeVar, Callable

from observer_pattern.observer_pattern import Subject
from typeguard import typechecked
from console_app_tools.Input.input_handling import get_input


class ITextModel(Subject):
    """Interface for TextModels"""

    @property
    @abstractmethod
    def content(self) -> str:
        """Text content stored by the TextModel"""
        pass

    @content.setter
    @abstractmethod
    def content(self, value: str) -> str:
        """Getter for content stored by TextModel"""
        pass

    @abstractmethod
    def add_content_on_new_line(self, content: str) -> None:
        """Add content to the TextModel starting on a new line"""
        pass

    @abstractmethod
    def add_new_lines(self, new_lines: list[str]) -> None:
        """Add new lines to the TextModel"""
        pass

    @abstractmethod
    def clear(self) -> None:
        """Clear content stored in the text Model"""
        pass


class TextModel(ITextModel):
    """Model for text"""

    def __init__(self, content: str = ""):
        super().__init__()
        self._content: str = content

    @property
    def content(self) -> str:
        """Getter for the content property

        Returns
        -------
        str
            TextContent
        """
        return self._content

    @content.setter
    @typechecked
    def content(self, value: str) -> None:
        """Setter for the content property

        Parameters
        ----------
        value
            New content to be stored in the model

        Raises
        ------
        TypeError
            value passed was not of type str
        """
        self._content = value

    @typechecked
    def add_content_on_new_line(self, additional_content: str) -> None:
        """Add additional content starting on a new line

        Parameters
        ----------
        additional_content
            Additional content to be added to the model

        Raises
        ------
        TypeError
            additional_content passed was not of type str
        """
        self.content = "{0}\n{1}".format(self.content, additional_content)

    @typechecked
    def add_new_lines(self, new_lines: [str]) -> None:
        """Add additional lines starting on a new line

        Parameters
        ----------
        new_lines
            Collection of new lines to be added to the content

        Raises
        ------
        TypeError
            value passed for new lines was not of type list[str]
        """
        self.content = "{0}\n{1}".format(self.content, "\n".join(new_lines))

    def clear(self):
        """Set content to empty string"""
        self.content = ""


T = TypeVar('T')


class IInputTextModel(TextModel):
    @property
    @abstractmethod
    def prompt(self) -> str:
        """Getter for the prompt portion of the models content"""
        pass

    @prompt.setter
    @abstractmethod
    def prompt(self, value: str):
        """Setter for the prompt portion of the models content"""
        pass

    @property
    @abstractmethod
    def input_value(self) -> T:
        """The input value portion of the models content"""
        pass

    @input_value.setter
    @abstractmethod
    def input_value(self, value: T):
        """Setter for the input value portion of the models content"""
        pass


class InputTextModel(IInputTextModel):
    """Model extending TextModel which is intended for representing Input()"""
    def __init__(self, prompt: str, value: T):
        content = self.create_content_from_prompt_and_value(prompt=prompt, value=value)
        super().__init__(content)
        self._prompt = prompt
        self._input_value = value

    # noinspection GrazieInspection
    @typechecked
    def create_content_from_prompt_and_value(self, prompt: str, value: T) -> str:
        """Constructs a string from prompt and value. Value color will match that from console input

        Parameters
        ----------
        prompt
            String of text that was displayed to the user when prompted for input

        value
            value input by the user

        Raises
        ------
        ValueError
            The input returned could not be converted to string

        Returns
        -------
        str
            Returns a string of the concatenated prompted and value. value colored to match input()
        """

        input_green = '\033[92m'
        endc = '\033[0m'

        try:
            return f"{prompt} {input_green}{value}{endc}"
        except ValueError as err:
            raise ValueError(f"Input: {value} of type: {type(value)} could not be converted to string.")

    @property
    def prompt(self) -> str:
        return self._prompt

    @prompt.setter
    @typechecked
    def prompt(self, value: str):
        self._prompt = value

    @property
    def input_value(self) -> T:
        return self._input_value

    @input_value.setter
    @typechecked
    def input_value(self, value: T):
        self._input_value = value


# noinspection SpellCheckingInspection
def InputTextModelFactory(prompt: str, expected_input_type: T = str, condition: Callable = None) -> TextModel:
    """Factory that will construct TextModels created from console input

    Parameters
    ----------
    prompt
        String of text to be displayed to the user when prompted for input

    expected_input_type
        The type expected to be returned by the input.
        This will be converted back to str but is neccesary for checking conditions

    condition
        boolean lambda function for the condition the input must meet to be accepted

    Returns
    -------
    TextModel
        Returns a TextModel representing the console input used to construct a text model
    """
    value = get_input(prompt=prompt, return_type=expected_input_type, condition=condition)
    return InputTextModel(prompt=prompt, value=value)
