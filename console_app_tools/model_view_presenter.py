"""Contains classes for model view presenter pattern in a console application"""

from __future__ import annotations
from typeguard import typechecked
from observer_pattern.observer_pattern import IObserver, Subject
import os


class ConsolePresenter(IObserver):
    def update(self, subject: ConsoleModel) -> None:
        """Updates the output when the model state has changed"""
        self.set_output(subject.content)

    @typechecked()
    def add_line(self, line: str) -> None:
        """Adds the provided line to the console output

        Parameters
        ----------
        line
            The line to be added to the console output

        Raises
        ------
        TypeError
            The argument given for line was not of type str
        """
        print(line)

    @typechecked()
    def add_lines(self, lines: list[str]) -> None:
        """Adds multiple lines to the console output

        Parameters
        ----------
        lines
            The lines to be added to the console output

        Raises
        ------
        TypeError
            The argument given for lines was not of type list[str]
        """
        for line in lines:
            self.add_line(line)

    @typechecked()
    def set_output(self, output: str) -> None:
        """Set the console output to the content provided

        Parameters
        ----------
        output
            The content to be displayed on the console

        Raises
        ------
        TypeError
            The argument given for line was not of type str
        """
        self.clear()
        self.add_line(output)

    @typechecked()
    def set_output_from_list(self, output: list[str]) -> None:
        """Set the console output to the content provided

        Parameters
        ----------
        output
            The content to be displayed on the console

        Raises
        ------
        TypeError
            The argument given for line was not of type list[str]
        """
        self.clear()
        self.add_lines(output)

    @staticmethod
    def clear() -> None:
        """Clears the console of all text"""
        os.system('cls' if os.name == 'nt' else 'clear')


class ConsoleModel(Subject):
    """Model for the text content to be displayed in the console"""

    def __init__(self, content: str = "", observer: IObserver = ConsolePresenter()) -> None:
        super().__init__()
        self.attach(observer)
        self._content = content

    @property
    def content(self) -> str:
        """Getter for output property

        Returns
        -------
            output
        """
        return self._content

    @content.setter
    def content(self, value: str) -> None:
        """Setter for output property

        Parameters
        ----------
        value
            The value to set content to

        Raises
        ------
        TypeError
            Attempt to set content to a non str value
        """
        if not isinstance(value, str):
            raise TypeError(f"Type {type(value)} given to setter for property: str content")
        self._content = value

    @typechecked
    def add_line(self, line: str) -> None:
        """Adds a list of lines to the output

        Parameters
        ----------
        line
            List of strings to be added to the output

        Raises
        ------
        TypeError
            Value given for argument lines was not of type list[str]
        """
        self.content = self.content + f"\n{line}"

    @typechecked
    def add_lines(self, lines: list[str]) -> None:
        """Adds a list of lines to the output

        Parameters
        ----------
        lines
            List of strings to be added to the output

        Raises
        ------
        TypeError
            Value given for argument lines was not of type list[str]
        """
        for line in lines:
            self.add_line(line)

    def clear_content(self) -> None:
        """Clear all content"""
        self.content = ""
