from PySide import QtCore
from PySide import QtGui

from shiboken import wrapInstance

class customQWidgetItem(QtGui.QWidget) : 
	def __init__(self, parent = None) : 
		super(customQWidgetItem, self).__init__(parent)
		# set label 
		self.textQVBoxLayout = QtGui.QVBoxLayout()
		self.text1Label = QtGui.QLabel()
		self.text2Label = QtGui.QLabel()
		self.text3Label = QtGui.QLabel()
		self.text4Label = QtGui.QLabel()
		self.text5Label = QtGui.QLabel()
		self.text6Label = QtGui.QLabel()
		self.text7Label = QtGui.QLabel()

		self.text1QHBoxLayout = QtGui.QHBoxLayout()
		self.text2QHBoxLayout = QtGui.QHBoxLayout()

		self.textQVBoxLayout.addWidget(self.text1Label)

		self.text1QHBoxLayout.addWidget(self.text2Label)
		self.text1QHBoxLayout.addWidget(self.text3Label)
		self.text1QHBoxLayout.addWidget(self.text4Label)

		self.text2QHBoxLayout.addWidget(self.text5Label)
		self.text2QHBoxLayout.addWidget(self.text6Label)
		self.text2QHBoxLayout.addWidget(self.text7Label)

		self.textQVBoxLayout.addLayout(self.text1QHBoxLayout, 1)
		self.textQVBoxLayout.addLayout(self.text2QHBoxLayout, 2)

		# alignment
		self.text1Label.setAlignment(QtCore.Qt.AlignCenter)
		self.text2Label.setAlignment(QtCore.Qt.AlignLeft)
		self.text3Label.setAlignment(QtCore.Qt.AlignCenter)
		self.text4Label.setAlignment(QtCore.Qt.AlignRight)
		self.text5Label.setAlignment(QtCore.Qt.AlignLeft)
		self.text6Label.setAlignment(QtCore.Qt.AlignCenter)
		self.text7Label.setAlignment(QtCore.Qt.AlignRight)


		# set icon
		self.allLayout = QtGui.QHBoxLayout()
		# self.iconQLabel = QtGui.QLabel()
		# self.allLayout.addWidget(self.iconQLabel, 0)
		self.allLayout.addLayout(self.textQVBoxLayout, 0)
		self.allLayout.setContentsMargins(2, 2, 2, 2)
		self.setLayout(self.allLayout)

		# set font
		font = QtGui.QFont()
		font.setPointSize(9)
		# font.setWeight(70)
		font.setBold(True)
		self.text1Label.setFont(font)

		font.setPointSize(8)
		self.text3Label.setFont(font)
		self.text6Label.setFont(font)


	def setTexts(self, texts) : 
		self.text1Label.setText(texts[0])
		self.text2Label.setText(texts[1])
		self.text3Label.setText(texts[2])
		self.text4Label.setText(texts[3])
		self.text5Label.setText(texts[4])
		self.text6Label.setText(texts[5])
		self.text7Label.setText(texts[6])



	def setTextColors(self, colors) : 
		self.text1Label.setStyleSheet('color: rgb(%s, %s, %s);' % (colors[0][0], colors[0][1], colors[0][2]))
		self.text2Label.setStyleSheet('color: rgb(%s, %s, %s);' % (colors[1][0], colors[1][1], colors[1][2]))
		self.text3Label.setStyleSheet('color: rgb(%s, %s, %s);' % (colors[2][0], colors[2][1], colors[2][2]))
		self.text4Label.setStyleSheet('color: rgb(%s, %s, %s);' % (colors[3][0], colors[3][1], colors[3][2]))
		self.text5Label.setStyleSheet('color: rgb(%s, %s, %s);' % (colors[4][0], colors[4][1], colors[4][2]))
		self.text6Label.setStyleSheet('color: rgb(%s, %s, %s);' % (colors[5][0], colors[5][1], colors[5][2]))
		self.text7Label.setStyleSheet('color: rgb(%s, %s, %s);' % (colors[6][0], colors[6][1], colors[6][2]))


	# def setIcon(self, iconPath, size) : 
	# 	self.iconQLabel.setPixmap(QtGui.QPixmap(iconPath).scaled(size, size, QtCore.Qt.KeepAspectRatio))


	def texts(self) : 
		texts = list()
		texts.append(self.text1Label.text())
		texts.append(self.text2Label.text())
		texts.append(self.text3Label.text())
		texts.append(self.text4Label.text())
		texts.append(self.text5Label.text())
		texts.append(self.text6Label.text())
		texts.append(self.text7Label.text())

		return texts