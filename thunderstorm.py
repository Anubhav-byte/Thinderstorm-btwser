import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *


class Mainwindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(Mainwindow,self).__init__(*args, **kwargs)

        self.setWindowTitle("Thunderstorm")
        self.setWindowIcon(QIcon('thunderstorm.png'))
        self.setGeometry(0,0,1200,800)

        self.browser=QWebEngineView()
        self.browser.load(QUrl("https://www.google.com"))

        self.setCentralWidget(self.browser)

        navgb=QToolBar("Navigation")
        navgb.setIconSize(QSize(30,30))
        self.addToolBar(navgb)

        bbtn=QAction(QIcon("arrow-180.png"),'Back',self)
        bbtn.setStatusTip("Back to previous page")
        bbtn.triggered.connect(self.browser.back)
        navgb.addAction(bbtn)

        fbtn=QAction(QIcon("arrow-0.png"),'Forward',self)
        fbtn.setStatusTip("Forward page")
        fbtn.triggered.connect(self.browser.forward)
        navgb.addAction(fbtn)

        rld=QAction(QIcon("reload.png"),'Reload',self)
        rld.setStatusTip("Reload")
        rld.setShortcut('f5')
        rld.triggered.connect(self.browser.reload)
        navgb.addAction(rld)

        home=QAction(QIcon("home.png"),'Home',self)
        home.setStatusTip("Home")
        home.triggered.connect(self.n_home)
        navgb.addAction(home)


        self.httpsicon = QLabel() # Yes, really!
        self.httpsicon.setPixmap( QPixmap( os.path.join('icons','lock-nossl.png') ) )
        navgb.addWidget(self.httpsicon)

        self.ubar=QLineEdit()
        self.ubar.returnPressed.connect(self.n_url)
        navgb.addWidget(self.ubar)

        stop_btn = QAction( QIcon('stop.png'), "Stop", self )
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        navgb.addAction(stop_btn)

        self.browser.urlChanged.connect(self.update_url)

        self.browser.loadFinished.connect(self.update_title)

    def n_url(self):
        q = QUrl( self.ubar.text() )
        if q.scheme() == "":
            q.setScheme("http")

        self.browser.setUrl(q)


    def n_home(self):
        q=QUrl("https://www.google.com")
        self.browser.setUrl(q)
    def update_title(self):
        title=self.browser.page().title()
        self.setWindowTitle("%s- Thunderstorm " % title)

    def update_url(self,q):
        self.ubar.setText(q.toString())
        self.ubar.setCursorPosition(0)

app=QApplication(sys.argv)
window=Mainwindow()
window.show()
app.exec_()
