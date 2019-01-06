"""
Convert the interface of a class into another
interface clients expect. Adapter lets classes
work together that couldn't otherwise because of
incompatible interfaces
"""

class EuropeanSocketInterface:
    """
    Adaptee (source) interface
    """
    def voltage(self) -> int:
        raise NotImplementedError()

    def live(self) -> int:
        raise NotImplementedError()

    def neutral(self) -> int:
        raise NotImplementedError()

    def earth(self) -> int:
        raise NotImplementedError()


class USASocketInterface:
    """
    Target interface
    """
    def voltage(self) -> int:
        raise NotImplementedError()

    def live(self) -> int:
        raise NotImplementedError()

    def neutral(self) -> int:
        raise NotImplementedError()


class EuropeanSocket(EuropeanSocketInterface):
    """
    Adaptee
    """
    def voltage(self) -> int:
        return 230

    def live(self) -> int:
        return 1

    def neutral(self) -> int:
        return -1


class AmericanKettle:
    """
    Client
    """
    __power : EuropeanSocketInterface = None

    def __init__(self, power: EuropeanSocketInterface) -> None:
        self.__power = power

    def boil(self) -> None:
        if self.__power.voltage() > 110:
            print('Kettle on fire!')
        else:
            if self.__power.live() == 1 and self.__power.neutral() == -1:
                print('Coffe time!')
            else:
                print('No power.')


class Adapter(USASocketInterface):
    __socket = None

    def __init__(self, socket) -> None:
        self.__socket = socket

    def voltage(self) -> int:
        return 110

    def live(self) -> int:
        return self.__socket.live()

    def neutral(self) -> int:
        return self.__socket.neutral()


socket = EuropeanSocket()
kettle = AmericanKettle(socket)
kettle.boil()

socket = EuropeanSocket()
adapter = Adapter(socket)
kettle = AmericanKettle(adapter)
kettle.boil()