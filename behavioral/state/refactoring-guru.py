"""
State is a behavioral design pattern that allows
an object to change the behavior when its internal
state changes.

The pattern extracts state-related behaviors into
separate state classes and forces original object
to delegate the work to an instance of these classes,
instead of acting on its own.
"""
from typing import List


class Player:

    def __init__(self):
        self._playing: bool = False
        self._playlist: List[str] = []
        self._current_track: int = 0

        self._state = ReadyState(self)
        self.set_playing(True)
        for i in range(1, 13):
            self._playlist.append(f'Track {i}')

    def change_state(self, state: "StateInterface") -> None:
        self._state = state

    def get_state(self) -> "StateInterface":
        return self._state

    def set_playing(self, playing: bool) -> None:
        self._playing = playing

    def is_playing(self) -> bool:
        return self._playing

    def start_playback(self) -> str:
        return f'Playing {self._playlist[self._current_track]}'

    def next_track(self) -> None:
        self._current_track += 1

        if self._current_track >= len(self._playlist):
            self._current_track = 0

        print(f'Playing {self._playlist[self._current_track]}')

    def previous_track(self) -> None:
        self._current_track -= 1
    
        if self._current_track < 0:
            self._current_track = 1

        print(f'Playing {self._playlist[self._current_track]}')

    def set_current_track_after_stop(self) -> None:
        self._current_track = 0


class StateInterface:
    """
    Common interface for all states
    """
    def __init__(self, player: Player) -> None:
        """
        Player acts a context class (i.e main class)

        Context passes itself through the state contructor.
        This may help a state to fetch some useful context
        data if needed.
        """
        self._player = player

    def on_lock(self) -> str:
        raise NotImplementedError()

    def on_play(self) -> str:
        raise NotImplementedError()

    def on_next(self) -> str:
        raise NotImplementedError()

    def on_previous(self) -> str:
        raise NotImplementedError()


class LockedState(StateInterface):
    """
    Concrete states provide the special implementation for all
    interface methods.
    """
    def __init__(self, player: Player) -> None:
        super().__init__(player)
        self._player.set_playing(False)

    def on_lock(self) -> str:
        if self._player.is_playing():
            self._player.change_state(ReadyState(self._player))
            return 'Stop playing'
        else:
            return 'Locked...'

    def on_play(self) -> str:
        self._player.change_state(ReadyState(self._player))
        return 'Ready'

    def on_next(self) -> str:
        return 'Locked...'

    def on_previous(self) -> str:
        return 'Locked...'


class ReadyState(StateInterface):
    """
    They can also trigger state transitions in the context.
    """
    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def on_lock(self) -> str:
        self._player.change_state(LockedState(self._player))
        return 'Locked...'

    def on_play(self) -> str:
        _action: str = self._player.start_playback()
        self._player.change_state(PlayingState(self._player))
        return _action

    def on_next(self) -> str:
        return 'Locked...'

    def on_previous(self) -> str:
        return 'Locked...'


class PlayingState(StateInterface):
    """
    Concrete states provide the special implementation for all
    interface methods.
    """
    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def on_lock(self) -> str:
        self._player.change_state(LockedState(self._player))
        self._player.set_current_track_after_stop()
        return 'Stop playing'

    def on_play(self) -> str:
        self._player.change_state(ReadyState(self._player))
        return 'Paused...'

    def on_next(self) -> str:
        return self._player.next_track()

    def on_previous(self) -> str:
        return self._player.previous_track()


class Demo:

    def run(self):
        _player: Player = Player()
        
        # play, initial state (PlayingState)
        print(_player.get_state().on_play())

        # play all tracks until start again, state remains the same (PlayingState)
        _player.get_state().on_next() # foward
        _player.get_state().on_next() # foward
        _player.get_state().on_next() # foward
        _player.get_state().on_next() # foward
        _player.get_state().on_next() # foward
        _player.get_state().on_next() # foward
        _player.get_state().on_next() # foward
        _player.get_state().on_next() # foward
        _player.get_state().on_next() # foward
        _player.get_state().on_next() # foward
        _player.get_state().on_next() # foward

        # change the state object from (PlayingState) to (ReadyState)
        print(_player.get_state().on_play())
        
        _player.get_state().on_next() # locked...
        _player.get_state().on_previous() # locked...

        # change the state object from (ReadyState) to (PlayingState) again
        print(_player.get_state().on_play())

        _player.get_state().on_previous() # backward
        _player.get_state().on_previous() # backward
        _player.get_state().on_previous() # backward
        _player.get_state().on_previous() # backward
        _player.get_state().on_previous() # backward
        _player.get_state().on_previous() # backward
        _player.get_state().on_previous() # backward
        _player.get_state().on_previous() # backward
        _player.get_state().on_previous() # backward
        _player.get_state().on_previous() # backward
        _player.get_state().on_previous() # backward

        # change the state object from (PlayingState) to (LockedState)
        print(_player.get_state().on_lock())
        
        _player.get_state().on_next() # locked...
        _player.get_state().on_previous() # locked...

        # state remains the same (LockedState)
        print(_player.get_state().on_lock())

        # change the state object from (LockedState) to (ReadyState) 
        print(_player.get_state().on_play())
        # change the state object from (ReadyState) to (PlayingState) 
        print(_player.get_state().on_play())
        # change the state object from (PlayingState) to (LockedState) 
        print(_player.get_state().on_lock())


demo: Demo = Demo()
demo.run()
