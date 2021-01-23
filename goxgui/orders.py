from PyQt4.QtCore import QObject, pyqtSignal
from level import Level
from market import Market
import money


class Orders(QObject):
    '''
    Represents a collection of ask or bid orders, grouped by levels.
    '''

    signal_changed = pyqtSignal()

    def __init__(self, market, typ, grouping=0):
      