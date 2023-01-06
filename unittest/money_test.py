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
        self.assertEquals('7,000.00000',
            money.to_string(700000000000, Currency('USD')))

    def test_to_long_string(self):
        self.assertEquals('2,000.00000 EUR',
            money.to_long_string(20