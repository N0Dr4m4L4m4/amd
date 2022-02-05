from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 

def showdialog(title,msg1,msg2):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        
        msg.setText(msg1)
        msg.setInformativeText(msg2)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
