"""
Attach additional responsabilities to an object dynamically.
Decorators provide a flexible alternative to subclassing for
extending functionality.
"""


class WindowsInterface:

    def build(self) -> None:
        raise NotImplementedError()


class Window(WindowsInterface):

    def build(self) -> None:
        print('Building a window')


class AbstractWindowDecorator(WindowsInterface):
    """
    Maintain a reference to a Window object and define
    an interface that conforms to Window's interface.
    """

    def __init__(self, window: WindowsInterface):
        self._window = window

    def build(self) -> None:
        raise NotImplementedError()


class BorderDecorator(AbstractWindowDecorator):

    def add_border(self) -> None:
        print('Adding border')

    def build(self) -> None:
        self.add_border()        
        self._window.build()


class VerticalSBDecorator(AbstractWindowDecorator):

    def add_vertical_scroll_bar(self) -> None:
        print('Adding vertical scroll bar')

    def build(self) -> None:
        self.add_vertical_scroll_bar()
        self._window.build()


class HorizontalSBDecorator(AbstractWindowDecorator):

    def add_horizontal_scroll_bar(self) -> None:
        print('Adding horizontal scroll bar')

    def build(self) -> None:
        self.add_horizontal_scroll_bar()
        self._window.build()


Window().build()

BorderDecorator(Window()).build()

VerticalSBDecorator(Window()).build()

HorizontalSBDecorator(Window()).build()

#dynamically wrappers

HorizontalSBDecorator(VerticalSBDecorator(BorderDecorator(Window()))).build()