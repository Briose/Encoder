
from PyQt4.QtCore import QAbstractTableModel, QVariant, Qt, SIGNAL
from preferences import Preferences
import money
import weakref


class Model(QAbstractTableModel):
    '''
    Adapter that makes orders accessible to Qt.
    '''