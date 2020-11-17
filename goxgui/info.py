from PyQt4.QtCore import QAbstractTableModel, QVariant, Qt, SIGNAL, pyqtSignal
from PyQt4.QtGui import QColor
from preferences import Preferences
import money


class Info(QAbstractTableModel):
    '''
    Model that represents a table with various information.
    '''

    __ROWS = 2
    __COLS = 6

    __COLOR_DEFAULT = QColor(255, 255, 255)
    __COLOR_BID_ASK = QColor(240, 255, 240)
    __COLOR_BALANCE = QColor(240, 240, 255)
    __COLOR_ORDERLAG = QColor(237, 243, 254)

    signal_base_balance_clicked = pyqtSignal()
    signal_quote_balance_clicked = pyqtSignal()

    def __init__(self, parent, preferences, signal_clicked):
        QAbstractTableModel.__init__(self, parent)

        # initialize data array with empty strings
        self.__data = [['' for i in range(self.__COLS)] for j in range(self.__ROWS)]  # @UnusedVariable @IgnorePep8

        # initialize color array with default color
        self.__color = [[self.__COLOR_DEFAULT for i in range(self.__COLS)] for j in range(self.__ROWS)]  # @UnusedVariable @IgnorePep8

        self.__preferences = preferences

        # initialize non-changing cell texts and colors
        self.__set_data(0, 0, "Crypto balance:")
        self.__set_data(1, 0, "Fiat balance:")
#         self.__set_color(0, 0, self.__COLOR_BALANCE)
#         self.__set_color(0, 1, self.__COLOR_BALANCE)
#         self.__set_co