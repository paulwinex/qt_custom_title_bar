# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\work\custom_title\main_window.ui'
#
# Created: Fri May 18 00:02:42 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName("MainDialog")
        MainDialog.resize(1061, 597)
        self.centralwidget = QtGui.QWidget(MainDialog)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.title_ly = QtGui.QHBoxLayout()
        self.title_ly.setObjectName("title_ly")
        self.verticalLayout_5.addLayout(self.title_ly)
        self.menu_ly = QtGui.QHBoxLayout()
        self.menu_ly.setContentsMargins(6, -1, 6, -1)
        self.menu_ly.setObjectName("menu_ly")
        self.verticalLayout_5.addLayout(self.menu_ly)
        self.content_ly = QtGui.QHBoxLayout()
        self.content_ly.setContentsMargins(5, -1, 5, -1)
        self.content_ly.setObjectName("content_ly")
        self.verticalLayout_5.addLayout(self.content_ly)
        self.verticalLayout_5.setStretch(2, 1)
        MainDialog.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainDialog)
        self.statusBar.setObjectName("statusBar")
        MainDialog.setStatusBar(self.statusBar)
        self.actionSet_User = QtGui.QAction(MainDialog)
        self.actionSet_User.setObjectName("actionSet_User")
        self.actionLogout_Current_User = QtGui.QAction(MainDialog)
        self.actionLogout_Current_User.setObjectName("actionLogout_Current_User")

        self.retranslateUi(MainDialog)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        MainDialog.setWindowTitle(QtGui.QApplication.translate("MainDialog", "Main Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSet_User.setText(QtGui.QApplication.translate("MainDialog", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLogout_Current_User.setText(QtGui.QApplication.translate("MainDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

