"""
Visitor is behavioral design pattern that
allows adding new behaviors to existing class
hierarchy without altering any existing code.
"""
import typing


class Shape:

    def move(self, x: int, y: int) -> None: raise NotImplementedError()
    def draw(self) -> None: raise NotImplementedError()
    def accept(self, visitor: "Visitor") -> str: raise NotImplementedError()


class Dot(Shape):

    def __init__(self, id_: int, x: int, y: int) -> None:
        self._id = id_
        self._x = x
        self._y = y

    def accept(self, visitor: "Visitor"):
        # double dispach
        return visitor.visit_dot(self)

    def move(self, x: int, y: int) -> None:
        print('Dot moved!')

    def draw(self) -> None:
        print('Dot drawn!')

    def get_id(self) -> None:
        return self._id

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y


class Circle(Shape):

    def __init__(self, id_: int, x: int, y: int, radius: int) -> None:
        self._id = id_
        self._x = x
        self._y = y
        self._radius = radius

    def accept(self, visitor: "Visitor") -> str:
        # double dispach
        return visitor.visit_circle(self)

    def move(self, x: int, y: int) -> None:
        print('Circle moved!')

    def draw(self) -> None:
        print('Circle drawn!')

    def get_id(self) -> None:
        return self._id

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def get_radius(self) -> int:
        return self._radius


class Rectangle(Shape):

    def __init__(self, id_: int, x: int, y: int, width: int, height: int) -> None:
        self._id = id_
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def accept(self, visitor: "Visitor") -> str:
        # double dispach
        return visitor.visit_rectangle(self)

    def move(self, x: int, y: int) -> None:
        print('Rectangle moved!')

    def draw(self) -> None:
        print('Rectangle drawn!')

    def get_id(self) -> None:
        return self._id

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def get_width(self) -> int:
        return self._width

    def get_height(self) -> int:
        return self._height


class CompoundShape(Shape):

    def __init__(self, _id: int) -> None:
        self._id = _id
        self._children: typing.List[Shape] = []

    def accept(self, visitor: "Visitor") -> str:
        # double dispach
        return visitor.visit_compound_shape(self)

    def move(self, x: int, y: int) -> None:
        print('CompoundShape moved!')

    def draw(self) -> None:
        print('CompoundShape drawn!')

    def get_id(self) -> None:
        return self._id

    def add(self, shape: Shape) -> None:
        self._children.append(shape)

    def get_children(self) -> typing.List[Shape]:
        return self._children


class VisitorInterface:
    def visit_dot(self, dot: Dot) -> str: raise NotImplementedError()
    def visit_circle(self, circle: Circle) -> str: raise NotImplementedError()
    def visit_rectangle(self, rectangle: Rectangle) -> str: raise NotImplementedError()
    def visit_compound_shape(self, compound_shape: CompoundShape) -> str: raise NotImplementedError()


class ExportXMLVisitor(VisitorInterface):

    def export(self, *shapes: Shape) -> None:
        _xml: str = ''
        for shape in shapes:
            _xml += '<?xml version=\"1.0\" encoding=\"utf-8\"?>" + "\n'
            _xml += shape.accept(self) + '\n'
        return _xml

    def visit_dot(self, dot: Dot) -> str:
        return '<dot>\n' + \
               '    <id>' + str(dot.get_id()) + '</id>\n' + \
               '    <x>' + str(dot.get_x()) + '</x>\n' + \
               '    <y>' + str(dot.get_y()) + '</y>\n' + \
               '</dot>'
    
    def visit_circle(self, circle: Circle) -> str:
        return '<circle>\n' + \
                '    <id>' + str(circle.get_id()) + '</id>\n' + \
                '    <x>' + str(circle.get_x()) + '</x>\n' + \
                '    <y>' + str(circle.get_y()) + '</y>\n' + \
                '    <radius>' + str(circle.get_y()) + '</radius>\n' + \
                '</circle>'

    def visit_rectangle(self, rectange: Rectangle) -> str:
        return '<rectangle>\n' + \
                '    <id>' + str(rectange.get_id()) + '</id>\n' + \
                '    <x>' + str(rectange.get_x()) + '</x>\n' + \
                '    <y>' + str(rectange.get_y()) + '</y>\n' + \
                '    <width>' + str(rectange.get_width()) + '</width>\n' + \
                '    <height>' + str(rectange.get_height()) + '</height>\n' + \
                '</rectangle>'

    def visit_compound_shape(self, compound_shape: CompoundShape) -> str:
        return '<compound_shape>\n' + \
                '    <id>' + str(compound_shape.get_id()) + '</id>\n' + \
                        self._visit_compound_shape(compound_shape) + \
                '</compound_shape>'

    def _visit_compound_shape(self, compound_shape: CompoundShape) -> str:
        _xml: str = ''
        for child in compound_shape.get_children():
            _child_xml: str = child.accept(self)
            # Proper identation for sub-objects.
            _child_xml = '    ' + _child_xml.replace('\n', '\n    ') + '\n'
            _xml += _child_xml
        return _xml


class Demo:

    def run(self) -> None:
        # create base shapes
        _dot: Dot = Dot(1, 10, 55)
        _circle: Circle = Circle(2, 23, 15, 10)
        _rectangle: Rectangle = Rectangle(3, 10, 17, 20, 30)

        # create a compound shape and add base shapes inside there
        _first_compound_shape: CompoundShape = CompoundShape(4)
        _first_compound_shape.add(_dot)
        _first_compound_shape.add(_circle)
        _first_compound_shape.add(_rectangle)

        # create a second compound shape and add dot inside there
        _second_compound_shape: CompoundShape = CompoundShape(5)
        _second_compound_shape.add(_dot)

        # add the second compound shape inside the first compound shape
        _first_compound_shape.add(_second_compound_shape)

        _exporter: ExportXMLVisitor = ExportXMLVisitor()
        _exported_shapes_as_xml = _exporter.export(_circle, _first_compound_shape)

        print(_exported_shapes_as_xml)


demo: Demo = Demo()
demo.run()
