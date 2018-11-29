"""
Singleton is a creational design pattern that lets you
ensure that a class has only one instance and provide
a globla access point to this instance.
"""

class SingletonMetaClass(type):

    def __init__(cls, name, bases, dict):
        super().__init__(name, bases, dict)
        original_new = cls.__new__

        def my_new(cls, *args, **kwargs):
            if cls.instance == None:
                cls.instance = original_new(cls)
            return cls.instance
        
        cls.instance = None
        cls.__new__ = staticmethod(my_new)


class Bar(metaclass=SingletonMetaClass):

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return 'self {}'.format(self.val)


class Client:

    def run(self):
        x = Bar('sausage')
        y = Bar('eggs')
        z = Bar('spam')

        print('x: {}'.format(x))
        print('y: {}'.format(y))
        print('z: {}'.format(z))

        print(x is y is z)


client = Client()
client.run()
