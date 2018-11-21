"""
Separate the construction of a complex object
from its representation so that the same construction
process can create different representations
"""

# car
class Car:

    def __init__(self):
        self._wheels = []
        self._engine = None
        self._body = None

    def set_body(self, body):
        self._body = body

    def attach_wheel(self, wheel):
        self._wheels.append(wheel)

    def set_engine(self, engine):
        self._engine = engine

    def specification(self):
        print('body: {}'.format(self._body.shape))
        print('engine horsepower: {}'.format(self._engine.horsepower))
        print('tire size: {}'.format(self._wheels[0].size))


# car parts
class Wheel:
    size = None


class Engine:
    horsepower = None


class Body:
    shape = None


# builder
class BuilderInterface:

    def get_body(self):
        raise NotImplementedError

    def get_engine(self):
        raise NotImplementedError

    def get_wheel(self):
        raise NotImplementedError


class JeepBuilder(BuilderInterface):

    def get_body(self):
        body = Body()
        body.shape = "SUV"
        return body

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel


class NissanBuilder(BuilderInterface):

    def get_body(self):
        body = Body()
        body.shape = "hatchback"
        return body

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 100
        return engine

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 16
        return wheel


# client builder
class Director:
    _builder = None

    def set_builder(self, builder):
        self._builder = builder

    # The algorithm for assembling a car
    def get_car(self):
        car = Car()

        body = self._builder.get_body()
        car.set_body(body)

        # Then engine
        engine = self._builder.get_engine()
        car.set_engine(engine)

        # And four wheels
        for i in range(4):
            wheel = self._builder.get_wheel()
            car.attach_wheel(wheel)

        return car


# run
director = Director()

# jeep
director.set_builder(JeepBuilder())
jeep = director.get_car()
jeep.specification()

# nissan
director.set_builder(NissanBuilder())
nissan = director.get_car()
nissan.specification()
