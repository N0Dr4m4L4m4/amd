from unicodedata import name
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QMessageBox
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt, QPoint

from app.welcomeClass import ApplicationWindow
import sys
from connection import connection
global username
global database

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    connection.database.connect()
    main()