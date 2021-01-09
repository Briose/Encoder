
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

    # price, size
    signal_ask = pyqtSignal(object, object)

    # list of [price, size]
    signal_asks = pyqtSignal(object)

    # bid, ask
    signal_ticker = pyqtSignal(object, object)

    # price, size, type
    signal_trade = pyqtSignal(object, object, object)

    def __init__(self, preferences):
        QObject.__init__(self)
        self.__key = ''
        self.__secret = ''
        self.__preferences = preferences
        self.__preferences.set_fiat_currencies(Market.__FIAT_CURRENCIES)

    def __create_gox(self):

        # these settings are currently recommended by prof7bit
        goxapi.FORCE_PROTOCOL = 'websocket'
        goxapi.FORCE_HTTP_API = 'True'

        # initialize config from our preferences
        config = goxapi.GoxConfig("goxtool.ini")
        config.set('gox', 'quote_currency',
            self.__preferences.get_currency(
                Preferences.CURRENCY_INDEX_QUOTE).symbol)
        config.save()

        # initialize secret from our preferences
        secret = goxapi.Secret(config)
        secret.key = self.__preferences.get_key()
        secret.secret = self.__preferences.get_secret()
        gox = goxapi.Gox(secret, config)

        # connect to gox' signals
        gox.signal_debug.connect(self.__slot_log)
        gox.signal_wallet.connect(self.__slot_wallet_changed)
        gox.signal_orderlag.connect(self.__slot_orderlag)
        gox.signal_userorder.connect(self.__slot_userorder)
        gox.orderbook.signal_fulldepth_processed.connect(self.__slot_fulldepth)
        gox.signal_depth.connect(self.__slot_depth)
        gox.signal_ticker.connect(self.__slot_ticker)
        gox.signal_trade.connect(self.__slot_trade)

        return gox

    # start private methods

    def __get_currency_shift(self, index):
        '''
        Retrieves the difference in decimal places between the
        external representation (i.e. market) and the
        internal representation (i.e. application).
        '''
        symbol = self.__preferences.get_currency(index).symbol

        if symbol in Market.__SHIFT:
            return Market.__SHIFT[symbol]

        # the default shift is 3
        return 3

    def __to_internal(self, index, value):