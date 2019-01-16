"""
Flyweight is a structural design pattern that
allows programs to support vast quantities of
objects by keeping their memory consumpition
low.

Pattern achieves it by sharing parts of object
state between multiple objects. In other words,
the Flyweight saves RAM by caching the same data
used by different objects.
"""
from enum import Enum
from typing import List
from random import randint


class Color(Enum):
    """
    enum for simulate colors
    """
    BLACK = 'black'
    GREEN = 'green'
    ORANGE = 'orange'


class Graphics:
    """
    util for simule render shapes on screen
    """
    def __init__(self):
        self._color: Color = None

    def set_color(self, color: Color) -> None:
        self._color = color

    def fill_rect(self, x: int, y: int, width: int, height: int):
        print('------------------------------------------------')
        print('      *      ')
        print('      *      ')
        print('      *      ')
        print(f'x: {x}, y: {y}, width: {width}, height: {height}, color: {self._color} ')

    def fill_oval(self, x: int, y: int, width: int, height: int):
        print('------------------------------------------------')
        print('     ***     ')
        print('    *****    ')
        print('     ***     ')
        print(f'x: {x}, y: {y}, width: {width}, height: {height}, color: {self._color} ')


class TreeType:
    """
    Flyweight object

    contain the "intrinsic" (immutable)
    and heavy sharable part of tree object
    """
    def __init__(self, name: str, color: Color, other_tree_data: str) -> None:
        self._name: str = name
        self._color: Color = color
        self._other_tree_data: str = other_tree_data

    def draw(self, graphics: Graphics, x: int, y: int) -> None:
        graphics.set_color(Color.BLACK)
        graphics.fill_rect(x - 1, y, 3, 5)
        graphics.set_color(self._color)
        graphics.fill_oval(x - 5, y - 10, 10, 10)


class Tree:
    """
    Contains the "extrinsic" (mutable)
    state unique for each tree
    """
    def __init__(self, x: int, y: int, tree_type: TreeType) -> None:
        self._x: int = x
        self._y: int = y
        self.tree_type: TreeType = tree_type

    def draw(self, graphics: Graphics) -> None:
        self.tree_type.draw(graphics, self._x, self._y)


class TreeFactory:
    """
    Factory that create cached and pooling Flyweight TreeType objects
    """
    tree_types_cache = {}

    @classmethod
    def get_tree_type(cls, name: str, color: Color, other_tree_data: str) -> TreeType:
        tree_type: TreeType = cls.tree_types_cache.get(name)
        if not tree_type:
            tree_type = TreeType(name, color, other_tree_data)
            cls.tree_types_cache[name] = tree_type

        return tree_type


class Forest:
    """
    Forest with we draw
    """
    def __init__(self) -> None:
        self._trees: List[Tree] = []

    def plant_tree(self, x: int, y: int, name: str, color: Color, other_tree_data: str) -> None:
        tree_type: TreeType = TreeFactory.get_tree_type(name, color, other_tree_data)
        tree: Tree = Tree(x, y, tree_type)
        self._trees.append(tree)

    def paint(self, graphics: Graphics) -> None:
        for tree in self._trees:
            tree.draw(graphics)


class Demo:
    CANVAS_SIZE = 500
    TREES_TO_DRAW = 1000000
    TREE_TYPES = 2

    def run(self) -> None:
        forest: Forest = Forest()

        for _ in range(1, self.TREES_TO_DRAW):
            forest.plant_tree(
                randint(0, self.CANVAS_SIZE),
                randint(0, self.CANVAS_SIZE),
                'Summer Oak',
                Color.GREEN,
                'Oak texture stub',
            )
            forest.plant_tree(
                randint(0, self.CANVAS_SIZE),
                randint(0, self.CANVAS_SIZE),
                'Autumn Oak',
                Color.ORANGE,
                'Autum Oak texture stub',
            )

        graphics = Graphics()
        forest.paint(graphics)

        print(f'{self.TREES_TO_DRAW} trees drawn')
        print('----------------')
        print('Memory usage:')
        print(f'Tree size (8 bytes) * {self.TREES_TO_DRAW}')
        print(f'+ TreeTypes size (~30 bytes) * {self.TREE_TYPES}')
        print('----------------')
        
        # TREES_TO_DRAW has 8 bytes each

        # TREE_TYPES has 30 bytes each, there will be only 2 shareable flyweight objects
        # this is done by: self.TREE_TYPES * 30

        # the mathematical expression is ((1000000 * 8) + (2 * 30)) / 1024 / 1204
        new_total: int = (self.TREES_TO_DRAW * 8 + self.TREE_TYPES * 30) / 1024 / 1024

        # TREES_TO_DRAW has 38 bytes each, it's equal the SUM of (extrinsic + instrinsic) data
        # because flyweight does not exist in this context

        # the mathematical expression is (1000000 * 38) / 1024 / 1204
        old_total: int = (self.TREES_TO_DRAW * 38) / 1024 / 1024
        
        print(f'Total: {new_total} MB (instead of {old_total} MB)')


demo: Demo = Demo()
demo.run()