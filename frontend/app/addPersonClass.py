from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt, QPoint
from userinterface import addPerson
import connection, dialog

class AddPersonWindow(QtWidgets.QDialog):
    database = None
    def __init__(self):
        self.oldPos = 0
        super(AddPersonWindow, self).__init__()
        self.ui = addPerson.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.center()
        self.ui.exit.clicked.connect(self.close)
        self.ui.addButton.clicked.connect(self.addPerson)
        self.database = connection.database()
        
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
        self.hide()
    
    def addPerson(self):
        surname = self.ui.surname.text()
        forname = self.ui.forname.text()
        sex = self.ui.sex.currentText()
        dateOfBirth = self.ui.dateOfBirth.text()
        response = self.database.addPerson(surname, forname, sex, dateOfBirth)
        if len(response) > 0:
            dialog.showdialog("Person hinzufügen",response[0][0])
            self.close()
        else:
            dialog.showdialog("Fehler",response[0][0])


