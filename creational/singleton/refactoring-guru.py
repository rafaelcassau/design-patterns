from typing import Optional


class Singleton:
    """
    The Singleton class defines the `getInstance` method that lets clients
    access the unique singleton instance.
    """

    _instance: Optional = None

    def __init__(self) -> None:
        if Singleton._instance is not None:
            raise ReferenceError("Cannot instantiate a singleton class.")
        else:
            Singleton._instance = self

    @staticmethod
    def get_instance() -> Singleton:
        """
        The static method that controls the access to the singleton instance.
        
        This implementation let you subclass the Singleton class while
        keeping just one instance of each subclass around.
        """

        if not Singleton._instance:
            Singleton()
    
        return Singleton._instance

    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can
        be executed on its instance.
        """
        pass


class Demo:
    # The client code.

    def run(self) -> None:
        s1 = Singleton.get_instance()
        s2 = Singleton.get_instance()

        if id(s1) == id(s2):
            print("Singleton works, both variables contain the same instance.")
        else:
            print("Singleton failed, variables contain different instances.")


demo: Demo = Demo()
demo.run()