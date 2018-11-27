"""
The Borg Idiom (a.k.a monostate pattern) lets a class have as many
instances as one likes, but ensures that they all share the same state. 

__init__ doesn't return anything; it's only responsible for initializing
the instance after it's beem created.


Pros:
    Derivatives of monostate classes can also be monostate.
    Access to monostate objects does not have to be through pointers of references.

Cons:
    No instantiation policy can exist for Monostate classes.
    Monostate instances may be allocated and deallocated many times.
"""

class Borg:
    __shared_state = {}

    def __init__(self):
        print(self.__shared_state)
        self.__dict__ = self.__shared_state


class Client:

    def run(self):
        b = Borg()
        c = Borg()

        print('b == c is {}'.format(b == c))
        print('b is c is {}'.format(b is c))

        b.val = 'milkshake'

        print('c.val is {} shared state'.format(c.val))


client = Client()
client.run()

