"""Tests for classes and methods in observer_pattern.py"""
import unittest
from unittest.mock import MagicMock

from parameterized import parameterized

from .observer_pattern import IObserver, Subject


class MockObserver(IObserver):
    """Mock concrete implementation of IObserver for testing"""

    def update(self, subject: Subject) -> None:
        pass


class SubjectAttachTests(unittest.TestCase):
    def test_attach_valid_observer_attaches_observer(self):
        observer = MockObserver()
        subject = Subject()
        self.assertTrue(len(subject._observers) == 0)
        subject.attach(observer=observer)
        self.assertTrue(len(subject._observers) == 1)

    @parameterized.expand([
        [1],
        [1.0],
        ["Hello"],
        [Subject()],
        [[1, 2, 3]],
        [(1, 2, 3)]
    ])
    def test_attach_invalid_observer_raises_type_error(self, invalid_type):
        subject = Subject()
        with self.assertRaises(TypeError):
            subject.attach(observer=invalid_type)


class SubjectDetachTests(unittest.TestCase):
    def test_detach_valid_observed_observer_detaches_observer(self):
        observer = MockObserver()
        subject = Subject()
        self.assertTrue(len(subject._observers) == 0)
        subject.attach(observer=observer)
        self.assertTrue(len(subject._observers) == 1)
        subject.detach(observer=observer)
        self.assertTrue(len(subject._observers) == 0)

    def test_detach_valid_not_observed_observer_raises_value_error(self):
        observer = MockObserver()
        subject = Subject()
        with self.assertRaises(ValueError):
            subject.detach(observer=observer)

    @parameterized.expand([
        [1],
        [1.0],
        ["Hello"],
        [Subject()],
        [[1, 2, 3]],
        [(1, 2, 3)]
    ])
    def test_detach_invalid_observer_raises_type_error(self, invalid_type):
        subject = Subject()
        with self.assertRaises(TypeError):
            subject.detach(observer=invalid_type)


class SubjectNotifyTests(unittest.TestCase):
    @parameterized.expand([
        [0],
        [1],
        [5]
    ])
    def test_notify_called_update_called_in_all_observers(self, number_of_observers: int):
        observers = [MockObserver() for _ in range(number_of_observers)]
        subject = Subject()

        for observer in observers:
            observer.update = MagicMock()
            subject.attach(observer=observer)
            self.assertTrue(not observer.update.called)

        subject.notify()

        for observer in observers:
            self.assertTrue(observer.update.called)


if __name__ == "__main__":
    unittest.main()
