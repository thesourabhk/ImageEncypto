################################################################################
##
## BY: SOURABH KUMAR
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
import os
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from Encrypt_Decrypt import Encrypter, Decrypter
import base64

# GUI FILE
from ui_main import Ui_MainWindow
# IMPORT FUNCTIONS FOR TOGGLE
from ui_functions import *

# ENcrypting the Image 
class encrypt_page():
    def __init__(self):
        self.file={}
        self.string=""
        self.Handel_Buttons()
        self.ui.btn_file_choose.clicked.connect(self.chooseFile)
        self.ui.btn_encrypt.clicked.connect(self.onClickEncrypt)
    def Handel_Buttons(self):
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
    def chooseFile(self):
        self.file= QFileDialog.getOpenFileName(self, "Load Image")
        pixmap = QtGui.QPixmap(self.file[0])
        self.ui.img_lbl.setPixmap(pixmap.scaledToHeight(201))
        if self.file != None:
            ba = QtCore.QByteArray()
            buff = QtCore.QBuffer(ba)
            buff.open(QtCore.QIODevice.WriteOnly)
            try:
                ok = pixmap.save(buff, "PNG")
                assert ok
            except AssertionError:
                self.message="No Image Selected"
                self.show_popup()
                return
            pixmap_bytes = ba.data()
            self.string = base64.b64encode(pixmap_bytes)
    def onClickEncrypt(self):
        mykey = self.ui.line_key.text()
        if not mykey:
            self.message="Enter a key"
            self.show_popup()
            return
        if not self.string:
            self.message="Select an Image"
            self.show_popup()
            return
        x = Encrypter(self.string, mykey)
        cipher = x.encrypt_image()
        if not os.path.exists("EncryptedFiles"):
            os.makedirs("EncryptedFiles")
        os.chdir(os.getcwd() + r"\EncryptedFiles")
        fh = open("cipher.txt", "wb")
        fh.write(cipher)
        fh.close()
        self.message = "Encryption Successfull: file strored in \n"+ os.getcwd()
        self.show_popup()
    def show_popup(self):
        font = QFont()
        font.setPointSize(10)
        msg = QMessageBox()
        if self.message == "Enter a key" or self.message == "Select an Image" or self.message=="No Image Selected":
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Warning")
        else:
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Result")
        msg.setFont(font)
        msg.setText(self.message)
        msg.setStyleSheet(u"background-color: rgb(35, 35, 35) ; color : white;")
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

# Decrypting the image 

class decrypt_page():
    def __init__(self):
        self.cipher = {}
        self.Handel_Buttons()
        self.ui.btn_file_choose_2.clicked.connect(self.chooseFile1)
        self.ui.btn_decrypt.clicked.connect(self.onClickDecrypt)

    def Handel_Buttons(self):
        self.ui.btn_page_3.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

    def chooseFile1(self):
        file = QFileDialog.getOpenFileName(self, 'Open File')
        try:
            text = open(file[0]).read()
        except FileNotFoundError:
            self.message="No file Selected"
            self.show_popup()
            return
        self.cipher = text.encode('utf-8')

    def onClickDecrypt(self):
        mykey = self.ui.line_key_2.text()
        if not mykey:
            self.message="Enter a key"
            self.show_popup()
            return
        if not self.cipher:
            self.message="Select an cipher.txt File"
            self.show_popup()
            return
        x = Decrypter(self.cipher)
        image = x.decrypt_image(mykey)

        ba = QtCore.QByteArray(image)
        pixmap = QtGui.QPixmap()
        ok = pixmap.loadFromData(ba, "PNG")
        assert ok
        self.ui.img_lbl_2.setPixmap(pixmap.scaledToHeight(201))
        self.message = "Decryption Successfull: file strored in \n"+ os.getcwd()
        self.show_popup()

    def show_popup(self):
        font = QFont()
        font.setPointSize(10)
        msg = QMessageBox()
        if self.message == "Enter a key" or self.message == "Select an cipher.txt File" or self.message == "No file Selected":
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Warning")
        else:
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Result")
        msg.setFont(font)
        msg.setText(self.message)
        msg.setStyleSheet(u"background-color: rgb(35, 35, 35) ; color : white;")
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

class MainWindow(QMainWindow, encrypt_page,decrypt_page):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        encrypt_page.__init__(self)
        decrypt_page.__init__(self)


        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        self.Handel_Buttons()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
    def Handel_Buttons(self):

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        # PAGE 3
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
