from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt, QPoint
from userinterface import searchForPerson
import connection

class searchForPersonWindow(QtWidgets.QDialog):
    name,database = None, None
    def __init__(self,title,year):
        super(searchForPersonWindow, self).__init__()
        self.name = ''
        self.oldPos = 0
        self.ui = searchForPerson.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.center()
        self.ui.exit.clicked.connect(self.closeWindow)
        self.ui.backButton.clicked.connect(self.closeWindow)
        self.ui.personList.itemDoubleClicked.connect(self.setPerson)
        self.database = connection.database()
        self.persons = self.database.getAllNotFilmRelatedPersons(title,year)
        self.ui.personList.clear()
        for person in self.persons:
            self.ui.personList.addItem(person[0] + ' ' +person[1])

    def setPerson(self,item):
        self.name = item.text()
        self.closeWindow()

    def getPerson(self):
        return self.name

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
    
    def closeWindow(self):
        self.close()