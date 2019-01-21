"""
Allow an object to alter its behavior when
its internal state changes.
"""
from typing import List


class ComputerState:
    """
    Base state class
    """
    _name = 'state'
    _allowed: List[str] = []    

    def switch(self, state: "ComputerState") -> None:
        """ Switch to new state """
        if state._name in self._allowed:
            print(f'Current: {self} -> switching to new state: {state._name}.')
            self.__class__ = state
        else:
            print(f'Current: {self} -> switching to: {state._name}, not possible.')

    def __str__(self) -> str:
        return self._name


class Off(ComputerState):
    """
    Off concrete state
    """
    _name = 'off'
    _allowed = ['on']


class On(ComputerState):
    """
    On concrete state
    """
    _name = 'on'
    _allowed = ['off', 'suspend', 'hibernate']


class Suspend(ComputerState):
    """
    Suspend concrete state
    """
    _name = 'suspend'
    _allowed = ['on']
        

class Hibernate(ComputerState):
    """
    Hibernate concrete state
    """
    _name = 'hibernate'
    _allowed = ['on']


class Computer:

    def __init__(self) -> None:
        self._current_state: ComputerState = Off()

    def change(self, new_state: ComputerState) -> None:
        self._current_state.switch(new_state)


computer = Computer()
print(computer._current_state)

# Off -> On (True)
computer.change(On)

# On -> Suspend (True)
computer.change(Suspend)

# Suspend -> Hibernate (False)
computer.change(Hibernate)

# Suspend -> On (True)
computer.change(On)

# On -> Off (True)
computer.change(Off)
