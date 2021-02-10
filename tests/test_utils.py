import unittest

from pysha256.utils import choice, majority, sigma0, sigma1, Sigma0, Sigma1


class TestUtils(unittest.TestCase):

    def test_choice(self):
        x, y, z = 18, 25, 4
        self.assertEqual(choice(x, y, z), 20)

    def test_majority(self):
        x, y, z = 18, 25, 4
        self.assertEqual(majority(x, y, z), 16)

    def test_sigma0(self):
        n = 37
        self.assertEqual(sigma0(n), 1242120196)

    def test_sigma1(self):
        n = 37
        self.assertEqual(sigma1(n), 1449984)

    def test_Sigma0(self):
        n = 37
        self.assertEqual(Sigma0(n), 1093178377)

    def test_Sigma1(self):
        n = 37
        self.assertEqual(Sigma1(n), 2426409600)


if __name__ == '__main__':
    unittest.main()
