from sqlite3 import connect
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt, QPoint
from userinterface import filmManager
from addFilmClass import addFilmWindow
from changeFilmClass import changeFilmWindow
import connection

class FilmManagerWindow(QtWidgets.QDialog):
    database = None
    user = None
    filmDict = {}
    show = False
    def __init__(self, user):
        self.user = user
        self.oldPos = 0
        super(FilmManagerWindow, self).__init__()
        self.ui = filmManager.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.center()
        self.ui.exit.clicked.connect(self.close)
        self.ui.backButton.clicked.connect(self.close)
        self.ui.addFilmButton.clicked.connect(self.addFilm)
        self.ui.videoList.itemClicked.connect(self.itemClicked_event)
        self.database = connection.database()
        self.showAllFilms()
        self.ui.resetFilmButton.clicked.connect(self.showAllFilms)
    
    def showAllFilms(self):
        self.show = False
        self.films = self.database.getAllFilms()
        self.ui.videoList.clear()
        for film in self.films:
            self.ui.videoList.addItem(film[0])
    
    def itemClicked_event(self, item):
        self.name = item.text()
        self.index = self.ui.videoList.currentRow()
        self.seasons = self.database.getFilmSeason(self.name)
        
        if self.show:
            if self.name in self.filmDict:
                self.changeFilmWindow = changeFilmWindow(self.name,self.filmDict[self.name], self.user)
                self.changeFilmWindow.exec()
                if self.changeFilmWindow.deleted:
                    self.showAllFilms()
                    return

        if not self.show:
            self.ui.videoList.clear()
            for season in self.seasons:
                    # Episode zur Season
                    if len(self.seasons[0][0]) < 2:
                        self.ui.videoList.addItem('Staffel '+season[0][0])
                        self.episodes = self.database.getAllEpisodes(self.name, season[0][0])
                        for episode in self.episodes:
                            self.filmDict[episode[1]] = episode[2]
                            self.ui.videoList.addItem(episode[1])
                        self.ui.videoList.addItem(' ')
                    # Filmreihe
                    elif len(self.seasons[0][0]) == 2:
                        self.ui.videoList.addItem(season[0][0])
                        self.filmDict[season[0][0]] = season[0][1]
            self.show = True

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
        self.addFilmManager = addFilmWindow()
        self.addFilmManager.exec()
        self.showAllFilms()