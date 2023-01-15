
import unittest
from orders import Orders
from money import to_money
from market import Market
from market_mock import MarketMock


class Test(unittest.TestCase):

    def setUp(self):
        self.market = MarketMock()

    def test_size(self):

        orders = Orders(self.market, Market.TYPE_ASK, 1)

        # group 0
        self.market.depth_ask(120.0, 1)
        self.assertEquals(1, orders.size())

        # group 1
        self.market.depth_ask(120.1, 1)
        self.assertEquals(2, orders.size())

        # group 1
        self.market.depth_ask(120.9, 1)
        self.assertEquals(2, orders.size())

        # group 1
        self.market.depth_ask(121.0, 1)
        self.assertEquals(2, orders.size())

        # group 2
        self.market.depth_ask(122.0, 1)