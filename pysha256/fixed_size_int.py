"""
Class to work in Z/nZ with n = 2 ** k.
"""


class FixedSizeInt:
    class Decorators:

        @classmethod
        def cast_other(cls, func):
            def wrapper(self, other):
                assert isinstance(self, FixedSizeInt)
                if isinstance(other, int):
                    other = FixedSizeInt(value=other, n_bits=self.n_bits)
                assert isinstance(other, FixedSizeInt)
                assert self.n_bits == other.n_bits
                return func(self, other)

            return wrapper

    def __init__(self, value=0, n_bits=32):
        self._n_bits = n_bits
        self.value = value

    @property
    def n_bits(self):
        return self._n_bits

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value & (2 ** self.n_bits - 1)

    def __repr__(self):
        return repr(self.value)

    @Decorators.cast_other
    def __eq__(self, other):
        return (self.value == other.value)

    @Decorators.cast_other
    def __add__(self, other):
        new_value = self.value + other.value
        return FixedSizeInt(value=new_value, n_bits=self.n_bits)

    @Decorators.cast_other
    def __mul__(self, other):
        new_value = self.value * other.value
        return FixedSizeInt(value=new_value, n_bits=self.n_bits)

    @Decorators.cast_other
    def __rshift__(self, other):
        new_value = self.value >> other.value
        return FixedSizeInt(value=new_value, n_bits=self.n_bits)

    @Decorators.cast_other
    def __lshift__(self, other):
        new_value = self.value << other.value
        return FixedSizeInt(value=new_value, n_bits=self.n_bits)

    @Decorators.cast_other
    def __or__(self, other):
        new_value = self.value | other.value
        return FixedSizeInt(value=new_value, n_bits=self.n_bits)

    @Decorators.cast_other
    def __and__(self, other):
        new_value = self.value & other.value
        return FixedSizeInt(value=new_value, n_bits=self.n_bits)

    @Decorators.cast_other
    def __xor__(self, other):
        new_value = self.value ^ other.value
        return FixedSizeInt(value=new_value, n_bits=self.n_bits)

    def __invert__(self):
        new_value = ~self.value
        return FixedSizeInt(value=new_value, n_bits=self.n_bits)

    def __radd__(self, other):
        return self + other

    def right_rotation(self, d=1):
        return (self >> d) | (self << (self.n_bits - d))

    def bin(self, n_bits=None):
        n_bits = n_bits if n_bits is not None else self.n_bits
        return "{0:0{1}b}".format(self.value, n_bits)

    def hex(self, n_hexits=None):
        if n_hexits is None:
            assert self.n_bits % 4 == 0
            n_hexits = self.n_bits // 4
        return "{0:0{1}x}".format(self.value, n_hexits)
