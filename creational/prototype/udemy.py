"""
Specify the kinds of objects to use a prototypical instance,
and create new objects by copying this prototype.
"""

from copy import deepcopy


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return "{}, {}".format(self.x, self.y)


# client
point = Point(0, 0)
cloned_point = point.clone()

point.move(1, 1)
print(point)

cloned_point.move(2, 2)
print(cloned_point)
