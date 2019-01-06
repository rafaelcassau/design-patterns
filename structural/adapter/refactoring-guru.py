"""
Adapter is a structural design pattern, which allows
imcompatible objects to collaborate.

Adapter acts as a wrapper between two objects,
it catches calls for one object and transforms them
to format and interface recognizable by the second
object.
"""
import math


class RoundPeg:
    """
    RoundPegs are compatible with RoundRoles.
    """
    __radius: float = None

    def __init__(self, radius: float) -> None:
        self.__radius = radius

    def get_radius(self) -> float:
        return self.__radius


class RoundHole:
    """
    RoundHoles are compatible with RoundPegs.
    """
    __radius: float = None

    def __init__(self, radius: float) -> None:
        self.__radius = radius

    def get_radius(self) -> float:
        return self.__radius

    def fits(self, round_peg: RoundPeg) -> bool:
        return self.get_radius() >= round_peg.get_radius()


class SquarePeg:
    """
    SquarePegs are not compatible with RoundHoles (they were
    implemented by previous development team). But we have to
    integrate them into our program.
    """
    __width: float = None

    def __init__(self, width: float) -> None:
        self.__width = width

    def get_width(self) -> float:
        return self.__width

    def get_square(self) -> float:
        return self.__width ** 2


class SquarePegAdapter(RoundPeg):
    """
    Adapter allows fitting square pegs into round holes.
    """
    __square_peg : SquarePeg = None

    def __init__(self, square_peg: SquarePeg) -> None:
        self.__square_peg = square_peg

    def get_radius(self) -> float:
        """
        Calculate a minimum circle radius, which can fit this peg.
        """
        result: float = self.__square_peg.get_width() / 2
        result = math.pow(result, 2) * 2
        result = math.sqrt(result)
        return result


class Demo:
    """
    Somewhere in client code...
    """
    def run(self):
        """
        Round fits round, no surpise.
        """
        round_hole: RoundHole = RoundHole(5)
        round_peg: RoundPeg = RoundPeg(5)

        if round_hole.fits(round_peg):
            print('Round peg r5 fits round hole r5.')

        small_square_peg: SquarePeg = SquarePeg(2)
        large_square_peg: SquarePeg = SquarePeg(20)
        # round_role.fits(small_square_peg) Won't compile.

        """
        Adapter solves the problem.
        """
        small_square_peg_adaper: SquarePegAdapter = SquarePegAdapter(small_square_peg)
        large_square_peg_adapter: SquarePegAdapter = SquarePegAdapter(large_square_peg)

        if round_hole.fits(small_square_peg_adaper):
            print('Square peg w2 fits round hole r5.')

        if not round_hole.fits(large_square_peg_adapter):
            print('Square peg w20 does not fit into round hole r5.')


demo = Demo()
demo.run()