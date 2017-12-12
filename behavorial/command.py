"""
Intent
	Encapsulate a request as an object, thereby letting you parametrize clients with
	different requests, queue or log requests, and support undoable operations.

	Promote "invocation of a method on an object" to full object status.

	An object-oriented callback.

Problem
	Need to issue requests to objects without knowing anything about the operation being
	requested or the receiver of the request.
"""

import abc


class Invoker:
    """
    Ask the command to carry out the request.
    """

    def __init__(self):
        self._commands = []

    def stored_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._comands:
            command.execute()


class Command(metaclass=abc.ABCMeta):
    """
    Declare an interface for executing an operation.
    """

    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    """
    Define a binding between a Receiver object and an action.
    Implement Execute by invoking the corresponding operation(s) on
    Receiver.
    """

    def execute(self):
        self._receiver.action()


class Receiver:
    """
    Know how to perform the operarions associated with carrying out a
    request. Any class may serve as a Receiver.
    """

    def action(self):
        pass


def main():
    receiver = Receiver()
    concrete_command = ConcreteCommand(receiver)
    invoker = Invoker()
    invoker.stored_command(concrete_command)
    invoker.execute_commands()
