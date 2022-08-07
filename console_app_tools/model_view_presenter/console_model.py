"""Model for console app model view presenter pattern"""

from typeguard import typechecked


class ConsoleModel:
    """Model for the text content to be displayed in the console"""
    def __init__(self):
        self._content = ""

    @property
    def content(self):
        """Getter for output property"""
        return self._content

    @typechecked()
    @content.setter
    def content(self, value: str):
        """Setter for output property"""
        self._content = value

    @typechecked
    def add_line(self, line: str):
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
        self.content += f"\n{line}"

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

    def clear_content(self):
        """Clear all content"""
        self.content = ""
