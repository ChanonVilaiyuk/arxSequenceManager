# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'U:/extensions/studioTools/python/arxSequencerManager/ui.ui'
#
# Created: Sat Jan 31 02:04:26 2015
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SequencerManagerWindow(object):
    def setupUi(self, SequencerManagerWindow):
        SequencerManagerWindow.setObjectName("SequencerManagerWindow")
        SequencerManagerWindow.resize(638, 770)
        SequencerManagerWindow.setMinimumSize(QtCore.QSize(0, 760))
        self.centralwidget = QtGui.QWidget(SequencerManagerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(310, 0))
        self.frame_2.setFrameShape(QtGui.QFrame.Box)
        self.frame_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_10 = QtGui.QFrame(self.frame_2)
        self.frame_10.setFrameShape(QtGui.QFrame.Box)
        self.frame_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_10)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_8 = QtGui.QFrame(self.frame_10)
        self.frame_8.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_25 = QtGui.QHBoxLayout(self.frame_8)
        self.horizontalLayout_25.setSpacing(2)
        self.horizontalLayout_25.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_10 = QtGui.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_25.addWidget(self.label_10)
        self.label_8 = QtGui.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_25.addWidget(self.label_8)
        self.label_6 = QtGui.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_25.addWidget(self.label_6)
        self.verticalLayout_3.addWidget(self.frame_8)
        self.frame_3 = QtGui.QFrame(self.frame_10)
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.editStart_lineEdit = QtGui.QLineEdit(self.frame_3)
        self.editStart_lineEdit.setObjectName("editStart_lineEdit")
        self.horizontalLayout_2.addWidget(self.editStart_lineEdit)
        self.duration_label = QtGui.QLabel(self.frame_3)
        self.duration_label.setAlignment(QtCore.Qt.AlignCenter)
        self.duration_label.setObjectName("duration_label")
        self.horizontalLayout_2.addWidget(self.duration_label)
        self.editEnd_lineEdit = QtGui.QLineEdit(self.frame_3)
        self.editEnd_lineEdit.setObjectName("editEnd_lineEdit")
        self.horizontalLayout_2.addWidget(self.editEnd_lineEdit)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame_10)
        self.frame_9 = QtGui.QFrame(self.frame_2)
        self.frame_9.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_31 = QtGui.QHBoxLayout(self.frame_9)
        self.horizontalLayout_31.setSpacing(2)
        self.horizontalLayout_31.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.moveShot_checkBox = QtGui.QCheckBox(self.frame_9)
        self.moveShot_checkBox.setObjectName("moveShot_checkBox")
        self.horizontalLayout_31.addWidget(self.moveShot_checkBox)
        self.moveShot_lineEdit = QtGui.QLineEdit(self.frame_9)
        self.moveShot_lineEdit.setText("")
        self.moveShot_lineEdit.setObjectName("moveShot_lineEdit")
        self.horizontalLayout_31.addWidget(self.moveShot_lineEdit)
        self.horizontalLayout_31.setStretch(0, 1)
        self.horizontalLayout_31.setStretch(1, 1)
        self.verticalLayout.addWidget(self.frame_9)
        self.linkedShot_checkBox = QtGui.QCheckBox(self.frame_2)
        self.linkedShot_checkBox.setObjectName("linkedShot_checkBox")
        self.verticalLayout.addWidget(self.linkedShot_checkBox)
        self.apply_pushButton = QtGui.QPushButton(self.frame_2)
        self.apply_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(96, 120, 172))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 120, 172))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 120, 172))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.apply_pushButton.setPalette(palette)
        self.apply_pushButton.setObjectName("apply_pushButton")
        self.verticalLayout.addWidget(self.apply_pushButton)
        spacerItem = QtGui.QSpacerItem(20, 7, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.label_16 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.listWidget = QtGui.QListWidget(self.frame_2)
        self.listWidget.setSpacing(1)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.activeShot_checkBox = QtGui.QCheckBox(self.frame_2)
        self.activeShot_checkBox.setObjectName("activeShot_checkBox")
        self.verticalLayout.addWidget(self.activeShot_checkBox)
        self.refresh_pushButton = QtGui.QPushButton(self.frame_2)
        self.refresh_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.refresh_pushButton.setObjectName("refresh_pushButton")
        self.verticalLayout.addWidget(self.refresh_pushButton)
        self.sequencer_pushButton = QtGui.QPushButton(self.frame_2)
        self.sequencer_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.sequencer_pushButton.setObjectName("sequencer_pushButton")
        self.verticalLayout.addWidget(self.sequencer_pushButton)
        self.line = QtGui.QFrame(self.frame_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.pullShotgun_pushButton = QtGui.QPushButton(self.frame_2)
        self.pullShotgun_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(211, 184, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 184, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 184, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pullShotgun_pushButton.setPalette(palette)
        self.pullShotgun_pushButton.setObjectName("pullShotgun_pushButton")
        self.verticalLayout.addWidget(self.pullShotgun_pushButton)
        self.pushShotgun_pushButton = QtGui.QPushButton(self.frame_2)
        self.pushShotgun_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(162, 217, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 22, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(162, 217, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 22, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(162, 217, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushShotgun_pushButton.setPalette(palette)
        self.pushShotgun_pushButton.setObjectName("pushShotgun_pushButton")
        self.verticalLayout.addWidget(self.pushShotgun_pushButton)
        self.restoreShotgun_pushButton = QtGui.QPushButton(self.frame_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(144, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 2, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(144, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 2, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(144, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.restoreShotgun_pushButton.setPalette(palette)
        self.restoreShotgun_pushButton.setObjectName("restoreShotgun_pushButton")
        self.verticalLayout.addWidget(self.restoreShotgun_pushButton)
        self.horizontalLayout_11.addWidget(self.frame_2)
        self.frame_6 = QtGui.QFrame(self.frame)
        self.frame_6.setMinimumSize(QtCore.QSize(251, 691))
        self.frame_6.setMaximumSize(QtCore.QSize(251, 2000))
        self.frame_6.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_15 = QtGui.QLabel(self.frame_6)
        self.label_15.setGeometry(QtCore.QRect(0, 180, 131, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.frame_5 = QtGui.QFrame(self.frame_6)
        self.frame_5.setGeometry(QtCore.QRect(0, 80, 251, 91))
        self.frame_5.setFrameShape(QtGui.QFrame.Box)
        self.frame_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.episode_label = QtGui.QLabel(self.frame_5)
        self.episode_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.episode_label.setObjectName("episode_label")
        self.gridLayout_2.addWidget(self.episode_label, 2, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.frame_5)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)
        self.project_label = QtGui.QLabel(self.frame_5)
        self.project_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.project_label.setObjectName("project_label")
        self.gridLayout_2.addWidget(self.project_label, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.frame_5)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.frame_5)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.sequence_label = QtGui.QLabel(self.frame_5)
        self.sequence_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.sequence_label.setObjectName("sequence_label")
        self.gridLayout_2.addWidget(self.sequence_label, 3, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.frame_5)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 4, 0, 1, 1)
        self.shot_label = QtGui.QLabel(self.frame_5)
        self.shot_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.shot_label.setObjectName("shot_label")
        self.gridLayout_2.addWidget(self.shot_label, 4, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.frame_4 = QtGui.QFrame(self.frame_6)
        self.frame_4.setGeometry(QtCore.QRect(0, 200, 251, 201))
        self.frame_4.setFrameShape(QtGui.QFrame.Box)
        self.frame_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtGui.QLabel(self.frame_4)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.prefix_lineEdit = QtGui.QLineEdit(self.frame_4)
        self.prefix_lineEdit.setText("")
        self.prefix_lineEdit.setObjectName("prefix_lineEdit")
        self.horizontalLayout_5.addWidget(self.prefix_lineEdit)
        self.shotName_lineEdit = QtGui.QLineEdit(self.frame_4)
        self.shotName_lineEdit.setText("")
        self.shotName_lineEdit.setObjectName("shotName_lineEdit")
        self.horizontalLayout_5.addWidget(self.shotName_lineEdit)
        self.auto_checkBox = QtGui.QCheckBox(self.frame_4)
        self.auto_checkBox.setChecked(True)
        self.auto_checkBox.setObjectName("auto_checkBox")
        self.horizontalLayout_5.addWidget(self.auto_checkBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.before_radioButton = QtGui.QRadioButton(self.frame_4)
        self.before_radioButton.setObjectName("before_radioButton")
        self.horizontalLayout_6.addWidget(self.before_radioButton)
        self.after_radioButton = QtGui.QRadioButton(self.frame_4)
        self.after_radioButton.setObjectName("after_radioButton")
        self.horizontalLayout_6.addWidget(self.after_radioButton)
        self.last_radioButton = QtGui.QRadioButton(self.frame_4)
        self.last_radioButton.setChecked(True)
        self.last_radioButton.setObjectName("last_radioButton")
        self.horizontalLayout_6.addWidget(self.last_radioButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_2 = QtGui.QLabel(self.frame_4)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.start_lineEdit = QtGui.QLineEdit(self.frame_4)
        self.start_lineEdit.setObjectName("start_lineEdit")
        self.horizontalLayout_9.addWidget(self.start_lineEdit)
        self.label_3 = QtGui.QLabel(self.frame_4)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        self.end_lineEdit = QtGui.QLineEdit(self.frame_4)
        self.end_lineEdit.setObjectName("end_lineEdit")
        self.horizontalLayout_9.addWidget(self.end_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_4 = QtGui.QLabel(self.frame_4)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.duration_lineEdit = QtGui.QLineEdit(self.frame_4)
        self.duration_lineEdit.setText("")
        self.duration_lineEdit.setObjectName("duration_lineEdit")
        self.horizontalLayout_10.addWidget(self.duration_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label = QtGui.QLabel(self.frame_4)
        self.label.setObjectName("label")
        self.horizontalLayout_20.addWidget(self.label)
        self.camera_comboBox = QtGui.QComboBox(self.frame_4)
        self.camera_comboBox.setObjectName("camera_comboBox")
        self.horizontalLayout_20.addWidget(self.camera_comboBox)
        self.horizontalLayout_20.setStretch(0, 1)
        self.horizontalLayout_20.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_20)
        self.camera_checkBox = QtGui.QCheckBox(self.frame_4)
        self.camera_checkBox.setObjectName("camera_checkBox")
        self.verticalLayout_2.addWidget(self.camera_checkBox)
        self.noMove_checkBox = QtGui.QCheckBox(self.frame_4)
        self.noMove_checkBox.setObjectName("noMove_checkBox")
        self.verticalLayout_2.addWidget(self.noMove_checkBox)
        self.label_17 = QtGui.QLabel(self.frame_6)
        self.label_17.setGeometry(QtCore.QRect(10, 520, 131, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.frame_7 = QtGui.QFrame(self.frame_6)
        self.frame_7.setGeometry(QtCore.QRect(0, 540, 251, 181))
        self.frame_7.setFrameShape(QtGui.QFrame.Box)
        self.frame_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_7)
        self.gridLayout_3.setVerticalSpacing(9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.rebuildShot_pushButton = QtGui.QPushButton(self.frame_7)
        self.rebuildShot_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.rebuildShot_pushButton.setObjectName("rebuildShot_pushButton")
        self.gridLayout_3.addWidget(self.rebuildShot_pushButton, 0, 0, 1, 1)
        self.frame_11 = QtGui.QFrame(self.frame_7)
        self.frame_11.setFrameShape(QtGui.QFrame.Box)
        self.frame_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.frame_11)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setContentsMargins(2, 4, 2, 9)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_23 = QtGui.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_6.addWidget(self.label_23)
        self.label_22 = QtGui.QLabel(self.frame_11)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_6.addWidget(self.label_22)
        self.frame_lineEdit = QtGui.QLineEdit(self.frame_11)
        self.frame_lineEdit.setObjectName("frame_lineEdit")
        self.verticalLayout_6.addWidget(self.frame_lineEdit)
        self.currentStart_checkBox = QtGui.QCheckBox(self.frame_11)
        self.currentStart_checkBox.setObjectName("currentStart_checkBox")
        self.verticalLayout_6.addWidget(self.currentStart_checkBox)
        self.shiftFrame_pushButton = QtGui.QPushButton(self.frame_11)
        self.shiftFrame_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(222, 223, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 223, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 223, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.shiftFrame_pushButton.setPalette(palette)
        self.shiftFrame_pushButton.setObjectName("shiftFrame_pushButton")
        self.verticalLayout_6.addWidget(self.shiftFrame_pushButton)
        self.gridLayout_3.addWidget(self.frame_11, 1, 0, 2, 1)
        self.logo_label = QtGui.QLabel(self.frame_6)
        self.logo_label.setGeometry(QtCore.QRect(20, 10, 221, 61))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.logo_label.setFont(font)
        self.logo_label.setText("")
        self.logo_label.setObjectName("logo_label")
        self.verticalLayoutWidget = QtGui.QWidget(self.frame_6)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 410, 251, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.addShot_pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.addShot_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(94, 149, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 149, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 149, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.addShot_pushButton.setPalette(palette)
        self.addShot_pushButton.setObjectName("addShot_pushButton")
        self.verticalLayout_9.addWidget(self.addShot_pushButton)
        self.disableShot_pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.disableShot_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.disableShot_pushButton.setObjectName("disableShot_pushButton")
        self.verticalLayout_9.addWidget(self.disableShot_pushButton)
        self.deleteShot_pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(144, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(144, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(144, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.deleteShot_pushButton.setPalette(palette)
        self.deleteShot_pushButton.setObjectName("deleteShot_pushButton")
        self.verticalLayout_9.addWidget(self.deleteShot_pushButton)
        self.horizontalLayout_11.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.frame)
        SequencerManagerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SequencerManagerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 21))
        self.menubar.setObjectName("menubar")
        SequencerManagerWindow.setMenuBar(self.menubar)

        self.retranslateUi(SequencerManagerWindow)
        QtCore.QMetaObject.connectSlotsByName(SequencerManagerWindow)

    def retranslateUi(self, SequencerManagerWindow):
        SequencerManagerWindow.setWindowTitle(QtGui.QApplication.translate("SequencerManagerWindow", "Arx Sequencer Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Duration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("SequencerManagerWindow", "End", None, QtGui.QApplication.UnicodeUTF8))
        self.duration_label.setText(QtGui.QApplication.translate("SequencerManagerWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.moveShot_checkBox.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Move shot", None, QtGui.QApplication.UnicodeUTF8))
        self.linkedShot_checkBox.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Linked shot", None, QtGui.QApplication.UnicodeUTF8))
        self.apply_pushButton.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Shot List", None, QtGui.QApplication.UnicodeUTF8))
        self.activeShot_checkBox.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Active Shot", None, QtGui.QApplication.UnicodeUTF8))
        self.refresh_pushButton.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.sequencer_pushButton.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Camera Sequencer", None, QtGui.QApplication.UnicodeUTF8))
        self.pullShotgun_pushButton.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Pull Shotgun Data", None, QtGui.QApplication.UnicodeUTF8))
        self.pushShotgun_pushButton.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Push Shotgun Data", None, QtGui.QApplication.UnicodeUTF8))
        self.restoreShotgun_pushButton.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Restore Shotgun Changes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Create Shot Options", None, QtGui.QApplication.UnicodeUTF8))
        self.episode_label.setText(QtGui.QApplication.translate("SequencerManagerWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Sequence : ", None, QtGui.QApplication.UnicodeUTF8))
        self.project_label.setText(QtGui.QApplication.translate("SequencerManagerWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Project : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Episdoe : ", None, QtGui.QApplication.UnicodeUTF8))
        self.sequence_label.setText(QtGui.QApplication.translate("SequencerManagerWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Shot : ", None, QtGui.QApplication.UnicodeUTF8))
        self.shot_label.setText(QtGui.QApplication.translate("SequencerManagerWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Shot Name", None, QtGui.QApplication.UnicodeUTF8))
        self.auto_checkBox.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Auto", None, QtGui.QApplication.UnicodeUTF8))
        self.before_radioButton.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Before", None, QtGui.QApplication.UnicodeUTF8))
        self.after_radioButton.setText(QtGui.QApplication.translate("SequencerManagerWindow", "After", None, QtGui.QApplication.UnicodeUTF8))
        self.last_radioButton.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Last", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Start : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SequencerManagerWindow", "End : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Duration", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.camera_checkBox.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Use existing camera", None, QtGui.QApplication.UnicodeUTF8))
        self.noMove_checkBox.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Add shot in gap / no move other shots", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.rebuildShot_pushButton.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Rebuild Shots", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Shift Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Move all keyframe (forward / backward)", None, QtGui.QApplication.UnicodeUTF8))
        self.currentStart_checkBox.setText(QtGui.QApplication.translate("SequencerManagerWindow", "move from current frame", None, QtGui.QApplication.UnicodeUTF8))
        self.shiftFrame_pushButton.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Shift Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.addShot_pushButton.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Add Shot", None, QtGui.QApplication.UnicodeUTF8))
        self.disableShot_pushButton.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Disable Selected Shot", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteShot_pushButton.setText(QtGui.QApplication.translate("SequencerManagerWindow", "Delete Shot", None, QtGui.QApplication.UnicodeUTF8))

