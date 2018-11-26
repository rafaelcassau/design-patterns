"""
Prototype is a creational design pattern that lets you
produce new objects by copying existing ones without
compromising their internals.
"""

class AbstractShape:
    x = 0
    y = 0
    color = 0

    def __init__(self, target=None):
        if target:
            self.x = target.x
            self.y = target.y
            self.color = target.color

    def __eq__(self, other):
        if not isinstance(other, AbstractShape):
            return False

        return other.x == self.x and other.y == self.y and other.color == self.color

    def clone(self):
        raise NotImplementedError


# concrete shapes

class Circle(AbstractShape):
    radius = 0

    def __init__(self, target=None):
        super().__init__(target=target)
        if target:
            self.radius = target.radius

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False

        return super().__eq__(other) and other.radius == self.radius

    def clone(self):
        return Circle(target=self)


class Rectangle(AbstractShape):
    width = 0
    height = 0

    def __init__(self, target=None):
        super().__init__(target=target)
        if target:
            self.width = target.width
            self.height = target.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False

        return super().__eq__(other) and other.width == self.width and other.height == self.height

    def clone(self):
        return Rectangle(target=self)


# client

class Client:

    def run(self):
        shapes = []

        # circle
        circle = Circle()
        circle.x = 10
        circle.y = 20
        circle.radius = 15

        shapes.append(circle)

        another_circle = circle.clone()
        shapes.append(another_circle)

        # rectangle
        rectangle = Rectangle()
        rectangle.width = 10
        rectangle.height = 20
        shapes.append(rectangle)

        self.clone_and_compare(shapes)

    def clone_and_compare(self, shapes):
        shapes_copy = []

        for shape in shapes:
            shapes_copy.append(shape.clone())

        for index, (shape, shape_copy) in enumerate(zip(shapes, shapes_copy)):
            shape, shape_copy = (shape, shape_copy)

            if shape is not shape_copy:
                print('{}: Shapes are different objects (yay!)'.format(index))
                if shape == shape_copy:
                    print('{}: And they are identical (yay)'.format(index))
                else:
                    print('{}: But they are not identical (booo!)'.format(index))
            else:
                print('{}: Shape objects are the same (booo!)'.format(index))


#run

client = Client()
client.run()


# Registered Prototype

class BundledShapeCache:
    cache = {}

    def __init__(self):
        circle = Circle()
        circle.x = 5
        circle.y = 7
        circle.radius = 45
        circle.color = "Green"

        rectangle = Rectangle()
        rectangle.x = 6
        rectangle.y = 9
        rectangle.width = 8
        rectangle.height = 10
        rectangle.color = "Blue"

        self.cache['Big green circle'] = circle
        self.cache['Medium blue rectangle'] = rectangle

    def put(self, key, shape):
        self.cache[key] = shape
        return shape

    def get(self, key):
        return self.cache[key].clone()



class RegisteredClient:

    def run(self):
        bundled_shape_cache = BundledShapeCache()

        shape1 = bundled_shape_cache.get('Big green circle')
        shape2 = bundled_shape_cache.get('Medium blue rectangle')
        shape3 = bundled_shape_cache.get('Medium blue rectangle')

        if shape1 is not shape2 and not shape1 == shape2:
            print('Big green circle != Medium blue rectangle (yay!)')
        else:
            print('Big green circle == Medium blue rectangle (booo!)')

        if shape2 is not shape3:
            print('Medium blue rectangles are two different objects (yay!)')

            if shape2 == shape3:
                print('And they are identical (yay!)')
            else:
                print('But they are not identical (booo!)')
        else:
            print('Rectangle objects are the same (booo!)')


registered_client = RegisteredClient()
registered_client.run()
