from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from connection import database
from userinterface import addFilm 
import connection
import dialog

import sys

from PyQt5 import QtWidgets

class addFilmWindow(QtWidgets.QDialog):
    database = None
    def __init__(self):
        super(addFilmWindow, self).__init__()
        self.oldPos = 0
        self.ui = addFilm.Ui_AddFilm()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.center()
        self.ui.exit.clicked.connect(self.close)
        self.ui.addButton.clicked.connect(self.addFilm)
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

    def addFilm(self):
        title = self.ui.title.text()
        release = self.ui.release.text()
        genre = [self.ui.genre.text()]
        minAge = self.ui.age.currentText()
        duration = self.ui.duration.text()
        episodeNr = self.ui.episode.text()
        season = self.ui.season.text()
        seriesName= self.ui.seriesName.text()
        response = self.database.addFilm(title,release,genre, minAge, duration, seriesName, episodeNr, season)
        dialog.showdialog("Film hinzugefügt","Folgender Film wurde hinzugefügt:",'Name: '+ response[0][0]+
        '\nJahr: '+ str(response[0][1]) + '\nGenre: '+','.join(response[0][2])+
        '\n' + 'Alter: '+str(response[0][3])+'\nDauer: '+str(response[0][4])+'min\nEpisode: '+
        str(response[0][5])+'\nStaffel: '+ str(response[0][6])+'\nReihe: '+response[0][7])
        self.close()
