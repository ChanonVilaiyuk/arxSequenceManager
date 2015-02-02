# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'U:/extensions/studioTools/python/arxSequencerManager/restoreDialog.ui'
#
# Created: Tue Feb 03 00:11:18 2015
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_restore_dialog(object):
    def setupUi(self, restore_dialog):
        restore_dialog.setObjectName("restore_dialog")
        restore_dialog.resize(286, 336)
        self.verticalLayout = QtGui.QVBoxLayout(restore_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(restore_dialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtGui.QListWidget(restore_dialog)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.pushButton = QtGui.QPushButton(restore_dialog)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(restore_dialog)
        QtCore.QMetaObject.connectSlotsByName(restore_dialog)

    def retranslateUi(self, restore_dialog):
        restore_dialog.setWindowTitle(QtGui.QApplication.translate("restore_dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("restore_dialog", "Choose restore file", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("restore_dialog", "Restore", None, QtGui.QApplication.UnicodeUTF8))

