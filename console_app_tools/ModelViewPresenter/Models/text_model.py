"""Model containing text information"""
from abc import ABC, abstractmethod

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
