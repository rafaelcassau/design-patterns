"""
Composite is a structural design pattern that
allows composing objects into a tree-like
structure and work with the it as if it was
a singular object.

Composite became a pretty popular solution for
the most problems that require building a tree
structure. Composite's great feature is the 
ability to run methods recursively over the whole
tree structure and sun up the results.
"""
from enum import Enum
from typing import List


class Color(Enum):
    """
    enum for simulate colors
    """
    LIGHT_GRAY = 'light_gray'
    BLACK = 'black'
    RED = 'red'
    BLUE = 'blue'
    GREEN = 'green'


class Graphics:
    """
    util for simule render shapes on screen
    """
    _color: Color = None
    _focus: bool = False

    def set_color(self, color: Color):
        self._color = color

    def get_color(self) -> Color:
        return self._color

    def set_focus(self, focus: bool) -> None:
        self._focus = focus

    def is_focused(self) -> bool:
        return self._focus

    def fill_rect(self, x: int, y: int, width: int, height: int):
        print('------------------------------------------------')
        print(' * ')
        print(f'x: {x}')
        print(f'y: {y}')
        print(f'width: {width}')
        print(f'height: {height}')
        print(f'color: {self._color}')
        print(f'focus: {self._focus}')

    def draw_oval(self, x: int, y: int, width: int, height: int):
        print('------------------------------------------------')
        print('     *********     ')
        print('   *************   ')
        print('  ***************  ')
        print(' ***************** ')
        print('  ***************  ')
        print('   *************   ')
        print('     *********     ')
        print(f'x: {x}')
        print(f'y: {y}')
        print(f'width: {width}')
        print(f'height: {height}')
        print(f'color: {self._color}')
        print(f'focus: {self._focus}')

    def draw_rect(self, x: int, y: int, width: int, height: int):
        print('------------------------------------------------')
        print('    ************************    ')
        print('    ************************    ')
        print('    ************************    ')
        print('    ************************    ')
        print('    ************************    ')
        print('    ************************    ')
        print('    ************************    ')
        print(f'x: {x}')
        print(f'y: {y}')
        print(f'width: {width}')
        print(f'height: {height}')
        print(f'color: {self._color}')
        print(f'focus: {self._focus}')


class ShapeInterface:
    """
    Common shape interface
    """
    def get_x(self) -> int:
        raise NotImplementedError()

    def get_y(self) -> int:
        raise NotImplementedError()

    def get_width(self) -> int:
        raise NotImplementedError()

    def get_height(self) -> int:
        raise NotImplementedError()

    def move(self, x: int, y: int) -> None:
        raise NotImplementedError()

    def is_inside_bounds(self, x: int, y: int) -> bool:
        raise NotImplementedError()

    def select(self) -> None:
        raise NotImplementedError()

    def unselect(self) -> None:
        raise NotImplementedError()

    def is_selected(self) -> bool:
        raise NotImplementedError()

    def paint(self, graphics: Graphics) -> None:
        raise NotImplementedError()


class AbstractShape(ShapeInterface):
    """
    Abstract shape with basic functionality
    """
    _x: int = 0
    _y: int = 0
    _color: Color = None
    _selected: bool = False

    def __init__(self, x: int, y: int, color: Color) -> None:
        self._x = x
        self._y = y
        self._color = color

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def get_width(self) -> int:
        return 0

    def get_height(self) -> int:
        return 0
    
    def move(self, x: int, y: int) -> None:
        self._x += x
        self._y += y

    def is_inside_bounds(self, x: int, y: int) -> bool:
        return x > self.get_x() and (self.get_x() + self.get_width()) and \
            y > self.get_y() and (self.get_y() + self.get_height())

    def select(self) -> None:
        self._selected = True

    def unselect(self) -> None:
        self._selected = False

    def is_selected(self) -> bool:
        return self._selected

    def paint(self, graphics: Graphics):
        if self.is_selected():
            self.enable_selection_style(graphics)
        else:
            self.disable_selection_style(graphics)

    # custom methods, those don't belong the Shape interface

    def enable_selection_style(self, graphics: Graphics) -> None:
        graphics.set_color(Color.LIGHT_GRAY)
        graphics.set_focus(True)

    def disable_selection_style(self, graphics: Graphics) -> None:
        graphics.set_color(self._color)
        graphics.set_focus(False)


class Dot(AbstractShape):
    """
    A dot
    """
    DOT_SIZE = 3

    def get_width(self) -> int:
        return self.DOT_SIZE

    def get_height(self) -> int:
        return self.DOT_SIZE

    def paint(self, graphics: Graphics):
        super().paint(graphics)
        graphics.fill_rect(self.get_x() - 1, self.get_y() - 1, self.get_width(), self.get_height())


class Circle(AbstractShape):
    """
    A circle
    """
    _radius: int = 0

    def __init__(self, x: int, y: int, radius: int, color: Color) -> None:
        super().__init__(x, y, color)
        self._radius = radius

    def get_width(self) -> int:
        return self._radius * 2

    def get_height(self) -> int:
        return self._radius * 2

    def paint(self, graphics: Graphics) -> None:
        super().paint(graphics)
        graphics.draw_oval(self.get_x(), self.get_y(), self.get_width() - 1, self.get_height() - 1)


