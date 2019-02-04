"""
Capture and externalize an object's internal state
so that the object can be returned to this state
later.
"""
import copy
from typing import List


class Memento:

    def __init__(self, data) -> None:
        """ make a deep copy of every variable in the given class. """
        for attribute in vars(data):
            setattr(self, attribute, copy.deepcopy(getattr(data, attribute)))


class Undoable:

    def __init__(self) -> None:
        """
        each instance keeps the latest saved copy so that there is only
        one copy of each in memory
        """
        self._last: Memento = None

    def save(self) -> None:
        self._last = Memento(self)

    def undo(self) -> None:
        for attibute in vars(self):
            setattr(self, attibute, copy.deepcopy(getattr(self._last, attibute)))


class Data(Undoable):

    def __init__(self) -> None:
        super().__init__()
        self.numbers: List[int] = []


data: Undoable = Data()

# foward
for i in range(10):
    data.save()
    data.numbers.append(i)

data.save()
print(data.numbers)

#backward
for i in range(10):
    data.undo()
    print(data.numbers)
