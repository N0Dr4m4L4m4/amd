from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt, QPoint
from userinterface import userManagement
import connection, dialog

class UserWindow(QtWidgets.QDialog):
    database = None
    def __init__(self, name):
        self.oldPos = 0
        self.user = name
        super(UserWindow, self).__init__()
        self.ui = userManagement.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.center()
        self.ui.exit.clicked.connect(self.close)
        self.ui.changeButton.clicked.connect(self.changeName)
        self.ui.title_3.setText(self.user)
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
    
    def changeName(self):
        response = self.database.changeUsername(self.user, self.ui.title_3.text())
        if 'gewechselt' in response[0][0]:
            dialog.showdialog("Name ändern","Antwort:",response[0][0])
            self.user = self.ui.title_3.text()
            self.close()
        else:
            dialog.showdialog("Name ändern","Fehler:",response[0][0])