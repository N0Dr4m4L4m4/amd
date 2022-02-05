from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt, QPoint
from userinterface import recommandation
import connection

class RecommandationWindow(QtWidgets.QDialog):
    database = None
    username = None
    def __init__(self, username):
        self.username = username
        super(RecommandationWindow, self).__init__()
        self.ui = recommandation.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.center()
        self.ui.exit.clicked.connect(self.close)
        self.ui.backButton.clicked.connect(self.close)
        self.database = connection.database()
        self.listRecommandation()

    def listRecommandation(self):
        self.suggestion = self.database.getSuggestion(self.username)
        self.ui.suggestionList.clear()
        for index in enumerate(self.suggestion):
            self.ui.suggestionList.addItem(str(index[0]+ 1)+ ". " + index[1][1])
            self.ui.suggestionList.addItem("\t⭐"+ str(index[1][0]) )
            self.ui.suggestionList.addItem("\t📅" + str(index[1][2]))


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