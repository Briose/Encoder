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
    __COLOR_B