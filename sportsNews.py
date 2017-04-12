import sys
from PyQt4 import QtGui, QtCore
import feedparser

class Window(QtGui.QMainWindow):
	
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(1280, 0, 642, 1080)
		self.setWindowTitle("Pro Sports News")
		self.setWindowIcon(QtGui.QIcon('sports.jpg'))

		self.home()
	
	def home(self):
		self.newsFeed = QtGui.QTextEdit()
		self.setCentralWidget(self.newsFeed)
		self.newsFeed.setReadOnly(True)
		self.newsFeed.insertPlainText('\n\n')
		
		btnMLB = QtGui.QPushButton("MLB", self)
		btnMLB.setFixedWidth(107)
		btnNCAAB = QtGui.QPushButton("NCAA Baseball", self)
		btnNCAAB.setFixedWidth(107)
		btnNFL = QtGui.QPushButton("NFL", self)
		btnNFL.setFixedWidth(107)
		btnNCAAF = QtGui.QPushButton("NCAA Football", self)
		btnNCAAF.setFixedWidth(107)
		btnSoccer = QtGui.QPushButton("Soccer", self)
		btnSoccer.setFixedWidth(107)
		btnPGA = QtGui.QPushButton("PGA", self)
		btnPGA.setFixedWidth(107)

		btnMLB.clicked.connect(lambda: self.parsefeed('MLB', self.newsFeed))
		btnNFL.clicked.connect(lambda: self.parsefeed('NFL', self.newsFeed))
		btnNCAAF.clicked.connect(lambda: self.parsefeed('NCAAF', self.newsFeed))
		btnSoccer.clicked.connect(lambda: self.parsefeed('Soccer', self.newsFeed))
		btnNCAAB.clicked.connect(lambda: self.parsefeed('NCAAB', self.newsFeed))
		btnPGA.clicked.connect(lambda: self.parsefeed('PGA', self.newsFeed))
		
		btnNCAAB.move(107, 0)
		btnNFL.move(214, 0)
		btnNCAAF.move(321, 0)
		btnSoccer.move(428, 0)
		btnPGA.move(535, 0)
		
		self.show()
		
	def parsefeed(self, sport, textEdit):
		if(sport == 'MLB'):
			feed = feedparser.parse("http://mlb.mlb.com/partnerxml/gen/news/rss/mlb.xml")
		if(sport == 'NFL'):
			feed = feedparser.parse("http://www.nfl.com/rss/rsslanding?searchString=home")
		if(sport == 'NCAAF'):
			feed = feedparser.parse("http://www.ncaa.com/news/football/fbs/rss.xml")
		if(sport == 'Soccer'):
			feed = feedparser.parse("http://feeds.bbci.co.uk/sport/football/rss.xml?edition=int")
		if(sport == 'NCAAB'):
			feed = feedparser.parse("http://www.ncaa.com/news/baseball/d1/rss.xml")
		if(sport == 'PGA'):
			feed = feedparser.parse("http://mlb.mlb.com/partnerxml/gen/news/rss/mlb.xml")
		
		for newsitem in feed['items']:
			textEdit.insertPlainText(newsitem['title'])
			textEdit.insertPlainText('\n\n')
			textEdit.insertPlainText(newsitem['summary'])
			textEdit.insertPlainText('\n\n\n')

def main():
	app = QtGui.QApplication(sys.argv)
	gui = Window()
	sys.exit(app.exec_())

main()
