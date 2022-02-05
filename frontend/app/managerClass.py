from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt, QPoint
from userinterface import manager
from filmManagerClass import FilmManagerWindow
from crewManagerClass import CrewManagerWindow
from recommandationClass import RecommandationWindow
from ratingClass import RatingWindow
from userManagementClass import UserWindow


class ManagerWindow(QtWidgets.QWidget):
    username = None
    def __init__(self, welcome_text, username):
        self.oldPos = 0
        self.username = username
        super(ManagerWindow, self).__init__()
        self.ui = manager.Ui_Manager()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.center()
        self.ui.exit.clicked.connect(self.close)
        self.ui.filmManagementButton.clicked.connect(self.openFilmManager)
        self.ui.CrewManagementButton.clicked.connect(self.openCrewManager)
        self.ui.bewertungButton.clicked.connect(self.openRating)
        self.ui.vorschlaegeButton.clicked.connect(self.openRecommandation)
        self.ui.editButton.clicked.connect(self.openUser)
        self.ui.helloMsg.setText(welcome_text)
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def close(self):
        exit()

    def openFilmManager(self):
        self.filmManager = FilmManagerWindow(self.username)
        self.filmManager.exec() 

    def openCrewManager(self):
        self.crewManager = CrewManagerWindow()
        self.crewManager.exec() 
    
    def openRating(self):
        self.rating = RatingWindow()
        self.rating.exec() 

    def openRecommandation(self):
        self.recommandation = RecommandationWindow(self.username)
        self.recommandation.exec() 

    def openUser(self):
        self.userManager = UserWindow(self.username)
        self.userManager.exec() 
