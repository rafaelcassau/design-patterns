"""
Avoids coupling the sender of a request to the
receiver by giving more than one object a chance
to handle the request.
"""


class Car:

    def __init__(self, name: str, water: int, fuel: int, oil: int) -> None:
        self._name = name
        self._water = water
        self._fuel = fuel
        self._oil = oil

    def is_fine(self) -> bool:
        if self._water >= 20 and self._fuel >= 5 and self._oil >= 10:
            print('Car is good to go')
            return True
        else:
            return False


class BaseHandler:

    def __init__(self, successor: "BaseHandler" = None):
        self._sucessor = successor

    def handle_request(self, car: Car) -> None:
        if not car.is_fine() and self._sucessor is not None:
            self._sucessor.handle_request(car)


class WaterHandler(BaseHandler):

    def handle_request(self, car):
        if car._water < 20:
            car._water = 100
            print('Added water')

        super().handle_request(car)


class FuelHandler(BaseHandler):

    def handle_request(self, car):
        if car._fuel < 5:
            car._fuel = 100
            print('Added fuel')

        super().handle_request(car)


class OilHandler(BaseHandler):

    def handle_request(self, car):
        if car._oil < 10:
            car._oil = 100
            print('Added oil')

        super().handle_request(car)


garage_handler: BaseHandler = OilHandler(FuelHandler(WaterHandler()))
car: Car = Car(name='my car', water=1, fuel=1, oil=1)
garage_handler.handle_request(car)


car: Car = Car(name='my car', water=5, fuel=5, oil=5)
garage_handler.handle_request(car)

car: Car = Car(name='my car', water=10, fuel=10, oil=10)
garage_handler.handle_request(car)

car: Car = Car(name='my car', water=20, fuel=20, oil=20)
garage_handler.handle_request(car)