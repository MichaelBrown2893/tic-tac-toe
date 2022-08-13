"""Model containing text information"""
from observer_pattern.observer_pattern import Subject, IObserver
from typeguard import typechecked


class TextModel(Subject):
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

    @typechecked
    @content.setter
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
    def add_new_lines(self, new_lines: list[str]) -> None:
        """Add additional lines starting on a new line

        Parameters
        ----------
        new_lines
            List of new lines to be added to the content

        Raises
        ------
        TypeError
            value passed for new lines was not of type list[str]
        """
        self.content = "{0}\n{1}".format(self.content, "\n".join(new_lines))

