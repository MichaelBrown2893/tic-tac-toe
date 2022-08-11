"""Contains classes for model view presenter pattern in a console application"""

from __future__ import annotations
from typeguard import typechecked
from observer_pattern.observer_pattern import Observer, Subject
import os


class ConsoleView:
    """Console view for MVP pattern"""

    @typechecked
    def add_line(self, line: str):
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

    @typechecked
    def add_lines(self, lines: list[str]):
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

    @staticmethod
    def clear():
        """Clears the console of all text"""
        os.system('cls' if os.name == 'nt' else 'clear')

    @typechecked()
    def set_output_from_list(self, output: list[str]):
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

    @typechecked
    def set_output(self, output: str):
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


class ConsolePresenter(Observer):
    def __init__(self, view: ConsoleView = ConsoleView()):
        self._view = view

    def update(self, subject: ConsoleModel) -> None:
        """Updates the output when the model state has changed"""
        self.set_output(subject.content)

    def add_line(self, line: str):
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
        self._view.add_line(line)

    def add_lines(self, lines: list[str]):
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
        self._view.add_lines(lines)

    def set_output(self, line: str):
        """Set the console output to the content provided

        Parameters
        ----------
        line
            The content to be displayed on the console

        Raises
        ------
        TypeError
            The argument given for line was not of type str
        """
        self._view.set_output(line)

    def set_output_from_list(self, lines: list[str]):
        """Set the console output to the content provided

        Parameters
        ----------
        lines
            The content to be displayed on the console

        Raises
        ------
        TypeError
            The argument given for line was not of type list[str]
        """
        self._view.set_output_from_list(lines)

    def clear(self):
        """Clears the console of all text"""
        self._view.clear()


class ConsoleModel(Subject):
    """Model for the text content to be displayed in the console"""

    _content = ""
    _observers = []

    def __init__(self, observer: Observer = ConsolePresenter(), content: str = "") -> None:
        self.attach(observer)
        self._content = content

    @typechecked
    def attach(self, observer: Observer) -> None:
        """Attaches an observer to this subject

        Parameters
        ----------
        observer
            Class that will observe the change to the state of this subject

        Raises
        ------
        TypeError
            Type for observer argument was not of type Observer
        """
        self._observers.append(observer)

    @typechecked
    def detach(self, observer) -> None:
        """Removes an observer from this subject

        Parameters
        ----------
        observer
            Class that is observing the change to the state of this subject

        Raises
        ------
        TypeError
            Type for observer argument was not of type Observer
        """
        self._observers.remove(observer)

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """
        for observer in self._observers:
            observer.update(self)

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
        """Setter for output property"""
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
    def add_lines(self, lines: list[str]):
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
