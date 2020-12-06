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
#         self.__set_color(1, 0, self.__COLOR_BALANCE)
#         self.__set_color(1, 1, self.__COLOR_BALANCE)

        self.__set_data(0, 2, "Trading lag:")
        self.__set_color(0, 2, self.__COLOR_ORDERLAG)
        self.__set_color(0, 3, self.__COLOR_ORDERLAG)
        self.__set_color(1, 2, self.__COLOR_ORDERLAG)
        self.__set_color(1, 3, self.__COLOR_ORDERLAG)

        self.__set_data(0, 4, "Bid:")
        self.__set_data(1, 4, "Ask:")
#         self.__set_color(0, 4, self.__COLOR_BID_ASK)
#         self.__set_color(0, 5, self.__COLOR_BID_ASK)
#         self.__set_color(1, 4, self.__COLOR_BID_ASK)
#         self.__set_color(1, 5, self.__COLOR_BID_ASK)

        # listen for clicks
        signal_clicked.connect(self.__slot_clicked)

    # private methods

    def __set_data(self, row, col, text):
        self.__data[row][col] = text
        self.emit(SIGNAL("layoutChanged()"))

    def __set_color(self, row, col, color):
        self.__color[row][col] = color
        self.emit(SIGNAL("layoutChanged()"))

    def __slot_clicked(self, index):
        row = index.row()
        col = index.column()

        if row == 0 and (col == 0 or col == 1):
            self.signal_base_balance_clicked.emit()
       