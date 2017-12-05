"""
Define one-to-many dependency between objects so that when on object
changes state, all its dependents are notified and updated automatically.

Encapsulate the core (or common or engine) components in a Subject abstraction,
and the variable (or optional or user interface) components in an Observer hierarchy.

The "View" part of Model-View-Controller.

Problem:

	A large monolithic design does not scale well as new graphing or monitoring
	requirements are levied.
"""

import abc


class Subject:
    """
    Know its observers. Any number of Observer objects many observe a subject.
    Send notification to its observers when its states changes.
    """

    def __init__(self):
        self._observers = set()
        self._subject_state = None

    def attach(self, observer):
        observer._subject = self
        self._observers.add(observer)

    def detatch(self, observer):
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update(self._subject_state)

    @property
    def subject_state(self):
        return self._subject_state

    @subject_state.setter
    def subject_state(self, arg):
        self._subject_state = arg
        self._notify()


class Observer(metaclass=ABCMeta):
    """
    Define an updating interface for objects that should be notified of
    changes in a subject.
    """

    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abc.abstractmethod
    def update(self, arg):
        pass


class ConcreteObserver(Observer):
    """
        Implement the Observer updating interface to keep its state
        consistent with the subject's.
        Store state that should stay consistent with the subject's.
    """

    def update(self, arg):
        self._observer_state = arg


def main():
    subject = Subject()
    concrete_observer = ConcreteObserver()
    subject.attach(concrete_observer)

    subject.subject_state = 123


if __name__ == '__main__':
    main()
