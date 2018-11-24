"""
Builder is a creational design pattern that lets
you produce different types and representations
of an object using the same process. Builder allows
constructing complex objects step by step.
"""

from enum import Enum


class BuilderInterface:
    """
    Builder interface defines all possible ways to configure a product.
    """

    def set_type(self, type):
        raise NotImplementedError

    def set_seats(self, seats):
        raise NotImplementedError

    def set_engine(self, engine):
        raise NotImplementedError

    def set_transmission(self, transmission):
        raise NotImplementedError

    def set_trip_computer(self, trip_computer):
        raise NotImplementedError

    def set_gps_navigator(self, gps_navigator):
        raise NotImplementedError


class CarBuilder(BuilderInterface):
    """
    Concrete builders implement steps defined in the common interface.
    """

    def set_type(self, type):
        self.type = type

    def set_seats(self, seats):
        self.seats = seats

    def set_engine(self, engine):
        self.engine = engine

    def set_transmission(self, transmission):
        self.transmission = transmission

    def set_trip_computer(self, trip_computer):
        self.trip_computer = trip_computer

    def set_gps_navigator(self, gps_navigator):
        self.gps_navigator = gps_navigator

    def get_result(self):
        return Car(
            type=self.type,
            seats=self.seats,
            engine=self.engine,
            transmission=self.transmission,
            trip_computer=self.trip_computer,
            gps_navigator=self.gps_navigator,
        )


class CarManualBuilder(BuilderInterface):
    """
    Unlike other creational patterns, Builder can construct unrelated products,
    which don't have the common interface.

    In this case we build a user manual for a car, using the same steps as we
    built a car. This allows to produce manuals for specific car models,
    configured with different features.
    """

    def set_type(self, type):
        self.type = type

    def set_seats(self, seats):
        self.seats = seats

    def set_engine(self, engine):
        self.engine = engine

    def set_transmission(self, tranmission):
        self.tranmission = tranmission

    def set_trip_computer(self, trip_computer):
        self.trip_computer = trip_computer

    def set_gps_navigator(self, gps_navigator):
        self.gps_navigator = gps_navigator

    def get_result(self):
        return Manual(
            type=self.type,
            seats=self.seats,
            engine=self.engine,
            transmission=self.tranmission,
            trip_computer=self.trip_computer,
            gps_navigator=self.gps_navigator
        )


class Car:
    """
    Car is a product class.
    """
    fuel = 0

    def __init__(self, type, seats, engine, transmission, trip_computer, gps_navigator):
        self.type = type
        self.seats = seats
        self.engine = engine
        self.transmission = transmission
        self.trip_computer = trip_computer

        # complexity instantiation process is incapsulated
        self.trip_computer.set_car(self)

        self.gps_navigator = gps_navigator

    # get custom attribute
    def get_fuel(self):
        return self.fuel

    # set custom attribute
    def set_fuel(self, fuel):
        self.fuel = fuel

    def get_type(self):
        return self.type

    def get_seats(self):
        return self.seats

    def get_engine(self):
        return self.engine

    def get_transmission(self):
        return self.transmission

    def get_trip_computer(self):
        return self.trip_computer

    def get_gps_navigator(self):
        return self.gps_navigator


class Manual:

    def __init__(self, type, seats, engine, transmission, trip_computer, gps_navigator):
        self.type = type
        self.seats = seats
        self.engine = engine
        self.transmission = transmission
        self.trip_computer = trip_computer
        self.gps_navigator = gps_navigator

    def print(self):
        info = ''
        info += 'Type of car: {} \n'.format(self.type)
        info += 'Count of seats: {} \n'.format(self.seats)
        info += 'Engine: volume - {}; mileage - {} \n'.format(
            self.engine.get_volume(),
            self.engine.get_mileage()
        )
        info += 'Transmission: {}'.format(self.transmission)

        if self.trip_computer:
            info += 'Trip Computer: Functional \n'
        else:
            info += 'Trip Computer: N/A \n'

        if self.gps_navigator:
            info += 'GPS Navigator: Functional \n'
        else:
            info += 'GPS Navigator: N/A \n'

        return info


class Type(Enum):
    CITY_CAR = 1
    SPORT_CAR = 2
    SUV = 3


# components

class Engine:
    """
    Just another feature of a car.
    """

    def __init__(self, volume, mileage):
        self.volume = volume
        self.mileage = mileage
        self.started = None

    def on(self):
        self.started = True

    def off(self):
        self.started = False

    def is_started(self):
        return self.is_started

    def go(self, mileage):
        if started:
            self.mileage += mileage
        else:
            print('Cannot go(), you must start engine first!')

    def get_volume(self):
        return self.volume

    def get_mileage(self):
        return self.mileage


class GPSNavigator:
    """
    Just another feature of a car.
    """

    def __init__(self, manual_route=None):
        if manual_route:
            self.route = manual_route
        else:
            self.route = '221b, Baker Street, London to Scoltand Yard, 8-10 Broadway, London'

    def get_route(self):
        return self.route


class Transmission(Enum):
    """
    Just another feature of a car.
    """
    SINGLE_SPEED = 1
    MANUAL = 2
    AUTOMATIC = 3
    SEMI_AUTOMATIC = 4


class TripComputer:
    """
    Just another feature of a car.
    """

    def set_car(self, car):
        self.car = car

    def show_fuel_level(self):
        print('Fuel level: {}'.format(car.get_fuel()))

    def show_status(self):
        if self.car.get_engine().is_started():
            print("Car is started")
        else:
            print("Car isn't started")


# class that will handle objects and it's builders

class Director:
    """
    Director defines the order of building steps.
    It works with a builder object through common Builder interface.
    Therefore it may not know what product is being built.
    """

    def construct_sports_car(self, builder):
        builder.set_type(Type.SPORT_CAR)
        builder.set_seats(2)
        builder.set_engine(Engine(volume=3.0, mileage=0))
        builder.set_transmission(Transmission.SEMI_AUTOMATIC)
        builder.set_trip_computer(TripComputer())
        builder.set_gps_navigator(GPSNavigator())

    def construct_city_car(self, builder):
        builder.set_type(type.CITY_CAR)
        builder.set_seats(2)
        builder.set_engine(volume=1.2, mileage=2)
        builder.set_transmission(Transmission.AUTOMATIC)
        builder.set_trip_computer(TripComputer())
        builder.set_gps_navigator(GPSNavigator())

    def constructSUV(self, builder):
        builder.set_type(Type.SUV)
        builder.set_seats(4)
        builder.set_engine(Engine(volume=2.5, mileage=0))
        builder.set_transmission(Transmission.MANUAL)
        builder.set_gps_navigator(GPSNavigator())


# client code

class Client:

    def run(self):
        """
        Client class. Everything comes together here.
        """
        director = Director()

        """
        Director gets the concrete builder object from the client
        (application code). That's because application knows better which
        builder to use to get a specific product.
        """
        car_builder = CarBuilder()
        director.construct_sports_car(car_builder)
        """
        The final product is often retrieved from a builder object, since
        Director is not aware and not dependent on concrete builders and products.
        """
        car = car_builder.get_result()
        print('Car built: {}'.format(car.get_type()))

        car_manual_builder = CarManualBuilder()

        """
        Director may know several building recipes.
        """
        director.construct_sports_car(car_manual_builder)
        car_manual = car_manual_builder.get_result()
        print('Car manual built: {} \n'.format(car_manual.print()))


client = Client()
client.run()
