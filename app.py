#Import python modules
import sys, os, re, shutil, urllib, subprocess, time

# import maya module
import maya.cmds as mc
import maya.mel as mm

# from PyQt4 import QtCore
# from PyQt4 import QtGui
# import sip
# from PyQt4.QtCore import *
# from PyQt4.QtGui import *

#Import GUI
from PySide import QtCore
from PySide import QtGui

from shiboken import wrapInstance

# import ui
from arxSequencerManager import ui as ui
reload(ui)

from arxSequencerManager import dialog
reload(dialog)

from tools.utils import config, fileUtils
reload(config)
reload(fileUtils)

from arxSequencerManager import customWidget as cw
reload(cw)

from arxSequencerManager import cameraRig
reload(cameraRig)

from arxSequencerManager import shiftFrame
reload(shiftFrame)

from sgUtils import sgUtils
reload(sgUtils)

moduleDir = sys.modules[__name__].__file__


# If inside Maya open Maya GUI
def getMayaWindow():
	ptr = mui.MQtUtil.mainWindow()
	return wrapInstance(long(ptr), QtGui.QWidget)
	# return sip.wrapinstance(long(ptr), QObject)

import maya.OpenMayaUI as mui
getMayaWindow()


class MyForm(QtGui.QMainWindow):

	def __init__(self, parent=None):
		self.count = 0
		#Setup Window
		super(MyForm, self).__init__(parent)
		# QtGui.QWidget.__init__(self, parent)
		self.ui = ui.Ui_SequencerManagerWindow()
		self.ui.setupUi(self)

		# custom variable
		self.configPath = '%s/config.txt' % os.path.split(moduleDir)[0]
		self.configData = config.readSetting(self.configPath)
		self.moduleDir = moduleDir
		self.iconPath = '%s/%s' % (os.path.split(self.moduleDir)[0], 'icons')
		self.defaultIcon = '%s/%s' % (self.iconPath, self.configData['defaultIcon'])
		self.defaultDuration = self.configData['defaultDuration']
		self.defaultStartFrame = self.configData['defaultStartFrame']

		self.cameraRigFile = self.configData['cameraRigFile']
		self.echo = True

		self.initFunctions()
		self.initConnections()



	def initFunctions(self) : 
		self.refreshUI()


	def initConnections(self) : 
		self.ui.refresh_pushButton.clicked.connect(self.refreshUI)
		self.ui.listWidget.itemSelectionChanged.connect(self.itemSelectCommand)
		self.ui.addShot_pushButton.clicked.connect(self.addShot)
		self.ui.before_radioButton.toggled.connect(self.setAutoInfo)
		self.ui.after_radioButton.toggled.connect(self.setAutoInfo)
		self.ui.last_radioButton.toggled.connect(self.setAutoInfo)
		self.ui.sequencer_pushButton.clicked.connect(self.openCameraSequencer)
		self.ui.apply_pushButton.clicked.connect(self.doShotEditDuration)
		self.ui.rebuildShot_pushButton.clicked.connect(self.rebuildSequencer)
		self.ui.camera_checkBox.stateChanged.connect(self.setUI)
		self.ui.moveShot_checkBox.stateChanged.connect(self.setUI)
		self.ui.start_lineEdit.returnPressed.connect(self.setAutoStartTime)
		self.ui.end_lineEdit.returnPressed.connect(self.setAutoEndTime)
		self.ui.duration_lineEdit.returnPressed.connect(self.setAutoDuration)
		self.ui.shiftFrame_pushButton.clicked.connect(self.shiftKeyFrame)
		self.ui.disableShot_pushButton.clicked.connect(self.toggledShot)
		self.ui.deleteShot_pushButton.clicked.connect(self.deleteShot)
		self.ui.auto_checkBox.stateChanged.connect(self.setAutoShotName)
		self.ui.noMove_checkBox.stateChanged.connect(self.setShotAutoDuration)


	def refreshUI(self) : 
		self.shotInfo = self.getShotInfo()
		self.listShots()
		self.setAutoInfo()
		self.setShotAutoDuration()
		self.setCameraList()
		self.setUI()


	def setUI(self) : 
		self.ui.camera_comboBox.setEnabled(self.ui.camera_checkBox.isChecked())
		self.ui.moveShot_lineEdit.setEnabled(self.ui.moveShot_checkBox.isChecked())
		self.ui.editStart_lineEdit.setEnabled(not self.ui.moveShot_checkBox.isChecked())
		self.ui.editEnd_lineEdit.setEnabled(not self.ui.moveShot_checkBox.isChecked())
		self.ui.moveShot_lineEdit.setText('0')
		self.setLogo()


	def setLogo(self) : 
		# set company logo
		logo = self.configData['logo']
		iconPath = '%s/%s' % (self.iconPath, logo)
		self.ui.logo_label.setPixmap(QtGui.QPixmap(iconPath).scaled(200, 40, QtCore.Qt.KeepAspectRatio))



	# command =============================================================================================

	def getShotInfo(self) : 
		shots = mc.ls(type = 'shot')
		shotInfo = dict()

		for eachShot in shots : 
			startTime = mc.shot(eachShot, q = True, startTime = True)
			endTime = mc.shot(eachShot, q = True, endTime = True)
			duration = mc.shot(eachShot, q = True, sourceDuration = True)
			sequenceStartTime = mc.shot(eachShot, q = True, sequenceStartTime = True)
			sequenceEndTime = mc.shot(eachShot, q = True, sequenceEndTime = True)
			status = mc.shot(eachShot, q = True, mute = True)

			shotInfo[eachShot] = {	'startTime': startTime, 
									'endTime': endTime, 
									'duration': duration, 
									'sequenceStartTime': sequenceStartTime, 
									'sequenceEndTime': sequenceEndTime, 
									'mute': status

									}

		return shotInfo



	def listShots(self) : 

		self.ui.listWidget.clear()

		if self.shotInfo : 
			for eachShot in sorted(self.shotInfo) : 

				shotName = eachShot 
				startTime = self.shotInfo[eachShot]['startTime']
				endTime = self.shotInfo[eachShot]['endTime']
				duration = self.shotInfo[eachShot]['duration']
				sequenceStartTime = self.shotInfo[eachShot]['sequenceStartTime']
				sequenceEndTime = self.shotInfo[eachShot]['sequenceEndTime']
				mute = self.shotInfo[eachShot]['mute']
				errorText = []

				text1 = str(shotName)
				text2 = str(startTime)
				text3 = str(duration)
				text4 = str(endTime)
				text5 = 'startTime'
				text6 = 'duration'
				text7 = 'endTime'
				text8 = ''
				text9 = ''


				color = [20, 20, 20]
				text1Color = [255, 255, 0]
				text2Color = [100, 180, 255]
				text3Color = [0, 200, 0]
				text4Color = [200, 0, 0]

				# check if disabled
				if mute : 
					color = [100, 20, 20]
					text9 = 'Disabled'


				# check if start and end frame is valid
				if startTime > endTime : 
					color = [100, 20, 20]
					errorText.append('Start/End frame')

				# check if shot stretch
				if not startTime == sequenceStartTime or not endTime == sequenceEndTime : 
					color = [100, 20, 20]
					errorText.append('Shot stretch')

				if duration <= 1 : 
					color = [100, 20, 20]
					errorText.append('Duration error ')

				if len(errorText) == 1 : 
					text8 = errorText[0]

				elif len(errorText) > 1 : 
					text8 = '%s errors' % len(errorText)

				print shotName

				for eachError in errorText : 
					self.printLog('Error %s' % eachError)

				
				texts = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
				textColors = [text1Color, text2Color, text2Color, text2Color, text3Color, text3Color, text3Color, text4Color, text4Color]

				self.addCustomListWidgetItem(texts, color, textColors, self.defaultIcon, 40)


	def itemSelectCommand(self) : 
		self.setEditField()
		self.setToggledMuteButton()
		self.setActiveCamera()



	def setEditField(self) : 
		# set editable field for startTime and endTime
		selectedItems = self.getSelectedWidgetItem()

		if selectedItems : 

			if len(selectedItems) == 1 : 
				startTime = int(float(selectedItems[0][1]))
				endTime = int(float(selectedItems[0][3]))

				duration = endTime - startTime + 1

				self.ui.editStart_lineEdit.setText(str(startTime))
				self.ui.editEnd_lineEdit.setText(str(endTime))
				self.ui.duration_label.setText(str(duration))

				self.setAutoInfo()

			else : 
				self.ui.editStart_lineEdit.clear()
				self.ui.editEnd_lineEdit.clear()



	def setToggledMuteButton(self) : 
		itemInfo = self.getCurrentWidgetItem()

		if itemInfo : 
			shotName = itemInfo[0]

			status = mc.shot(shotName, q = True, mute = True)

			if status : 
				self.ui.disableShot_pushButton.setText('Enable Selected Shot')

			else : 
				self.ui.disableShot_pushButton.setText('Disable Selected Shot')



	def setActiveCamera(self) : 
		itemInfo = self.getCurrentWidgetItem()

		if itemInfo : 
			shotName = itemInfo[0]
			startTime = itemInfo[1]

			if self.ui.activeShot_checkBox.isChecked() : 
				mc.sequenceManager(ct = startTime)



	def setAutoStartTime(self) : 
		startFrame = float(self.ui.start_lineEdit.text())
		endFrame = float(self.ui.end_lineEdit.text())
		duration = float(self.ui.duration_lineEdit.text())

		newEndFrame = startFrame + duration - 1
		newDuration = endFrame - startFrame + 1

		self.ui.end_lineEdit.setText(str(newEndFrame))


	def setAutoEndTime(self) : 
		startFrame = float(self.ui.start_lineEdit.text())
		endFrame = float(self.ui.end_lineEdit.text())
		duration = float(self.ui.duration_lineEdit.text())

		newStartFrame = endFrame - duration + 1
		newDuration = endFrame - startFrame + 1

		self.ui.duration_lineEdit.setText(str(newDuration))



	def setAutoDuration(self) : 
		startFrame = float(self.ui.start_lineEdit.text())
		endFrame = float(self.ui.end_lineEdit.text())
		duration = float(self.ui.duration_lineEdit.text())

		newStartFrame = endFrame - duration + 1
		newEndFrame = startFrame + duration - 1

		self.ui.end_lineEdit.setText(str(newEndFrame))


	def setAutoInfo(self) : 
		self.setAutoShotName()
		self.setShotAutoDuration()


	def setAutoShotName(self) : 
		# 1 item is selected

		self.ui.shotName_lineEdit.setEnabled(not self.ui.auto_checkBox.isChecked())

		if self.ui.auto_checkBox.isChecked() : 
			currentShot = None
			prevShot = None
			nextShot = None 

			allRow = self.ui.listWidget.count()

			# get last shot

			if self.shotInfo : 
				lastShot = self.getIndexWidgetItem(allRow - 1)[0]

				lastShotNum = re.findall('\d+', lastShot)[0]
				newLastShot = ((int(lastShotNum)/10) * 10) + 10

				padding = len(lastShotNum)

				tmp = '"%0' + str(padding) + 'd" % newLastShot' 
				newLastShotString = eval(tmp)

				newLastShotName = lastShot.replace(lastShotNum, newLastShotString)

			else : 
				newLastShotName = 'shot_010'

			if self.ui.last_radioButton.isChecked() : 
				self.ui.shotName_lineEdit.setText(newLastShotName)


			# if 1 item is selected

			if self.ui.listWidget.currentItem() : 
				currentIndex = self.ui.listWidget.currentRow()
				prevIndex = currentIndex - 1
				nextIndex = currentIndex + 1

				currentShot = self.getIndexWidgetItem(currentIndex)[0]

				if prevIndex >= 0 : 
					prevShot = self.getIndexWidgetItem(prevIndex)[0]

				if nextIndex <= allRow - 1 : 
					nextShot = self.getIndexWidgetItem(nextIndex)[0]


				# calculate shot
				# assume that shot has only one set of digit -> shot_0010
				currentShotNum = re.findall('\d+', currentShot)[0]
				padding = len(currentShotNum)

				if prevShot : 
					prevShotNum = re.findall('\d+', prevShot)[0]
					newPrevShot = (int(currentShotNum) + int(prevShotNum)) / 2

				else : 
					newPrevShot = int(currentShotNum) - 5

				if nextShot : 
					nextShotNum = re.findall('\d+', nextShot)[0]
					newNextShot = (int(currentShotNum) + int(nextShotNum)) / 2

				else : 
					newNextShot = int(currentShotNum) + 10


				tmp = '"%0' + str(padding) + 'd" % newPrevShot' 
				newPrevShotString = eval(tmp)

				tmp = '"%0' + str(padding) + 'd" % newNextShot' 
				newNextShotString = eval(tmp)

				

				newPrevShotName = currentShot.replace(currentShotNum, newPrevShotString)
				newNextShotName = currentShot.replace(currentShotNum, newNextShotString)
				

				# return data on choice from radioButton
				if self.ui.before_radioButton.isChecked() : 
					self.ui.shotName_lineEdit.setText(newPrevShotName)

				if self.ui.after_radioButton.isChecked() : 
					self.ui.shotName_lineEdit.setText(newNextShotName)


	def setShotAutoDuration(self) : 

		# if shot in camera sequencer 
		newStartFrame = int()
		newEndFrame = int()
		newDuration = int()

		if self.shotInfo : 

			if self.ui.last_radioButton.isChecked() : 
				# set for last shot
				allRow = self.ui.listWidget.count()

				# get last shot
				lastShotInfo = self.getIndexWidgetItem(allRow - 1)

				endFrame = int(float(lastShotInfo[3]))

				newStartFrame = endFrame + 1
				newEndFrame = newStartFrame + int(self.defaultDuration) - 1


			if self.ui.after_radioButton.isChecked() :
				if not self.ui.noMove_checkBox.isChecked() : 
					self.ui.start_lineEdit.setEnabled(False)

				else : 
					self.ui.start_lineEdit.setEnabled(True)

				# if select one item
				if self.ui.listWidget.currentItem() : 
					itemInfo = self.getCurrentWidgetItem()
					currentEndFrame = int(float(itemInfo[3]))
					newStartFrame = currentEndFrame + 1
					newEndFrame = newStartFrame + int(self.defaultDuration) - 1


			if self.ui.before_radioButton.isChecked() : 
				if not self.ui.noMove_checkBox.isChecked() : 
					self.ui.start_lineEdit.setEnabled(False)

				else : 
					self.ui.start_lineEdit.setEnabled(True)


				if self.ui.listWidget.currentItem() : 
					itemInfo = self.getCurrentWidgetItem()
					currentStartFrame = int(float(itemInfo[1]))
					newStartFrame = currentStartFrame
					newEndFrame = newStartFrame + int(self.defaultDuration) - 1



		else : 
			newStartFrame = int(self.defaultStartFrame)
			newEndFrame = newStartFrame + int(self.defaultDuration)
			
		self.ui.start_lineEdit.setText(str(newStartFrame))
		self.ui.end_lineEdit.setText(str(newEndFrame))
		self.ui.duration_lineEdit.setText(str(newEndFrame - newStartFrame + 1))



	def setCameraList(self) : 
		exception = ['persp', 'top', 'front', 'side']
		cameras = mc.listCameras()
		self.ui.camera_comboBox.clear()

		for each in cameras : 
			if not each in exception : 
				self.ui.camera_comboBox.addItem(each)


	# UI Command

	def openCameraSequencer(self) : 
		mm.eval('SequenceEditor')


	# make camera function
	def addShot(self) : 
		shotName = str(self.ui.shotName_lineEdit.text())
		startTime = float(self.ui.start_lineEdit.text())
		endTime = float(self.ui.end_lineEdit.text())
		duration = endTime - startTime + 1
		pushValue = duration

		currentIndex = self.ui.listWidget.currentRow()

		# push sequencer according to insert shot
		if not self.ui.noMove_checkBox.isChecked() : 
			if self.ui.after_radioButton.isChecked() : 
				self.moveShotCmd(currentIndex + 1, pushValue)

			if self.ui.before_radioButton.isChecked() : 
				self.moveShotCmd(currentIndex, pushValue)
		
		if not self.ui.camera_checkBox.isChecked() : 
			cam = cameraRig.referenceCamera(self.cameraRigFile, shotName)

			if cam : 
				cameraRig.setStartEndTime(shotName, startTime, endTime)
				shot = cameraRig.makeSequencerShot(shotName, cam, startTime, endTime)

				try : 
					cameraRig.linkCameraToShot(shotName, shot)

				except Exception as error : 
					print error

			# cameraRig.makeCameraRig(self.cameraRigFile, shotName, startTime, endTime)

		else : 
			self.createShotFromExistingCamera(shotName, startTime, endTime)



		self.refreshUI()


	def doShotEditDuration(self) : 
		# shot edit
		if not self.ui.moveShot_checkBox.isChecked() : 
			self.shotEditDurationCmd()

		else : 
			self.moveShot()



	def shotEditDurationCmd(self) : 

		# 1 item is selected
		if self.ui.listWidget.currentItem() : 

			itemInfo = self.getCurrentWidgetItem()

			itemIndex = int(self.ui.listWidget.currentRow())

			currentStartTime = int(float(itemInfo[1]))
			currentEndTime = int(float(itemInfo[3]))

			inputStartTime = int(str(self.ui.editStart_lineEdit.text()))
			inputEndTime = int(str(self.ui.editEnd_lineEdit.text()))

			count = self.ui.listWidget.count()

			cancel = False
			message = ''

			''' condition 1 extend shot 
			- extend sequencer
			- shiftFrame  
			'''

			if inputEndTime > currentEndTime : 
				extendFrame = inputEndTime - currentEndTime

				message2 = 'Extend %s frames. Please select extend options.' % extendFrame
				choice1 = 'Extend + Move key'
				choice2 = 'Extend'
				choice3 = 'Cancel'

				result = self.customMessageBox('Information', message2, choice1, choice2, choice3)

				if result == choice1 : 

					self.extendTailShot(itemIndex, extendFrame)
					shiftFrame.shiftKey('start', [currentEndTime + 1], extendFrame)
					message = 'Extend successful'


				if result == choice2 : 
					self.extendTailOverlap(itemIndex, extendFrame)
					message = 'Extend successful'

				if result == choice3 : 
					cancel = True


			''' condition 2 trim shot
			- trim sequencer
			- no frame shift
			'''

			if inputEndTime < currentEndTime : 
				trimFrame = inputEndTime
				lastItem = count - 1
				trimDuration = currentEndTime - inputEndTime

				result = self.messageBox('Confirm', 'Trim End Frame to %s?' % trimFrame)

				if result == QtGui.QMessageBox.Ok : 
					if self.ui.linkedShot_checkBox.isChecked() and not itemIndex == lastItem : 
						self.extendHeadShot(itemIndex + 1, trimDuration)

					else : 
						self.trimShot(itemIndex, trimFrame, False, True)
						message = 'Trim successful'


			''' condition 3 trim head
			- trim sequencer
			- no frame shift
			''' 

			if inputStartTime > currentStartTime : 
				trimFrame = inputStartTime
				trimDuration = inputStartTime - currentStartTime

				result = self.messageBox('Confirm', 'Trim Start Frame to %s?' % trimFrame)

				if result == QtGui.QMessageBox.Ok : 
					if self.ui.linkedShot_checkBox.isChecked() and not itemIndex == 0 : 
						self.extendTailOverlap(itemIndex - 1, trimDuration)

					else : 
						self.trimShot(itemIndex, trimFrame, True, False, False)
						message = 'Trim successful'


			''' condition 4 extend head
			- extend sequencer
			- no frame shift
			- push previous shot
			'''
			if inputStartTime < currentStartTime : 
				extendFrame = currentStartTime - inputStartTime

				result = self.messageBox('Confirm', 'Extend Start Frame to %s?' % inputStartTime)

				if result == QtGui.QMessageBox.Ok : 
					self.extendHeadShot(itemIndex, extendFrame)
					message = 'Extend successful'

			self.refreshUI()

			# if not cancel : 
			# 	self.completeDialog('Success', message)



	def toggledShot(self) : 
		itemInfo = self.getCurrentWidgetItem()

		if itemInfo : 
			shotName = itemInfo[0]

			status = mc.shot(shotName, q = True, mute = True)
			mc.shot(shotName, e = True, mute = (not status))

			self.refreshUI()


	def deleteShot(self) : 
		itemInfo = self.getCurrentWidgetItem()

		if itemInfo : 
			shotName = itemInfo[0]

			if mc.objExists(shotName) : 
				mc.delete(shotName)


			self.refreshUI()



	def moveShot(self) : 
		# selected shot
		index = self.ui.listWidget.currentRow()
		moveFrames = int(str(self.ui.moveShot_lineEdit.text()))

		self.moveShotCmd(index, moveFrames)


	def moveShotCmd(self, startIndex, frames) : 
		# find all items 

		if not frames == 0 : 

			count = self.ui.listWidget.count()
			startShot = self.getIndexWidgetItem(startIndex)
			startFrameShot = startShot[1]

			if frames > 0 : 
				countIndex = reversed(range(startIndex, count))
			
			if frames < 0 : 
				countIndex = range(startIndex, count)

			
			for i in countIndex : 
				itemInfo = self.getIndexWidgetItem(i)
				shotName = itemInfo[0]
				startFrame = float(itemInfo[1])
				endFrame = float(itemInfo[3])
				setStartFrame = startFrame + frames
				setEndFrame = endFrame + frames 

				self.editShotTime(shotName, setStartFrame, setEndFrame, True, True)

			shiftFrame.shiftKey('start', [startFrameShot], frames)

			self.refreshUI()



	def extendTailShot(self, currentIndex, extendFrame) : 
		# looking for all indexs
		count = self.ui.listWidget.count()

		for i in reversed(range(currentIndex, count)) : 
			itemInfo = self.getIndexWidgetItem(i)

			endTime = float(itemInfo[3]) + extendFrame
			startTime = float(itemInfo[1]) + extendFrame
			shotName = itemInfo[0]

			# if currentItem, don't adjust startTime
			if i == currentIndex : 
				startTime = float(itemInfo[1])

			self.editShotTime(shotName, startTime, endTime)

		# self.editShotTime(currentShotName, currentStartFrame, currentEndFrame + extendFrame)


	def extendTailOverlap(self, currentIndex, extendFrame) : 
		lastItem = int(self.ui.listWidget.count()) - 1

		itemInfo = self.getIndexWidgetItem(currentIndex)
		shotName = itemInfo[0]
		startTime = float(itemInfo[1])
		endTime = float(itemInfo[3])
		setEndTime = endTime + extendFrame


		if not currentIndex == lastItem : 
			nItemInfo = self.getIndexWidgetItem(currentIndex + 1)
			nShotName = nItemInfo[0]
			nStartTime = float(nItemInfo[1])
			nEndTime = float(nItemInfo[3])

			# calculate space 
			spaceShot = nStartTime - endTime - 1

			# no space
			if spaceShot == 0 : 
				nnStartTime = nStartTime + extendFrame

			# space shot
			else : 
				nnStartTime = nStartTime + extendFrame - spaceShot

			# check if extend more than next shot duration			
			if nnStartTime < nEndTime - 1 : 				
				self.editShotTime(nShotName, nnStartTime, nEndTime, True, False, False)
				self.editShotTime(shotName, startTime, setEndTime, False, True, False)

			else : 
				setEndTime = nEndTime - 2 
				self.editShotTime(nShotName, nnStartTime, nEndTime, True, False, False)
				self.editShotTime(shotName, startTime, setEndTime, False, True, False)

		else : 
			self.editShotTime(shotName, startTime, setEndTime, False, True, False)



	def extendHeadShot(self, currentIndex, extendFrame) : 
		# current ================================================

		itemInfo = self.getIndexWidgetItem(currentIndex)

		startTime = float(itemInfo[1]) - extendFrame
		endTime = float(itemInfo[3])
		shotName = itemInfo[0]

		if not currentIndex == 0 : 
			startIndex = currentIndex - 1

			if startIndex < 0 : 
				startIndex = 0

			# previous item 

			itemInfo = self.getIndexWidgetItem(startIndex)

			pStartTime = float(itemInfo[1])
			pEndTime = float(itemInfo[3]) - extendFrame
			pShotName = itemInfo[0]
			

			# check if extend range overlapping prevShot
			spaceShot = startTime - pEndTime - 1

			if spaceShot == 0 : 
				self.editShotTime(pShotName, pStartTime, pEndTime)
				self.editShotTime(shotName, startTime, endTime)

			else : 
				npEndTime = pEndTime + spaceShot

				# trim is not more than previous shot duration
				if npEndTime > pStartTime : 
					self.editShotTime(pShotName, pStartTime, npEndTime)
					self.editShotTime(shotName, startTime, endTime)

				# if trim is more than previuos shot duration, trim to only minimal duration allow
				else : 
					self.editShotTime(pShotName, pStartTime, pStartTime+1)
					self.editShotTime(shotName, pStartTime+2, endTime)


		else : 
			self.editShotTime(shotName, startTime, endTime)






	def trimShot(self, currentIndex, trimFrame, setStart, setEnd, sequencePriority = True) : 

		shotName = self.getIndexWidgetItem(currentIndex)[0]
		start = 0
		end = 0

		if setStart : 
			start = trimFrame

		if setEnd : 
			end = trimFrame

		self.editShotTime(shotName, start, end, setStart, setEnd, sequencePriority)


	def editShotTime(self, shotName, start, end, setStart = True, setEnd = True, sequencePriority = True) : 

		ctrl = '%s_camera_ctrl' % shotName

		if setStart : 
			if sequencePriority : 
				mc.setAttr('%s.sequenceStartFrame' % shotName, start)
				mc.setAttr('%s.startFrame' % shotName, start)

			else : 
				mc.setAttr('%s.startFrame' % shotName, start)
				mc.setAttr('%s.sequenceStartFrame' % shotName, start)

			self.printLog('%s set startFrame %s' % (shotName, start)) 

		if setEnd : 
			if sequencePriority : 
				mc.setAttr('%s.sequenceEndFrame' % shotName, end)
				mc.setAttr('%s.endFrame' % shotName, end)

			else : 
				mc.setAttr('%s.endFrame' % shotName, end)
				mc.setAttr('%s.sequenceEndFrame' % shotName, end)

			self.printLog('%s sest endFrame %s' % (shotName, end))


	def rebuildSequencer(self) : 
		# list current shot
		shots = mc.ls(type = 'shot')

		for eachShot in shots : 
			self.printLog('Reading %s ...' % eachShot)

			startTime = mc.shot(eachShot, q = True, st = True)
			endTime = mc.shot(eachShot, q = True, et = True)
			sequenceStartTime = mc.shot(eachShot, q = True, sst = True)
			sequenceEndTime = mc.shot(eachShot, q = True, set = True)
			currentCamera = mc.shot(eachShot, q = True, cc = True)

			mc.delete(eachShot)

			self.printLog('Delete %s' % eachShot)

			cameraRig.makeSequencerShot(eachShot, currentCamera, startTime, endTime)
			self.printLog('Create %s' % eachShot)
			
			try : 
				cameraRig.linkCameraToShot(eachShot, eachShot)
				self.printLog('Linked camera rig to shot %s' % eachShot)

			except Exception as error : 
				print error


		self.completeDialog('Complete', 'Rebuilt shot complete. See script editor for details')



	def shiftKeyFrame(self) : 
		frames = int(self.ui.frame_lineEdit.text())
		currentFrame = mc.currentTime(q = True)

		if not frames == 0 : 
			if not self.ui.currentStart_checkBox.isChecked() : 
				shiftFrame.shiftKey('default', [1, 10000], frames)

			else : 
				shiftFrame.shiftKey('start', [currentFrame], frames)



	def createShotFromExistingCamera(self, shotName, startTime, endTime) : 
		camera = str(self.ui.camera_comboBox.currentText())

		shot = cameraRig.makeSequencerShot(shotName, camera, startTime, endTime)

		try : 
			cameraRig.linkCameraToShot(shotName, shot)
			pass

		except Exception as error : 
			print error


	# UI widget 

	def addCustomListWidgetItem(self, texts, color, textColors, iconPath, size = 90) : 

		myCustomWidget = cw.customQWidgetItem()
		myCustomWidget.setTexts(texts)

		myCustomWidget.setTextColors(textColors)


		# myCustomWidget.setIcon(iconPath, size)

		item = QtGui.QListWidgetItem(self.ui.listWidget)

		item.setSizeHint(myCustomWidget.sizeHint())
		self.ui.listWidget.addItem(item)
		self.ui.listWidget.setItemWidget(item, myCustomWidget)
		item.setBackground(QtGui.QColor(color[0], color[1], color[2]))


	def getCurrentWidgetItem(self) : 
		item = self.ui.listWidget.currentItem()

		if item : 
			customWidget = self.ui.listWidget.itemWidget(item)
			itemInfo = customWidget.texts()

			return itemInfo


	def getIndexWidgetItem(self, index) : 
		item = self.ui.listWidget.item(index)
		customWidget = self.ui.listWidget.itemWidget(item)
		itemInfo = customWidget.texts()

		return itemInfo



	def getSelectedWidgetItem(self) : 
		items = self.ui.listWidget.selectedItems()
		allTexts = []

		for item in items : 
			customWidget = self.ui.listWidget.itemWidget(item)

			texts = customWidget.texts()
			allTexts.append(texts)

			return allTexts


	def getAllListWidgetItems(self) : 

		count = self.ui.listWidget.count()
		items = []

		for i in range(count) : 
			item = self.ui.listWidget.item(i)
			customWidget = self.ui.listWidget.itemWidget(item)
			texts = customWidget.texts()
			items.append(texts)


		return items



	def messageBox(self, title, description) : 
		result = QtGui.QMessageBox.question(self,title,description ,QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)

		return result


	def completeDialog(self, title, dialog) : 
		QtGui.QMessageBox.information(self, title, dialog, QtGui.QMessageBox.Ok)



	def customMessageBox(self, title, description, label1, label2, label3) : 
		myDialog = MyDialog()
		myDialog.setWindowTitle(title)
		myDialog.ui.text_label.setText(description)
		myDialog.ui.b1_pushButton.setText(label1)
		myDialog.ui.b2_pushButton.setText(label2)
		myDialog.ui.b3_pushButton.setText(label3)
		myDialog.exec_()
		return myDialog.value


	def printLog(self, message, echo = True) : 
		if echo : 
			print message

		
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




