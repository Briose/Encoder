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
        self.lineEditKey.setObjectName(_fromUtf8("lineEditKey"))
        self.gridLayout_5.addWidget(self.lineEditKey, 4, 2, 1, 1)
        self.lineEditSecret = QtGui.QLineEdit(self.tabSecurity)
        self.lineEditSecret.setInputMethodHints(QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.lineEditSecret.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.lineEditSecret.setObjectName(_fromUtf8("lineEditSecret"))
        self.gridLayout_5.addWidget(self.lineEditSecret, 5, 2, 1, 1)
        self.lineEditPassword = QtGui.QLineEdit(self.tabSecurity)
        self.lineEditPassword.setEnabled(False)
        self.lineEditPassword.setInputMethodHints(QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.lineEditPassword.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.lineEditPassword.setObjectName(_fromUtf8("lineEditPassword"))
        self.gridLayout_5.addWidget(self.lineEditPassword, 1, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 6, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.tabSecurity)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_5.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.tabSecurity)
        self.label_4.setMinimumSize(QtCore.QSize(100, 0))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_5.addWidget(self.label_4, 5, 0, 1, 1)
        self.tabWidget.addTab(self.tabSecurity, _fromUtf8(""))
        self.tabOrderBook = QtGui.QWidget()
        self.tabOrderBook.setObjectName(_fromUtf8("tabOrderBook"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tabOrderBook)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.line_2 = QtGui.QFrame(self.tabOrderBook)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_3.addWidget(self.line_2, 10, 0, 1, 3)
        spacerItem3 = QtGui.QSpacerItem(20, 164, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 13, 1, 1, 1)
        self.doubleSpinBoxOffset = QtGui.QDoubleSpinBox(self.tabOrderBook)
        self.doubleSpinBoxOffset.setDecimals(0)
        self.doubleSpinBoxOffset.setMaximum(999999.0)
        self.doubleSpinBoxOffset.setObjectName(_fromUtf8("doubleSpinBoxOffset"))
        self.gridLayout_3.addWidget(self.doubleSpinBoxOffset, 12, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.tabOrderBook)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 12, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.tabOrderBook)
        self.label_8.setMinimumSize(QtCore.QSize(100, 0))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 4, 0, 1, 1)
        self.checkBoxTotalQuote = QtGui.QCheckBox(self.tabOrderBook)
        self.checkBoxTotalQuote.setObjectName(_fromUtf8("checkBoxTotalQuote"))
        self.gridLayout_3.addWidget(self.checkBoxTotalQuote, 9, 1, 1, 1)
        self.checkBoxPrice = QtGui.QCheckBox(self.tabOrderBook)
        self.checkBoxPrice.setObjectName(_fromUtf8("checkBoxPrice"))
        self.gridLayout_3.addWidget(self.checkBoxPrice, 4, 1, 1, 1)
        self.doubleSpinBoxGrouping = QtGui.QDoubleSpinBox(self.tabOrderBook)
        self.doubleSpinBoxGrouping.setDecimals(3)
        self.doubleSpinBoxGrouping.setMinimum(-9999999.0)
        self.doubleSpinBoxGrouping.setMaximum(9999999.0)
        self.doubleSpinBoxGrouping.setSingleStep(0.01)
        self.doubleSpinBoxGrouping.setObjectName(_fromUtf8("doubleSpinBoxGrouping"))
        self.gridLayout_3.addWidget(self.doubleSpinBoxGrouping, 1, 1, 1, 1)
        self.labelGrouping = QtGui.QLabel(self.tabOrderBook)
        self.labelGrouping.setTextFormat(QtCore.Qt.AutoText)
        self.labelGrouping.setWordWrap(True)
        self.labelGrouping.setObjectName(_fromUtf8("labelGrouping"))
        self.gridLayout_3.addWidget(self.labelGrouping, 0, 1, 1, 2)
        self.checkBoxSize = QtGui.QCheckBox(self.tabOrderBook)
        self.checkBoxSize.setObjectName(_fromUtf8("checkBoxSize"))
        self.gridLayout_3.addWidget(self.checkBoxSize, 5, 1, 1, 1)
        self.labelColumns = QtGui.QLabel(self.tabOrderBook)
        self.labelColumns.setTextFormat(QtCore.Qt.AutoText)
        self.labelColumns.setWordWrap(True)
        self.labelColumns.setObjectName(_fromUtf8("labelColumns"))
        self.gridLayout_3.addWidget(self.labelColumns, 3, 1, 1, 2)
        self.checkBoxQuote = QtGui.QCheckBox(self.tabOrderBook)
        self.checkBoxQuote.setObjectName(_fromUtf8("checkBoxQuote"))
        self.gridLayout_3.addWidget(self.checkBoxQuote, 7, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.tabOrderBook)
        self.label_7.setMinimumSize(QtCore.QSize(100, 0))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)
        self.line = QtGui.QFrame(self.tabOrderBook)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_3.addWidget(self.line, 2, 0, 1, 3)
        self.labelOffset = QtGui.QLabel(self.tabOrderBook)
        self.labelOffset.setObjectName(_fromUtf8("labelOffset"))
        self.gridLayout_3.addWidget(self.labelOffset, 11, 1, 1, 1)
        self.checkBoxTotalSize = QtGui.QCheckBox(self.tabOrderBook)
        self.checkBoxTotalSize.setObjectName(_fromUtf8("checkBoxTotalSize"))
        self.gridLayout_3.addWidget(self.checkBoxTotalSize, 6, 1, 1, 1)
        self.tabWidget.addTab(self.tabOrderBook, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelStatus = QtGui.QLabel(Preferences)
        self.labelStatus.setText(_fromUtf8(""))
        self.labelStatus.setObjectName(_fromUtf8("labelStatus"))
        self.horizontalLayout.addWidget(self.labelStatus)
        self.buttonBox = QtGui.QDialogButtonBox(Preferences)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.setStretch(0, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Preferences)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Preferences.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Preferences.reject)
        QtCore.QMetaObject.connectSlotsByName(Preferences)
        Preferences.setTabOrder(self.buttonBox, self.tabWidget)

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(QtGui.QApplication.translate("Preferences", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Preferences", "Fiat:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCurrency.setText(QtGui.QApplication.translate("Preferences", "Fiat currency you would like to trade", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCurrency), QtGui.QApplication.translate("Preferences", "Currency", None, QtGui.QApplication.UnicodeUTF8))
        self.labelKeySecret.setText(QtGui.QApplication.translate("Preferences", "Insert your market\'s (e.g. MtGox) API key here. If you don\'t have an API key yet, you should be able to generate one on your market\'s website.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Preferences", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPassword.setText(QtGui.QApplication.translate("Preferences", "Set an application-wide password to protect account-related functionalities against misuse.", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditKey.setToolTip(QtGui.QApplication.translate("Preferences", "Insert your MtGox key here", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditKey.setPlaceholderText(QtGui.QApplication.translate("Preferences", "Key", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditSecret.setToolTip(QtGui.QApplication.translate("Preferences", "Insert your MtGox secret here", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditSecret.setPlaceholderText(QtGui.QApplication.translate("Preferences", "Secret", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditPassword.setToolTip(QtGui.QApplication.translate("Preferences", "Application password", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditPassword.setPlaceholderText(QtGui.QApplication.translate("Preferences", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Preferences", "Key:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Preferences", "Secret:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSecurity), QtGui.QApplication.translate("Preferences", "Security", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Preferences", "Offset:", None, QtGui.QAppl