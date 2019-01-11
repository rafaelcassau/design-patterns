"""
Bridge is a structural design pattern that
divides business logic or huge class into
separate class hierarchies that can be developed
independently.

One of these hierarchies (often called the Abstraction)
will get a reference to an object of the second hierarchy
(Implementation). The abstraction will be able to delegate
some (sometimes, most) of its calls to the implementations
object. Since all implementations will have a common interface,
they'd be interchangeable inside the abstraction.
"""

class DeviceInterface:

    def is_enabled(self) -> bool:
        raise NotImplementedError()

    def enable(self) -> None:
        raise NotImplementedError()

    def disable(self) -> None:
        raise NotImplementedError()

    def get_volume(self) -> int:
        raise NotImplementedError()

    def set_volume(self, volume: int) -> None:
        raise NotImplementedError()

    def get_channel(self) -> int:
        raise NotImplementedError()

    def set_channel(self, channel) -> None:
        raise NotImplementedError()

    def print_status(self) -> None:
        raise NotImplementedError()


class Radio(DeviceInterface):
    _on: bool = False
    _volume: int = 30
    _channel: int = 1

    def is_enabled(self) -> bool:
        return self._on

    def enable(self) -> None:
        self._on = True

    def disable(self) -> None:
        self._on = False

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, volume: int) -> None:
        if volume > 100:
            self._volume = 100
        elif volume < 0:
            self._volume = 0
        else:
            self._volume = volume

    def get_channel(self) -> int:
        return self._channel

    def set_channel(self, channel: int) -> None:
        self._channel = channel

    def print_status(self) -> None:
        print("--------------------------")
        print("| I'm radio.")
        print("| I'm enable" if self._on else "I'm disable")
        print(f"| Current volume is {self._volume}%")
        print(f"| Current channel is {self._channel}")
        print("--------------------------")


class Tv(DeviceInterface):
    _on: bool = False
    _volume: int = 30
    _channel: int = 1

    def is_enabled(self) -> bool:
        return self._on

    def enable(self) -> None:
        self._on = True

    def disable(self) -> None:
        self._on = False

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, volume: int) -> None:
        if volume > 100:
            self._volume = 100
        elif volume < 0:
            self._volume = 0
        else:
            self._volume = volume

    def get_channel(self) -> int:
        return self._channel

    def set_channel(self, channel: int) -> None:
        self._channel = channel

    def print_status(self) -> None:
        print("--------------------------")
        print("| I'm TV set.")
        print("| I'm enabled" if self._on else "I'm disabled")
        print(f"| Current volume is {self._volume}%")
        print(f"| Current channel is {self._channel}")
        print("--------------------------")


class RemoteInterface:

    def power(self) -> None:
        raise NotImplementedError()

    def volume_down(self) -> None:
        raise NotImplementedError()

    def volume_up(self) -> None:
        raise NotImplementedError()

    def channel_down(self) -> None:
        raise NotImplementedError()

    def channel_up(self) -> None:
        raise NotImplementedError()


class BasicRemote(RemoteInterface):

    def __init__(self, device: DeviceInterface) -> None:
        self._device = device

    def power(self) -> None:
        print('Remote: power toggle')
        if self._device.is_enabled():
            self._device.disable()
        else:
            self._device.enable()

    def volume_down(self) -> None:
        print('Remote: volume down')
        current_volume = self._device.get_volume()
        new_volume = current_volume - 10
        self._device.set_volume(new_volume)

    def volume_up(self) -> None:
        print('Remote: volume up')
        current_volume = self._device.get_volume()
        new_volume = current_volume + 10
        self._device.set_volume(new_volume)

    def channel_down(self) -> None:
        print('Remote: channel down')
        current_channel = self._device.get_channel()
        new_channel = current_channel - 1
        self._device.set_channel(new_channel)

    def channel_up(self) -> None:
        print('Remote: channel up')
        current_channel = self._device.get_channel()
        new_channel = current_channel + 1
        self._device.set_channel(new_channel)


class AdvancedRemote(BasicRemote):

    def __init__(self, device: DeviceInterface):
        self._device = device

    def mute(self):
        print('Remote: mute')
        self._device.set_volume(0)


# TV + BasicRemote
tv = Tv()
basic_remote = BasicRemote(tv)
basic_remote.power()
tv.print_status()

# TV + AdvancedRemote
tv = Tv()
advanced_remote = AdvancedRemote(tv)
advanced_remote.power()
advanced_remote.mute()
tv.print_status()

# Radio + BasicRemote
radio = Radio()
basic_remote = BasicRemote(radio)
basic_remote.power()
radio.print_status()

# Radio + AdvancedRemote
radio = Radio()
advanced_remote = AdvancedRemote(radio)
advanced_remote.power()
advanced_remote.mute()
radio.print_status()
