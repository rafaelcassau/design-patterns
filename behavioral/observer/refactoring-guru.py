"""
Observer is a behavioral design pattern that
allows one objects to notify other objects about
changes in their state.

The Observer pattern provides a way to subscribe
and unsubscribe to and from these events for any
object that implements a subscriber interface.
"""
from typing import List, Dict


class File:
    """
    File, this class just simulate a file object
    """
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path
        self._name = file_path.rsplit('/')[-1]

    def get_name(self) -> str:
        return self._name


class EventListenerInterface:
    """
    EventListenerInterface, this interface will be implemented for all subscribers
    that want to be notified about any update in the Observable object.
    """
    def update(self, event_type: str, file: File) -> None:
        raise NotImplementedError()


class EventManager:
    """
    EventManager, this helper class acts as a Publisher component.
    this class contains all necessary methods to register, unregister
    and notify all subscribers registered here.
    """
    def __init__(self, *operations: List[str]) -> None:
        """ listeners are composed by event_type and a list of subscribers """
        self._listeners: Dict[str, List[EventListenerInterface]] = {}

        for operation in operations:
            self._listeners[operation]: List[EventListenerInterface] = []

    def subscribe(self, event_type: str, listener: EventListenerInterface) -> None:
        """ register subscribers grouped by event_type (operations) """
        users: List[EventListenerInterface] = self._listeners[event_type]
        users.append(listener)

    def unsubscribe(self, event_type: str, listener: EventListenerInterface) -> None:
        """ unregister subscribers grouped by event_type (operations) """
        users: List[EventListenerInterface] = self._listeners[event_type]
        if listener in users:
            users.remove(listener)

    def notify(self, event_type: str, file: File):
        """ notify all registered subscribers by event_type """
        users: List[EventListenerInterface] = self._listeners[event_type]
        for listener in users:
            listener.update(event_type, file)


class EmailNotificationListener(EventListenerInterface):
    """
    Concrete Observer class
    """
    def __init__(self, email: str) -> None:
        self._email = email

    def update(self, event_type: str, file: File) -> None:
        message: str = f"""
            Email to {self._email}: Someone has performed {event_type}
            operation with the following file: {file.get_name()}
            """
        print(message)


class LogOpenListener(EventListenerInterface):
    """
    Concrete Observer class
    """
    def __init__(self, filename: str) -> None:
        self._log = File(filename)

    def update(self, event_type: str, file: File) -> None:
        message: str = f"""
            Save to log {self._log.get_name()}: Someone has performed {event_type}
            operation with the following file: {file.get_name()}
            """
        print(message)


class Editor:
    """
    Editor, class that acts as a text editor,
    when some operation are executed a custom event is triggered
    """
    def __init__(self) -> None:
        self._events: EventManager = EventManager('open', 'save')
        self._file: File = None

    def open_file(self, file_path: str) -> None:
        """
        dispach open event
        """
        self._file = File(file_path)
        self._events.notify('open', self._file)

    def save_file(self) -> None:
        """
        dispach save event
        """
        if self._file:
            self._events.notify('save', self._file)
        else:
            raise Exception('Please open a file first.')


class Demo:

    def run(self):
        """
        Instantiate a editor object and register some subscribers to acts as observers.
        When a file is opened or saved, then all subscribers below will be notified and
        a action will be executed for each subscriber.
        """
        _editor: Editor = Editor()
        _editor._events.subscribe('open', LogOpenListener('/path/to/log/file.text'))
        _editor._events.subscribe('save', EmailNotificationListener('admin@example.com'))

        try:
            _editor.open_file('text.txt')
            _editor.save_file()
        except Exception as err:
            print(f'An error occured when try to open file, error: {err}')


demo: Demo = Demo()
demo.run()
