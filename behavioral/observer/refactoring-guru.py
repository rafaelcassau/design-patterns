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

    def __init__(self, file_path: str) -> None:
        self._file_path = file_path
        self._name = file_path.rsplit('/')[-1]

    def get_name(self) -> str:
        return self._name


class EventListenerInterface:

    def update(self, event_type: str, file: File) -> None:
        raise NotImplementedError()


class EventManager:

    def __init__(self, *operations: List[str]) -> None:
        self._listeners: Dict[str, List[EventListenerInterface]] = {}

        for operation in operations:
            self._listeners[operation]: List[EventListenerInterface] = []

    def subscribe(self, event_type: str, listener: EventListenerInterface) -> None:
        users: List[EventListenerInterface] = self._listeners[event_type]
        users.append(listener)

    def unsubscribe(self, event_type: str, listener: EventListenerInterface) -> None:
        users: List[EventListenerInterface] = self._listeners[event_type]
        if listener in users:
            users.remove(listener)

    def notify(self, event_type: str, file: File):
        users: List[EventListenerInterface] = self._listeners[event_type]
        for listener in users:
            listener.update(event_type, file)


class EmailNotificationListener(EventListenerInterface):

    def __init__(self, email: str) -> None:
        self._email = email

    def update(self, event_type: str, file: File) -> None:
        message: str = f"""
            Email to {self._email}: Someone has performed {event_type}
            operation with the following file: {file.get_name()}
            """
        print(message)


class LogOpenListener(EventListenerInterface):

    def __init__(self, filename: str) -> None:
        self._log = File(filename)

    def update(self, event_type: str, file: File) -> None:
        message: str = f"""
            Save to log {self._log.get_name()}: Someone has performed {event_type}
            operation with the following file: {file.get_name()}
            """
        print(message)


class Editor:

    def __init__(self) -> None:
        self._events: EventManager = EventManager('open', 'save')
        self._file: File = None

    def open_file(self, file_path: str) -> None:
        self._file = File(file_path)
        self._events.notify('open', self._file)

    def save_file(self) -> None:
        if self._file:
            self._events.notify('save', self._file)
        else:
            raise Exception('Please open a file first.')


class Demo:

    def run(self):
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
