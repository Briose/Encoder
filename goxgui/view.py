
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
            self.cancel_order)
        self.ui.textBrowserStatus.anchorClicked.connect(
            self.order_selected)
        self.ui.pushButtonSize.released.connect(
            self.recalculate_size)
        self.ui.pushButtonPrice.released.connect(
            self.update_price_best)
        self.ui.pushButtonTotal.released.connect(
            self.recalculate_total)
        self.ui.actionPreferences_2.triggered.connect(
            self.show_preferences)

        # associate log channels with their check boxes
        self.logchannels = [
            [self.ui.checkBoxLogTicker, 'tick'],
            [self.ui.checkBoxLogTrade, 'TRADE'],
            [self.ui.checkBoxLogDepth, 'depth'],
        ]

        # set correct resizing for the bid and ask tables
        self.ui.tableAsk.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.ui.tableBid.horizontalHeader().setResizeMode(QHeaderView.Stretch)

        # set up info table
        self.info = Info(self, self.preferences, self.ui.tableInfo.clicked)
        self.ui.tableInfo.setModel(self.info)
        self.ui.tableInfo.horizontalHeader().setResizeMode(QHeaderView.Stretch)

        # connect to signals from info table
        self.info.signal_base_balance_clicked.connect(
            self.set_trade_size_from_wallet)
        self.info.signal_quote_balance_clicked.connect(
            self.set_trade_total_from_wallet)

        # initializes dynamic ui elements
        self.init()

        # activate market
        self.market.start()

        # show main window
        self.adjustSize()
        self.show()
        self.raise_()

    def get_base_currency(self):
        return self.preferences.get_currency(Preferences.CURRENCY_INDEX_BASE)

    def get_quote_currency(self):
        return self.preferences.get_currency(Preferences.CURRENCY_INDEX_QUOTE)

    def init(self):

        # initialize wallet values
        self.info.set_wallet_a(None)
        self.info.set_wallet_b(None)

        # initialize ticker values