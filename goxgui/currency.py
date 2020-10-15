class Currency(object):
    '''
    Represents a currency.
    '''

    # The amount of decimals is used when rendering the currency.
    # Also used to determine the size of a pip.
    # All currencies not listed here will have 5 decimals.
    __DECIMALS = {
        'BTC': 8,
        'JPY': 3,
        'SEK': 3,
        }

    def __init__(self, symbol):

        if symbol in self.__DECIMALS:
            self.__decimals = Currency.__DECIMALS[symbol]
        else:
            self.__de