from PyQt4 import QtCore, QtGui
import sys
import WebCamera
import sip
import cv2
sip.setapi('QString', 1)
sip.setapi('QVariant', 1)
class Display(QtGui.QMainWindow):
	
	def __init__(self):	
		super(Display, self).__init__()		
		#Main window		
		self.setWindowTitle("Air Drawing")
		self.setFixedSize(600,400)
		
		#Central widget		
		self.centralwidget = QtGui.QWidget()
		
		#Horizontal layout to contain menu bar		
		self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0,350,600,50))
		self.horizontalLayoutWidget.setStyleSheet("QWidget { background-color: rgb(50,150,150);}")
		#save button		
		self.SaveButton = QtGui.QPushButton(self.centralwidget)
		self.SaveButton.setGeometry(QtCore.QRect(20, 360, 99, 27))
		self.SaveButton.setText('Save')
		
		#Clear button		
		self.ClearButton = QtGui.QPushButton(self.centralwidget)
		self.ClearButton.setGeometry(QtCore.QRect(130, 360, 99, 27))
		self.ClearButton.setText('Clear')
		
		#Camera button		
		self.StartCamera = QtGui.QPushButton(self.centralwidget)
		self.StartCamera.setGeometry(QtCore.QRect(240,360,99,27));
		self.StartCamera.setText('Start capture')		
		self.flag = 0
		#Help button		
		self.HelpButton = QtGui.QPushButton(self.centralwidget)
		self.HelpButton.setGeometry(QtCore.QRect(470, 360, 99, 27))
		self.HelpButton.setText('Help')
		
		#Color picker button May need changes 		
		self.ColorPicker = QtGui.QPushButton(self.centralwidget)
		self.ColorPicker.setGeometry(QtCore.QRect(360,360,99,27))
		self.ColorPicker.setText('Color')
		
		#Drawing area		
		self.label_Image = QtGui.QLabel(self.centralwidget)
		self.imageSize = QtCore.QSize(600, 350)
		self.image = QtGui.QImage(self.imageSize, QtGui.QImage.Format_RGB32)		
		self.image.fill(QtCore.Qt.white)		
		self.label_Image.setPixmap(QtGui.QPixmap.fromImage(self.image))
		
		
		#Setting scene	
		self.setCentralWidget(self.centralwidget)		
		
		#event handling			
		self.SaveButton.clicked.connect(self.SaveFile)
		self.ColorPicker.clicked.connect(self.ChooseColor)
		self.StartCamera.clicked.connect(self.Camera)
		self.ClearButton.clicked.connect(self.Clear)		
		#Setting default color
		self.color = QtGui.QColor(0,0,0)
		
		self.save = Save() 
		self.pickColor = Color()
		self.Clear = ClearScreen()
		self.help = HelpInfo()
	#Save file
	def SaveFile(self):
		self.save.SaveFile(self,self.image)
		#action = self.sender()
		
			#print fileName
      	
	#Choose color can be implemented for both screen and pen color 
	def ChooseColor(self):
		self.color = self.pickColor.choose(self) 
		

	#Open camera Need to check how to prevent error if button clicked twice!	
	def Camera(self):
		camera = WebCamera.WebCamera(window)		
		camera.startcapture()		
	#self.StartCamera.setEnabled(False)		
	
	def Help(self):
		if self.window2 is None:
			self.window2 = Form2(self)
		self.window2.show()		
		self.help.info() 
		
	def Clear(self):
		self.Clear.clear(self.image,self.imageSize,self.label_Image)
		 
	

class Save():
	def __init__(self):
		pass
	def SaveFile(self,prev,image):
		action = prev.sender()
		fileFormat = 'png'		
		initialPath = QtCore.QDir.currentPath() + '/untitled.' + fileFormat
		fileName = QtGui.QFileDialog.getSaveFileName(prev, "Save As", initialPath, "%s Files (*.%s);;All Files (*)" %  (fileFormat.upper(), fileFormat))
		visibleImage = image
		if fileName:
			image.save(fileName)	

class Color():
	def __init__(self):
		pass
	def choose(self,prev):
		return QtGui.QColorDialog.getColor()
class ClearScreen():
	def __init__(self):
		pass
	def clear(self,image,imageSize,label_Image):
		image = QtGui.QImage(imageSize, QtGui.QImage.Format_RGB32)		
		image.fill(QtCore.Qt.white)		
		label_Image.setPixmap(QtGui.QPixmap.fromImage(image))
		
class HelpInfo(QtGui.QMainWindow):
	def __init__(self):
		pass
	def info(self):
		print "help"
class Form2(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		
		self.setupUi(self)


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = Display()
	window.show()
	sys.exit(app.exec_())
