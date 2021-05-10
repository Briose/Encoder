
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/user/git/goxgui/goxgui/ui/main_window.ui'
#
# Created: Mon Jun  3 21:02:22 2013
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(906, 846)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.widgetMain = QtGui.QWidget(MainWindow)
        self.widgetMain.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetMain.sizePolicy().hasHeightForWidth())
        self.widgetMain.setSizePolicy(sizePolicy)
        self.widgetMain.setObjectName(_fromUtf8("widgetMain"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widgetMain)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableInfo = QtGui.QTableView(self.widgetMain)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableInfo.sizePolicy().hasHeightForWidth())
        self.tableInfo.setSizePolicy(sizePolicy)
        self.tableInfo.setMaximumSize(QtCore.QSize(16777215, 42))
        self.tableInfo.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tableInfo.setFrameShadow(QtGui.QFrame.Plain)
        self.tableInfo.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableInfo.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableInfo.setAutoScroll(False)
        self.tableInfo.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableInfo.setTabKeyNavigation(False)
        self.tableInfo.setProperty("showDropIndicator", False)
        self.tableInfo.setAlternatingRowColors(False)
        self.tableInfo.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tableInfo.setShowGrid(True)
        self.tableInfo.setGridStyle(QtCore.Qt.DotLine)
        self.tableInfo.setWordWrap(False)
        self.tableInfo.setCornerButtonEnabled(False)
        self.tableInfo.setObjectName(_fromUtf8("tableInfo"))
        self.tableInfo.horizontalHeader().setVisible(False)
        self.tableInfo.verticalHeader().setVisible(False)
        self.tableInfo.verticalHeader().setDefaultSectionSize(20)
        self.tableInfo.verticalHeader().setMinimumSectionSize(20)
        self.verticalLayout_2.addWidget(self.tableInfo)
        self.tabTrading = QtGui.QTabWidget(self.widgetMain)
        self.tabTrading.setObjectName(_fromUtf8("tabTrading"))
        self.tabManual = QtGui.QWidget()
        self.tabManual.setObjectName(_fromUtf8("tabManual"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabManual)
        self.verticalLayout_3.setContentsMargins(12, -1, 12, 12)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.widget = QtGui.QWidget(self.tabManual)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.radioButtonBuy = QtGui.QRadioButton(self.widget)
        self.radioButtonBuy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButtonBuy.setChecked(True)
        self.radioButtonBuy.setObjectName(_fromUtf8("radioButtonBuy"))
        self.horizontalLayout_4.addWidget(self.radioButtonBuy)
        self.radioButtonSell = QtGui.QRadioButton(self.widget)
        self.radioButtonSell.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButtonSell.setChecked(False)
        self.radioButtonSell.setObjectName(_fromUtf8("radioButtonSell"))
        self.horizontalLayout_4.addWidget(self.radioButtonSell)
        self.pushButtonSize = QtGui.QPushButton(self.widget)
        self.pushButtonSize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonSize.setObjectName(_fromUtf8("pushButtonSize"))
        self.horizontalLayout_4.addWidget(self.pushButtonSize)
        self.doubleSpinBoxSize = QtGui.QDoubleSpinBox(self.widget)