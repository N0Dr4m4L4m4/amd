from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt, QPoint
from userinterface import crewManager
from addPersonClass import AddPersonWindow
from changePersonClass import changePersonWindow
import connection

class CrewManagerWindow(QtWidgets.QDialog):
    database = None
    def __init__(self):
        super(CrewManagerWindow, self).__init__()
        self.ui = crewManager.Ui_CrewManager()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.center()
        self.ui.exit.clicked.connect(self.close)
        self.ui.backButton.clicked.connect(self.close)
        self.ui.addPersonButton.clicked.connect(self.addPerson)
        self.ui.crewList.itemClicked.connect(self.itemClicked_event)
        self.database = connection.database()
        self.listCrew()

    def listCrew(self):
        self.crew = self.database.getCrew()
        self.ui.crewList.clear()
        for person in self.crew:
            self.ui.crewList.addItem(person[0] +" "+ person[1])

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def itemClicked_event(self, item):
        self.name = item.text()
        forname,surname = self.name.split(' ')
        self.changeFilmWindow = changePersonWindow(forname,surname)
        self.changeFilmWindow.exec()
        self.listCrew()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
    
    def close(self):
        self.hide()

    def addPerson(self):
        self.addPersonManager = AddPersonWindow()
        self.addPersonManager.exec()
        self.listCrew()
    
    