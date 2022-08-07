"""Script for handling console view

note: this may not need to be a class.
"""

from typeguard import typechecked
import functools
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

    def clear(self):
        """Clears the console of all text"""
        os.system('cls' if os.name == 'nt' else 'clear')

    @functools.singledispatch
    @typechecked
    def set_output(self, output: list[str]):
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

    @set_output.register(str)
    @typechecked
    def set_output(self, output):
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
