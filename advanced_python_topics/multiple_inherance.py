
class A:
    def __init__(self):
        print('A')

    @staticmethod
    def bar():
        print('bar')


class B:
    def __init__(self):
        print('B')

    @staticmethod
    def foo():
        print('foo')


class C(A, B):
    def foobar(self):
        self.foo()
        self.bar()


c = C()    # "A"
C.__mro__  # (__main__.C, __main__.A, __main__.B, object)
c.foobar() # foo \n bar