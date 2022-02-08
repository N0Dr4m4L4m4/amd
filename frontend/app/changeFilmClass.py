from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from connection import database
from searchForPersonClass import searchForPersonWindow
from userinterface import changeFilm
import connection, dialog

from PyQt5 import QtWidgets

class changeFilmWindow(QtWidgets.QDialog):
    personList = {}
    check = False
    deleted,database,user,year,title = None,None,None,None,None
    
    def __init__(self, title, year, user):
        self.user = user
        self.year= year
        self.title = title

        super(changeFilmWindow, self).__init__()
        self.oldPos = 0
        self.ui = changeFilm.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.center()

        self.ui.searchPersonButton.clicked.connect(self.searchForFilmRelatedPerson)
        self.ui.changePersonRoleButton.setHidden(True)
        self.ui.deleteFilmRelatedPerson.setHidden(True)
        self.ui.exit.clicked.connect(self.close)
        self.ui.changeButton.clicked.connect(self.changeAttributes)
        self.ui.changePersonRoleButton.clicked.connect(self.addFilmRelatedPerson)
        self.ui.resetButton.clicked.connect(self.resetInput)
        self.ui.deleteButton.clicked.connect(self.deleteFilm)
        self.ui.deleteFilmRelatedPerson.clicked.connect(self.deleteRole)

        self.database = connection.database()
        self.resp = self.database.getFilmInfo(title,year)
        self.rate = self.database.getUserFilmRate(title,year,user)
        self.ui.title.setText(self.resp[0][0])
        self.ui.release.setText(str(self.resp[0][1]))
        self.ui.genre.setText(self.resp[0][2])
        self.ui.age.setCurrentText(str(self.resp[0][3]))
        self.ui.duration.setText(str(self.resp[0][4]))
        self.ui.episode.setText(str(self.resp[0][5]))

        if(str(self.resp[0][6]) == 'None'): self.ui.season.setText('') 
        else: self.ui.season.setText(str(self.resp[0][6]))

        self.ui.seriesName.setText(self.resp[0][7])
        self.ui.rate.setCurrentText(str(self.rate[0][0]))
        self.ui.label.setText(self.resp[0][7])
        self.ui.filmRelatedPersonsList.itemClicked.connect(self.itemClicked_event)
        self.getPersonTable()

    def getPersonTable(self):
        self.ui.filmRelatedPersonsList.clear()
        self.filmRelatedPersons = self.database.getFilmRelatedPerson(self.title, self.year)
        for person in self.filmRelatedPersons:
            self.ui.filmRelatedPersonsList.addItem(person[0]+' '+person[1])
            self.personList[person[0]] = person[2]
            for role in person[2]:
                self.ui.filmRelatedPersonsList.addItem('\t'+role)

    def resetInput(self):
        if self.check: 
            self.ui.searchPersonButton.clicked.disconnect(self.addFilmRelatedPerson)
            self.ui.searchPersonButton.clicked.connect(self.searchForFilmRelatedPerson)
            self.ui.searchPersonButton.setText('Suchen')
            self.check = False
        self.ui.forname.clear()
        self.ui.surname.clear()
        self.ui.role.clear()
        self.ui.changePersonRoleButton.setHidden(True)
        self.ui.deleteFilmRelatedPerson.setHidden(True)
        self.ui.searchPersonButton.setHidden(False)
        self.ui.role.setEnabled(False)

    def itemClicked_event(self, item):
        if ' ' in item.text():
            surname,forname = item.text().split(' ')
            if surname in self.personList:
                self.ui.forname.setText(forname)
                self.ui.surname.setText(surname)
                self.ui.role.setText(','.join(self.personList[surname]))
                self.ui.changePersonRoleButton.setHidden(False)
                self.ui.deleteFilmRelatedPerson.setHidden(False)
                self.ui.searchPersonButton.setHidden(True)
                self.ui.role.setEnabled(True)
        
    def searchForFilmRelatedPerson(self):
        self.searchForPerson = searchForPersonWindow(self.resp[0][0],self.resp[0][1])
        self.searchForPerson.exec()
        if not self.searchForPerson.getPerson() == '':
            self.ui.searchPersonButton.clicked.connect(self.addFilmRelatedPerson)
            surname,forname  = self.searchForPerson.getPerson().split(' ')
            self.ui.forname.setText(forname)
            self.ui.surname.setText(surname)
            self.ui.role.setEnabled(True)
            self.ui.searchPersonButton.setText('Hinzufügen')
            self.ui.searchPersonButton.clicked.disconnect(self.searchForFilmRelatedPerson)
            self.check = True
         
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
        self.ui.title.setEnabled(True)
        self.ui.release.setEnabled(True)
        self.ui.genre.setEnabled(True)
        self.ui.age.setEnabled(True)
        self.ui.duration.setEnabled(True)
        self.ui.episode.setEnabled(True)
        self.ui.season.setEnabled(True)
        self.ui.seriesName.setEnabled(True)
        self.ui.rate.setEnabled(True)
        self.ui.changeButton.setText('Bestätigen')
        self.ui.searchPersonButton.setText('Suchen')
        self.ui.deleteButton.setText('Abbrechen')
        self.ui.changeButton.clicked.disconnect(self.changeAttributes)
        self.ui.deleteButton.clicked.disconnect(self.deleteFilm)
        self.ui.changeButton.clicked.connect(self.uploadNewAttributes)
        self.ui.deleteButton.clicked.connect(self.reset)

    def deleteFilm(self):
        response = self.database.deleteFilm(self.title,self.year)
        dialog.showdialog("Film gelöscht","Folgender Film wurde gelöscht:",'Name: '+ response[0][0]+
        '\nJahr: '+ str(response[0][1]) + '\nGenre: '+','.join(response[0][2])+
        '\n' + 'Alter: '+str(response[0][3])+'\nDauer: '+str(response[0][4])+' min\nEpisode: '+
        str(response[0][5])+'\nStaffel: '+ str(response[0][6])+'\nReihe: '+response[0][7])
        self.deleted = True
        self.close()
    
    def deleteRole(self):
        response = self.database.deleteRole(self.ui.title.text(), self.ui.release.text(), self.ui.surname.text(), self.ui.forname.text())
        dialog.showdialog("Personenrolle gelöscht","Folges wurde entfernt: ", 'Film: ' + response[0][0]+' '+str(response[0][1])+ 
         '\nName: '+ response[0][2] + ' '+ response[0][3] + '\nRollen: ' + ','.join(response[0][4]))
        
        self.getPersonTable()
        self.resetInput()

    def reset(self):
        self.ui.title.setEnabled(False)
        self.ui.release.setEnabled(False)
        self.ui.genre.setEnabled(False)
        self.ui.age.setEnabled(False)
        self.ui.duration.setEnabled(False)
        self.ui.episode.setEnabled(False)
        self.ui.season.setEnabled(False)
        self.ui.seriesName.setEnabled(False)
        self.ui.rate.setEnabled(False)
        self.ui.changeButton.setText('Ändern')
        self.ui.deleteButton.setText('Löschen')
        self.ui.searchPersonButton.setText('Suchen')
        self.ui.changeButton.clicked.connect(self.changeAttributes)
        self.ui.deleteButton.clicked.connect(self.deleteFilm)
        self.ui.changeButton.clicked.disconnect(self.uploadNewAttributes)
        self.ui.deleteButton.clicked.disconnect(self.reset)
        
    def addFilmRelatedPerson(self):
        if self.check: 
            self.ui.searchPersonButton.clicked.disconnect(self.addFilmRelatedPerson)
            self.ui.searchPersonButton.clicked.connect(self.searchForFilmRelatedPerson)
            self.check = False
    
        response = self.database.addFilmRelatedPerson(self.ui.title.text(), self.ui.release.text(), self.ui.surname.text(), self.ui.forname.text(), list(self.ui.role.text().split(",")))
        dialog.showdialog("Personenrolle hinzugefügt","Antwort der Datenbank: ", response[0][0])
        self.getPersonTable()
        self.resetInput()

    def uploadNewAttributes(self):
        response_rating = ''
        if self.ui.rate.currentText() != '':
            response_rating = self.database.changeRating(self.resp[0][0], self.resp[0][1], self.user, self.ui.rate.currentText())
            response_rating = str(response_rating[0][3])
        elif self.ui.rate.currentText() == '':
            response_rating = self.database.changeRating(self.resp[0][0], self.resp[0][1], self.user, None)
            response_rating = str(response_rating[0][3]) if response_rating else ''
        genre = [self.ui.genre.text()]
        season = self.ui.season.text()
        if self.ui.season.text() == 'None' or self.ui.season.text() == '':
            season = None
        response = self.database.changeFilmAttributes(self.resp[0][0], self.resp[0][1], self.ui.title.text(), 
         self.ui.release.text(), genre, self.ui.age.currentText(), self.ui.duration.text(), 
         self.ui.episode.text(), season, self.ui.seriesName.text(),)
        dialog.showdialog("Film geändert","Folgender Film wurde geändert:",response[0][0])
        self.reset()