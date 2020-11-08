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