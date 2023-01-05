import unittest
from currency import Currency
import money


class Test(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(1000000000,
            money.multiply(200000000, 500000000))

    def test_divide(self):
        self.assertEqual(200000000,
            money.divide(1000000000, 500000000))

    def test_to_string(self):
        self.assertEqual