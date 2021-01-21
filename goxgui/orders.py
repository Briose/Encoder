from PyQt4.QtCore import QObject, pyqtSignal
from level import Level
from market import Market
import money


class Orders(QObject):
    '''
    Represents a collection of 