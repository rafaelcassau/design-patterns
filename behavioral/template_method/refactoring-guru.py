"""
Template Method is a behavioral design pattern
that allows you to defines a skeleton of an
algorithm in a base class and let subclasses
override the steps without changing the overall
algorithm's structure.
"""
from time import sleep


class AbstractNetwork:
    """
    Base class of social network.
    """
    def __init__(self, username: str, password: str) -> None:
        self._username = username
        self._password = password

    def post(self, message: str) -> bool:
        """
        Publish the data to whatever network.

        Authenticate before posting. Every network uses a different
        authentication method.
        """
        if self.login(self._username, self._password):
            # Send the post data.
            result: bool = self.send_data(message)
            self.logout()
            return result
        
        return False

    def login(self, username: str, password: str) -> bool:
        raise NotImplementedError()

    def send_data(self, data: str) -> bool:
        raise NotImplementedError()

    def logout(self) -> None:
        raise NotImplementedError()


class Facebook(AbstractNetwork):

    def login(self, username: str, password: str) -> bool:
        print("Checking user's parameters.")
        print(f"Name: {username}")
        print(f"Password: {'*' * len(password)}")
        
        self.simulate_network_latency()

        print("Login success on Facebook.")
        return True

    def send_data(self, data: str) -> bool:
        message_posted: bool = True
        if message_posted:
            print(f"Message: {data} was posted on Facebook.")
            return True
        else:
            return False

    def logout(self) -> None:
        print(f"User: {self._username} was logged out from Facebook.")

    def simulate_network_latency(self) -> None:
        count: int = 0
        while(count < 10):
            sleep(0.5)
            print(".", end="")
            count += 1


class Twitter(AbstractNetwork):

    def login(self, username: str, password: str) -> bool:
        print("Checking user's parameters.")
        print(f"Name: {username}")
        print(f"Password: {'*' * len(password)}")
        
        self.simulate_network_latency()

        print("Login success on Twitter.")
        return True

    def send_data(self, data: str) -> bool:
        message_posted: bool = True
        if message_posted:
            print(f"Message: {data} was posted on Twitter.")
            return True
        else:
            return False

    def logout(self) -> None:
        print(f"User: {self._username} was logged out from Twitter.")

    def simulate_network_latency(self) -> None:
        count: int = 0
        while(count < 10):
            sleep(0.5)
            print(".", end="")
            count += 1


class Demo:

    def run(self):
        username: str = input("Input username: ")
        password: str = input("Input password: ")
        message: str = input("Input message: ")

        print("Choose social network for posting message.")
        print("1 - Facebook")
        print("2 - Twitter")

        choice: int = int(input("Input your choice: "))
        if choice == 1:
            network: AbstractNetwork = Facebook(username, password)
        elif choice == 2:
            network: AbstractNetwork = Twitter(username, password)

        network.post(message)


demo: Demo = Demo()
demo.run()