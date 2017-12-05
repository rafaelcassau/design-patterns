"""
Intent
	Define a family of algorithms, encapsulate each one, and make them interchangeable.
	Strategy lets the algorithm vary idependently from clients that use it.

	Capture the abstraction in an interface, bury implementation details in derived classes.

Problem
	One of the dominant strategies of object-oriented design is the "open-closed principle".

	Encapsulae interface details in a base class, and bury implementation details in a derived
	class. Clients can then couple themselves to an interface, and not have to experience the
	upheaval associated with change: no impact when the number of derived classes changes,
	and no impact when the implementation of derived class changes.
"""

import abc


class Context:
	"""
	Define the interface of interest to clients.
	Maintain a referenece to a strategy object.
	"""

    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        self._strategy.algorithm_interface()


class Strategy(metaclass.abc.ABCMeta):
	"""
	Declare an interface common to all supported algorithms.
	Context uses this interface to call the algorithm defined by a
	ConcreteStrategy.
	"""

	@abc.abstractmethod
	def algorithm_interface(self):
		pass


class ConcreteStrategyA(Strategy):
	"""
	Implement the algorithm using the Strategy interface.
	"""

	def algorithm_interface(self):
		pass


class ConcreteStrategyB(Strategy):
	"""
	Implement the algorithm using the Strategy interface
	"""

	def algorithm_interface(self):
		pass


def main():
	concrete_strategy_a = ConcreteStrategyA()
	context = Context(strategy=concrete_strategy_a)
	context.context_interface()


if __name__ == '__main__':
	main()
