"""
A proxy provides a surrogate or place holder to provide
access to an object.

Ex1:
    Use an extra level of indirection to support distributed,
    controlled, or conditional access.
"""

class SubjectInterface:
    """
    Define the common interface for RealSubject and Proxy so that a
    Proxy can be used anywhere a RealSubject is expected.
    """
    def request(self):
        raise NotImplementedError()


class Proxy(SubjectInterface):
    """
    Maintain a reference that lets the proxy access the real subject.
    Provide an interface identical to Subject's.
    """
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def request(self):
        print('Proxy may be doing something, like controlling request access.')
        self.real_subject.request()


class RealSubject(SubjectInterface):
    """
    Define the real object that the proxy represents.
    """
    def request(self):
        print('The real thing is dealing with the request')


real_subject = RealSubject()
real_subject.request()

proxy = Proxy(real_subject)
proxy.request()