class Rectangle(AbstractShape):
    """
    A rectangle
    """
    _width: int = 0
    _height: int = 0

    def __init__(self, x: int, y: int, width: int, height: int, color: Color) -> None:
        super().__init__(x, y, color)
        self._width = width
        self._height = height

    def get_width(self) -> int:
        return self._width

    def get_height(self) -> int:
        return self._height

    def paint(self, graphics: Graphics) -> None:
        super().paint(graphics)
        graphics.draw_rect(self.get_x(), self.get_y(), self.get_width() - 1, self.get_height() - 1)


class CompoundShape(AbstractShape):
    """
    Compound shape, which consists of other shape objects

    here is where the pattern works.

    (CompoundShape) implements the same interface through AbstractShape class (ShapeInterface),
    but acts handle one or many shapes (composed), this means that there are methods
    like "add(shapes)", "remove(shapes)" that deal with a collection of shapes with
    same interface.

    It's means that the client don't need know if a component is single or a collection of
    shapes. In another words, the client just call the same methods defined on (ShapeInterface)
    it's means the client can deal with a single or a collection of shapes without know it's 
    implementation details.

    CompoundShape will run the request if it's a leaf or will delegate to each child
    run it's request, it's interchangeable and execute recursively
    """

    def __init__(self, *shapes: ShapeInterface) -> None:
        super().__init__(0, 0, Color.BLACK)
        self._children: List[ShapeInterface] = []
        self.add(shapes)

    def get_x(self) -> int:
        """
        return min X of children's CompoundShape
        """
        child = min(self._children, default=None, key=lambda item: item.get_x())
        if child:
            return child.get_x()
        return 0

    def get_y(self) -> int:
        """
        return min Y of children's CompoundShape
        """
        child = min(self._children, default=None, key=lambda item: item.get_y())
        if child:
            return child.get_y()
        return 0

    def get_width(self) -> int:
        """
        return max width of children's CompoundShape
        """
        max_width: int = 0
        x: int = self.get_x()

        for child in self._children:
            child_relative_x: int = child.get_x() - x
            child_width: int = child_relative_x + child.get_width()
            if child_width > max_width:
                max_width = child_width

        return max_width

    def get_height(self) -> int:
        """
        return max height of children's CompoundShape
        """
        max_height: int = 0
        y: int = self.get_y()

        for child in self._children:
            child_relative_y: int = child.get_y() - y
            child_height: int = child_relative_y + child.get_height()
            if child_height > max_height:
                max_height = child_height

        return max_height

    def move(self, x: int, y: int) -> None:
        """
        move all children's CompoundShape
        """
        for child in self._children:
            child.move(x, y)

    def is_inside_bounds(self, x: int, y: int) -> bool:
        """
        check if there're a child in inside the bounds
        """
        for child in self._children:
            if child.is_inside_bounds(x, y):
                return True
    
        return False

    def unselect(self) -> None:
        """
        unselect all children's CompoundShape
        """
        super().unselect()
        for child in self._children:
            child.unselect()


    # custom methods, those don't belong the Shape interface

    def add(self, shapes: List[ShapeInterface]) -> None:
        """
        add one or more shapes 
        """
        self._children.extend(shapes)

    def remove(self, shapes: List[ShapeInterface]) -> None:
        """
        remove one or more shapes 
        """
        for child in self._children:
            if child in shapes:
                self._children.remove(child)

    def clear(self) -> None:
        """
        clear all children's CompoundShape
        """
        self._children.clear()

    def select_child_at(self, x: int, y: int) -> bool:
        """
        select a child that is inside the bounds
        """
        for child in self._children:
            if child.is_inside_bounds(x, y):
                child.select()
                return True

            return False

    def paint(self, graphics: Graphics):
        """
        paint selected child if there are at least one 
        or paint all not selected children
        """
        if self.is_selected():
            self.enable_selection_style(graphics)
            graphics.draw_rect(self.get_x() - 1, self.get_y() - 1, self.get_width() + 1, self.get_height() + 1)
            self.disable_selection_style(graphics)
        else:
            for child in self._children:
                child.paint(graphics)


class Demo:

    def run(self):
        circle: Circle = Circle(10, 10, 10, Color.BLUE)
        
        circle_with_dot_compound: CompoundShape = CompoundShape(
            Circle(110, 110, 50, Color.RED),
            Dot(160, 160, Color.RED),
        )

        rectangle_with_dot_compound: CompoundShape = CompoundShape(
            Rectangle(250, 250, 100, 100, Color.GREEN),
            Dot(240, 240, Color.GREEN),
            Dot(240, 360, Color.GREEN),
            Dot(360, 360, Color.GREEN),
            Dot(360, 240, Color.GREEN),
        )

        all_shapes: List[ShapeInterface] = []
        all_shapes.append(circle)
        all_shapes.append(circle_with_dot_compound)
        all_shapes.append(rectangle_with_dot_compound)

        graphics: Graphics = Graphics()

        for shape in all_shapes:
            shape.paint(graphics)


Demo().run()
