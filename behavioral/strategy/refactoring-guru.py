"""
Strategy is a behavioral design pattern that
turns a set of behaviors into objects and makes
them interchangeable inside original context object.

The original object, called context, holds a reference
to a strategy object and delegates it executing the
behavior. In order to change the way the context performs
its work, other objects may replace currently linked
strategy object with another one.
"""
from typing import Dict


class CreditCard:

    def __init__(self, number: int, date: str, cvv: str) -> None:
        self._amount: int = 100_000
        self._number = number
        self._date = date
        self._cvv = cvv

    def get_amount(self) -> int:
        return self._amount

    def set_amount(self, amount: int) -> None:
        self._amount = amount


class Order:
    """
    Order class. Doesn't know the concrete payment method (strategy) user has
    picked. It users common strategy interface to delegate collecting payment data
    to strategy object. It can be used to save order to database.
    """
    def __init__(self):
        self._total_cost: int = 0
        self._is_closed: bool = False

    def process_order(self, strategy: "PayStrategy") -> None:
        strategy.collect_payment_details()
        # Here we could collect and store payment data from the strategy.

    def set_total_cost(self, cost: int) -> None:
        self._total_cost += cost

    def get_total_cost(self) -> int:
        return self._total_cost

    def set_closed(self) -> None:
        self._is_closed = True

    def is_closed(self) -> bool:
        return self._is_closed


class PayStrategy:
    """ Common interface for all strategies. """

    def collect_payment_details(self) -> None:
        raise NotImplementedError()

    def pay(self, payment_amount: int) -> bool:
        raise NotImplementedError()


class PayByPayPal(PayStrategy):
    """ Concrete strategy. Implements PayPal payment method. """

    def __init__(self) -> None:
        self._email: str = ''
        self._password: str = ''
        self._signed_in: bool = False

        self.DATABASES: Dict[str, str] = {
            'amanda1985': 'amanda@ya.com',
            'qwerty': 'jonh@amazon.eu'
        }

    def collect_payment_details(self) -> None:
        """ Collect customer's data """

        while not self._signed_in:
            self._email: str = input("Enter the user's email: ")
            self._password: str = input("Enter the password: ")
            if self.verify():
                print("Data verification has been successful.")
            else:
                print("Wrong email or password!")

    def pay(self, payment_amount: int) -> bool:
        """ Save customer data for future shopping attempts. """

        if self._signed_in:
            print(f'Paying {payment_amount} using PayPal.')
            return True
        else:
            return False

    def verify(self) -> bool:
        _verified: bool = self._email == self.DATABASES.get(self._password)
        self.set_signed_in(_verified)
        return self._signed_in

    def set_signed_in(self, signed_in: bool) -> None:
        self._signed_in = signed_in


class PayByCreditCard(PayStrategy):
    """ Concrete strategy. Implements credit card payment method. """

    def __init__(self):
        self._card: CreditCard = None

    def collect_payment_details(self) -> None:
        """ Collect credit card data. """

        _number: int = int(input("Enter the card number: "))
        _date: str = input("Enter the card expiration date 'mm/yy': ")
        _cvv: str = input("Enter the cvv code: ")

        self._card = CreditCard(_number, _date, _cvv)

    def pay(self, payment_amount: int) -> bool:
        """ After card validation we can charge customer's credit card """

        if self.card_is_present():
            print(f'Paying {payment_amount} using Credit Card.')
            _balance: int = self._card.get_amount() - payment_amount
            self._card.set_amount(_balance)
            return True
        else:
            return False

    def card_is_present(self) -> bool:
        return self._card != None


class Demo:
    """ World first console e-commerce application """

    def __init__(self):
        self._PRICES_ON_PRODUCTS: Dict[int, int] = {1: 2200, 2: 1850, 3: 1100, 4: 890,}
        self._order: Order = Order()
        self._strategy: PayStrategy = None

    def run(self):
        while not self._order.is_closed():
            _cost: int = 0
            _count: int = 0
            _continue_choice_shopping: str = 'C'
            _continue_choice_products: str = 'Y'
            _payment_method_choice: int = 0

            while _continue_choice_products == 'Y':
                print(_continue_choice_products)
                print("Please, select a product: ")
                print("1 - Mother board")
                print("2 - CPU")
                print("3 - HDD")
                print("4 - Memory")

                _choice: int = int(input('Enter your choice here: '))
                _cost = self._PRICES_ON_PRODUCTS.get(_choice)
                _count: int = int(input("Count: "))
                
                self._order.set_total_cost(_count * _cost)
                _continue_choice_products: str = input("Do you wish to continue selecting products? Y/N: ")

            print("Please, select the payment method: ")
            print("1 - PayPal")
            print("2 - Credit Card")
            _payment_method_choice: int = int(input('Enter your choice here: '))

            # Client creates different strategies based on input from user,
            # application configuration, etc.
            if _payment_method_choice == 1:
                self._strategy = PayByPayPal()
            else:
                self._strategy = PayByCreditCard()

            # Order object delegates gathering payment data to strategy
            # object, since only strategies know what data they need to
            # process a payment.
            self._order.process_order(self._strategy)

            _continue_choice_shopping: str = input(f"Pay {self._order.get_total_cost()} units or Continue shopping? P/C: ")
            if _continue_choice_shopping == 'P':
                # Finally, strategy handles the payment.
                if self._strategy.pay(self._order.get_total_cost()):
                    print('Payment has been successful.')
                else:
                    print('FAIL! Please, check your data.')

                self._order.set_closed()


demo: Demo = Demo()
demo.run()