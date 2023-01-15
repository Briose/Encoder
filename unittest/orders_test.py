
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
        self.assertEquals(3, orders.size())

    def test_grouping(self):

        orders = Orders(self.market, Market.TYPE_ASK, 0.6)

        # group 0
        self.market.depth_ask(0.0, 1)
        # group 1
        self.market.depth_ask(0.1, 1)
        self.market.depth_ask(0.3, 1)
        self.market.depth_ask(0.6, 1)
        self.assertEquals(2, orders.size())
        self.assertEquals(to_money(3), orders.get_volume(1))

        # group 2
        self.market.depth_ask(1.1, 1)
        self.market.depth_ask(1.2, 1)
        self.assertEquals(3, orders.size())

        # remove group 2
        self.market.depth_ask(1.1, 0)
        self.market.depth_ask(1.2, 0)
        self.assertEquals(2, orders.size())

    def test_no_grouping(self):

        orders = Orders(self.market, Market.TYPE_ASK)

        self.market.depth_ask(0.00000000, 1)
        self.market.depth_ask(0.00000001, 1)
        self.market.depth_ask(0.00000002, 1)

        self.assertEquals(3, orders.size())

    def test_grouping_price(self):

        orders = Orders(self.market, Market.TYPE_ASK, 1)

        # group 0
        self.market.depth_ask(120.0, 1)
        # group 1
        self.market.depth_ask(120.4, 1)
        self.market.depth_ask(121.0, 1)
        # group 2
        self.market.depth_ask(121.8, 1)

        self.assertEquals(to_money(120.0), orders.get_price(0))
        self.assertEquals(to_money(121.0), orders.get_price(1))
        self.assertEquals(to_money(122.0), orders.get_price(2))

    def test_remove_empty(self):

        orders = Orders(self.market, Market.TYPE_ASK, 1)

        self.market.depth_ask(120, 20)
        self.assertEquals(1, orders.size())

        self.market.depth_ask(120, 0)
        self.assertEquals(0, orders.size())

    def test_total(self):

        orders = Orders(self.market, Market.TYPE_ASK)

        self.market.depth_ask(10, 3)