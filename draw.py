import cv2
import numpy as np
from PyQt4 import QtCore, QtGui
import sys
import sip
from display import Display
sip.setapi('QString', 1)
sip.setapi('QVariant', 1)
class Draw():
	def __init__(self):
		pass	
	def drawPattern(self,window,palm,previous):
		self.window = window
		drawLine = DrawLine()		
		print palm, ' palm previous' ,previous
		drawLine.drawPattern(window,palm,previous)		
		window.show()	

class DrawLine():
	def __init__(Draw):
		pass
	def drawPattern(self,window,palm,previous):
		self.window = window
		painter = QtGui.QPainter()
		painter.begin(self.window.image)
		painter.setPen(window.color)		
		palmco = palm[0]
		prevco = previous[0]
		x1 , y1 = palmco
		if previous == [0 , 0]:		
			x2 = 0
			y2 = 0
		else:
			x2, y2 = prevco
			if( ( x2 > x1 + 50 or y2 > y1 + 50 ) or ( x1 > x2 + 50 or y1 > y2 + 50 )):			
				painter.drawLine(x1,y1,x2,y2)
				painter.end()
				self.window.label_Image.setPixmap(QtGui.QPixmap.fromImage(window.image))
		
			
