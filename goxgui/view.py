
import utilities
import time
import logging
import money

from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QTextCursor
from PyQt4.QtGui import QHeaderView
from ui.main_window_ import Ui_MainWindow
from model import Model
from orders import Orders
from PyQt4 import QtGui
from preferences import Preferences
from market import Market
from info import Info


class View(QMainWindow):
    '''
    Represents the combined view / control.
    '''

    def __init__(self, preferences, market):

        QMainWindow.__init__(self)

        self.preferences = preferences
        self.market = market

        # set up main window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # improve ui on mac
        if utilities.platform_is_mac():
            self.adjust_for_mac()

        # connect market signals to our logic
        self.market.signal_log.connect(self.slot_log)
        self.market.signal_wallet.connect(self.display_wallet)
        self.market.signal_orderlag.connect(self.display_orderlag)
        self.market.signal_userorder.connect(self.display_userorder)
        self.market.signal_ticker.connect(self.update_ticker)

        # connect ui signals to our logic
        self.ui.pushButtonGo.released.connect(
            self.execute_trade)
        self.ui.tableAsk.clicked.connect(
            self.slot_update_price_from_asks)
        self.ui.tableBid.clicked.connect(
            self.slot_update_price_from_bids)
        self.ui.pushButtonCancel.released.connect(