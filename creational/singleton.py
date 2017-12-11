"""
Intent
	Ensure a class has only one instance, and provide a global point of access to it.
	Encapsulated "just-in-time initialization" or "initialization on first use."

Problem
	Application needs one, and only one, instance of an object. Addionally, lazy
	initialization and global access are necessary.
"""


class Singleton(type):
    """
    Define an instance operation that lets clients access its unique instance.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, base, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class MyClass(metaclass=Singleton):
    """
    Example class.
    """
    pass


def main():
    m1 = MyClass()
    m2 = MyClass()
    assert m1 is m2


if __name__ == '__main__':
    main()
