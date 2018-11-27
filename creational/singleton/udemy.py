"""
The Singleton pattern ensures that a class has only
one instance, and provide a global point of access to it,
for example, a logging class.

__new__ is the first step of instance creation; it's called
before __init__, and is responsible for returning a new instance
of your class.


Pros:
    Singletons are allocated once and only once.
    Policies can be added to the method that provides access to the singleton pointer.

Cons:
    Derivatives of Singletons are not automatically Singletons.
    Singletons must always be accessed through a pointer of reference (obtaining this has overhead).
"""

class Singleton:
    __instance = None

    def __new__(cls, val=None):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        cls.__instance.val = val

        return cls.__instance


class Client:

    def run(self):
        x = Singleton()
        x.val = 'burger'
        print(x.val)

        y = Singleton()
        y.val = 'chips'
        print(y.val)

        print(x.val)
        print('x == y is {}'.format(x == y))
        print('x is y is {}'.format(x is y))


client = Client()
client.run()
