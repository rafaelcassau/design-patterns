"""
Mediator is a behavioral design pattern that
reduces coupling between components of a program
by making them communicate indirectly, through
a special mediator object.

The Mediator makes it easy to modify, extend
and reuse individual components because they're
no longer dependent on the dozens of other classes.
"""


class MediatorInterface:
    """
    The Mediator interface declares a method used by components
    to notify the mediator about various events. The mediator
    may react to these events and pass the execution to other
    components.
    """

    def notify(self, sender: object, event: str) -> None:
        raise NotImplementedError()


class ConcreteMediator(MediatorInterface):

    def __init__(self, component_1: 'Component1', component_2: 'Component2') -> None:
        self._component_1 = component_1
        self._component_2 = component_2

        self._component_1.set_mediator(self)
        self._component_2.set_mediator(self)

    def notify(self, sender: object, event: str) -> None:
        if event == 'A':
            print('Mediator reacts on A and triggers following operations:')
            self._component_2.do_c()
        elif event == 'D':
            print('Mediator reacts on D and triggers following operations:')
            self._component_1.do_b()
            self._component_2.do_c()



class BaseComponent:
    """
    The Base Component provides the basic functionality of storing a
    mediator's instance inside component objects.
    """

    def __init__(self, mediator: MediatorInterface = None) -> None:
        self._mediator = mediator

    def set_mediator(self, mediator: MediatorInterface) -> None:
        self._mediator = mediator


class Component1(BaseComponent):
    """
    Concrete Components implement various functionality. They don't
    depend on other components. They also don't depend on any
    concrete mediator classes.
    """
    def do_a(self) -> None:
        print('Component 1 does A.')
        self._mediator.notify(self, 'A')

    def do_b(self) -> None:
        print('Component 1 does B.')
        self._mediator.notify(self, 'B')


class Component2(BaseComponent):

    def do_c(self) -> None:
        print('Component 2 does C.')
        self._mediator.notify(self, 'C')

    def do_d(self) -> None:
        print('Component 2 does D.')
        self._mediator.notify(self, 'D')


class Demo:

    def run(self) -> None:
        _component1 = Component1()
        _component2 = Component2()

        _mediator: MediatorInterface = ConcreteMediator(_component1, _component2)

        print("Client triggers operation A.")
        _component1.do_a()

        print('\n', end="")

        print("Client triggers operation D.")
        _component2.do_d()


demo: Demo = Demo()
demo.run()
