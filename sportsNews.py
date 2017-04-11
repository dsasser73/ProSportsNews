import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
	
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(1280, 0, 642, 1080)
		self.setWindowTitle("Pro Sports News")
		self.setWindowIcon(QtGui.QIcon('sports.jpg'))
		self.home()
	
	def home(self):
		btnMLB = QtGui.QPushButton("MLB", self)
		btnMLB.setFixedWidth(107)
		btnNFL = QtGui.QPushButton("NFL", self)
		btnNFL.setFixedWidth(107)
		btnNBA = QtGui.QPushButton("NBA", self)
		btnNBA.setFixedWidth(107)
		btnMLS = QtGui.QPushButton("MLS", self)
		btnMLS.setFixedWidth(107)
		btnNHL = QtGui.QPushButton("NHL", self)
		btnNHL.setFixedWidth(107)
		btnPGA = QtGui.QPushButton("PGA", self)
		btnPGA.setFixedWidth(107)

		btnNFL.move(107, 0)
		btnNBA.move(214, 0)
		btnMLS.move(321, 0)
		btnNHL.move(428, 0)
		btnPGA.move(535, 0)

		self.show()

def main():
	app = QtGui.QApplication(sys.argv)
	gui = Window()
	sys.exit(app.exec_())

main()
