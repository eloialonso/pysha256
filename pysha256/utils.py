"""
Utility function to do rotation, choice, etc on bits.
"""

from .fixed_size_int import FixedSizeInt


def cast_args_to_fixed_size_int_32(func):
    def wrapper(*numbers):
        casted_numbers = []
        for number in numbers:
            if isinstance(number, int):
                number = FixedSizeInt(value=number, n_bits=32)
            if number.n_bits != 32:
                number = FixedSizeInt(value=number.value, n_bits=32)
            casted_numbers.append(number)
        return func(*casted_numbers)

    return wrapper


@cast_args_to_fixed_size_int_32
def sigma0(n):
    return n.right_rotation(7) ^ n.right_rotation(18) ^ (n >> 3)


@cast_args_to_fixed_size_int_32
def sigma1(n):
    return n.right_rotation(17) ^ n.right_rotation(19) ^ (n >> 10)


@cast_args_to_fixed_size_int_32
def Sigma0(n):
    return n.right_rotation(2) ^ n.right_rotation(13) ^ n.right_rotation(22)


@cast_args_to_fixed_size_int_32
def Sigma1(n):
    return n.right_rotation(6) ^ n.right_rotation(11) ^ n.right_rotation(25)


@cast_args_to_fixed_size_int_32
def choice(x, y, z):
    """Use x to choose bits from y or z (1: y, 0: z)"""
    return (x & y) ^ (~x & z)


@cast_args_to_fixed_size_int_32
def majority(x, y, z):
    """Bitwise majority of x, y, and z"""
    return (x & y) ^ (y & z) ^ (z & x)
