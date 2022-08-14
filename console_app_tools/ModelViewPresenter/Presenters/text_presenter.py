"""Presenter for Text model in MVP pattern"""
from abc import abstractmethod
from typeguard import typechecked
from console_app_tools.ModelViewPresenter.Models.text_model import ITextModel
from observer_pattern.observer_pattern import IObserver, Subject


class ITextPresenter(IObserver):
    @abstractmethod
    def display_text(self, text: str) -> None:
        """Display the text from the model"""
        pass


class ConsoleTextPresenter(ITextPresenter):
    @typechecked
    def update(self, model: ITextModel) -> None:
        """Responds to a change in state of the model and updates display

        Parameters
        ----------
        model
            The model the instance of ConsoleTextPresenter is observing

        Raises
        ------
        TypeError
            Argument passed for model was not of type ITextModel
        """
        self.display_text(model.content)

    @typechecked
    def display_text(self, text: str) -> None:
        """Prints text from the model to the console

        Parameters
        ----------
        text
            Text to be printed to the console

        Raises
        ------
        TypeError
            Argument passed for text was not of type str
        """
        print(text)
