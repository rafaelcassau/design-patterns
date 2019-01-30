"""
Define a family of algorithms,
encapsulate each one, and make them
interchangeable. Strategy lets the
algorithm vary independently from
the clients that use it.
"""
from typing import List, Tuple


class PrimeFinder:

    def __init__(self) -> None:
        self._primes: List[int] = []

    def calculate(self, limit: int) -> None:
        """ Will calculate all the primes below limit. """
        raise NotImplementedError()

    def out(self) -> None:
        """ Prints the list of primes prefixed with which algorithm made it """
        print(self.__class__.__name__)
        for prime in self._primes:
            print(prime)


class HardcodedPrimeFinder(PrimeFinder):

    def calculate(self, limit: int) -> None:
        _hardcoded_primes: Tuple[int] = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
        for prime in _hardcoded_primes:
            if prime < limit:
                self._primes.append(prime)


class StandardPrimeFinder(PrimeFinder):

    def calculate(self, limit: int) -> None:
        self._primes: List[int] = [2]
        # check only odd numbers
        for _number in range(3, limit, 2):
            _is_prime: bool = True
            
            for _prime in self._primes:
                if _number % _prime == 0:
                    _is_prime = False
                    break

            if _is_prime:
                self._primes.append(_number)


class PrimeFinderClient:

    def __init__(self, limit: int) -> None:
        self._limit = limit
        if limit <= 50:
            self._finder = HardcodedPrimeFinder()
        else:
            self._finder = StandardPrimeFinder()

    def get_primes(self) -> None:
        self._finder.calculate(self._limit)
        self._finder.out()


prime_finder_client: PrimeFinderClient = PrimeFinderClient(50)
prime_finder_client.get_primes()

prime_finder_client: PrimeFinderClient = PrimeFinderClient(100)
prime_finder_client.get_primes()
