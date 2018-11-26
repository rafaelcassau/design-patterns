"""
A factory pattern defines a interface for creating an 
object, but defer object instantiation to run time.
"""

# abstract class (Interface)
class ShapeInterface:

    def draw(self):
        raise NotImplementedError()


# concrete classes
class Circle(ShapeInterface):

    def draw(self):
        print('Circle.draw')


class Square(ShapeInterface):

    def draw(self):
        print('Square.draw')


# factory
class ShapeFactory:

    @staticmethod
    def get_shape(shape_type):
        if shape_type == 'circle':
            return Circle()
        elif shape_type == 'square':
            return Square()
        raise Exception('Could not find shape ' + shape_type)

# run
ShapeFactory.get_shape('circle')
ShapeFactory.get_shape('square')
ShapeFactory.get_shape('triange')