"""Observer pattern observer class

https://refactoring.guru/design-patterns/observer/python/example#:~:text=Observer%20is%20a%20behavioral%20design,that%20implements%20a%20subscriber%20interface."""

from __future__ import annotations
from abc import ABC, abstractmethod
from typeguard import typechecked


class IObserver(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass


class ISubject(ABC):
    """"
    The ISubject Interface declares methods used to manage observers
    """

    @abstractmethod
    def attach(self, observer: IObserver) -> None:
        """Attach an observer to the Subject"""
        pass

    @abstractmethod
    def detach(self, observer: IObserver) -> None:
        """Detach and observer from the Subject"""
        pass

    @abstractmethod
    def notify(self) -> None:
        """Notify observers of a change of state in the Subject"""
        pass


class Subject:
    """
    The Subject class manages subscribers.
    """

    def __init__(self):
        self._observers: list[IObserver] = []

    @typechecked
    def attach(self, observer: IObserver) -> None:
        """Attach an observer to the subject.

        Parameters
        ----------
        observer
            Instance observer to observe the state of the subject

        Raises
        ------
        TypeError
            observer was not an instance of Observer
        """
        self._observers.append(observer)

    @typechecked()
    def detach(self, observer: IObserver) -> None:
        """Detach an observer from the subject.

        Parameters
        ----------
        observer
            Instance of observer to be removed from the list of observers

        Raises
        ------
        ValueError
            Raised when attempt is made to detach observer which is not attached
        TypeError
            observer was not an instance of Observer
        """
        try:
            self._observers.remove(observer)
        except ValueError as err:
            raise ValueError(f"Attempt to remove observer: {observer} which is not attached")

    def notify(self) -> None:
        """Notify all observers about an event."""
        for observer in self._observers:
            observer.update(self)
