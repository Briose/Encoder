
from PyQt4.QtCore import pyqtSignal, QObject
from money import to_money


class MarketMock(QObject):
    '''
    Mock object to simulate a market object in unit tests.
    Also used for profiling.
    '''

    # log message
    signal_log = pyqtSignal(str)