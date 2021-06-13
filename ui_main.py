# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainaEZprG.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 549)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0, 40))
        self.btn_page_1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_1)

        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 40))
        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 40))
        self.btn_page_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_3)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.label_1 = QLabel(self.page_1)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(200, 70, 511, 81))
        font = QFont()
        font.setPointSize(40)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(u"color: #FFF;")
        self.label_1.setAlignment(Qt.AlignCenter)
        self.label_info = QLabel(self.page_1)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setGeometry(QRect(200, 160, 511, 31))
        font1 = QFont()
        font1.setPointSize(15)
        self.label_info.setFont(font1)
        self.label_info.setStyleSheet(u"color: rgb(120, 120, 120);")
        self.label_info.setAlignment(Qt.AlignCenter)
        self.label_credit = QLabel(self.page_1)
        self.label_credit.setObjectName(u"label_credit")
        self.label_credit.setGeometry(QRect(720, 480, 201, 31))
        font2 = QFont()
        font2.setFamily(u"Myanmar Text")
        font2.setPointSize(10)
        self.label_credit.setFont(font2)
        self.label_credit.setStyleSheet(u"color: rgb(120, 120, 120);")
        self.label = QLabel(self.page_1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 250, 661, 71))
        font3 = QFont()
        font3.setPointSize(14)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: rgb(111, 111, 111);")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 20, 451, 81))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: #FFF;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.line_key = QLineEdit(self.page_2)
        self.line_key.setObjectName(u"line_key")
        self.line_key.setGeometry(QRect(440, 160, 221, 41))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.line_key.setFont(font4)
        self.line_key.setStyleSheet(u"QLineEdit{\n"
"	color:#FFF;\n"
"}")
        self.line_key.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 150, 201, 61))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: #FFF;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setMargin(1)
        self.btn_file_choose = QPushButton(self.page_2)
        self.btn_file_choose.setObjectName(u"btn_file_choose")
        self.btn_file_choose.setGeometry(QRect(220, 240, 141, 41))
        font5 = QFont()
        font5.setPointSize(12)
        self.btn_file_choose.setFont(font5)
        self.btn_file_choose.setStyleSheet(u"QPushButton{\n"
"	color: #FFF;\n"
"	border:1px solid white;\n"
"	border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.334545, x2:1, y2:0.489, stop:0.0243902 rgba(100, 100, 100, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	color: rgba(0, 0, 0,100);\n"
"}")
        self.img_lbl = QLabel(self.page_2)
        self.img_lbl.setObjectName(u"img_lbl")
        self.img_lbl.setGeometry(QRect(410, 220, 351, 211))
        self.img_lbl.setStyleSheet(u"background-color:rgba(128,128,128,0.1)")
        self.img_lbl.setFrameShadow(QFrame.Raised)
        self.img_lbl.setAlignment(Qt.AlignCenter)
        self.btn_encrypt = QPushButton(self.page_2)
        self.btn_encrypt.setObjectName(u"btn_encrypt")
        self.btn_encrypt.setGeometry(QRect(220, 300, 141, 41))
        self.btn_encrypt.setFont(font5)
        self.btn_encrypt.setStyleSheet(u"QPushButton{\n"
"	color: #FFF;\n"
"	border:1px solid white;\n"
"	border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.334545, x2:1, y2:0.489, stop:0.0243902 rgba(100, 100, 100, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	color: rgba(0, 0, 0,100);\n"
"}")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(230, 20, 451, 81))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: #FFF;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 150, 201, 61))
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: #FFF;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setMargin(1)
        self.line_key_2 = QLineEdit(self.page_3)
        self.line_key_2.setObjectName(u"line_key_2")
        self.line_key_2.setGeometry(QRect(440, 160, 232, 41))
        self.line_key_2.setFont(font4)
        self.line_key_2.setStyleSheet(u"QLineEdit{\n"
"	color:#FFF;\n"
"	padding-right: 2px;\n"
"}")
        self.line_key_2.setAlignment(Qt.AlignCenter)
        self.btn_file_choose_2 = QPushButton(self.page_3)
        self.btn_file_choose_2.setObjectName(u"btn_file_choose_2")
        self.btn_file_choose_2.setGeometry(QRect(220, 240, 141, 41))
        self.btn_file_choose_2.setFont(font5)
        self.btn_file_choose_2.setStyleSheet(u"QPushButton{\n"
"	color: #FFF;\n"
"	border:1px solid white;\n"
"	border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.334545, x2:1, y2:0.489, stop:0.0243902 rgba(100, 100, 100, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	color: rgba(0, 0, 0,100);\n"
"}")
        self.btn_decrypt = QPushButton(self.page_3)
        self.btn_decrypt.setObjectName(u"btn_decrypt")
        self.btn_decrypt.setGeometry(QRect(220, 300, 141, 41))
        self.btn_decrypt.setFont(font5)
        self.btn_decrypt.setStyleSheet(u"QPushButton{\n"
"	color: #FFF;\n"
"	border:1px solid white;\n"
"	border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.334545, x2:1, y2:0.489, stop:0.0243902 rgba(100, 100, 100, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	color: rgba(0, 0, 0,100);\n"
"}")
        self.img_lbl_2 = QLabel(self.page_3)
        self.img_lbl_2.setObjectName(u"img_lbl_2")
        self.img_lbl_2.setGeometry(QRect(410, 220, 351, 211))
        self.img_lbl_2.setStyleSheet(u"background-color:rgba(128,128,128,0.1)")
        self.img_lbl_2.setFrameShadow(QFrame.Raised)
        self.img_lbl_2.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"TOGGLE", None))
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Image Encryptor", None))
        self.label_info.setText(QCoreApplication.translate("MainWindow", u"Secure your Image", None))
        self.label_credit.setText(QCoreApplication.translate("MainWindow", u"Credit: SOURABH KUMAR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>An Image Encryption system Based on the Triple DES Algorithm.</p><p><br/></p><p><br/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Encrypt Image", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Encryption key", None))
        self.btn_file_choose.setText(QCoreApplication.translate("MainWindow", u"ChooseFile", None))
        self.img_lbl.setText("")
        self.btn_encrypt.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Decrypt Image", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Decryption key", None))
        self.btn_file_choose_2.setText(QCoreApplication.translate("MainWindow", u"ChooseFile", None))
        self.btn_decrypt.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.img_lbl_2.setText("")
    # retranslateUi

