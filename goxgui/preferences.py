
import utilities

from ConfigParser import RawConfigParser
from os import path
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QDialogButtonBox
from ui.preferences_ import Ui_Preferences
from PyQt4 import QtGui
from currency import Currency


class Preferences(QDialog):
    '''
    Represents the application preferences.
    '''

    CURRENCY_INDEX_BASE = 1
    CURRENCY_INDEX_QUOTE = 2

    ORDERS_COLUMN_PRICE = 0
    ORDERS_COLUMN_SIZE = 1
    ORDERS_COLUMN_TOTAL_SIZE = 2
    ORDERS_COLUMN_QUOTE = 3
    ORDERS_COLUMN_TOTAL_QUOTE = 4

    __PASSPHRASE = 'fffuuuuuuu'
    __FILENAME = 'goxgui.ini'
    __SECTION_GLOBAL = 'Global'

    def __init__(self):
        QDialog.__init__(self)

        # set up ui
        self.__ui = Ui_Preferences()
        self.__ui.setupUi(self)

        # improve ui on mac
        if utilities.platform_is_mac():
            self.__adjust_for_mac()

        # connect ui signals to logic
        self.__ui.lineEditKey.textChanged.connect(
            self.__slot_validate_credentials)
        self.__ui.lineEditSecret.textChanged.connect(
            self.__slot_validate_credentials)

        # initialize config parser
        self.__configparser = RawConfigParser({
            'grouping': '0.0',
            'currency_{}'.format(Preferences.CURRENCY_INDEX_BASE): 'BTC',
            'currency_{}'.format(Preferences.CURRENCY_INDEX_QUOTE): 'USD',
            'orders_column_{}'.format(Preferences.ORDERS_COLUMN_PRICE): 'True',
            'orders_column_{}'.format(Preferences.ORDERS_COLUMN_SIZE): 'True',
            'orders_column_{}'.format(Preferences.ORDERS_COLUMN_QUOTE): 'False', # @IgnorePep8
            'orders_column_{}'.format(Preferences.ORDERS_COLUMN_TOTAL_SIZE): 'True',
            'orders_column_{}'.format(Preferences.ORDERS_COLUMN_TOTAL_QUOTE): 'False', # @IgnorePep8
            'key': '',
            'secret': '',
            'proposed_pips': '0'
        })

        # load config file (if exists)
        if path.isfile(self.__FILENAME):
            self.__load()
        else:
            self.__configparser.add_section(self.__SECTION_GLOBAL)
            self.__save()

        self.set_fiat_currencies([])

    # start slots

    def __slot_validate_credentials(self):

        key = str(self.__ui.lineEditKey.text())
        secret = str(self.__ui.lineEditSecret.text())

        # empty credentials are allowed
        if key == '' and secret == '':
            self.__enable_ok()
            return

        try:
            utilities.assert_valid_key(key)
        except Exception as e:
            self.__disable_ok('Invalid key.'.format(str(e)))
            return

        try:
            utilities.assert_valid_secret(secret)
        except Exception as e:
            self.__disable_ok('Invalid secret.'.format(str(e)))
            return

        self.__enable_ok()

    # end slots

    # start private methods

    def __get_fiat_currency_index(self, other):
        '''
        Returns the index of the given currency in the
        fiat currency list.
        '''
        index = 0
        for currency in self.__fiat_currencies:
            if currency == other:
                return index
            index += 1
        raise Exception('Currency {} not found.'.format(other.symbol))

    def __load_to_gui(self):
        self.__ui.doubleSpinBoxGrouping.setValue(self.get_grouping())
        self.__ui.lineEditKey.setText(self.get_key())
        self.__ui.lineEditSecret.setText(self.get_secret())
        quoteCurrency = self.get_currency(Preferences.CURRENCY_INDEX_QUOTE)
        index = self.__get_fiat_currency_index(quoteCurrency)
        self.__ui.comboBoxCurrency.setCurrentIndex(index)
        self.__set_status('')
        self.__ui.checkBoxPrice.setChecked(self.is_orders_column_enabled(
            Preferences.ORDERS_COLUMN_PRICE))
        self.__ui.checkBoxSize.setChecked(self.is_orders_column_enabled(