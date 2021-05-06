
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