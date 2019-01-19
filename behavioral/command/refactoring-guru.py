"""
Command is a behavioral design pattern that
converts requests or simple operations into
objects.

The conversion allows deferred or remote execution
of commands, storing command history, etc.
"""
from typing import List


class TextField:
    """
    TextField works a GUI text component, is this context it's acts as (receiver)
    
    Receiver -> is the object that perform the concrete action triggered on commands
    """
    def __init__(self) -> None:
        # text
        self._text: str = ''
        self._selected_text: str = ''
        # positions
        self._offset: int = 0
        self._start: int = 0
        self._end: int = 0

    # text methods

    def set_text(self, text: str) -> None:
        self._text = text

    def get_text(self) -> str:
        return self._text

    def select_text(self, start: int = 0, end: int = 0) -> None:
        self._selected_text = self._text[start:end]

    def get_selected_text(self) -> str:
        return self._selected_text

    def insert_text(self, clipboard: str, offset: int = 0) -> None:
        self._text = self._text[:offset] + clipboard + self._text[offset:]
        self._offset = offset

    # positions

    def set_caret_position(self, offset: int) -> None:
        self._offset = offset

    def get_caret_position(self) -> int:
        return self._offset

    def get_selection_start(self) -> int:
        return self._start

    def get_selection_end(self) -> int:
        return self._end


class Editor:
    """
    Editor works as GUI rich editor, in this context it's acts as a (sender)

    Sender -> is the object that create and trigger all commands
    """
    def __init__(self) -> None:
        self._text_field: TextField = TextField()
        self._clipboard: str = ''
        self._history: CommandHistory = CommandHistory()

    def _execute_command(self, command: "AbstractCommand") -> None:
        if command.execute():
            self._history.push(command)

    def _undo(self) -> None:
        # import pdb; pdb.set_trace()
        if self._history.is_empty():
            return False

        _command: AbstractCommand = self._history.pop()
        if _command:
            _command.undo()

    # simulate actions on text editor

    def typing_text(self, text: str) -> None:
        self._text_field.set_text(text)

    def ctrl_c(self, start: int, end: int) -> None:
        self._text_field.select_text(start, end)
        self._execute_command(CopyCommand(self))

    def ctrl_v(self, offset: int) -> None:
        self._text_field.set_caret_position(offset)
        self._execute_command(PasteCommand(self))

    def ctrl_x(self, start: int, end: int) -> None:
        self._text_field.select_text(start, end)
        self._execute_command(CutCommand(self))

    def ctrl_z(self) -> None:
        self._undo()


class AbstractCommand:
    """
    Abstract base command
    """
    def __init__(self, editor: Editor) -> None:
        self._editor = editor
        self._backup: str = ''

    def backup(self) -> None:
        self._backup = self._editor._text_field.get_text()

    def undo(self) -> None:
        self._editor._text_field.set_text(self._backup)

    def execute(self) -> bool:
        """
        execute perform a operation and return True if current state was changed.
        """
        raise NotImplementedError()


class CopyCommand(AbstractCommand):
    """
    CopyCommand class, implement the copy operation from receiver

    copy selected text to clipboard
    """
    def execute(self) -> bool:
        _selected_text: str = self._editor._text_field.get_selected_text()
        self._editor._clipboard = _selected_text
        return False


class PasteCommand(AbstractCommand):
    """
    PasteCommand class, implement the paste operation from receiver

    paste text from clipboard
    """
    def execute(self) -> bool:
        if not self._editor._clipboard:
            return False

        self.backup()

        _clipboard = self._editor._clipboard
        _offset = self._editor._text_field.get_caret_position()
        self._editor._text_field.insert_text(_clipboard, offset=_offset)

        return True


class CutCommand(AbstractCommand):
    """
    CutCommand class, implement the cut operation from receiver

    cut text from clipboard
    """
    def execute(self) -> bool:
        if not self._editor._text_field.get_selected_text():
            return False

        self.backup()

        _current_text: str = self._editor._text_field.get_text()
        self._editor._clipboard = self._editor._text_field.get_selected_text()
        
        _cuttted_text: str = self._cut_text(_current_text)
        self._editor._text_field.set_text(_cuttted_text)

    def _cut_text(self, text: str) -> str:
        _start = self._editor._text_field.get_selection_start()
        _end = self._editor._text_field.get_selection_end()
        
        _cutted_text: str = text[_start:] + text[:_end]

        return _cutted_text


class CommandHistory:
    """
    CommandHistory class, save history of all command
    that has was change editor state.
    """
    def __init__(self) -> None:
        self._history: List[AbstractCommand] = []

    def push(self, command: AbstractCommand) -> None:
        self._history.append(command)

    def pop(self) -> AbstractCommand:
        return self._history.pop()

    def is_empty(self) -> bool:
        return not self._history


class Demo:

    def run(self) -> None:
        editor: Editor = Editor()
        editor.typing_text('Hi my name is Rafael Cassau!')

        # simule Ctrl+C Ctrl+V action
        editor.ctrl_c(13, 28)
        editor.ctrl_v(28)
        print('Ctrl+C Ctrl+V:')
        print('-------------------')
        print('Text copied: {}'.format(editor._text_field.get_selected_text()))
        print('Text pasted, new text: {}'.format(editor._text_field.get_text()))
        print('-------------------')

        # simulate Ctrl+Z action
        editor.ctrl_z()
        print('Ctrl+Z:')
        print('-------------------')
        print('undo, new text: {}'.format(editor._text_field.get_text()))
        print('-------------------')

        # simulate Ctrl+X Ctrl+V action
        editor.ctrl_x(13, 28)
        editor.ctrl_v(0)
        print('Ctrl+X + Ctrl+V:')
        print('-------------------')
        print('Text cutted: {}'.format(editor._text_field.get_selected_text()))
        print('Text pasted, new text: {}'.format(editor._text_field.get_text()))
        print('-------------------')

        editor.ctrl_z()
        print('Ctrl+Z:')
        print('-------------------')
        print('undo, new text: {}'.format(editor._text_field.get_text()))
        print('-------------------')


demo: Demo = Demo()
demo.run()
