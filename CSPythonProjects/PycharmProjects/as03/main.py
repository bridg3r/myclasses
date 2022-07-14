"""
A module demonstrating generator functions and related concepts.
"""

__author__ = "A student in CSE 30, bahckort@ucsc.edu"

from collections.abc import Callable, Iterator  # For typing hints (we'll talk about "abc" later)


def elements_under(sequence: Iterator[int], bound: int, predicate: Callable[[int], bool] = None) \
      -> Iterator[int]:
    """    Yields a finite sequence of elements under a given bound, optionally matching a predicate.

    :param sequence: an infinite sequence of integers, e.g. primes()
    :param bound:  an exclusive upper bound for the yielded sequence
    :param predicate: if present, the sequence includes only values for which this function returns True
    """
    while predicate is None:
        a = next(sequence)
        if a < bound:
            yield a
        else:
            break
    b = 1
    while predicate is not None and b < bound:
        b = next(sequence)
        if (b < bound) and (predicate(b) is True):
            yield b


def is_prime(n: int) -> bool:
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True


def nth_element(sequence: Iterator[int], n: int) -> int:
    """
    Returns the nth element of a possibly infinite sequence of integers.

    :param sequence: a sequence of integers, e.g. primes()
    :param n: the sequence index desired
    :return: the value at index n of the sequence
    """
    i = 0
    while i < n + 1:
        b = next(sequence)
        i += 1
    return b


def primes() -> Iterator[int]:
    """ Yields an infinite sequence of prime numbers, in ascending order. """
    i = 1
    while True:
        i += 1
        if is_prime(i) is True:
            yield i


def prime_factors(n: int) -> list[int]:
    """ Returns a list of prime numbers with product n, in ascending order. """
    factors = []
    i = 1
    while i <= n:
        i += 1
        if n % i == 0:
            if is_prime(i) is True:
                factors.append(i)
                n = n / i
                i = 1
    return factors


def semiprimes() -> Iterator[int]:
    """ Yields an infinite sequence of semiprimes, in ascending order. """
    i = 2
    while True:
        i += 1
        b = elements_under(primes(), i)
        for j in b:
            if (i % j == 0) and (is_prime(i // j) is True):
                yield i
                break


if __name__ == '__main__':
    assert list(elements_under(primes(), 10)) == [2, 3, 5, 7]
    assert all(is_prime(n) for n in (2, 3, 5, 7))
    assert all(not is_prime(n) for n in (4, 6, 8, 9))
    assert list(elements_under(primes(), 10)) == [2, 3, 5, 7]
    assert list(elements_under(semiprimes(), 10)) == [4, 6, 9]
    assert nth_element(primes(), 2) == 5
    assert nth_element(semiprimes(), 2) == 9
    assert list(elements_under(primes(), 1386, lambda p: not 1386 % p)) == [2, 3, 7, 11]
    assert prime_factors(1386) == [2, 3, 3, 7, 11]
