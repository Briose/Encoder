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
        self.labelCurrency.setObjectName(_fromUtf8("labelCurrency"))
        self.gridLayout_2.addWidget(self.labelCurrency, 1, 1, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tabCurrency, _fromUtf8(""))
        self.tabSecurity = QtGui.QWidget()
        self.tabSecurity.setObjectName(_fromUtf8("tabSecurity"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tabSecurity)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.labelKeySecret = QtGui.QLabel(self.tabSecurity)
        self.labelKeySecret.setWordWrap(True)
        self.labelKeySecret.setObjectName(_fromUtf8("labelKeySecret"))
        self.gridLayout_5.addWidget(self.labelKeySecret, 3, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.tabSecurity)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.tabSecurity)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_5.addWidget(self.line_3, 2, 0, 1, 3)
        self.labelPassword = QtGui.QLabel(self.tabSecurity)
        self.labelPassword.setWordWrap(True)
        self.labelPassword.setObjectName(_fromUtf8("labelPassword"))
        self.gridLayout_5.addWidget(self.labelPassword, 0, 2, 1, 1)
        self.lineEditKey = QtGui.QLineEdit(self.tabSecurity)
        self.lineEditKe