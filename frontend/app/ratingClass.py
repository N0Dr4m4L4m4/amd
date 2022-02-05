from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt, QPoint
from userinterface import rating
import connection

class RatingWindow(QtWidgets.QDialog):
    database = None
    def __init__(self):
        super(RatingWindow, self).__init__()
        self.oldPos = 0
        self.ui = rating.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.center()
        self.ui.exit.clicked.connect(self.close)
        self.ui.backButton.clicked.connect(self.close)
        self.database = connection.database()
        self.listRating()

    def listRating(self):
        self.rating = self.database.getRating()
        self.ui.ratingList.clear()
        for rate in self.rating:
            self.ui.ratingList.addItem(rate[0] +"\t⭐"+ str(rate[2]))

 
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