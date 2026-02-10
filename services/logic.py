from math import gcd
from functools import reduce

def fibonacci_series(n: int):
    if n < 0:
        raise ValueError("Fibonacci input must be non-negative")

    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def filter_primes(arr: list[int]):
    return [x for x in arr if is_prime(x)]


def find_hcf(arr: list[int]):
    return reduce(gcd, arr)


def find_lcm(arr: list[int]):
    def lcm(a, b):
        return a * b // gcd(a, b)
    return reduce(lcm, arr)
