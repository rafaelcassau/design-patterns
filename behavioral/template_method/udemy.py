"""
Define the skeleton of an algorithm,
deferring some steps to client
subclasses. Let subclasses redefine
certain steps of an algorithm without
changing the algorithm's structure.
"""


class MakeMeal:

    def __init__(self) -> None:
        self._cost: float = 0

    def buy_ingredients(self, money: float) -> None:
        if money < self._cost:
            assert 0, "Not enough money to buy ingredients!" 

    def prepare(self) -> None:
        raise NotImplementedError()

    def cook(self) -> None:
        raise NotImplementedError()

    def go(self, money: float) -> None:
        self.buy_ingredients(money)
        self.prepare()
        self.cook()


class MakePizza(MakeMeal):

    def __init__(self) -> None:
        self._cost: float = 3

    def prepare(self) -> None:
        print('Prepare Pizza - make a dough and add toppings.')

    def cook(self) -> None:
        print('Cook Pizza - cook in the oven on gas mark 8 for 10 minutes.')


class MakeCake(MakeMeal):

    def __init__(self) -> None:
        self._cost: float = 2

    def prepare(self) -> None:
        print('Prepare Cake - mix ingredients together and pour into a cake tin.')

    def cook(self) -> None:
        print('Cook Cake - bake in the oven on gas mark 6 to 20 minutes.')


pizza_maker: MakePizza = MakePizza()
pizza_maker.go(5)

cake_maker: MakeCake = MakeCake()
cake_maker.go(5)
