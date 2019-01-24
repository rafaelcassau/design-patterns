"""
Chain of Responsability is a behavioral design
pattern that allows passing request along the
chain of potential handlers until one of them
handles request.

The pattern allows multiple objects to handle the request without
coupling sender class to the concrete classes of the receivers. The chain
can be composed dynamically at runtime with any handler that follows
a standard handler interface.
"""
import time
from typing import Dict


class Server:
    """
    Server class.
    """
    def __init__(self) -> None:
        self._users: Dict[str] = {}
        self._middleware: "AbstractMiddleware" = None

    def set_middleware(self, middleware: "AbstractMiddleware") -> None:
        """
        Client passes a chain of object to server. This improves flexibility and
        makes testing the server class easier.
        """
        self._middleware = middleware

    def login(self, email: str, password: str) -> bool:
        if self._middleware.check(email, password):
            print('Authorization have been successful!')

            """ Do something useful here for authorized users. """
            return True
        else:
            return False

    def register(self, email: str, password: str) -> None:
        self._users[email] = password

    def has_email(self, email: str) -> bool:
        return email in self._users.keys()

    def is_valid_password(self, email: str, password: str) -> bool:
        return self._users.get(email) == password


class AbstractMiddleware:

    def link_with(self, next: "AbstractMiddleware") -> "AbstractMiddleware":
        """ Builds chains of middleware objects. """
        self._next = next
        return next

    def check(self, email: str, password: str) -> bool:
        """ Subclasses will implement this method with concrete checks. """
        raise NotImplementedError()

    def next_check(self, email: str, password: str) -> bool:
        """
        Runs check on the next object in a chain or ends traversing if we're in
        last object in chain.
        """
        if not self._next:
            return True

        return self._next.check(email, password)


class ThrottlingMiddleware(AbstractMiddleware):
    """
    ConcreteHandler. Checks whether there are too many failed login requests.
    """
    def __init__(self, request_per_minute: int) -> None:
        self._request_per_minute: int = request_per_minute

        self._current_time: int = int(time.time())
        self._request: int = 0

    def check(self, email: str, password: str) -> bool:
        """
        Please, note that check_next() call can be inserted both in the beginning
        of this method and in the end.

        This gives much more flexibility than a simple loop over all middleware
        objects. For instance, an element of a chain can change the order of
        checks by running its check after all other checks.
        """
        if int(time.time()) > self._current_time + 60_000:
            self._request = 0
            self._current_time = int(time.time())

        self._request += 1

        if self._request > self._request_per_minute:
            print('Request limit excedeed!')
            return False

        return self.next_check(email, password)


class UserExistsMiddleware(AbstractMiddleware):
    """
    ConcreteHandler. Checks whether a user with the given credentials exists.
    """
    def __init__(self, server: Server = None):
        self._server = server

    def check(self, email: str, password: str) -> bool:
        if not self._server.has_email(email):
            print('This email is not registered!')
            return False

        if not self._server.is_valid_password(email, password):
            print('Wrong password!')
            return False

        return self.next_check(email, password)


class RoleCheckMiddleware(AbstractMiddleware):
    """
    ConcreteHandler. Checks a user's role.
    """

    def check(self, email: str, password: str) -> bool:
        if email == 'admin@example.com':
            print('Hello, admin!')
            return True
        else:
            print('Hello, user!')

        return self.next_check(email, password)


class Demo:
    """
    Demo class. Everything comes together here.
    """

    def run(self):
        _server: Server = Server()

        _server.register('admin@example.com', 'admin_pass')
        _server.register('user@example.com', 'user_pass')

        """
        All checks are linked. Client can build various chains
        using the same components.
        """
        _middleware: ThrottlingMiddleware = ThrottlingMiddleware(request_per_minute=2)

        """ This is the pattern """
        _middleware.link_with(
            UserExistsMiddleware(_server)
        ).link_with(
            RoleCheckMiddleware()
        )

        """ Server gets a chain from client code. """
        _server.set_middleware(_middleware)

        _success: bool = False
        while not _success:
            _email: str = input('Enter a email: ')
            _password: str = input('Enter a password: ')
    
            _success = _server.login(_email, _password)


demo: Demo = Demo()
demo.run()