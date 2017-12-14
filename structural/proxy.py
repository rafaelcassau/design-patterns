"""
Intent
	Provide a surrogate or placeholder for another object to control access to it
	or add other responsabilities.

	Use an extra level of indirection to support distributed, controlled, or intelligent
	access.

	Add a wrapper and delegation to protect the real component from undue complexity.

Problem
	You need to support resource-hungry objects, and you do not want to instantiate
	such objects unless and until they are actually requested by the client.
"""

import abc


class Subject(metaclass=abc.ABCMeta):
    """
    Define the common interface for RealSubject and Proxy so that a Proxy
    can be used anywhere a RealSubject is expected.
    """

    @abc.abstractmethod
    def request(self):
        pass


class Proxy(Subject):
    """
    Maintain a reference that lets the proxy access the real subject.
    Provide an interface identical to Subject's
    """

    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        # ......
        self._real_subject.request()
        # ......


class RealSubject(Subject):
    """
    Define the real object that the proxy represents.
    """

    def request(self):
        pass


def main():
	real_subject = RealSubject()
    proxy = Proxy(real_subject)
    proxy.request()


if __name__ == '__main__':
	main()
