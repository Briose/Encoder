
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
        Currency('CAD'),
        Currency('GBP'),
        Currency('CHF'),
        Currency('RUB'),
        Currency('AUD'),
        Currency('SEK'),
        Currency('DKK'),
        Currency('HKD'),
        Currency('PLN'),
        Currency('CNY'),
        Currency('SGD'),
        Currency('THB'),
        Currency('NZD'),
        Currency('NOK'),
        Currency('CZK'),
        ]

    # how currencies have to be shifted in terms of decimal places
    # between the market and the internal representation
    __SHIFT = {
        'BTC': 0,
        'JPY': 5,
        'SEK': 5,
        }

    # these constants mark the type of orders, trades etc
    TYPE_BID = 0
    TYPE_ASK = 1

    # we're using objects as paramters for the signals,
    # because long integers will cause type errors
    # (with both type long and type 'long long')

    # log message
    signal_log = pyqtSignal(str)

    # none
    signal_wallet = pyqtSignal()

    # milliseconds
    signal_orderlag = pyqtSignal(object, str)

    # price, size, order type, order id, status
    signal_userorder = pyqtSignal(object, object, str, str, str)

    # price, size
    signal_bid = pyqtSignal(object, object)

    # list of [price, size]
    signal_bids = pyqtSignal(object)