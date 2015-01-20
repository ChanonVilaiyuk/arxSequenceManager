import maya.cmds as mc
import maya.mel as mm

def shiftKey(type = 'default', frameRange = [1, 10000], frame = 0) : 
	if type == 'default' : 
		mm.eval('selectKey  -t (":") `ls -dag`;')

	if type == 'start' : 
		mm.eval('selectKey -t ("%s:") `ls -dag`;' % frameRange[0])

	if type == 'range' : 
		mm.eval('selectKey  -t ("%s:%s") `ls -dag`;' % (frameRange[0], frameRange[1]))

	mc.keyframe(e = True, iub = 0, an = 'keys', r = True, o = 'over', tc = frame)