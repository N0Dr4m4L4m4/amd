from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from numpy import tile
from connection import database
from userinterface import changePerson
import connection, dialog

from PyQt5 import QtWidgets

class changePersonWindow(QtWidgets.QDialog):
    database = None
    def __init__(self,forname, surname):
        super(changePersonWindow, self).__init__()
        self.oldPos = 0
        self.ui = changePerson.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.center()
        self.ui.exit.clicked.connect(self.close)
        self.ui.changeButton.clicked.connect(self.changeAttributes)
        self.ui.deleteButton.clicked.connect(self.deletePerson)

        self.database = connection.database()
        self.resp = self.database.getPersonInfo(forname,surname)
        self.ui.surname.setText(self.resp[0][0])
        self.ui.forname.setText(self.resp[0][1])
        self.ui.dateOfBirth.setText(self.resp[0][2].strftime("%d.%m.%Y"))
        self.ui.sex.setCurrentText(self.resp[0][3])
        self.ui.name.setText(forname +' '+surname)

    def deletePerson(self):
        response = self.database.deletePerson(self.resp[0][0],self.resp[0][1])
        dialog.showdialog("Person gelöscht","Folgende Daten wurde gelöscht:",response[0][0]+' '+response[0][1]+ '\n'+ response[0][2].strftime("%d.%m.%Y") + '\n'+ response[0][3])
        self.close()

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

    def changeAttributes(self):
        self.ui.surname.setEnabled(True)
        self.ui.forname.setEnabled(True)
        self.ui.dateOfBirth.setEnabled(True)
        self.ui.sex.setEnabled(True)
        self.ui.changeButton.setText('Bestätigen')
        self.ui.deleteButton.setText('Abbrechen')
        self.ui.changeButton.clicked.disconnect(self.changeAttributes)
        self.ui.changeButton.clicked.connect(self.uploadNewAttributes)
        self.ui.deleteButton.clicked.connect(self.reset)

    def reset(self):
        self.ui.surname.setEnabled(False)
        self.ui.forname.setEnabled(False)
        self.ui.dateOfBirth.setEnabled(False)
        self.ui.sex.setEnabled(False)
        self.ui.changeButton.setText('Ändern')
        self.ui.deleteButton.setText('Löschen')
        self.ui.changeButton.clicked.disconnect(self.uploadNewAttributes)
        self.ui.changeButton.clicked.connect(self.changeAttributes)
        self.ui.deleteButton.clicked.disconnect(self.reset)

    def uploadNewAttributes(self):
        response = self.database.changePersonAttributes(self.resp[0][0],self.resp[0][1],self.ui.surname.text(),self.ui.forname.text(),self.ui.dateOfBirth.text(),self.ui.sex.currentText())
        dialog.showdialog("Person geändert","Folgende Daten wurden geändert:",response[0][0]+' '+response[0][1]+ '\n'+ response[0][2].strftime("%d.%m.%Y") + '\n'+ response[0][3])
        self.close()
