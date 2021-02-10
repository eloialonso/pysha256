import unittest

from pysha256.fixed_size_int import FixedSizeInt


class TestFixedSizeInt(unittest.TestCase):

    def test_bin(self):
        a = FixedSizeInt(23, n_bits=15)
        self.assertEqual(a.bin(), "000000000010111")
        self.assertEqual(a.bin(n_bits=6), "010111")

    def test_hex(self):
        a = FixedSizeInt(58, n_bits=16)
        self.assertEqual(a.hex(), "003a")
        self.assertEqual(a.hex(n_hexits=6), "00003a")

    def test_right_rotation(self):
        a = FixedSizeInt(19, n_bits=8)
        self.assertEqual(a.right_rotation(0), 19)
        self.assertEqual(a.right_rotation(1), 137)
        self.assertEqual(a.right_rotation(2), 196)
        self.assertEqual(a.right_rotation(8), 19)

    def test_right_shift(self):
        a = FixedSizeInt(19, n_bits=5)
        self.assertEqual(a >> 1, 9)
        self.assertEqual(a >> 1 >> 1, 4)
        self.assertEqual(a >> 3, 2)
        self.assertEqual(a >> 4, 1)
        self.assertEqual(a >> 5, 0)
        self.assertEqual(a >> 157, 0)

    def test_add(self):
        a = FixedSizeInt(200, n_bits=8)
        b = FixedSizeInt(100, n_bits=8)
        self.assertEqual(a + b, 44)


if __name__ == '__main__':
    unittest.main()
