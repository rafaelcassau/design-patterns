"""
Provide an interface for creating
families of related objects without 
specifying their concrete classes.
"""

# abstract classes (interfaces)
class Shape2DInterface:

    def draw(self):
        raise NotImplementedError()


class Shape3DInterface:

    def build(self):
        raise NotImplementedError()


# concrete 2D classes
class Circle(Shape2DInterface):

    def draw(self):
        print('Circle.draw')


class Square(Shape2DInterface):

    def draw(self):
        print('Square.draw')


# concrete 3D classes
class Sphere(Shape3DInterface):

    def build(self):
        print('Sphere.build')


class Cube(Shape3DInterface):

    def build(self):
        print('Cube.build')


# abstract shape factory
class ShapeFactoryInterface:

    def get_shape(sides):
        raise NotImplementedError()


# concrete shape factories
class Shape2DFactory(ShapeFactoryInterface):

    @staticmethod
    def get_shape(sides):
        if sides == 1:
            return Circle()
        elif sides == 4:
            return Square()
        raise Exception('Bad 2D shape creation: shape not defined for ' + sides + ' sides')


class Shape3DFactory(ShapeFactoryInterface):
    
    @staticmethod
    def get_shape(sides):
        """ here, sides refers to the numbers of faces """
        if sides == 1:
            return Sphere()
        elif sides == 6:
            return Cube()
        raise Exception('Bad 3D shape creation: shape not defined for ' + sides + ' faces')


# run
shape_2 = Shape2DFactory.get_shape(1)
shape_2.draw() # circle
shape_2 = Shape2DFactory.get_shape(4)
shape_2.draw() # square

shape_3 = Shape3DFactory.get_shape(1)
shape_3.build() # sphere
shape_3 = Shape3DFactory.get_shape(6)
shape_3.build() # cube
