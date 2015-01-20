# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'U:/extensions/studioTools/python/arxSequencerManager/dialog.ui'
#
# Created: Tue Jan 20 20:55:48 2015
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(297, 87)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_label = QtGui.QLabel(Dialog)
        self.text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.text_label.setObjectName("text_label")
        self.verticalLayout.addWidget(self.text_label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.b1_pushButton = QtGui.QPushButton(Dialog)
        self.b1_pushButton.setObjectName("b1_pushButton")
        self.horizontalLayout.addWidget(self.b1_pushButton)
        self.b2_pushButton = QtGui.QPushButton(Dialog)
        self.b2_pushButton.setObjectName("b2_pushButton")
        self.horizontalLayout.addWidget(self.b2_pushButton)
        self.b3_pushButton = QtGui.QPushButton(Dialog)
        self.b3_pushButton.setObjectName("b3_pushButton")
        self.horizontalLayout.addWidget(self.b3_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.text_label.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.b1_pushButton.setText(QtGui.QApplication.translate("Dialog", "Yes", None, QtGui.QApplication.UnicodeUTF8))
        self.b2_pushButton.setText(QtGui.QApplication.translate("Dialog", "No", None, QtGui.QApplication.UnicodeUTF8))
        self.b3_pushButton.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

