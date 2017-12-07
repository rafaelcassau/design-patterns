"""
Intent

	Attach additional responsabilities to an object dynamically.
	Decorators provide a flexible alternative to subclassing for extending
	funcionality.

	Client-specified embellishment of a core object by recursively wrapping it.

	Wrapping a gift, putting it in a box, and wrapping the box.

Problem

	You want to add behavior or state to individual objects at run-time. Inheritance is not 
	feasible because it is static and applies to an entire class.
"""

import abc


class Component(metaclass=abc.ABCMeta):
    """
    Define the interface for objects that can have responsabilities added to then dynamically.
    """

    @abc.abstractmethod
    def operarion(self):
        pass


class Decorator(Component, metaclass=abc.ABCMeta):
    """
    Maintain a reference to a Componet object and define an interface that conforms to
    Component's interface.
    """

    def __init__(self, component):
        self._component = component

    @abc.abstractmethod
    def operation(self):
        pass


class ConcreteDecoratorA(Decorator):
    """
    Add responsabilities to the component.
    """

    def operation(self):
        self._component.operation()


class ConcreteDecoratorB(Decorator):
    """
    Add responsabilities to the component.
    """

    def operation(self):
        self._component.operation()


class ConcreteComponent(Component):
    """
    Define an object to which additional responsabilities can be attached.
    """

    def operation(self):
        pass


def main():
    concrete_component = ConcreteComponent()
    concrete_decorator_a = ConcreteDecoratorA(concrete_component)
    concrete_decorator_b = ConcreteDecoratorA(concrete_decorator_a)
    concrete_decorator_b.operation()


if __name__ == '__main__':
    main()
