from PySide import QtCore
from PySide import QtGui

from shiboken import wrapInstance

# import ui

from arxSequencerManager import dialog, restoreDialog, app
reload(dialog)
reload(restoreDialog)
reload(app)

MyForm = app.MyForm()



class MyDialog(QtGui.QDialog, MyForm):

	def __init__(self, parent=None):
		self.count = 0
		#Setup Window
		super(MyDialog, self).__init__(parent)
		# QtGui.QWidget.__init__(self, parent)
		self.ui = dialog.Ui_Dialog()
		self.ui.setupUi(self)

		self.value = None

		self.initConnection()


	def initConnection(self) : 
		self.ui.b1_pushButton.clicked.connect(self.command1)
		self.ui.b2_pushButton.clicked.connect(self.command2)
		self.ui.b3_pushButton.clicked.connect(self.command3)

	def command1(self) : 
		result = str(self.ui.b1_pushButton.text())
		self.value = result
		self.close()
		


	def command2(self) : 
		result = str(self.ui.b2_pushButton.text())
		self.value = result
		self.close()



	def command3(self) : 
		result = str(self.ui.b3_pushButton.text())
		self.value = result
		self.close()


# backup dialog
class Dialog2(QtGui.QDialog, MyForm):

	def __init__(self, backupFile, parent=None):
		self.count = 0
		#Setup Window
		super(Dialog2, self).__init__(parent)
		# QtGui.QWidget.__init__(self, parent)
		self.ui = restoreDialog.Ui_restore_dialog()
		self.ui.setupUi(self)

		self.myApp = MyForm()
		self.backupLog = self.myApp.backupLog
		self.file = None
		self.backupFile = backupFile


		self.initFunctions()
		


	def initFunctions(self) : 
		self.listFile()
		self.ui.pushButton.clicked.connect(self.doRestore)
		self.ui.latest_checkBox.stateChanged.connect(self.listFile)



	def listFile(self) : 
		if os.path.exists(self.backupLog) : 
			files = fileUtils.listFile(self.backupLog)

			self.ui.listWidget.clear()

			if self.ui.latest_checkBox.isChecked() : 
				latestFile = sorted(files)[-1]
				self.ui.listWidget.addItem(latestFile)

			else : 

				for each in files : 
					print self.backupFile
					if self.backupFile in each : 
						self.ui.listWidget.addItem(each)


	def doRestore(self) : 
		sel = self.ui.listWidget.currentItem()

		if sel : 
			item = str(sel.text())

			self.file = item
			self.close()