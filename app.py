#Import python modules
import sys, os, re, shutil, urllib, subprocess, time

from datetime import datetime

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

from arxSequencerManager import dialog, restoreDialog
reload(dialog)
reload(restoreDialog)

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
		self.shotPrefix = self.configData['shotPrefix']
		self.shotPadding = self.configData['shotPadding']
		self.sequencePrefix = self.configData['sequencePrefix']

		self.cameraRigFile = self.configData['cameraRigFile']

		self.backupLog = self.configData['backupLog']
		self.scriptLogs = self.configData['scriptLog']
		self.backupFile = None

		self.readShotgun = True
		self.echo = True
		self.sgData = None

		self.initFunctions()
		self.initConnections()



	def initFunctions(self) : 
		self.setShotgun()
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
		self.ui.start_lineEdit.editingFinished.connect(self.setAutoStartTime)
		self.ui.end_lineEdit.editingFinished.connect(self.setAutoEndTime)
		self.ui.duration_lineEdit.editingFinished.connect(self.setAutoDuration)
		self.ui.shiftFrame_pushButton.clicked.connect(self.shiftKeyFrame)
		self.ui.disableShot_pushButton.clicked.connect(self.toggledShot)
		self.ui.deleteShot_pushButton.clicked.connect(self.deleteShot)
		self.ui.auto_checkBox.stateChanged.connect(self.setAutoShotName)
		self.ui.noMove_checkBox.stateChanged.connect(self.setShotAutoDuration)
		self.ui.pullShotgun_pushButton.clicked.connect(self.pullShotgunData)
		self.ui.pushShotgun_pushButton.clicked.connect(self.pushShotgunData)
		self.ui.restoreShotgun_pushButton.clicked.connect(self.restoreBackup)


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
		self.ui.prefix_lineEdit.setText(self.shotPrefix)
		self.ui.prefix_lineEdit.setEnabled(False)


	def setLogo(self) : 
		# set company logo
		logo = self.configData['logo']
		iconPath = '%s/%s' % (self.iconPath, logo)
		self.ui.logo_label.setPixmap(QtGui.QPixmap(iconPath).scaled(200, 40, QtCore.Qt.KeepAspectRatio))


	def setShotgun(self) : 
		self.setProjectInfo()

		if self.readShotgun : 
			self.sgData = self.getShotgunData()



	def setProjectInfo(self) : 
		currentScene = mc.file(q = True, sn = True)

		if currentScene : 
			path = os.path.splitdrive(currentScene)[-1]
			pathEles = path.split('/')

			project = pathEles[2]
			episode = pathEles[4]
			sequence = pathEles[6]
			shotType = pathEles[7]

			self.ui.project_label.setText('%s_%s' % (project, episode))
			self.ui.episode_label.setText(episode)
			self.ui.sequence_label.setText(sequence)
			self.ui.shot_label.setText(shotType)



	def getShotgunData(self) : 
		project = str(self.ui.project_label.text())
		sequenceName = str(self.ui.sequence_label.text())

		sequenceInfo = sgUtils.sgGetShotTime(project, sequenceName)
		dictInfo = dict()

		sqPrefix = self.sequencePrefix
		shotPrefix = self.shotPrefix

		if sequenceInfo : 
			for each in sequenceInfo : 
				sgShotName = each['code']

				# sg shot e100_040_010 -> episode_sequence_shot convert to shot_010
				shotName = '%s%s' % (self.shotPrefix, sgShotName.split('_')[-1])

				if not 'layout' in sgShotName : 
					dictInfo[shotName] = each

			return dictInfo



	def getShotgunAllSequencesData(self) : 
		project = str(self.ui.project_label.text())
		sequenceName = str(self.ui.sequence_label.text())

		sequenceInfo = sgUtils.sgGetAllShotTime(project)
		allSeqInfo = dict()

		sqPrefix = self.sequencePrefix

		if sequenceInfo : 
			for each in sequenceInfo : 
				sgSequenceName = each['sg_sequence']['name']

				if not sgSequenceName in allSeqInfo.keys() : 
					allSeqInfo[sgSequenceName] = [each]

				else : 
					allSeqInfo[sgSequenceName].append(each)



		return allSeqInfo


	def pullShotgunData(self) : 
		self.readShotgun = True
		self.setShotgun()
		self.refreshUI()


	def pushShotgunData(self) : 	
		self.backupFile = self.startBackupFile()
		# update cut in, cut out
		result = self.pushMayaSgCut()

		# update timeline_in, timeline_out
		if result : 
			result2 = self.updateTimelineDuration()

			if result2 : 
				self.completeDialog('Success', 'Update shotgun success!')

		self.refreshUI()



	def pushMayaSgCut(self) : 
		# pushing maya cut information to shotgun

		# load shotgun data again
		self.pullShotgunData()
	
		# load all items from listWidget
		allItems = self.getAllListWidgetItems()
		sgData = self.sgData

		project = str(self.ui.project_label.text())
		episode = str(self.ui.episode_label.text())
		sequenceName = str(self.ui.sequence_label.text()).replace(self.sequencePrefix, '')
		error = False
		errorInfo = []

		batch_data = []
		self.batch_dataBackup = []

		'''check all shot in scene =======================================================================
		# if exists in shotgun, update. if not, create

		check in scene compare to shotgun'''

		for eachShot in allItems : 
			data = dict()
			shotName = eachShot[0]
			sgCutIn = int(float(eachShot[1]))
			sgCutOut = int(float(eachShot[3]))
			sgDuration = int(float(eachShot[2]))
			shotStatus = eachShot[8]
			errorMessage = eachShot[7]

			data.update({'sg_cut_in': sgCutIn})
			data.update({'sg_cut_out': sgCutOut})
			data.update({'sg_cut_duration': sgDuration})

			# error message, set error status to true
			if not errorMessage == '' : 
				error = True
				errorInfo.append('%s-%s' % (shotName, errorMessage))

			
			# if this is an active shot
			if shotStatus == '' : 
				
				# if shotname is in shotgun data
				if shotName in self.sgData.keys() : 
					# valid shot 
					# update

					entityID = self.sgData[shotName]['id']

					# set working status to ip = "in progress"
					data.update({'sg_status_list': 'ip'})
					batch_data.append({"request_type":"update","entity_type":"Shot","entity_id":entityID, "data":data})	
					
					self.printLog('%s will be updated' % shotName)

				
				# if shotname is not in shotgun data
				else : 
					# shot not exists 
					# create shot

					# set working status to ip
					data.update({'sg_status_list': 'ip'})
					batch_data.append({"request_type":"create","entity_type":"Asset","data":data})
					
					self.printLog('%s does not exists, shot will be created.' % shotName)


			# this shot is disabled
			elif shotStatus == 'Disabled' : 

				# if shotName in shotgun already
				if shotName in self.sgData.keys() : 

					entityID = self.sgData[shotName]['id']

					# set status to omit
					data.update({'sg_status_list': 'omt'})
					batch_data.append({"request_type":"update","entity_type":"Shot","entity_id":entityID, "data":data})	

					self.printLog('%s will be set to "omit".' % shotName)


		
		''' check in shotgun compare to in scene =========================================================================

		'''
		# check if any shot in shotgun not in the scene 
		for each in self.sgData : 
			data = dict()
			data2 = dict()
			entityID = self.sgData[each]['id']


			if not each in [eachItem[0] for eachItem in allItems] : 
				data.update({'sg_status_list': 'omt'})
				batch_data.append({"request_type":"update","entity_type":"Shot","entity_id":entityID, "data":data})	


				self.printLog('%s not in the scene, status will be set to omit' % shotName)

			
			''' gather data for backup '''
			# send to log
			data2.update({'sg_cut_in': self.sgData[each]['sg_cut_in']})
			data2.update({'sg_cut_out': self.sgData[each]['sg_cut_out']})
			data2.update({'sg_cut_duration': self.sgData[each]['sg_cut_duration']})
			data2.update({'sg_status_list': self.sgData[each]['sg_status_list']})
			data2.update({'sg_timeline_in': self.sgData[each]['sg_timeline_in']})
			data2.update({'sg_timeline_out': self.sgData[each]['sg_timeline_out']})
			self.batch_dataBackup.append({"request_type":"update","entity_type":"Shot","entity_id":entityID, "data":data2})
		

		''' all data is ready ===========================================================================
		do actual command 
		'''

		# if nothing error, update shotgun
		if not error : 
			result = self.messageBox('Update all shotgun cut data', 'Update all shotgun cut data might take several minutes. \nDo you want to proceed?')

			if result == QtGui.QMessageBox.Ok : 

				# backup data to log
				self.backupData()

				# run command
				sgResult = self.sgBatch(batch_data)	

				return sgResult

		else : 
			message = str()
			for each in errorInfo : 
				message += str('Error: %s\n' % each)

			message+= '\nPlease fix before update data.'
			self.completeDialog('Error', message)



	def updateTimelineDuration(self) : 
		# update premiere duration for all sequence after current sequence
		self.allSeqInfo = self.getShotgunAllSequencesData()

		# find current sequence
		currentSequence = str(self.ui.sequence_label.text())
		affectedSequence = []
		seqCount = 0
		pTimelineOut = 0
		logs = []
		batch_data = []

		for eachSequence in sorted(self.allSeqInfo) : 
			startShot = int()
			curSeq = int(currentSequence.replace(self.sequencePrefix, ''))

			if self.sequencePrefix in eachSequence : 
				eachSeq = int(eachSequence.replace(self.sequencePrefix, ''))

				# if eachSequence >= this sequence, add in to calculate sequences
				if eachSeq >= curSeq : 
					affectedSequence.append(eachSequence)
					logs.append(eachSequence)
					self.printLog(eachSequence)

					shotCount = 0
					nTimelineIn = 0
					nTimelineOut = 0

					for eachShot in sorted(self.allSeqInfo[eachSequence]) : 
						shotName = eachShot['code']
						timelineIn = eachShot['sg_timeline_in']
						timelineOut = eachShot['sg_timeline_out']
						duration = eachShot['sg_cut_duration']
						entityID = eachShot['id']
						data = dict()
						dataBk = dict()

						if not 'layout'	in shotName : 

							if seqCount == 0 and shotCount == 0 : 
								# print 'This is start shot %s %s' % (eachSequence, shotName)
								timelineInStart = timelineIn
								nTimelineIn = timelineInStart
								nTimelineOut = nTimelineIn + duration
								pTimelineOut = nTimelineOut

							else : 
								nTimelineIn = pTimelineOut
								nTimelineOut = nTimelineIn + duration
								pTimelineOut = nTimelineOut

							message = '%s %s-%s -> %s-%s %s' % (shotName, timelineIn, timelineOut, nTimelineIn, nTimelineOut, duration)
							self.printLog(message)
							logs.append(message)

							# shotgun command 
							data.update({'sg_timeline_in': nTimelineIn})
							data.update({'sg_timeline_out': nTimelineOut})
							batch_data.append({"request_type":"update","entity_type":"Shot","entity_id":entityID, "data":data})

							# shotgun command backup
							dataBk.update({'sg_timeline_in': timelineIn})
							dataBk.update({'sg_timeline_out': timelineOut})
							self.batch_dataBackup.append({"request_type":"update","entity_type":"Shot","entity_id":entityID, "data":dataBk})


							shotCount += 1

					seqCount += 1

		self.writeLog(str(('\n\r').join(logs)))

		# backup data
		self.backupData()

		# run command
		result = self.sgBatch(batch_data)

		return result



	def sgBatch(self, batch_data) : 
		from sgUtils import sgUtils
		reload(sgUtils)

		result = sgUtils.sg.batch(batch_data)

		return result



	def startBackupFile(self) : 
		project = str(self.ui.project_label.text())
		sequenceName = str(self.ui.sequence_label.text()).replace(self.sequencePrefix, '')
		backupFile = '%s_%s_%s' % (project, sequenceName, str(datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0])

		backupFile = '%s/%s' % (self.backupLog, backupFile)

		if not os.path.exists(self.backupLog) : 
			os.makedirs(self.backupLog)

		dst = backupFile
		data = '[]'
		fileUtils.writeFile(dst, data)

		return backupFile


	def backupData(self) : 

		if os.path.exists(self.backupFile) : 
			data = eval(fileUtils.readFile(self.backupFile))
			data = data + self.batch_dataBackup
			result = fileUtils.writeFile(self.backupFile, str(data))

			return result


	def restoreBackup(self) : 
		project = str(self.ui.project_label.text())
		sequenceName = str(self.ui.sequence_label.text()).replace('sq', '')
		fileName = '%s_%s' % (project, sequenceName)

		dst = self.backupLog
		files = fileUtils.listFile(dst)
		validFiles = []

		myDialog = Dialog2(self.backupLog)
		myDialog.exec_()

		selFile = myDialog.file

		if selFile : 

			restoreFile = '%s/%s' % (self.backupLog, selFile)

			batch_data = eval(fileUtils.readFile(restoreFile))

			result = self.messageBox('Restore previous update', 'Restore previous update shotgun data %s. \nDo you want to proceed?' % selFile)

			if result == QtGui.QMessageBox.Ok : 

				result = sgUtils.sg.batch(batch_data)

				self.completeDialog('Success', 'Restore previous data success.')




	# command =============================================================================================

	def getShotInfo(self) : 
		shots = mc.ls(type = 'shot')
		shotInfo = dict()
		i = 0

		for eachShot in shots : 
			startTime = mc.shot(eachShot, q = True, startTime = True)
			endTime = mc.shot(eachShot, q = True, endTime = True)
			duration = mc.shot(eachShot, q = True, sourceDuration = True)
			sequenceStartTime = mc.shot(eachShot, q = True, sequenceStartTime = True)
			sequenceEndTime = mc.shot(eachShot, q = True, sequenceEndTime = True)
			status = mc.shot(eachShot, q = True, mute = True)
			gapStart = False
			gapEnd = False

			if not i == 0 : 
				previousEndFrame = mc.shot(shots[i-1], q = True, endTime = True)

				if not (startTime - previousEndFrame) == 1 : 
					gapStart = True


			if not i == (len(shots) - 1) : 
				nextShotStartFrame = mc.shot(shots[i+1], q = True, startTime = True)

				if not (nextShotStartFrame - endTime) == 1 : 
					gapEnd = True



			shotInfo[eachShot] = {	'startTime': startTime, 
									'endTime': endTime, 
									'duration': duration, 
									'sequenceStartTime': sequenceStartTime, 
									'sequenceEndTime': sequenceEndTime, 
									'mute': status, 
									'gap': [gapStart, gapEnd]

									}

			i+=1

		return shotInfo



	def listShots(self) : 

		self.ui.listWidget.clear()

		episode = str(self.ui.episode_label.text())
		sequenceName = str(self.ui.sequence_label.text())


		if self.shotInfo : 
			self.occupiedFrame = []

			for eachShot in sorted(self.shotInfo) : 

				shotName = eachShot 
				startTime = self.shotInfo[eachShot]['startTime']
				endTime = self.shotInfo[eachShot]['endTime']
				duration = self.shotInfo[eachShot]['duration']
				sequenceStartTime = self.shotInfo[eachShot]['sequenceStartTime']
				sequenceEndTime = self.shotInfo[eachShot]['sequenceEndTime']
				mute = self.shotInfo[eachShot]['mute']
				gap = self.shotInfo[eachShot]['gap']
				errorText = []
				overlapStatus = False

				# calculate occupiedFrame
				for i in range(int(startTime), int(endTime) + 1) : 
					if not i in self.occupiedFrame : 
						self.occupiedFrame.append(i)

					else : 
						overlapStatus = True			

				text1 = str(shotName)
				text2 = str(startTime)
				text3 = str(duration)
				text4 = str(endTime)
				text5 = 'startTime'
				text6 = 'duration'
				text7 = 'endTime'
				text8 = ''
				text9 = ''


				# read shotgun data
				if self.readShotgun : 
					sgData = self.sgData
					info = sgData[shotName]
					sgCutIn = info['sg_cut_in']
					sgCutOut = info['sg_cut_out']
					sgTimelineIn = info['sg_timeline_in']
					sgTimelineOut = info['sg_timeline_out']
					sgDuration = info['sg_cut_duration']
					text5 = str(sgCutIn)
					text6 = str(sgDuration)
					text7 = str(sgCutOut)

					# if not str(startTime) == str(sgCutIn) : 
					# 	errorText.append('sg not sync')
					# 	self.printLog('Error: sg_cut_in not sync')

					# if not str(endTime) == str(sgCutOut) : 
					# 	if not 'sg not sync' in errorText : 
					# 		errorText.append('sg not sync')
					# 		self.printLog('Error: sg_cut_out not sync')


				color = [20, 20, 20]
				text1Color = [255, 255, 0]
				text2Color = [100, 180, 255]
				text3Color = [100, 180, 255]
				text4Color = [100, 180, 255]
				text5Color = [0, 200, 0]
				text6Color = [0, 200, 0]
				text7Color = [0, 200, 0]
				text8Color = [200, 0, 0]
				text9Color = [200, 0, 0]

				textIndex = 0
				textBgColor = [0, 0, 0]

				# check if disabled
				if mute : 
					color = [100, 20, 20]
					text9 = 'Disabled'


				# error path =================================================================
				# check if start and end frame is valid
				if startTime > endTime : 
					color = [100, 20, 20]
					errorText.append('Start/End frame')

				# check if shot stretch
				if not startTime == sequenceStartTime or not endTime == sequenceEndTime : 
					color = [100, 20, 20]
					print startTime, sequenceStartTime, endTime, sequenceEndTime
					errorText.append('Shot stretch')

				if duration <= 1 : 
					color = [100, 20, 20]
					errorText.append('Duration error ')

				if overlapStatus : 
					color = [100, 20, 20]
					errorText.append('Overlaping shot')

				if len(errorText) == 1 : 
					text8 = errorText[0]

				elif len(errorText) > 1 : 
					text8 = '%s errors' % len(errorText)


				for eachError in errorText : 
					self.printLog('Error %s' % eachError)


				# checking for gap start and end
				if gap[0] : 
					text2Color = [180, 30, 30]

				if gap[1] : 
					text4Color = [180, 30, 30]


				# display ========================================================================

				
				texts = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
				textColors = [text1Color, text2Color, text3Color, text4Color, text5Color, text6Color, text7Color, text8Color, text9Color]

				self.addCustomListWidgetItem(texts, color, textColors, self.defaultIcon, 40, textIndex, textBgColor)


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
			prefix = self.shotPrefix

			allRow = self.ui.listWidget.count()

			# get last shot

			if self.shotInfo : 
				lastShot = self.getIndexWidgetItem(allRow - 1)[0]

				# get digit ####
				lastShotNum = re.findall('\d+', lastShot)[0]

				# calculate last shot
				newLastShot = ((int(lastShotNum)/10) * 10) + 10

				# calculate padding
				padding = len(lastShotNum)

				# insert padding
				tmp = '"%0' + str(padding) + 'd" % newLastShot' 
				newLastShotString = eval(tmp)

				# replace existing digit by new digit
				# 010 replace by 020 -> shot_020
				newLastShotName = lastShot.replace(lastShotNum, newLastShotString)

				# get prefix 
				prefix = lastShot.replace(lastShotNum, '')

			else : 
				# shot_010
				newLastShotName = '%s' % prefix
				newLastShotString = '010'


			if self.ui.last_radioButton.isChecked() : 
				self.ui.prefix_lineEdit.setText(prefix)
				self.ui.shotName_lineEdit.setText(newLastShotString)


			if self.shotInfo : 
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

					

					pPrefix = currentShot.replace(currentShotNum, '')
					newPrevShotName = currentShot.replace(currentShotNum, newPrevShotString)

					nPrefix = currentShot.replace(currentShotNum, '')
					newNextShotName = currentShot.replace(currentShotNum, newNextShotString)
					

					# return data on choice from radioButton
					if self.ui.before_radioButton.isChecked() : 
						self.ui.prefix_lineEdit.setText(pPrefix)
						self.ui.shotName_lineEdit.setText(newPrevShotString)

					if self.ui.after_radioButton.isChecked() : 
						self.ui.prefix_lineEdit.setText(nPrefix)
						self.ui.shotName_lineEdit.setText(newNextShotString)


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
		prefix = str(self.ui.prefix_lineEdit.text())
		shotNumber = int(str(self.ui.shotName_lineEdit.text()))
		tmp = '"%0' + str(self.shotPadding) + 'd" % shotNumber' 
		shotNumberStr = eval(tmp)
		shotName = '%s%s' % (prefix, str(self.ui.shotName_lineEdit.text()))

		startTime = float(self.ui.start_lineEdit.text())
		endTime = float(self.ui.end_lineEdit.text())
		duration = endTime - startTime + 1
		pushValue = duration
		frameList = [i for i in range(int(startTime), int(endTime) + 1)]
		overlapStatus = False

		currentIndex = self.ui.listWidget.currentRow()

		# push sequencer according to insert shot
		if not self.ui.noMove_checkBox.isChecked() : 
			if self.ui.after_radioButton.isChecked() : 
				self.moveShotCmd(currentIndex + 1, pushValue)

			if self.ui.before_radioButton.isChecked() : 
				self.moveShotCmd(currentIndex, pushValue)
		
		if not self.ui.camera_checkBox.isChecked() : 
			if self.ui.noMove_checkBox.isChecked() : 
				for i in frameList : 
					if i in self.occupiedFrame : 
						overlapStatus = True

			if not overlapStatus : 
				cam = cameraRig.referenceCamera(self.cameraRigFile, shotName)

				if cam : 
					cameraRig.setStartEndTime(shotName, startTime, endTime)
					shot = cameraRig.makeSequencerShot(shotName, cam, startTime, endTime)

					try : 
						cameraRig.linkCameraToShot(shotName, shot)

					except Exception as error : 
						print error

			else : 
				self.completeDialog('Error', 'Cannot crate verlapping shot')

			# cameraRig.makeCameraRig(self.cameraRigFile, shotName, startTime, endTime)

		else : 
			self.createShotFromExistingCamera(shotName, startTime, endTime)



		self.refreshUI()


	def doShotEditDuration(self) : 
		# shot edit
		try : 
			if not self.ui.moveShot_checkBox.isChecked() : 
				self.shotEditDurationCmd()

			else : 
				self.moveShot()

		except Exception as error : 
			self.completeDialog('Error', 'Shots are locked and cannot be modified. Please try Rebuild Shot')
			print error



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

			self.ui.listWidget.itemSelectionChanged.disconnect(self.itemSelectCommand)
			self.refreshUI()
			self.ui.listWidget.itemSelectionChanged.connect(self.itemSelectCommand)



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

	def addCustomListWidgetItem(self, texts, color, textColors, iconPath, size = 90, textIndex = 0, textBgColor = [0, 0, 0]) : 

		myCustomWidget = cw.customQWidgetItem()
		myCustomWidget.setTexts(texts)

		myCustomWidget.setTextColors(textColors)


		if not textIndex == 0 : 
			myCustomWidget.setBackgroundColor(textIndex, textBgColor)

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



	def writeLog(self, data) : 
		if not os.path.exists(self.scriptLogs) : 
			os.makedirs(self.scriptLogs)

		logFile = 'arxSequenceManagerLog_%s.txt' % (str(datetime.now()).replace(' ', '_').replace(':', '-').split('.')[0])
		dst = '%s/%s' % (self.scriptLogs, logFile)
		result = fileUtils.writeFile(dst, data)

		self.printLog('log created %s' % dst)

		return result

		
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

	def __init__(self, backupPath, parent=None):
		self.count = 0
		#Setup Window
		super(Dialog2, self).__init__(parent)
		# QtGui.QWidget.__init__(self, parent)
		self.ui = restoreDialog.Ui_restore_dialog()
		self.ui.setupUi(self)

		self.backupLog = backupPath
		self.file = None
		self.initFunctions()


	def initFunctions(self) : 
		self.listFile()
		self.ui.pushButton.clicked.connect(self.doRestore)



	def listFile(self) : 
		if os.path.exists(self.backupLog) : 
			files = fileUtils.listFile(self.backupLog)

			self.ui.listWidget.clear()

			for each in files : 
				self.ui.listWidget.addItem(each)



	def doRestore(self) : 
		sel = self.ui.listWidget.currentItem()

		if sel : 
			item = str(sel.text())

			self.file = item
			self.close()
