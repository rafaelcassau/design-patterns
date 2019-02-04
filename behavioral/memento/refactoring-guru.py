"""
Memento is a behavioral design pattern that
allows making snapshots of an object's state
and restoring it in future.

The Memento doesn't compromise the internal structure
of the object it works with, as well as data kept
inside the snapshots
"""
import string
import random
from datetime import datetime
from typing import List


class MementoInterface:
    """
    The Memento interface provides a way to retrieve the memento's metadata,
    such as creation date or name. However, it doesn't expose the Originator's state.
    """
    def get_name(self) -> str: raise NotImplementedError()
    def get_date(self) -> datetime: raise NotImplementedError()


class ConcreteMemento(MementoInterface):
    """
    The Concrete Memento contains the infrastructure for storing the Originator's state.
    """
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = datetime.now()

    def get_state(self) -> str:
        """ The Originator uses this method when restoring its state. """
        return self._state

    # The rest of the methods are used by caretaker to display metadata.

    def get_name(self) -> str:
        return f"{self._date}/{self._state[:9]}..."

    def get_date(self) -> datetime:
        return self._date



class Originator:
    """
    The Originator holds some important state that may change over time.
    It also defines a method for saving the state inside a memento and
    another method for restoring the state from it.
    """
    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def do_something(self) -> None:
        print("Originator: I'm doing something important.")
        self._state = self.generate_random_string()
        print(f"Originator: And my state has changed to {self._state}")

    def generate_random_string(self) -> str:
        random_string: str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=30))
        return random_string

    def save(self) -> MementoInterface:
        """ Saves the current state inside a memento. """
        return ConcreteMemento(self._state)

    def restore(self, memento: MementoInterface) -> None:
        """ Restores the Originator's state from a memento object. """
        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")


class Caretaker:
    """
    The Caretaker doesn't depend on the Concrete Memento class.
    Therefore, it doesn't have access to the originator's state,
    stored inside the memento. It works with all mementos via
    the base Memento interface.
    """
    def __init__(self, originator: Originator) -> None:
        self._originator = originator
        self._mementos: List[MementoInterface] = []

    def backup(self) -> None:
        print("Caretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not self._mementos:
            return

        _memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {_memento.get_name()}")

        self._originator.restore(_memento)

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for _memento in self._mementos:
            print(_memento.get_name())


class Demo:

    def run(self) -> None:
        originator: Originator = Originator("Super-duper-super-puper-super.")
        caretaker: Caretaker = Caretaker(originator)

        caretaker.backup()
        originator.do_something()

        caretaker.backup()
        originator.do_something()

        caretaker.backup()
        originator.do_something()

        print("Show history")
        caretaker.show_history()

        print("Client: Now, let's rollback!")
        caretaker.undo()

        print("Client: Once more!")
        caretaker.undo()


demo: Demo = Demo()
demo.run()
