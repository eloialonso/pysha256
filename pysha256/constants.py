"""
Get constants used in SHA256.
"""

import math

from .fixed_size_int import FixedSizeInt


def get_first_bits_of_dec_part(number, n_bits=32):
    dec_part = number - math.floor(number)
    first_bits = math.floor(dec_part * (2 ** n_bits))
    return FixedSizeInt(first_bits, n_bits)


def compute_n_first_primes(n):
    def is_prime(n):
        for x in range(2, int(math.sqrt(n)) + 1):
            if n % x == 0:
                return False
        return True

    p = 2
    n_primes = 0
    while n_primes < n:
        if is_prime(p):
            n_primes += 1
            yield p
        p += 1


def compute_sha256_constants():
    first_64_cube_roots, first_8_square_roots = [], []
    for i, p in enumerate(compute_n_first_primes(64)):
        cube_root = get_first_bits_of_dec_part(p ** (1 / 3), n_bits=32)
        first_64_cube_roots.append(cube_root)
        if i < 8:
            square_root = get_first_bits_of_dec_part(p ** (1 / 2), n_bits=32)
            first_8_square_roots.append(square_root)

    return (tuple(first_64_cube_roots),
            tuple(first_8_square_roots))
