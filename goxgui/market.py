
from PyQt4.QtCore import QObject, pyqtSignal
from currency import Currency
from preferences import Preferences
import goxapi
import time


class Market(QObject):
    '''
    Wrapper for gox object used to decouple gui code
    from market implementation.
    '''

    # all available fiat currencies for this market
    __FIAT_CURRENCIES = [
        Currency('USD'),
        Currency('EUR'),
        Currency('JPY'),