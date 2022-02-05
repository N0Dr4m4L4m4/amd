from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt, QPoint
import sys

from userinterface import welcome
from managerClass import ManagerWindow
import connection

class ApplicationWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.oldPos = 0
        self.ui = welcome.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.center()

        self.ui.exit.clicked.connect(self.close)
        self.ui.login.clicked.connect(self.login)
        self.ui.reg.clicked.connect(self.register)
    
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

    def login(self):
        username =  self.ui.username.text()
        response = database.login(username)

        if 'Herzlich' in response:
            self.manager = ManagerWindow(response, username)
            self.hide()
            self.manager.show()
        else:
            self.ui.infoLabel.setText(response)
            
    def close(self):
        exit()

    def register(self):
        self.ui.label.setText('<html><head/><body><p><span style=" color:#be62e8;">Registrierung</span></p></body></html>')
        self.ui.login.setText('Abbrechen')
        self.ui.reg.setText('Registrieren')
        self.ui.reg.clicked.connect(self.setBack)
        self.ui.login.clicked.connect(self.abort)
        self.ui.login.clicked.disconnect(self.login)
        self.ui.reg.clicked.disconnect(self.register)

    def abort(self):
        self.setBack()

    def setBack(self):
        self.ui.label.setText('<html><head/><body><p><span style=" color:#be62e8;">Willkommen</span></p></body></html>')
        self.ui.login.setText('Login')
        self.ui.reg.setText('Registrieren')
        self.ui.reg.clicked.connect(self.register)
        self.ui.login.clicked.connect(self.login)
        self.ui.reg.clicked.disconnect(self.setBack)
        self.ui.login.clicked.disconnect(self.abort)
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    database = connection.database()
    main()