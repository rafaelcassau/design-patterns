"""
Define a one-to-many dependency between objects
so that when on object changes state, all its
dependents are notified and updated automatically.
"""
from typing import List


class ObserverInterface:
    """
    ObserverInterface defines a update method that will receiver
    all notifications when a state of observable object is updated.
    """
    def update(self, *args, **kwargs) -> None:
        raise NotImplementedError()


class Observable:
    """
    Observable define some methods to register observers that will be notified 
    when any change in this object occur.
    """
    def __init__(self) -> None:
        self._observers: List[ObserverInterface] = []

    def register(self, observer: ObserverInterface) -> None:
        self._observers.append(observer)

    def unregister(self, observer: ObserverInterface) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def unregister_all(self) -> None:
        self._observers.clear()

    def update_observers(self, *args, **kwargs) -> None:
        for observer in self._observers:
            observer.update(*args, **kwargs)


class AmericanStockMarket(ObserverInterface):
    """
    Concrete observer will be notified when any change occur in the
    observable object.
    """
    def update(self, *args, **kwargs) -> None:
        print(f'American stock market received: {args}')
        print(f'{kwargs}')


class EuropeanStockMarket(ObserverInterface):
    """
    Concrete observer will be notified when any change occur in the
    observable object.
    """
    def update(self, *args, **kwargs) -> None:
        print(f'European stock market received: {args}')
        print(f'{kwargs}')


really_big_company: Observable = Observable()

american_observer: AmericanStockMarket = AmericanStockMarket()
european_observer: EuropeanStockMarket = EuropeanStockMarket()

really_big_company.register(american_observer)
really_big_company.register(european_observer)

really_big_company.update_observers('important update', msg='CEO unexpectedly resigns')