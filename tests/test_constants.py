import unittest

from pysha256.constants import compute_n_first_primes, compute_sha256_constants, get_first_bits_of_dec_part


class TestConstants(unittest.TestCase):

    def test_get_first_bits_of_dec_part(self):
        self.assertEqual(get_first_bits_of_dec_part(5.1, 8), 25)  # 0.1 * 256 = 25.6 -> 25
        self.assertEqual(get_first_bits_of_dec_part(5 / 3, 10), 1706)

    def test_compute_n_first_primes(self):
        eight_first_primes = [2, 3, 5, 7, 11, 13, 17, 19]
        for p1, p2 in zip(eight_first_primes, compute_n_first_primes(8)):
            self.assertEqual(p1, p2)

    def test_compute_sha256_constants(self):
        constants, initial_working_variables = compute_sha256_constants()
        self.assertIsInstance(constants, tuple)
        self.assertIsInstance(initial_working_variables, tuple)
        self.assertEqual(len(constants), 64)
        self.assertEqual(len(initial_working_variables), 8)
        first_8_constants = ["428a2f98", "71374491", "b5c0fbcf", "e9b5dba5", "3956c25b", "59f111f1", "923f82a4",
                             "ab1c5ed5"]
        first_8_constants = tuple(map(lambda x: int(x, base=16), first_8_constants))
        self.assertEqual(first_8_constants, constants[:8])


if __name__ == '__main__':
    unittest.main()
