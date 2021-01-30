from PyQt4.QtCore import QObject, pyqtSignal
from level import Level
from market import Market
import money


class Orders(QObject):
    '''
    Represents a collection of ask or bid orders, grouped by levels.
    '''

    signal_changed = pyqtSignal()

    def __init__(self, market, typ, grouping=0):
        QObject.__init__(self)

        self.__typ = typ

        self.__market = market
        self.__market.signal_trade.connect(self.__slot_trade)
        self.__market.signal_ticker.connect(self.__slot_ticker)

        if typ == Market.TYPE_BID:

            self.__market.signal_bid.connect(self.__slot_depth)
            self.__market.signal_bids.connect(self.__slot_depths)
            self.__compare = lambda x, y: x > y

        elif typ == Market.TYPE_ASK:

            self.__market.signal_ask.connect(self.__slot_dept