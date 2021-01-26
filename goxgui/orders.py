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

        i