"""
Intent
	Convert the interface of a class into another interface clients expect.
	Adapter lets class work together that couldn't otherwise because of incompatible
	interfaces.
	
	Wrap an existing class with a new interface.

	Impedance match an old component to a new system.

Problem
	An "off the shelf" component offers compelling functionality that you would like to
	reuse, but its "view of the world" is not compatible with the philosophy and archicteture
	of the system currently being developed.
"""

import abc


class Target(metaclass=abc.ABCMeta):
    """
    Define the domain-specific interface that Client uses.
    """

    def __init__(self):
        self._adaptee = Adaptee()

    @abc.abstractmethod
    def request(self):
        pass


class Adapter(Target):
    """
    Adapt the interface of Adaptee to the Target interface.
    """

    def request(self):
        self._adaptee.specific_request()


class Adaptee:
    """
    Define an existing interface that needs adapting.
    """

    def specific_request(self):
        pass


def main():
    adapter = Adapter(Adaptee())
    adapter.request()


if __name__ == '__main__':
    main()
