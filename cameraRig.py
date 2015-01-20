import maya.cmds as mc
import maya.mel as mm


def makeCameraRig(path, shotName, startTime, endTime) : 
	cam = referenceCamera(path, shotName)

	if cam : 
		setStartEndTime(shotName, startTime, endTime)
		shot = makeSequencerShot(shotName, cam, startTime, endTime)
		linkCameraToShot(shotName, shot)

		return shotName


def referenceCamera(camRigFile, shotName) : 
	camera = '%s_cam' % shotName

	if not mc.objExists(camera) : 
		result = mc.file(camRigFile, r=1, type = 'mayaAscii', mnc=0, rpr=shotName)
	
		return camera


def makeSequencerShot(shotName, camera, startTime, endTime) : 
	result = mc.shot(shotName, startTime = startTime, endTime = endTime, sequenceStartTime = startTime, sequenceEndTime = endTime, currentCamera = camera)

	return result

def linkCameraToShot(camera, shotName) : 
	ctrl = '%s_camera_ctrl' % camera

	# connect Attributes
	# mc.connectAttr('%s.CutIn' % ctrl, '%s.startFrame' % shotName, f = True)
	# mc.connectAttr('%s.CutOut' % ctrl, '%s.endFrame' % shotName, f = True)
	# mc.connectAttr('%s.CutIn' % ctrl, '%s.sequenceStartFrame' % shotName, f = True)

	mc.connectAttr('%s.startFrame' % shotName, '%s.CutIn' % ctrl, f = True)
	mc.connectAttr('%s.endFrame' % shotName, '%s.CutOut' % ctrl, f = True)


	# calculate duration
	pma = mc.createNode('plusMinusAverage', n = 'duration_pma')
	mc.setAttr('%s.operation' % pma, 2)

	mc.connectAttr('%s.CutOut' % ctrl, '%s.input3D[0].input3Dx' % pma, f = True)
	mc.connectAttr('%s.CutIn' % ctrl, '%s.input3D[1].input3Dx' % pma, f = True)
	
	pma2 = mc.createNode('plusMinusAverage', n = 'durationAdd_pma')
	mc.connectAttr('%s.output3D.output3Dx' % pma, '%s.input3D[0].input3Dx' % pma2, f = True)
	mc.setAttr('%s.input3D[1].input3Dx' % pma2, 1)

	mc.connectAttr('%s.output3D.output3Dx' % pma2, '%s.Duration' % ctrl, f = True)


def setStartEndTime(shotName, startTime, endTime) : 
	mc.setAttr('%s_camera_ctrl.CutIn' % shotName, startTime)
	mc.setAttr('%s_camera_ctrl.CutOut' % shotName, endTime)

	# shot_010_camera_ctrl.Shot
	# shot_010_camera_ctrl.CutIn
	# shot_010_camera_ctrl.CutOut
	# shot_010_camera_ctrl.Handles
	# shot_010_camera_ctrl.Sequence
	# shot_010_camera_ctrl.Duration

