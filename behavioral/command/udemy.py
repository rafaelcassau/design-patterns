"""
Decouple the object that invokes the operation from
the one that knows how to perform it.
"""
from typing import List


class Screen:

    def __init__(self, text: str = '') -> None:
        self._text = text
        self._clip_board: str = ''

    def cut(self, start: int = 0, end: int =0) -> None:
        self._clip_board = self._text[start:end]
        self._text = self._text[:start] + self._text[end:]

    def paste(self, offset: int = 0) -> None:
        self._text = self._text[:offset] + self._clip_board + self._text[offset:]

    def clear_clipboard(self):
        self._clip_board = ''

    def length(self):
        return len(self._text)

    def __str__(self):
        return self._text


class ScreenCommandInterface:
    """
    Screen command interface
    """
    def __init__(self, screen: Screen) -> None:
        self._screen = screen
        self._previous_state: str = screen._text

    def execute(self) -> None:
        raise NotImplementedError()

    def undo(self):
        raise NotImplementedError()


class CutCommand(ScreenCommandInterface):

    def __init__(self, screen: Screen, start: int = 0, end: int = 0) -> None:
        super().__init__(screen)
        self._start = start
        self._end = end

    def execute(self) -> None:
        self._screen.cut(start=self._start, end=self._end)

    def undo(self):
        self._screen.clear_clipboard()
        self._screen._text = self._previous_state


class PasteCommand(ScreenCommandInterface):

    def __init__(self, screen: Screen, offset: int = 0) -> None:
        super().__init__(screen)
        self._offset = offset

    def execute(self) -> None:
        self._screen.paste(offset=self._offset)

    def undo(self) -> None:
        self._screen.clear_clipboard()
        self._screen._text = self._previous_state


class ScreenInvoker:

    def __init__(self) -> None:
        self._history: List[ScreenCommandInterface] = []

    def store_and_execute(self, command: ScreenCommandInterface) -> None:
        command.execute()
        self._history.append(command)

    def undo_last(self) -> None:
        if self._history:
            _last_commit: ScreenCommandInterface = self._history.pop()
            _last_commit.undo()


invokers: ScreenInvoker = ScreenInvoker()

screen: Screen = Screen(text='Hello world')
print(screen)

cut_command: CutCommand = CutCommand(screen, start=5, end=11)
invokers.store_and_execute(cut_command)
print(screen)

paste_command: PasteCommand = PasteCommand(screen, offset=0)
invokers.store_and_execute(paste_command)
print(screen)

invokers.undo_last()
print(screen)

invokers.undo_last()
print(screen)
