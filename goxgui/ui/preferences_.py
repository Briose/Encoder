# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/user/git/goxgui/goxgui/ui/preferences.ui'
#
# Created: Mon May 27 21:32:10 2013
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName(_fromUtf8("Preferences"))
        Preferences.resize(740, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Preferences.sizePolicy().hasHeightForWidth())
        Preferences.setSizePolicy(sizePolicy)
        Preferences.setMinimumSize(QtCore.QSize(740, 600))
        Preferences.setMaximumSize(QtCore.QSize(740, 600))
        self.gridLayout = QtGui.QGridLayout(Preferences)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(Preferences)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabCurrency = QtGui.QWidget()
        self.tabCurrency.setObjectName(_fromUtf8("tabCurrency"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tabCurrency)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.tabCurrency)
        self.label_6.setMinimumSize(QtCore.QSize(100, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.comboBoxCurrency = QtGui.QComboBox(self.tabCurrency)
        self.comboBoxCurrency.setObjectName(_fromUtf8("comboBoxCurrency"))
        self.gridLayout_2.addWidget(self.comboBoxCurrency, 2, 1, 1, 1)
        self.labelCurrency = QtGui.QLabel(self.tabCurrency)
        self.labelCurrency.setTextFormat(QtCore.Qt.AutoText)
        self.labelCurrency.setWordWrap(True)
        se