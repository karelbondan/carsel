# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUIhROJWL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(888, 671)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.verticalLayout_31 = QVBoxLayout(self.login)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_58 = QFrame(self.login)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMaximumSize(QSize(16777215, 90))
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_58)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label = QLabel(self.frame_58)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 19pt \"Century Gothic\";\n"
"font: 63 28pt \"Bahnschrift SemiBold Condensed\";")

        self.verticalLayout_29.addWidget(self.label)

        self.label_2 = QLabel(self.frame_58)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 10pt;")

        self.verticalLayout_29.addWidget(self.label_2)


        self.verticalLayout_31.addWidget(self.frame_58)

        self.frame_59 = QFrame(self.login)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_110 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.frame_61 = QFrame(self.frame_59)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_61)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_6 = QLabel(self.frame_61)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 19pt \"Century Gothic\";\n"
"font: 63 28pt \"Bahnschrift SemiBold Condensed\";")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_6)

        self.frame_2 = QFrame(self.frame_61)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_108 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.frame_62 = QFrame(self.frame_2)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_108.addWidget(self.frame_62)

        self.label_118 = QLabel(self.frame_2)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMinimumSize(QSize(100, 0))
        self.label_118.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_108.addWidget(self.label_118)

        self.loginaschoose = QComboBox(self.frame_2)
        self.loginaschoose.setObjectName(u"loginaschoose")
        self.loginaschoose.setMinimumSize(QSize(183, 25))
        self.loginaschoose.setMaximumSize(QSize(183, 16777215))

        self.horizontalLayout_108.addWidget(self.loginaschoose)

        self.frame_63 = QFrame(self.frame_2)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_108.addWidget(self.frame_63)


        self.verticalLayout_33.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_61)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_107 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.frame_64 = QFrame(self.frame_3)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_107.addWidget(self.frame_64)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 0))
        self.label_5.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_107.addWidget(self.label_5)

        self.password = QLineEdit(self.frame_3)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(125, 25))
        self.password.setMaximumSize(QSize(183, 16777215))
        self.password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_107.addWidget(self.password)

        self.frame_65 = QFrame(self.frame_3)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_107.addWidget(self.frame_65)


        self.verticalLayout_33.addWidget(self.frame_3)

        self.frame_60 = QFrame(self.frame_61)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_109 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.signinbutton = QPushButton(self.frame_60)
        self.signinbutton.setObjectName(u"signinbutton")
        self.signinbutton.setMinimumSize(QSize(150, 40))
        self.signinbutton.setMaximumSize(QSize(125, 16777215))

        self.horizontalLayout_109.addWidget(self.signinbutton)


        self.verticalLayout_33.addWidget(self.frame_60)

        self.frame_67 = QFrame(self.frame_61)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)

        self.verticalLayout_33.addWidget(self.frame_67)

        self.frame_66 = QFrame(self.frame_61)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)

        self.verticalLayout_33.addWidget(self.frame_66)


        self.horizontalLayout_110.addWidget(self.frame_61)


        self.verticalLayout_31.addWidget(self.frame_59)

        self.stackedWidget.addWidget(self.login)
        self.manager = QWidget()
        self.manager.setObjectName(u"manager")
        self.verticalLayout_26 = QVBoxLayout(self.manager)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_18 = QFrame(self.manager)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.refreshbuttonmanager = QPushButton(self.frame_18)
        self.refreshbuttonmanager.setObjectName(u"refreshbuttonmanager")
        self.refreshbuttonmanager.setMinimumSize(QSize(50, 50))
        self.refreshbuttonmanager.setMaximumSize(QSize(50, 50))
        self.refreshbuttonmanager.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"data/img/refresh_border_large.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshbuttonmanager.setIcon(icon)
        self.refreshbuttonmanager.setIconSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.refreshbuttonmanager)

        self.label_85 = QLabel(self.frame_18)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setStyleSheet(u"font: 19pt \"Century Gothic\";\n"
"font: 63 28pt \"Bahnschrift SemiBold Condensed\";")
        self.label_85.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_85)

        self.profilebuttonmanager = QPushButton(self.frame_18)
        self.profilebuttonmanager.setObjectName(u"profilebuttonmanager")
        self.profilebuttonmanager.setMinimumSize(QSize(50, 50))
        self.profilebuttonmanager.setMaximumSize(QSize(50, 50))
        self.profilebuttonmanager.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"data/img/login_border.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profilebuttonmanager.setIcon(icon1)
        self.profilebuttonmanager.setIconSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.profilebuttonmanager)


        self.verticalLayout_26.addWidget(self.frame_18)

        self.scrollArea = QScrollArea(self.manager)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -1419, 831, 3116))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_8 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.frame_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_8.addWidget(self.label_9)


        self.verticalLayout.addWidget(self.frame_8)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(500, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_13 = QFrame(self.frame_4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.label_8 = QLabel(self.frame_13)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(90, 0))
        self.label_8.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_6.addWidget(self.label_8)

        self.branchchoose_manager = QComboBox(self.frame_13)
        self.branchchoose_manager.addItem("")
        self.branchchoose_manager.addItem("")
        self.branchchoose_manager.addItem("")
        self.branchchoose_manager.addItem("")
        self.branchchoose_manager.addItem("")
        self.branchchoose_manager.addItem("")
        self.branchchoose_manager.addItem("")
        self.branchchoose_manager.setObjectName(u"branchchoose_manager")
        self.branchchoose_manager.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_6.addWidget(self.branchchoose_manager)


        self.verticalLayout_3.addWidget(self.frame_13)

        self.addresslabel_manager = QLabel(self.frame_4)
        self.addresslabel_manager.setObjectName(u"addresslabel_manager")

        self.verticalLayout_3.addWidget(self.addresslabel_manager)

        self.establishedlabel_manager = QLabel(self.frame_4)
        self.establishedlabel_manager.setObjectName(u"establishedlabel_manager")

        self.verticalLayout_3.addWidget(self.establishedlabel_manager)

        self.employeecount_manager_2 = QLabel(self.frame_4)
        self.employeecount_manager_2.setObjectName(u"employeecount_manager_2")

        self.verticalLayout_3.addWidget(self.employeecount_manager_2)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 75 11pt \"MS Shell Dlg 2\";")

        self.verticalLayout_2.addWidget(self.label_7)

        self.firstnamecheckboxemployee_manager = QCheckBox(self.frame_5)
        self.firstnamecheckboxemployee_manager.setObjectName(u"firstnamecheckboxemployee_manager")

        self.verticalLayout_2.addWidget(self.firstnamecheckboxemployee_manager)

        self.lastnamecheckboxemployee_manager = QCheckBox(self.frame_5)
        self.lastnamecheckboxemployee_manager.setObjectName(u"lastnamecheckboxemployee_manager")

        self.verticalLayout_2.addWidget(self.lastnamecheckboxemployee_manager)

        self.gendercheckboxemployee_manager = QCheckBox(self.frame_5)
        self.gendercheckboxemployee_manager.setObjectName(u"gendercheckboxemployee_manager")

        self.verticalLayout_2.addWidget(self.gendercheckboxemployee_manager)

        self.agecheckboxemployee_manager = QCheckBox(self.frame_5)
        self.agecheckboxemployee_manager.setObjectName(u"agecheckboxemployee_manager")

        self.verticalLayout_2.addWidget(self.agecheckboxemployee_manager)

        self.positioncheckboxemployee_manager = QCheckBox(self.frame_5)
        self.positioncheckboxemployee_manager.setObjectName(u"positioncheckboxemployee_manager")

        self.verticalLayout_2.addWidget(self.positioncheckboxemployee_manager)

        self.addresscheckboxemployee_manager = QCheckBox(self.frame_5)
        self.addresscheckboxemployee_manager.setObjectName(u"addresscheckboxemployee_manager")

        self.verticalLayout_2.addWidget(self.addresscheckboxemployee_manager)

        self.phonenocheckboxemployee_manager = QCheckBox(self.frame_5)
        self.phonenocheckboxemployee_manager.setObjectName(u"phonenocheckboxemployee_manager")

        self.verticalLayout_2.addWidget(self.phonenocheckboxemployee_manager)

        self.datecheckboxemployee_manager = QCheckBox(self.frame_5)
        self.datecheckboxemployee_manager.setObjectName(u"datecheckboxemployee_manager")

        self.verticalLayout_2.addWidget(self.datecheckboxemployee_manager)


        self.verticalLayout.addWidget(self.frame_5)

        self.displaygenderframe_manager = QFrame(self.scrollAreaWidgetContents_2)
        self.displaygenderframe_manager.setObjectName(u"displaygenderframe_manager")
        self.displaygenderframe_manager.setMaximumSize(QSize(500, 16777215))
        self.displaygenderframe_manager.setFrameShape(QFrame.StyledPanel)
        self.displaygenderframe_manager.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.displaygenderframe_manager)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.displaygenderframe_manager)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(90, 0))
        self.label_10.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_11.addWidget(self.label_10)

        self.genderchoose_manager = QComboBox(self.displaygenderframe_manager)
        self.genderchoose_manager.addItem("")
        self.genderchoose_manager.addItem("")
        self.genderchoose_manager.addItem("")
        self.genderchoose_manager.setObjectName(u"genderchoose_manager")
        self.genderchoose_manager.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_11.addWidget(self.genderchoose_manager)


        self.verticalLayout.addWidget(self.displaygenderframe_manager)

        self.displayageframe_manager = QFrame(self.scrollAreaWidgetContents_2)
        self.displayageframe_manager.setObjectName(u"displayageframe_manager")
        self.displayageframe_manager.setMinimumSize(QSize(0, 41))
        self.displayageframe_manager.setMaximumSize(QSize(500, 16777215))
        self.displayageframe_manager.setFrameShape(QFrame.StyledPanel)
        self.displayageframe_manager.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.displayageframe_manager)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.displayageframe_manager)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(90, 0))
        self.label_11.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_10.addWidget(self.label_11)

        self.minagechoose_manager = QSpinBox(self.displayageframe_manager)
        self.minagechoose_manager.setObjectName(u"minagechoose_manager")
        self.minagechoose_manager.setMinimumSize(QSize(0, 25))
        self.minagechoose_manager.setMinimum(0)
        self.minagechoose_manager.setMaximum(9999)

        self.horizontalLayout_10.addWidget(self.minagechoose_manager)

        self.label_12 = QLabel(self.displayageframe_manager)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 0))
        self.label_12.setMaximumSize(QSize(16777215, 16777215))
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_12)

        self.maxagechoose_manager = QSpinBox(self.displayageframe_manager)
        self.maxagechoose_manager.setObjectName(u"maxagechoose_manager")
        self.maxagechoose_manager.setMinimumSize(QSize(0, 25))
        self.maxagechoose_manager.setMinimum(0)
        self.maxagechoose_manager.setMaximum(9999)

        self.horizontalLayout_10.addWidget(self.maxagechoose_manager)

        self.label_13 = QLabel(self.displayageframe_manager)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 0))
        self.label_13.setMaximumSize(QSize(16777215, 16777215))
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_13)


        self.verticalLayout.addWidget(self.displayageframe_manager)

        self.displaypositionframe_manager = QFrame(self.scrollAreaWidgetContents_2)
        self.displaypositionframe_manager.setObjectName(u"displaypositionframe_manager")
        self.displaypositionframe_manager.setMinimumSize(QSize(0, 41))
        self.displaypositionframe_manager.setMaximumSize(QSize(500, 16777215))
        self.displaypositionframe_manager.setFrameShape(QFrame.StyledPanel)
        self.displaypositionframe_manager.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.displaypositionframe_manager)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_14 = QLabel(self.displaypositionframe_manager)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(90, 0))
        self.label_14.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_13.addWidget(self.label_14)

        self.positionchooser_manager = QComboBox(self.displaypositionframe_manager)
        self.positionchooser_manager.addItem("")
        self.positionchooser_manager.addItem("")
        self.positionchooser_manager.addItem("")
        self.positionchooser_manager.addItem("")
        self.positionchooser_manager.addItem("")
        self.positionchooser_manager.addItem("")
        self.positionchooser_manager.addItem("")
        self.positionchooser_manager.addItem("")
        self.positionchooser_manager.addItem("")
        self.positionchooser_manager.setObjectName(u"positionchooser_manager")
        self.positionchooser_manager.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_13.addWidget(self.positionchooser_manager)


        self.verticalLayout.addWidget(self.displaypositionframe_manager)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.submitbuttonemployee_manager = QPushButton(self.frame_7)
        self.submitbuttonemployee_manager.setObjectName(u"submitbuttonemployee_manager")
        self.submitbuttonemployee_manager.setMinimumSize(QSize(0, 25))
        self.submitbuttonemployee_manager.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_12.addWidget(self.submitbuttonemployee_manager)


        self.verticalLayout.addWidget(self.frame_7)

        self.employeecountframe_manager = QFrame(self.scrollAreaWidgetContents_2)
        self.employeecountframe_manager.setObjectName(u"employeecountframe_manager")
        self.employeecountframe_manager.setFrameShape(QFrame.StyledPanel)
        self.employeecountframe_manager.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.employeecountframe_manager)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.employeecount_manager = QLabel(self.employeecountframe_manager)
        self.employeecount_manager.setObjectName(u"employeecount_manager")

        self.horizontalLayout_26.addWidget(self.employeecount_manager)


        self.verticalLayout.addWidget(self.employeecountframe_manager)

        self.employeetableframe_manager = QFrame(self.scrollAreaWidgetContents_2)
        self.employeetableframe_manager.setObjectName(u"employeetableframe_manager")
        self.employeetableframe_manager.setMinimumSize(QSize(0, 0))
        self.employeetableframe_manager.setFrameShape(QFrame.StyledPanel)
        self.employeetableframe_manager.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.employeetableframe_manager)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.employeetable_manager = QTableWidget(self.employeetableframe_manager)
        if (self.employeetable_manager.columnCount() < 8):
            self.employeetable_manager.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.employeetable_manager.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.employeetable_manager.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.employeetable_manager.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.employeetable_manager.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.employeetable_manager.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.employeetable_manager.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.employeetable_manager.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.employeetable_manager.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.employeetable_manager.setObjectName(u"employeetable_manager")
        self.employeetable_manager.setMinimumSize(QSize(0, 450))

        self.horizontalLayout_9.addWidget(self.employeetable_manager)


        self.verticalLayout.addWidget(self.employeetableframe_manager)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 0))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_15 = QLabel(self.frame_12)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_14.addWidget(self.label_15)


        self.verticalLayout_7.addWidget(self.frame_12)

        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 0))
        self.frame_14.setMaximumSize(QSize(500, 16777215))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_14)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, -1, -1, -1)
        self.label_16 = QLabel(self.frame_15)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(90, 0))
        self.label_16.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_15.addWidget(self.label_16)

        self.branchchoose_manager_2 = QComboBox(self.frame_15)
        self.branchchoose_manager_2.addItem("")
        self.branchchoose_manager_2.addItem("")
        self.branchchoose_manager_2.addItem("")
        self.branchchoose_manager_2.addItem("")
        self.branchchoose_manager_2.addItem("")
        self.branchchoose_manager_2.addItem("")
        self.branchchoose_manager_2.addItem("")
        self.branchchoose_manager_2.setObjectName(u"branchchoose_manager_2")
        self.branchchoose_manager_2.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_15.addWidget(self.branchchoose_manager_2)


        self.verticalLayout_5.addWidget(self.frame_15)

        self.addresslabel_manager_2 = QLabel(self.frame_14)
        self.addresslabel_manager_2.setObjectName(u"addresslabel_manager_2")

        self.verticalLayout_5.addWidget(self.addresslabel_manager_2)

        self.establishedlabel_manager_2 = QLabel(self.frame_14)
        self.establishedlabel_manager_2.setObjectName(u"establishedlabel_manager_2")

        self.verticalLayout_5.addWidget(self.establishedlabel_manager_2)

        self.productcount_branch = QLabel(self.frame_14)
        self.productcount_branch.setObjectName(u"productcount_branch")

        self.verticalLayout_5.addWidget(self.productcount_branch)


        self.verticalLayout_7.addWidget(self.frame_14)

        self.frame_16 = QFrame(self.frame_10)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 0))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_16)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_17 = QLabel(self.frame_16)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font: 75 11pt \"MS Shell Dlg 2\";")

        self.verticalLayout_6.addWidget(self.label_17)

        self.cartype_manager = QCheckBox(self.frame_16)
        self.cartype_manager.setObjectName(u"cartype_manager")

        self.verticalLayout_6.addWidget(self.cartype_manager)

        self.carname_manager = QCheckBox(self.frame_16)
        self.carname_manager.setObjectName(u"carname_manager")

        self.verticalLayout_6.addWidget(self.carname_manager)

        self.yearreleased_manager = QCheckBox(self.frame_16)
        self.yearreleased_manager.setObjectName(u"yearreleased_manager")

        self.verticalLayout_6.addWidget(self.yearreleased_manager)

        self.topspeed_manager = QCheckBox(self.frame_16)
        self.topspeed_manager.setObjectName(u"topspeed_manager")

        self.verticalLayout_6.addWidget(self.topspeed_manager)

        self.horsepower_manager = QCheckBox(self.frame_16)
        self.horsepower_manager.setObjectName(u"horsepower_manager")

        self.verticalLayout_6.addWidget(self.horsepower_manager)

        self.seatcount_manager = QCheckBox(self.frame_16)
        self.seatcount_manager.setObjectName(u"seatcount_manager")

        self.verticalLayout_6.addWidget(self.seatcount_manager)

        self.length_manager = QCheckBox(self.frame_16)
        self.length_manager.setObjectName(u"length_manager")

        self.verticalLayout_6.addWidget(self.length_manager)

        self.width_manager = QCheckBox(self.frame_16)
        self.width_manager.setObjectName(u"width_manager")

        self.verticalLayout_6.addWidget(self.width_manager)

        self.dateadded_manager = QCheckBox(self.frame_16)
        self.dateadded_manager.setObjectName(u"dateadded_manager")

        self.verticalLayout_6.addWidget(self.dateadded_manager)

        self.price_manager = QCheckBox(self.frame_16)
        self.price_manager.setObjectName(u"price_manager")

        self.verticalLayout_6.addWidget(self.price_manager)


        self.verticalLayout_7.addWidget(self.frame_16)

        self.frame_92 = QFrame(self.frame_10)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMaximumSize(QSize(500, 16777215))
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.label_98 = QLabel(self.frame_92)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMinimumSize(QSize(120, 0))
        self.label_98.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_94.addWidget(self.label_98)

        self.manuselect_manager = QComboBox(self.frame_92)
        self.manuselect_manager.addItem("")
        self.manuselect_manager.addItem("")
        self.manuselect_manager.addItem("")
        self.manuselect_manager.setObjectName(u"manuselect_manager")
        self.manuselect_manager.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_94.addWidget(self.manuselect_manager)


        self.verticalLayout_7.addWidget(self.frame_92)

        self.cartypeframe_manager = QFrame(self.frame_10)
        self.cartypeframe_manager.setObjectName(u"cartypeframe_manager")
        self.cartypeframe_manager.setMaximumSize(QSize(500, 16777215))
        self.cartypeframe_manager.setFrameShape(QFrame.StyledPanel)
        self.cartypeframe_manager.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.cartypeframe_manager)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_21 = QLabel(self.cartypeframe_manager)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(120, 0))
        self.label_21.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_17.addWidget(self.label_21)

        self.cartypechoose_manager = QComboBox(self.cartypeframe_manager)
        self.cartypechoose_manager.addItem("")
        self.cartypechoose_manager.addItem("")
        self.cartypechoose_manager.addItem("")
        self.cartypechoose_manager.setObjectName(u"cartypechoose_manager")
        self.cartypechoose_manager.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_17.addWidget(self.cartypechoose_manager)


        self.verticalLayout_7.addWidget(self.cartypeframe_manager)

        self.yearreleasedframe_manager = QFrame(self.frame_10)
        self.yearreleasedframe_manager.setObjectName(u"yearreleasedframe_manager")
        self.yearreleasedframe_manager.setMinimumSize(QSize(0, 41))
        self.yearreleasedframe_manager.setMaximumSize(QSize(500, 16777215))
        self.yearreleasedframe_manager.setFrameShape(QFrame.StyledPanel)
        self.yearreleasedframe_manager.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.yearreleasedframe_manager)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_37 = QLabel(self.yearreleasedframe_manager)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(130, 0))
        self.label_37.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_23.addWidget(self.label_37)

        self.minyear_manager = QSpinBox(self.yearreleasedframe_manager)
        self.minyear_manager.setObjectName(u"minyear_manager")
        self.minyear_manager.setMinimumSize(QSize(0, 25))
        self.minyear_manager.setMinimum(0)
        self.minyear_manager.setMaximum(9999)

        self.horizontalLayout_23.addWidget(self.minyear_manager)

        self.label_38 = QLabel(self.yearreleasedframe_manager)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(0, 0))
        self.label_38.setMaximumSize(QSize(16777215, 16777215))
        self.label_38.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_38)

        self.maxyear_manager = QSpinBox(self.yearreleasedframe_manager)
        self.maxyear_manager.setObjectName(u"maxyear_manager")
        self.maxyear_manager.setMinimumSize(QSize(0, 25))
        self.maxyear_manager.setMinimum(0)
        self.maxyear_manager.setMaximum(9999)

        self.horizontalLayout_23.addWidget(self.maxyear_manager)

        self.label_39 = QLabel(self.yearreleasedframe_manager)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(0, 0))
        self.label_39.setMaximumSize(QSize(16777215, 16777215))
        self.label_39.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_39)


        self.verticalLayout_7.addWidget(self.yearreleasedframe_manager)

        self.topspeedframe_manager = QFrame(self.frame_10)
        self.topspeedframe_manager.setObjectName(u"topspeedframe_manager")
        self.topspeedframe_manager.setMinimumSize(QSize(0, 41))
        self.topspeedframe_manager.setMaximumSize(QSize(500, 16777215))
        self.topspeedframe_manager.setFrameShape(QFrame.StyledPanel)
        self.topspeedframe_manager.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.topspeedframe_manager)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_34 = QLabel(self.topspeedframe_manager)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(130, 0))
        self.label_34.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_22.addWidget(self.label_34)

        self.mintopspeed_manager = QSpinBox(self.topspeedframe_manager)
        self.mintopspeed_manager.setObjectName(u"mintopspeed_manager")
        self.mintopspeed_manager.setMinimumSize(QSize(0, 25))
        self.mintopspeed_manager.setMinimum(0)
        self.mintopspeed_manager.setMaximum(9999)

        self.horizontalLayout_22.addWidget(self.mintopspeed_manager)

        self.label_35 = QLabel(self.topspeedframe_manager)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(0, 0))
        self.label_35.setMaximumSize(QSize(16777215, 16777215))
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_35)

        self.maxtopspeed_manager = QSpinBox(self.topspeedframe_manager)
        self.maxtopspeed_manager.setObjectName(u"maxtopspeed_manager")
        self.maxtopspeed_manager.setMinimumSize(QSize(0, 25))
        self.maxtopspeed_manager.setMinimum(0)
        self.maxtopspeed_manager.setMaximum(9999)

        self.horizontalLayout_22.addWidget(self.maxtopspeed_manager)

        self.label_36 = QLabel(self.topspeedframe_manager)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(0, 0))
        self.label_36.setMaximumSize(QSize(16777215, 16777215))
        self.label_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_36)


        self.verticalLayout_7.addWidget(self.topspeedframe_manager)

        self.horsepowerframe_manager = QFrame(self.frame_10)
        self.horsepowerframe_manager.setObjectName(u"horsepowerframe_manager")
        self.horsepowerframe_manager.setMinimumSize(QSize(0, 41))
        self.horsepowerframe_manager.setMaximumSize(QSize(500, 16777215))
        self.horsepowerframe_manager.setFrameShape(QFrame.StyledPanel)
        self.horsepowerframe_manager.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.horsepowerframe_manager)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_18 = QLabel(self.horsepowerframe_manager)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(130, 0))
        self.label_18.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_16.addWidget(self.label_18)

        self.minhorsepower_manager = QSpinBox(self.horsepowerframe_manager)
        self.minhorsepower_manager.setObjectName(u"minhorsepower_manager")
        self.minhorsepower_manager.setMinimumSize(QSize(0, 25))
        self.minhorsepower_manager.setMinimum(0)
        self.minhorsepower_manager.setMaximum(9999)

        self.horizontalLayout_16.addWidget(self.minhorsepower_manager)

        self.label_19 = QLabel(self.horsepowerframe_manager)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 0))
        self.label_19.setMaximumSize(QSize(16777215, 16777215))
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_19)

        self.maxhorsepower_manager = QSpinBox(self.horsepowerframe_manager)
        self.maxhorsepower_manager.setObjectName(u"maxhorsepower_manager")
        self.maxhorsepower_manager.setMinimumSize(QSize(0, 25))
        self.maxhorsepower_manager.setMinimum(0)
        self.maxhorsepower_manager.setMaximum(9999)

        self.horizontalLayout_16.addWidget(self.maxhorsepower_manager)

        self.label_20 = QLabel(self.horsepowerframe_manager)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 0))
        self.label_20.setMaximumSize(QSize(16777215, 16777215))
        self.label_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_20)


        self.verticalLayout_7.addWidget(self.horsepowerframe_manager)

        self.seatcountframe_manager = QFrame(self.frame_10)
        self.seatcountframe_manager.setObjectName(u"seatcountframe_manager")
        self.seatcountframe_manager.setMinimumSize(QSize(0, 41))
        self.seatcountframe_manager.setMaximumSize(QSize(500, 16777215))
        self.seatcountframe_manager.setFrameShape(QFrame.StyledPanel)
        self.seatcountframe_manager.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.seatcountframe_manager)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_22 = QLabel(self.seatcountframe_manager)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(130, 0))
        self.label_22.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_18.addWidget(self.label_22)

        self.minseatcount_manager = QSpinBox(self.seatcountframe_manager)
        self.minseatcount_manager.setObjectName(u"minseatcount_manager")
        self.minseatcount_manager.setMinimumSize(QSize(0, 25))
        self.minseatcount_manager.setMinimum(0)
        self.minseatcount_manager.setMaximum(9999)

        self.horizontalLayout_18.addWidget(self.minseatcount_manager)

        self.label_23 = QLabel(self.seatcountframe_manager)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 0))
        self.label_23.setMaximumSize(QSize(16777215, 16777215))
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_23)

        self.maxseatcount_manager = QSpinBox(self.seatcountframe_manager)
        self.maxseatcount_manager.setObjectName(u"maxseatcount_manager")
        self.maxseatcount_manager.setMinimumSize(QSize(0, 25))
        self.maxseatcount_manager.setMinimum(0)
        self.maxseatcount_manager.setMaximum(9999)

        self.horizontalLayout_18.addWidget(self.maxseatcount_manager)

        self.label_24 = QLabel(self.seatcountframe_manager)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 0))
        self.label_24.setMaximumSize(QSize(16777215, 16777215))
        self.label_24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_24)


        self.verticalLayout_7.addWidget(self.seatcountframe_manager)

        self.lengthframe_manager = QFrame(self.frame_10)
        self.lengthframe_manager.setObjectName(u"lengthframe_manager")
        self.lengthframe_manager.setMinimumSize(QSize(0, 41))
        self.lengthframe_manager.setMaximumSize(QSize(500, 16777215))
        self.lengthframe_manager.setFrameShape(QFrame.StyledPanel)
        self.lengthframe_manager.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.lengthframe_manager)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_25 = QLabel(self.lengthframe_manager)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(130, 0))
        self.label_25.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_19.addWidget(self.label_25)

        self.minlength_manager = QSpinBox(self.lengthframe_manager)
        self.minlength_manager.setObjectName(u"minlength_manager")
        self.minlength_manager.setMinimumSize(QSize(0, 25))
        self.minlength_manager.setMinimum(0)
        self.minlength_manager.setMaximum(9999)

        self.horizontalLayout_19.addWidget(self.minlength_manager)

        self.label_26 = QLabel(self.lengthframe_manager)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 0))
        self.label_26.setMaximumSize(QSize(16777215, 16777215))
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_26)

        self.maxlength_manager = QSpinBox(self.lengthframe_manager)
        self.maxlength_manager.setObjectName(u"maxlength_manager")
        self.maxlength_manager.setMinimumSize(QSize(0, 25))
        self.maxlength_manager.setMinimum(0)
        self.maxlength_manager.setMaximum(9999)

        self.horizontalLayout_19.addWidget(self.maxlength_manager)

        self.label_27 = QLabel(self.lengthframe_manager)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 0))
        self.label_27.setMaximumSize(QSize(16777215, 16777215))
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_27)


        self.verticalLayout_7.addWidget(self.lengthframe_manager)

        self.widthframe_manager = QFrame(self.frame_10)
        self.widthframe_manager.setObjectName(u"widthframe_manager")
        self.widthframe_manager.setMinimumSize(QSize(0, 41))
        self.widthframe_manager.setMaximumSize(QSize(500, 16777215))
        self.widthframe_manager.setFrameShape(QFrame.StyledPanel)
        self.widthframe_manager.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.widthframe_manager)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_28 = QLabel(self.widthframe_manager)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(130, 0))
        self.label_28.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_20.addWidget(self.label_28)

        self.minwidth_manager = QSpinBox(self.widthframe_manager)
        self.minwidth_manager.setObjectName(u"minwidth_manager")
        self.minwidth_manager.setMinimumSize(QSize(0, 25))
        self.minwidth_manager.setMinimum(0)
        self.minwidth_manager.setMaximum(9999)

        self.horizontalLayout_20.addWidget(self.minwidth_manager)

        self.label_29 = QLabel(self.widthframe_manager)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 0))
        self.label_29.setMaximumSize(QSize(16777215, 16777215))
        self.label_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_29)

        self.maxwidth_manager = QSpinBox(self.widthframe_manager)
        self.maxwidth_manager.setObjectName(u"maxwidth_manager")
        self.maxwidth_manager.setMinimumSize(QSize(0, 25))
        self.maxwidth_manager.setMinimum(0)
        self.maxwidth_manager.setMaximum(9999)

        self.horizontalLayout_20.addWidget(self.maxwidth_manager)

        self.label_30 = QLabel(self.widthframe_manager)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 0))
        self.label_30.setMaximumSize(QSize(16777215, 16777215))
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_30)


        self.verticalLayout_7.addWidget(self.widthframe_manager)

        self.priceframe_manager = QFrame(self.frame_10)
        self.priceframe_manager.setObjectName(u"priceframe_manager")
        self.priceframe_manager.setMinimumSize(QSize(0, 41))
        self.priceframe_manager.setMaximumSize(QSize(500, 16777215))
        self.priceframe_manager.setFrameShape(QFrame.StyledPanel)
        self.priceframe_manager.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.priceframe_manager)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_31 = QLabel(self.priceframe_manager)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(130, 0))
        self.label_31.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_21.addWidget(self.label_31)

        self.minprice_manager = QSpinBox(self.priceframe_manager)
        self.minprice_manager.setObjectName(u"minprice_manager")
        self.minprice_manager.setMinimumSize(QSize(0, 25))
        self.minprice_manager.setMinimum(0)
        self.minprice_manager.setMaximum(9999)

        self.horizontalLayout_21.addWidget(self.minprice_manager)

        self.label_32 = QLabel(self.priceframe_manager)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(0, 0))
        self.label_32.setMaximumSize(QSize(16777215, 16777215))
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_32)

        self.maxprice_manager = QSpinBox(self.priceframe_manager)
        self.maxprice_manager.setObjectName(u"maxprice_manager")
        self.maxprice_manager.setMinimumSize(QSize(0, 25))
        self.maxprice_manager.setMinimum(0)
        self.maxprice_manager.setMaximum(9999)

        self.horizontalLayout_21.addWidget(self.maxprice_manager)

        self.label_33 = QLabel(self.priceframe_manager)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 0))
        self.label_33.setMaximumSize(QSize(16777215, 16777215))
        self.label_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_33)


        self.verticalLayout_7.addWidget(self.priceframe_manager)

        self.frame_17 = QFrame(self.frame_10)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.submitbuttonproduct_manager = QPushButton(self.frame_17)
        self.submitbuttonproduct_manager.setObjectName(u"submitbuttonproduct_manager")
        self.submitbuttonproduct_manager.setMinimumSize(QSize(0, 25))
        self.submitbuttonproduct_manager.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_25.addWidget(self.submitbuttonproduct_manager)


        self.verticalLayout_7.addWidget(self.frame_17)

        self.productcountframe_manager = QFrame(self.frame_10)
        self.productcountframe_manager.setObjectName(u"productcountframe_manager")
        self.productcountframe_manager.setFrameShape(QFrame.StyledPanel)
        self.productcountframe_manager.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.productcountframe_manager)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.productcount_manager = QLabel(self.productcountframe_manager)
        self.productcount_manager.setObjectName(u"productcount_manager")

        self.horizontalLayout_27.addWidget(self.productcount_manager)


        self.verticalLayout_7.addWidget(self.productcountframe_manager)

        self.producttableframe_manager = QFrame(self.frame_10)
        self.producttableframe_manager.setObjectName(u"producttableframe_manager")
        self.producttableframe_manager.setMinimumSize(QSize(0, 0))
        self.producttableframe_manager.setFrameShape(QFrame.StyledPanel)
        self.producttableframe_manager.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.producttableframe_manager)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.producttable_manager = QTableWidget(self.producttableframe_manager)
        if (self.producttable_manager.columnCount() < 12):
            self.producttable_manager.setColumnCount(12)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.producttable_manager.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.producttable_manager.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.producttable_manager.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.producttable_manager.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.producttable_manager.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.producttable_manager.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.producttable_manager.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.producttable_manager.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.producttable_manager.setHorizontalHeaderItem(8, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.producttable_manager.setHorizontalHeaderItem(9, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.producttable_manager.setHorizontalHeaderItem(10, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.producttable_manager.setHorizontalHeaderItem(11, __qtablewidgetitem19)
        self.producttable_manager.setObjectName(u"producttable_manager")
        self.producttable_manager.setMinimumSize(QSize(0, 450))

        self.horizontalLayout_24.addWidget(self.producttable_manager)


        self.verticalLayout_7.addWidget(self.producttableframe_manager)


        self.verticalLayout.addWidget(self.frame_10)

        self.frame_82 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setMinimumSize(QSize(0, 0))
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_82)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.frame_84 = QFrame(self.frame_82)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.label_82 = QLabel(self.frame_84)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_90.addWidget(self.label_82)


        self.verticalLayout_40.addWidget(self.frame_84)

        self.frame_83 = QFrame(self.frame_82)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMaximumSize(QSize(500, 16777215))
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.label_60 = QLabel(self.frame_83)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(120, 0))
        self.label_60.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_89.addWidget(self.label_60)

        self.branchchoosecount_counts = QComboBox(self.frame_83)
        self.branchchoosecount_counts.addItem("")
        self.branchchoosecount_counts.setObjectName(u"branchchoosecount_counts")
        self.branchchoosecount_counts.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_89.addWidget(self.branchchoosecount_counts)


        self.verticalLayout_40.addWidget(self.frame_83)

        self.frame_85 = QFrame(self.frame_82)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_85)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.employeecount_counts = QLabel(self.frame_85)
        self.employeecount_counts.setObjectName(u"employeecount_counts")

        self.verticalLayout_36.addWidget(self.employeecount_counts)

        self.productcount_counts = QLabel(self.frame_85)
        self.productcount_counts.setObjectName(u"productcount_counts")

        self.verticalLayout_36.addWidget(self.productcount_counts)


        self.verticalLayout_40.addWidget(self.frame_85)

        self.frame_91 = QFrame(self.frame_82)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setMaximumSize(QSize(500, 16777215))
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.label_106 = QLabel(self.frame_91)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setMinimumSize(QSize(120, 0))
        self.label_106.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_93.addWidget(self.label_106)

        self.positionchoose_counts = QComboBox(self.frame_91)
        self.positionchoose_counts.addItem("")
        self.positionchoose_counts.setObjectName(u"positionchoose_counts")
        self.positionchoose_counts.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_93.addWidget(self.positionchoose_counts)


        self.verticalLayout_40.addWidget(self.frame_91)

        self.frame_90 = QFrame(self.frame_82)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_90)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.employeenrolled = QLabel(self.frame_90)
        self.employeenrolled.setObjectName(u"employeenrolled")

        self.verticalLayout_39.addWidget(self.employeenrolled)


        self.verticalLayout_40.addWidget(self.frame_90)

        self.frame_86 = QFrame(self.frame_82)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMaximumSize(QSize(500, 16777215))
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.label_93 = QLabel(self.frame_86)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setMinimumSize(QSize(120, 0))
        self.label_93.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_91.addWidget(self.label_93)

        self.manufacturerchoose_counts = QComboBox(self.frame_86)
        self.manufacturerchoose_counts.addItem("")
        self.manufacturerchoose_counts.setObjectName(u"manufacturerchoose_counts")
        self.manufacturerchoose_counts.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_91.addWidget(self.manufacturerchoose_counts)


        self.verticalLayout_40.addWidget(self.frame_86)

        self.frame_87 = QFrame(self.frame_82)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_87)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.manu_onsale_counts = QLabel(self.frame_87)
        self.manu_onsale_counts.setObjectName(u"manu_onsale_counts")

        self.verticalLayout_37.addWidget(self.manu_onsale_counts)


        self.verticalLayout_40.addWidget(self.frame_87)

        self.frame_88 = QFrame(self.frame_82)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMaximumSize(QSize(500, 16777215))
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.frame_88)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.label_100 = QLabel(self.frame_88)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setMinimumSize(QSize(120, 0))
        self.label_100.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_92.addWidget(self.label_100)

        self.cartypechoose_counts = QComboBox(self.frame_88)
        self.cartypechoose_counts.addItem("")
        self.cartypechoose_counts.setObjectName(u"cartypechoose_counts")
        self.cartypechoose_counts.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_92.addWidget(self.cartypechoose_counts)


        self.verticalLayout_40.addWidget(self.frame_88)

        self.frame_89 = QFrame(self.frame_82)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_89)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.cartype_onsale_counts = QLabel(self.frame_89)
        self.cartype_onsale_counts.setObjectName(u"cartype_onsale_counts")

        self.verticalLayout_38.addWidget(self.cartype_onsale_counts)


        self.verticalLayout_40.addWidget(self.frame_89)


        self.verticalLayout.addWidget(self.frame_82)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_26.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.manager)
        self.it = QWidget()
        self.it.setObjectName(u"it")
        self.verticalLayout_8 = QVBoxLayout(self.it)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_24 = QFrame(self.it)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.refrehsbuttonit = QPushButton(self.frame_24)
        self.refrehsbuttonit.setObjectName(u"refrehsbuttonit")
        self.refrehsbuttonit.setMinimumSize(QSize(50, 50))
        self.refrehsbuttonit.setMaximumSize(QSize(50, 50))
        self.refrehsbuttonit.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"\n"
"")
        self.refrehsbuttonit.setIcon(icon)
        self.refrehsbuttonit.setIconSize(QSize(40, 40))

        self.horizontalLayout_46.addWidget(self.refrehsbuttonit)

        self.label_58 = QLabel(self.frame_24)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"font: 19pt \"Century Gothic\";\n"
"font: 63 28pt \"Bahnschrift SemiBold Condensed\";")
        self.label_58.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_46.addWidget(self.label_58)

        self.profilebuttonit = QPushButton(self.frame_24)
        self.profilebuttonit.setObjectName(u"profilebuttonit")
        self.profilebuttonit.setMinimumSize(QSize(50, 50))
        self.profilebuttonit.setMaximumSize(QSize(50, 50))
        self.profilebuttonit.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"\n"
"")
        self.profilebuttonit.setIcon(icon1)
        self.profilebuttonit.setIconSize(QSize(40, 40))

        self.horizontalLayout_46.addWidget(self.profilebuttonit)


        self.verticalLayout_8.addWidget(self.frame_24)

        self.scrollArea_2 = QScrollArea(self.it)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -3787, 831, 4317))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_70 = QFrame(self.scrollAreaWidgetContents)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(0, 0))
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_70)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_11 = QFrame(self.frame_70)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_40 = QLabel(self.frame_11)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_28.addWidget(self.label_40)


        self.verticalLayout_21.addWidget(self.frame_11)

        self.frame_19 = QFrame(self.frame_70)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(500, 16777215))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_19)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_43 = QLabel(self.frame_19)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"font: 75 11pt \"MS Shell Dlg 2\";")

        self.verticalLayout_10.addWidget(self.label_43)

        self.branchactionchoose_it = QComboBox(self.frame_19)
        self.branchactionchoose_it.addItem("")
        self.branchactionchoose_it.addItem("")
        self.branchactionchoose_it.addItem("")
        self.branchactionchoose_it.setObjectName(u"branchactionchoose_it")
        self.branchactionchoose_it.setMinimumSize(QSize(0, 25))

        self.verticalLayout_10.addWidget(self.branchactionchoose_it)


        self.verticalLayout_21.addWidget(self.frame_19)

        self.selectbranchframe_it = QFrame(self.frame_70)
        self.selectbranchframe_it.setObjectName(u"selectbranchframe_it")
        self.selectbranchframe_it.setMaximumSize(QSize(500, 16777215))
        self.selectbranchframe_it.setFrameShape(QFrame.StyledPanel)
        self.selectbranchframe_it.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.selectbranchframe_it)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_46 = QLabel(self.selectbranchframe_it)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(120, 0))
        self.label_46.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_33.addWidget(self.label_46)

        self.selectbranch_it = QComboBox(self.selectbranchframe_it)
        self.selectbranch_it.addItem("")
        self.selectbranch_it.addItem("")
        self.selectbranch_it.addItem("")
        self.selectbranch_it.addItem("")
        self.selectbranch_it.addItem("")
        self.selectbranch_it.addItem("")
        self.selectbranch_it.addItem("")
        self.selectbranch_it.setObjectName(u"selectbranch_it")
        self.selectbranch_it.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_33.addWidget(self.selectbranch_it)


        self.verticalLayout_21.addWidget(self.selectbranchframe_it)

        self.newbranchframe_it = QFrame(self.frame_70)
        self.newbranchframe_it.setObjectName(u"newbranchframe_it")
        self.newbranchframe_it.setMaximumSize(QSize(500, 16777215))
        self.newbranchframe_it.setFrameShape(QFrame.StyledPanel)
        self.newbranchframe_it.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.newbranchframe_it)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_42 = QLabel(self.newbranchframe_it)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(120, 0))
        self.label_42.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_30.addWidget(self.label_42)

        self.branchname_addedit_it = QLineEdit(self.newbranchframe_it)
        self.branchname_addedit_it.setObjectName(u"branchname_addedit_it")

        self.horizontalLayout_30.addWidget(self.branchname_addedit_it)


        self.verticalLayout_21.addWidget(self.newbranchframe_it)

        self.addressframe_it = QFrame(self.frame_70)
        self.addressframe_it.setObjectName(u"addressframe_it")
        self.addressframe_it.setMaximumSize(QSize(500, 16777215))
        self.addressframe_it.setFrameShape(QFrame.StyledPanel)
        self.addressframe_it.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.addressframe_it)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_44 = QLabel(self.addressframe_it)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(120, 0))
        self.label_44.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_31.addWidget(self.label_44)

        self.address_addedit_it = QTextEdit(self.addressframe_it)
        self.address_addedit_it.setObjectName(u"address_addedit_it")

        self.horizontalLayout_31.addWidget(self.address_addedit_it)


        self.verticalLayout_21.addWidget(self.addressframe_it)

        self.establishedframe_edit = QFrame(self.frame_70)
        self.establishedframe_edit.setObjectName(u"establishedframe_edit")
        self.establishedframe_edit.setMaximumSize(QSize(500, 16777215))
        self.establishedframe_edit.setFrameShape(QFrame.StyledPanel)
        self.establishedframe_edit.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.establishedframe_edit)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_45 = QLabel(self.establishedframe_edit)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(120, 0))
        self.label_45.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_32.addWidget(self.label_45)

        self.established_addedit_it = QSpinBox(self.establishedframe_edit)
        self.established_addedit_it.setObjectName(u"established_addedit_it")
        self.established_addedit_it.setMaximum(999999999)

        self.horizontalLayout_32.addWidget(self.established_addedit_it)


        self.verticalLayout_21.addWidget(self.establishedframe_edit)

        self.frame_20 = QFrame(self.frame_70)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.addbranchbt_it = QPushButton(self.frame_20)
        self.addbranchbt_it.setObjectName(u"addbranchbt_it")
        self.addbranchbt_it.setMinimumSize(QSize(0, 25))
        self.addbranchbt_it.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_36.addWidget(self.addbranchbt_it)

        self.editbranchbt_it = QPushButton(self.frame_20)
        self.editbranchbt_it.setObjectName(u"editbranchbt_it")
        self.editbranchbt_it.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_36.addWidget(self.editbranchbt_it)

        self.deletebranchbt_it = QPushButton(self.frame_20)
        self.deletebranchbt_it.setObjectName(u"deletebranchbt_it")
        self.deletebranchbt_it.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_36.addWidget(self.deletebranchbt_it)


        self.verticalLayout_21.addWidget(self.frame_20)


        self.verticalLayout_9.addWidget(self.frame_70)

        self.frame_31 = QFrame(self.scrollAreaWidgetContents)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(0, 0))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_31)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_62 = QLabel(self.frame_32)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_49.addWidget(self.label_62)


        self.verticalLayout_17.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_31)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(500, 16777215))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_33)
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_63 = QLabel(self.frame_33)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setStyleSheet(u"font: 75 11pt \"MS Shell Dlg 2\";")

        self.verticalLayout_16.addWidget(self.label_63)

        self.positionchoose = QComboBox(self.frame_33)
        self.positionchoose.addItem("")
        self.positionchoose.addItem("")
        self.positionchoose.addItem("")
        self.positionchoose.setObjectName(u"positionchoose")
        self.positionchoose.setMinimumSize(QSize(0, 25))

        self.verticalLayout_16.addWidget(self.positionchoose)


        self.verticalLayout_17.addWidget(self.frame_33)

        self.selectpositionframe = QFrame(self.frame_31)
        self.selectpositionframe.setObjectName(u"selectpositionframe")
        self.selectpositionframe.setMaximumSize(QSize(500, 16777215))
        self.selectpositionframe.setFrameShape(QFrame.StyledPanel)
        self.selectpositionframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.selectpositionframe)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_65 = QLabel(self.selectpositionframe)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(120, 0))
        self.label_65.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_51.addWidget(self.label_65)

        self.selectposition = QComboBox(self.selectpositionframe)
        self.selectposition.addItem("")
        self.selectposition.addItem("")
        self.selectposition.addItem("")
        self.selectposition.addItem("")
        self.selectposition.addItem("")
        self.selectposition.addItem("")
        self.selectposition.addItem("")
        self.selectposition.setObjectName(u"selectposition")
        self.selectposition.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_51.addWidget(self.selectposition)


        self.verticalLayout_17.addWidget(self.selectpositionframe)

        self.newpositionnameframe = QFrame(self.frame_31)
        self.newpositionnameframe.setObjectName(u"newpositionnameframe")
        self.newpositionnameframe.setMaximumSize(QSize(500, 16777215))
        self.newpositionnameframe.setFrameShape(QFrame.StyledPanel)
        self.newpositionnameframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.newpositionnameframe)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_64 = QLabel(self.newpositionnameframe)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(120, 0))
        self.label_64.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_50.addWidget(self.label_64)

        self.newposname = QLineEdit(self.newpositionnameframe)
        self.newposname.setObjectName(u"newposname")

        self.horizontalLayout_50.addWidget(self.newposname)


        self.verticalLayout_17.addWidget(self.newpositionnameframe)

        self.posdescframe_it = QFrame(self.frame_31)
        self.posdescframe_it.setObjectName(u"posdescframe_it")
        self.posdescframe_it.setMinimumSize(QSize(0, 0))
        self.posdescframe_it.setMaximumSize(QSize(500, 16777215))
        self.posdescframe_it.setFrameShape(QFrame.StyledPanel)
        self.posdescframe_it.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.posdescframe_it)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.label_69 = QLabel(self.posdescframe_it)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMinimumSize(QSize(120, 0))
        self.label_69.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_79.addWidget(self.label_69)

        self.positiondesc_it = QTextEdit(self.posdescframe_it)
        self.positiondesc_it.setObjectName(u"positiondesc_it")

        self.horizontalLayout_79.addWidget(self.positiondesc_it)


        self.verticalLayout_17.addWidget(self.posdescframe_it)

        self.frame_34 = QFrame(self.frame_31)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.addpositionbt_it = QPushButton(self.frame_34)
        self.addpositionbt_it.setObjectName(u"addpositionbt_it")
        self.addpositionbt_it.setMinimumSize(QSize(0, 25))
        self.addpositionbt_it.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_53.addWidget(self.addpositionbt_it)

        self.editpositionbt_it = QPushButton(self.frame_34)
        self.editpositionbt_it.setObjectName(u"editpositionbt_it")
        self.editpositionbt_it.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_53.addWidget(self.editpositionbt_it)

        self.deletepositionbt_it = QPushButton(self.frame_34)
        self.deletepositionbt_it.setObjectName(u"deletepositionbt_it")
        self.deletepositionbt_it.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_53.addWidget(self.deletepositionbt_it)


        self.verticalLayout_17.addWidget(self.frame_34)


        self.verticalLayout_9.addWidget(self.frame_31)

        self.frame_22 = QFrame(self.scrollAreaWidgetContents)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 0))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_22)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_21 = QFrame(self.frame_22)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_48 = QLabel(self.frame_21)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_34.addWidget(self.label_48)


        self.verticalLayout_15.addWidget(self.frame_21)

        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(500, 16777215))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_23)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_49 = QLabel(self.frame_23)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"font: 75 11pt \"MS Shell Dlg 2\";")

        self.verticalLayout_11.addWidget(self.label_49)

        self.employeeactionchoose_it = QComboBox(self.frame_23)
        self.employeeactionchoose_it.addItem("")
        self.employeeactionchoose_it.addItem("")
        self.employeeactionchoose_it.addItem("")
        self.employeeactionchoose_it.setObjectName(u"employeeactionchoose_it")
        self.employeeactionchoose_it.setMinimumSize(QSize(0, 25))

        self.verticalLayout_11.addWidget(self.employeeactionchoose_it)


        self.verticalLayout_15.addWidget(self.frame_23)

        self.employeetableframe_editdel_it = QFrame(self.frame_22)
        self.employeetableframe_editdel_it.setObjectName(u"employeetableframe_editdel_it")
        self.employeetableframe_editdel_it.setMinimumSize(QSize(0, 0))
        self.employeetableframe_editdel_it.setFrameShape(QFrame.StyledPanel)
        self.employeetableframe_editdel_it.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.employeetableframe_editdel_it)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_69 = QFrame(self.employeetableframe_editdel_it)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.getemployeebt_it = QPushButton(self.frame_69)
        self.getemployeebt_it.setObjectName(u"getemployeebt_it")
        self.getemployeebt_it.setMinimumSize(QSize(0, 25))
        self.getemployeebt_it.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_3.addWidget(self.getemployeebt_it)


        self.verticalLayout_13.addWidget(self.frame_69)

        self.frame_25 = QFrame(self.employeetableframe_editdel_it)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_38.addWidget(self.frame_26)

        self.label_51 = QLabel(self.frame_25)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMaximumSize(QSize(61, 31))
        self.label_51.setStyleSheet(u"")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_51)

        self.searchbox_it = QLineEdit(self.frame_25)
        self.searchbox_it.setObjectName(u"searchbox_it")
        self.searchbox_it.setMinimumSize(QSize(200, 0))
        self.searchbox_it.setMaximumSize(QSize(171, 31))
        self.searchbox_it.setStyleSheet(u"QLineEdit {\n"
"	padding: 5px;\n"
"}")

        self.horizontalLayout_38.addWidget(self.searchbox_it)

        self.searchbutton_it = QPushButton(self.frame_25)
        self.searchbutton_it.setObjectName(u"searchbutton_it")
        self.searchbutton_it.setMinimumSize(QSize(0, 30))
        self.searchbutton_it.setMaximumSize(QSize(30, 16777215))
        self.searchbutton_it.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"data/img/search_large.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchbutton_it.setIcon(icon2)
        self.searchbutton_it.setIconSize(QSize(15, 15))

        self.horizontalLayout_38.addWidget(self.searchbutton_it)


        self.verticalLayout_13.addWidget(self.frame_25)

        self.frame_78 = QFrame(self.employeetableframe_editdel_it)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMinimumSize(QSize(0, 0))
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(9, 0, 0, 0)
        self.employeecount_it = QLabel(self.frame_78)
        self.employeecount_it.setObjectName(u"employeecount_it")

        self.horizontalLayout_69.addWidget(self.employeecount_it)


        self.verticalLayout_13.addWidget(self.frame_78)

        self.employeetableframe_it = QFrame(self.employeetableframe_editdel_it)
        self.employeetableframe_it.setObjectName(u"employeetableframe_it")
        self.employeetableframe_it.setMinimumSize(QSize(0, 450))
        self.employeetableframe_it.setFrameShape(QFrame.StyledPanel)
        self.employeetableframe_it.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.employeetableframe_it)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.employeetable_editdelete_it = QTableWidget(self.employeetableframe_it)
        if (self.employeetable_editdelete_it.columnCount() < 10):
            self.employeetable_editdelete_it.setColumnCount(10)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.employeetable_editdelete_it.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.employeetable_editdelete_it.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.employeetable_editdelete_it.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.employeetable_editdelete_it.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.employeetable_editdelete_it.setHorizontalHeaderItem(4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.employeetable_editdelete_it.setHorizontalHeaderItem(5, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.employeetable_editdelete_it.setHorizontalHeaderItem(6, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.employeetable_editdelete_it.setHorizontalHeaderItem(7, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.employeetable_editdelete_it.setHorizontalHeaderItem(8, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.employeetable_editdelete_it.setHorizontalHeaderItem(9, __qtablewidgetitem29)
        self.employeetable_editdelete_it.setObjectName(u"employeetable_editdelete_it")

        self.horizontalLayout_37.addWidget(self.employeetable_editdelete_it)


        self.verticalLayout_13.addWidget(self.employeetableframe_it)


        self.verticalLayout_15.addWidget(self.employeetableframe_editdel_it)

        self.employee_addedit_it = QFrame(self.frame_22)
        self.employee_addedit_it.setObjectName(u"employee_addedit_it")
        self.employee_addedit_it.setMinimumSize(QSize(0, 0))
        self.employee_addedit_it.setFrameShape(QFrame.StyledPanel)
        self.employee_addedit_it.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.employee_addedit_it)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_28 = QFrame(self.employee_addedit_it)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(500, 16777215))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_53 = QLabel(self.frame_28)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(90, 0))
        self.label_53.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_41.addWidget(self.label_53)

        self.branchchoose_addedit_it = QComboBox(self.frame_28)
        self.branchchoose_addedit_it.addItem("")
        self.branchchoose_addedit_it.addItem("")
        self.branchchoose_addedit_it.addItem("")
        self.branchchoose_addedit_it.addItem("")
        self.branchchoose_addedit_it.addItem("")
        self.branchchoose_addedit_it.addItem("")
        self.branchchoose_addedit_it.addItem("")
        self.branchchoose_addedit_it.setObjectName(u"branchchoose_addedit_it")
        self.branchchoose_addedit_it.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_41.addWidget(self.branchchoose_addedit_it)


        self.verticalLayout_12.addWidget(self.frame_28)

        self.newbranchframe_it_2 = QFrame(self.employee_addedit_it)
        self.newbranchframe_it_2.setObjectName(u"newbranchframe_it_2")
        self.newbranchframe_it_2.setMaximumSize(QSize(500, 16777215))
        self.newbranchframe_it_2.setFrameShape(QFrame.StyledPanel)
        self.newbranchframe_it_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.newbranchframe_it_2)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_50 = QLabel(self.newbranchframe_it_2)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(90, 0))
        self.label_50.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_39.addWidget(self.label_50)

        self.firstname_addedit_it = QLineEdit(self.newbranchframe_it_2)
        self.firstname_addedit_it.setObjectName(u"firstname_addedit_it")

        self.horizontalLayout_39.addWidget(self.firstname_addedit_it)


        self.verticalLayout_12.addWidget(self.newbranchframe_it_2)

        self.newbranchframe_it_3 = QFrame(self.employee_addedit_it)
        self.newbranchframe_it_3.setObjectName(u"newbranchframe_it_3")
        self.newbranchframe_it_3.setMaximumSize(QSize(500, 16777215))
        self.newbranchframe_it_3.setFrameShape(QFrame.StyledPanel)
        self.newbranchframe_it_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.newbranchframe_it_3)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_52 = QLabel(self.newbranchframe_it_3)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(90, 0))
        self.label_52.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_40.addWidget(self.label_52)

        self.lastname_addedit_it = QLineEdit(self.newbranchframe_it_3)
        self.lastname_addedit_it.setObjectName(u"lastname_addedit_it")

        self.horizontalLayout_40.addWidget(self.lastname_addedit_it)


        self.verticalLayout_12.addWidget(self.newbranchframe_it_3)

        self.displaygenderframe_manager_2 = QFrame(self.employee_addedit_it)
        self.displaygenderframe_manager_2.setObjectName(u"displaygenderframe_manager_2")
        self.displaygenderframe_manager_2.setMaximumSize(QSize(500, 16777215))
        self.displaygenderframe_manager_2.setFrameShape(QFrame.StyledPanel)
        self.displaygenderframe_manager_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.displaygenderframe_manager_2)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_54 = QLabel(self.displaygenderframe_manager_2)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(90, 0))
        self.label_54.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_42.addWidget(self.label_54)

        self.gender_addedit_it = QComboBox(self.displaygenderframe_manager_2)
        self.gender_addedit_it.addItem("")
        self.gender_addedit_it.addItem("")
        self.gender_addedit_it.setObjectName(u"gender_addedit_it")
        self.gender_addedit_it.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_42.addWidget(self.gender_addedit_it)


        self.verticalLayout_12.addWidget(self.displaygenderframe_manager_2)

        self.frame_72 = QFrame(self.employee_addedit_it)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMinimumSize(QSize(0, 0))
        self.frame_72.setMaximumSize(QSize(500, 16777215))
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_72)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_73 = QFrame(self.frame_72)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMaximumSize(QSize(16777215, 16777215))
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, -1, -1, -1)
        self.label_66 = QLabel(self.frame_73)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(90, 0))
        self.label_66.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_52.addWidget(self.label_66)

        self.born_addedit_it = QDateEdit(self.frame_73)
        self.born_addedit_it.setObjectName(u"born_addedit_it")
        self.born_addedit_it.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_52.addWidget(self.born_addedit_it)


        self.verticalLayout_28.addWidget(self.frame_73)

        self.label_73 = QLabel(self.frame_72)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setStyleSheet(u"")

        self.verticalLayout_28.addWidget(self.label_73)


        self.verticalLayout_12.addWidget(self.frame_72)

        self.displaypositionframe_manager_2 = QFrame(self.employee_addedit_it)
        self.displaypositionframe_manager_2.setObjectName(u"displaypositionframe_manager_2")
        self.displaypositionframe_manager_2.setMinimumSize(QSize(0, 41))
        self.displaypositionframe_manager_2.setMaximumSize(QSize(500, 16777215))
        self.displaypositionframe_manager_2.setFrameShape(QFrame.StyledPanel)
        self.displaypositionframe_manager_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.displaypositionframe_manager_2)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_59 = QLabel(self.displaypositionframe_manager_2)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(90, 0))
        self.label_59.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_47.addWidget(self.label_59)

        self.position_addedit_it = QComboBox(self.displaypositionframe_manager_2)
        self.position_addedit_it.addItem("")
        self.position_addedit_it.addItem("")
        self.position_addedit_it.addItem("")
        self.position_addedit_it.addItem("")
        self.position_addedit_it.addItem("")
        self.position_addedit_it.addItem("")
        self.position_addedit_it.addItem("")
        self.position_addedit_it.addItem("")
        self.position_addedit_it.setObjectName(u"position_addedit_it")
        self.position_addedit_it.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_47.addWidget(self.position_addedit_it)


        self.verticalLayout_12.addWidget(self.displaypositionframe_manager_2)

        self.loginpassframe_it = QFrame(self.employee_addedit_it)
        self.loginpassframe_it.setObjectName(u"loginpassframe_it")
        self.loginpassframe_it.setMinimumSize(QSize(0, 0))
        self.loginpassframe_it.setMaximumSize(QSize(500, 16777215))
        self.loginpassframe_it.setFrameShape(QFrame.StyledPanel)
        self.loginpassframe_it.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.loginpassframe_it)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_75 = QLabel(self.loginpassframe_it)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMinimumSize(QSize(90, 0))
        self.label_75.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_35.addWidget(self.label_75)

        self.password_addedit_it = QLineEdit(self.loginpassframe_it)
        self.password_addedit_it.setObjectName(u"password_addedit_it")

        self.horizontalLayout_35.addWidget(self.password_addedit_it)


        self.verticalLayout_12.addWidget(self.loginpassframe_it)

        self.newbranchframe_it_6 = QFrame(self.employee_addedit_it)
        self.newbranchframe_it_6.setObjectName(u"newbranchframe_it_6")
        self.newbranchframe_it_6.setMaximumSize(QSize(500, 16777215))
        self.newbranchframe_it_6.setFrameShape(QFrame.StyledPanel)
        self.newbranchframe_it_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.newbranchframe_it_6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_29 = QFrame(self.newbranchframe_it_6)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, -1, -1, -1)
        self.label_56 = QLabel(self.frame_29)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(90, 0))
        self.label_56.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_44.addWidget(self.label_56)

        self.phonenumber_addedit_it = QLineEdit(self.frame_29)
        self.phonenumber_addedit_it.setObjectName(u"phonenumber_addedit_it")

        self.horizontalLayout_44.addWidget(self.phonenumber_addedit_it)


        self.verticalLayout_14.addWidget(self.frame_29)

        self.label_61 = QLabel(self.newbranchframe_it_6)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setStyleSheet(u"")

        self.verticalLayout_14.addWidget(self.label_61)


        self.verticalLayout_12.addWidget(self.newbranchframe_it_6)

        self.newbranchframe_it_7 = QFrame(self.employee_addedit_it)
        self.newbranchframe_it_7.setObjectName(u"newbranchframe_it_7")
        self.newbranchframe_it_7.setMinimumSize(QSize(500, 80))
        self.newbranchframe_it_7.setMaximumSize(QSize(500, 80))
        self.newbranchframe_it_7.setFrameShape(QFrame.StyledPanel)
        self.newbranchframe_it_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.newbranchframe_it_7)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_57 = QLabel(self.newbranchframe_it_7)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(90, 0))
        self.label_57.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_45.addWidget(self.label_57)

        self.addressemp_addedit_it = QTextEdit(self.newbranchframe_it_7)
        self.addressemp_addedit_it.setObjectName(u"addressemp_addedit_it")

        self.horizontalLayout_45.addWidget(self.addressemp_addedit_it)


        self.verticalLayout_12.addWidget(self.newbranchframe_it_7)


        self.verticalLayout_15.addWidget(self.employee_addedit_it)

        self.frame_30 = QFrame(self.frame_22)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.addemployeebtt_it = QPushButton(self.frame_30)
        self.addemployeebtt_it.setObjectName(u"addemployeebtt_it")
        self.addemployeebtt_it.setMinimumSize(QSize(0, 25))
        self.addemployeebtt_it.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_48.addWidget(self.addemployeebtt_it)

        self.editemployeebtt_it = QPushButton(self.frame_30)
        self.editemployeebtt_it.setObjectName(u"editemployeebtt_it")
        self.editemployeebtt_it.setMinimumSize(QSize(0, 25))
        self.editemployeebtt_it.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_48.addWidget(self.editemployeebtt_it)

        self.deleteemployeebtt_it = QPushButton(self.frame_30)
        self.deleteemployeebtt_it.setObjectName(u"deleteemployeebtt_it")
        self.deleteemployeebtt_it.setMinimumSize(QSize(0, 25))
        self.deleteemployeebtt_it.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_48.addWidget(self.deleteemployeebtt_it)


        self.verticalLayout_15.addWidget(self.frame_30)


        self.verticalLayout_9.addWidget(self.frame_22)

        self.frame_41 = QFrame(self.scrollAreaWidgetContents)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(0, 0))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_41)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_42 = QFrame(self.frame_41)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_70 = QLabel(self.frame_42)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_57.addWidget(self.label_70)


        self.verticalLayout_20.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.frame_41)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMaximumSize(QSize(500, 16777215))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_43)
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_71 = QLabel(self.frame_43)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setStyleSheet(u"font: 75 11pt \"MS Shell Dlg 2\";")

        self.verticalLayout_19.addWidget(self.label_71)

        self.manufacturerchoose = QComboBox(self.frame_43)
        self.manufacturerchoose.addItem("")
        self.manufacturerchoose.addItem("")
        self.manufacturerchoose.addItem("")
        self.manufacturerchoose.setObjectName(u"manufacturerchoose")
        self.manufacturerchoose.setMinimumSize(QSize(0, 25))

        self.verticalLayout_19.addWidget(self.manufacturerchoose)


        self.verticalLayout_20.addWidget(self.frame_43)

        self.selectmanufacturerframe = QFrame(self.frame_41)
        self.selectmanufacturerframe.setObjectName(u"selectmanufacturerframe")
        self.selectmanufacturerframe.setMaximumSize(QSize(500, 16777215))
        self.selectmanufacturerframe.setFrameShape(QFrame.StyledPanel)
        self.selectmanufacturerframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.selectmanufacturerframe)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_72 = QLabel(self.selectmanufacturerframe)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMinimumSize(QSize(150, 0))
        self.label_72.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_58.addWidget(self.label_72)

        self.selectmanufacturer = QComboBox(self.selectmanufacturerframe)
        self.selectmanufacturer.addItem("")
        self.selectmanufacturer.addItem("")
        self.selectmanufacturer.addItem("")
        self.selectmanufacturer.addItem("")
        self.selectmanufacturer.addItem("")
        self.selectmanufacturer.addItem("")
        self.selectmanufacturer.addItem("")
        self.selectmanufacturer.setObjectName(u"selectmanufacturer")
        self.selectmanufacturer.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_58.addWidget(self.selectmanufacturer)


        self.verticalLayout_20.addWidget(self.selectmanufacturerframe)

        self.newmanufacturerframe = QFrame(self.frame_41)
        self.newmanufacturerframe.setObjectName(u"newmanufacturerframe")
        self.newmanufacturerframe.setMaximumSize(QSize(500, 16777215))
        self.newmanufacturerframe.setFrameShape(QFrame.StyledPanel)
        self.newmanufacturerframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.newmanufacturerframe)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_74 = QLabel(self.newmanufacturerframe)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMinimumSize(QSize(150, 0))
        self.label_74.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_60.addWidget(self.label_74)

        self.newmanufacturername = QLineEdit(self.newmanufacturerframe)
        self.newmanufacturername.setObjectName(u"newmanufacturername")

        self.horizontalLayout_60.addWidget(self.newmanufacturername)


        self.verticalLayout_20.addWidget(self.newmanufacturerframe)

        self.countryframe_it = QFrame(self.frame_41)
        self.countryframe_it.setObjectName(u"countryframe_it")
        self.countryframe_it.setMinimumSize(QSize(0, 0))
        self.countryframe_it.setMaximumSize(QSize(500, 16777215))
        self.countryframe_it.setFrameShape(QFrame.StyledPanel)
        self.countryframe_it.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.countryframe_it)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_76 = QLabel(self.countryframe_it)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMinimumSize(QSize(150, 0))
        self.label_76.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_43.addWidget(self.label_76)

        self.mcountry_it = QLineEdit(self.countryframe_it)
        self.mcountry_it.setObjectName(u"mcountry_it")

        self.horizontalLayout_43.addWidget(self.mcountry_it)


        self.verticalLayout_20.addWidget(self.countryframe_it)

        self.yearframe_it = QFrame(self.frame_41)
        self.yearframe_it.setObjectName(u"yearframe_it")
        self.yearframe_it.setMinimumSize(QSize(0, 0))
        self.yearframe_it.setMaximumSize(QSize(500, 16777215))
        self.yearframe_it.setFrameShape(QFrame.StyledPanel)
        self.yearframe_it.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.yearframe_it)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_77 = QLabel(self.yearframe_it)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMinimumSize(QSize(150, 0))
        self.label_77.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_59.addWidget(self.label_77)

        self.yearestablished_it = QSpinBox(self.yearframe_it)
        self.yearestablished_it.setObjectName(u"yearestablished_it")
        self.yearestablished_it.setMaximum(99999)

        self.horizontalLayout_59.addWidget(self.yearestablished_it)


        self.verticalLayout_20.addWidget(self.yearframe_it)

        self.frame_44 = QFrame(self.frame_41)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.addmanufacturerbt = QPushButton(self.frame_44)
        self.addmanufacturerbt.setObjectName(u"addmanufacturerbt")
        self.addmanufacturerbt.setMinimumSize(QSize(0, 25))
        self.addmanufacturerbt.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_61.addWidget(self.addmanufacturerbt)

        self.editmanufacturerbt = QPushButton(self.frame_44)
        self.editmanufacturerbt.setObjectName(u"editmanufacturerbt")
        self.editmanufacturerbt.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_61.addWidget(self.editmanufacturerbt)

        self.deletemanufacturerbt = QPushButton(self.frame_44)
        self.deletemanufacturerbt.setObjectName(u"deletemanufacturerbt")
        self.deletemanufacturerbt.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_61.addWidget(self.deletemanufacturerbt)


        self.verticalLayout_20.addWidget(self.frame_44)


        self.verticalLayout_9.addWidget(self.frame_41)

        self.frame_45 = QFrame(self.scrollAreaWidgetContents)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(0, 0))
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_45)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_46 = QFrame(self.frame_45)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_80 = QLabel(self.frame_46)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_67.addWidget(self.label_80)


        self.verticalLayout_23.addWidget(self.frame_46)

        self.frame_48 = QFrame(self.frame_45)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMaximumSize(QSize(500, 16777215))
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_48)
        self.verticalLayout_22.setSpacing(10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_84 = QLabel(self.frame_48)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setStyleSheet(u"font: 75 11pt \"MS Shell Dlg 2\";")

        self.verticalLayout_22.addWidget(self.label_84)

        self.cartypechoose = QComboBox(self.frame_48)
        self.cartypechoose.addItem("")
        self.cartypechoose.addItem("")
        self.cartypechoose.addItem("")
        self.cartypechoose.setObjectName(u"cartypechoose")
        self.cartypechoose.setMinimumSize(QSize(0, 25))

        self.verticalLayout_22.addWidget(self.cartypechoose)


        self.verticalLayout_23.addWidget(self.frame_48)

        self.selectcartypeframe = QFrame(self.frame_45)
        self.selectcartypeframe.setObjectName(u"selectcartypeframe")
        self.selectcartypeframe.setMaximumSize(QSize(500, 16777215))
        self.selectcartypeframe.setFrameShape(QFrame.StyledPanel)
        self.selectcartypeframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.selectcartypeframe)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_81 = QLabel(self.selectcartypeframe)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setMinimumSize(QSize(150, 0))
        self.label_81.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_68.addWidget(self.label_81)

        self.selectcartype = QComboBox(self.selectcartypeframe)
        self.selectcartype.addItem("")
        self.selectcartype.addItem("")
        self.selectcartype.addItem("")
        self.selectcartype.addItem("")
        self.selectcartype.addItem("")
        self.selectcartype.addItem("")
        self.selectcartype.addItem("")
        self.selectcartype.setObjectName(u"selectcartype")
        self.selectcartype.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_68.addWidget(self.selectcartype)


        self.verticalLayout_23.addWidget(self.selectcartypeframe)

        self.newcartypenameframe = QFrame(self.frame_45)
        self.newcartypenameframe.setObjectName(u"newcartypenameframe")
        self.newcartypenameframe.setMaximumSize(QSize(500, 16777215))
        self.newcartypenameframe.setFrameShape(QFrame.StyledPanel)
        self.newcartypenameframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.newcartypenameframe)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.label_83 = QLabel(self.newcartypenameframe)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setMinimumSize(QSize(150, 0))
        self.label_83.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_70.addWidget(self.label_83)

        self.newcartypename = QLineEdit(self.newcartypenameframe)
        self.newcartypename.setObjectName(u"newcartypename")

        self.horizontalLayout_70.addWidget(self.newcartypename)


        self.verticalLayout_23.addWidget(self.newcartypenameframe)

        self.inventedframe_it = QFrame(self.frame_45)
        self.inventedframe_it.setObjectName(u"inventedframe_it")
        self.inventedframe_it.setMinimumSize(QSize(0, 0))
        self.inventedframe_it.setMaximumSize(QSize(500, 16777215))
        self.inventedframe_it.setFrameShape(QFrame.StyledPanel)
        self.inventedframe_it.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.inventedframe_it)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.label_79 = QLabel(self.inventedframe_it)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMinimumSize(QSize(150, 0))
        self.label_79.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_88.addWidget(self.label_79)

        self.invented_it = QSpinBox(self.inventedframe_it)
        self.invented_it.setObjectName(u"invented_it")
        self.invented_it.setMaximum(99999)

        self.horizontalLayout_88.addWidget(self.invented_it)


        self.verticalLayout_23.addWidget(self.inventedframe_it)

        self.frame_47 = QFrame(self.frame_45)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.addcartypebt = QPushButton(self.frame_47)
        self.addcartypebt.setObjectName(u"addcartypebt")
        self.addcartypebt.setMinimumSize(QSize(0, 25))
        self.addcartypebt.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_71.addWidget(self.addcartypebt)

        self.editcartypebt = QPushButton(self.frame_47)
        self.editcartypebt.setObjectName(u"editcartypebt")
        self.editcartypebt.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_71.addWidget(self.editcartypebt)

        self.deletecartypebt = QPushButton(self.frame_47)
        self.deletecartypebt.setObjectName(u"deletecartypebt")
        self.deletecartypebt.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_71.addWidget(self.deletecartypebt)


        self.verticalLayout_23.addWidget(self.frame_47)


        self.verticalLayout_9.addWidget(self.frame_45)

        self.frame_35 = QFrame(self.scrollAreaWidgetContents)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 0))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_35)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_37 = QFrame(self.frame_35)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_68 = QLabel(self.frame_37)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_54.addWidget(self.label_68)


        self.verticalLayout_32.addWidget(self.frame_37)

        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(500, 16777215))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_36)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_67 = QLabel(self.frame_36)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setStyleSheet(u"font: 75 11pt \"MS Shell Dlg 2\";")

        self.verticalLayout_18.addWidget(self.label_67)

        self.productchoose = QComboBox(self.frame_36)
        self.productchoose.addItem("")
        self.productchoose.addItem("")
        self.productchoose.addItem("")
        self.productchoose.setObjectName(u"productchoose")
        self.productchoose.setMinimumSize(QSize(0, 25))

        self.verticalLayout_18.addWidget(self.productchoose)


        self.verticalLayout_32.addWidget(self.frame_36)

        self.producttableframe_it = QFrame(self.frame_35)
        self.producttableframe_it.setObjectName(u"producttableframe_it")
        self.producttableframe_it.setMinimumSize(QSize(0, 0))
        self.producttableframe_it.setFrameShape(QFrame.StyledPanel)
        self.producttableframe_it.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.producttableframe_it)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_71 = QFrame(self.producttableframe_it)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMinimumSize(QSize(0, 0))
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.getproductbt_it_2 = QPushButton(self.frame_71)
        self.getproductbt_it_2.setObjectName(u"getproductbt_it_2")
        self.getproductbt_it_2.setMinimumSize(QSize(0, 25))
        self.getproductbt_it_2.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_63.addWidget(self.getproductbt_it_2)


        self.verticalLayout_34.addWidget(self.frame_71)

        self.frame_38 = QFrame(self.producttableframe_it)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.frame_74 = QFrame(self.frame_38)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_64.addWidget(self.frame_74)

        self.label_78 = QLabel(self.frame_38)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMaximumSize(QSize(61, 31))
        self.label_78.setStyleSheet(u"")
        self.label_78.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_64.addWidget(self.label_78)

        self.searchproductfield_2 = QLineEdit(self.frame_38)
        self.searchproductfield_2.setObjectName(u"searchproductfield_2")
        self.searchproductfield_2.setMinimumSize(QSize(200, 0))
        self.searchproductfield_2.setMaximumSize(QSize(171, 31))
        self.searchproductfield_2.setStyleSheet(u"QLineEdit {\n"
"	padding: 5px;\n"
"}")

        self.horizontalLayout_64.addWidget(self.searchproductfield_2)

        self.searchproductbutton_2 = QPushButton(self.frame_38)
        self.searchproductbutton_2.setObjectName(u"searchproductbutton_2")
        self.searchproductbutton_2.setMinimumSize(QSize(0, 30))
        self.searchproductbutton_2.setMaximumSize(QSize(30, 16777215))
        self.searchproductbutton_2.setStyleSheet(u"")
        self.searchproductbutton_2.setIcon(icon2)
        self.searchproductbutton_2.setIconSize(QSize(15, 15))

        self.horizontalLayout_64.addWidget(self.searchproductbutton_2)


        self.verticalLayout_34.addWidget(self.frame_38)

        self.frame_81 = QFrame(self.producttableframe_it)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setMinimumSize(QSize(0, 0))
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(-1, 0, 0, 0)
        self.productcount_it = QLabel(self.frame_81)
        self.productcount_it.setObjectName(u"productcount_it")

        self.horizontalLayout_72.addWidget(self.productcount_it)


        self.verticalLayout_34.addWidget(self.frame_81)

        self.frame_40 = QFrame(self.producttableframe_it)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(0, 450))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.producttable_editdelete_it_2 = QTableWidget(self.frame_40)
        if (self.producttable_editdelete_it_2.columnCount() < 13):
            self.producttable_editdelete_it_2.setColumnCount(13)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.producttable_editdelete_it_2.setHorizontalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.producttable_editdelete_it_2.setHorizontalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.producttable_editdelete_it_2.setHorizontalHeaderItem(2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.producttable_editdelete_it_2.setHorizontalHeaderItem(3, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.producttable_editdelete_it_2.setHorizontalHeaderItem(4, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.producttable_editdelete_it_2.setHorizontalHeaderItem(5, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.producttable_editdelete_it_2.setHorizontalHeaderItem(6, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.producttable_editdelete_it_2.setHorizontalHeaderItem(7, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.producttable_editdelete_it_2.setHorizontalHeaderItem(8, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.producttable_editdelete_it_2.setHorizontalHeaderItem(9, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.producttable_editdelete_it_2.setHorizontalHeaderItem(10, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.producttable_editdelete_it_2.setHorizontalHeaderItem(11, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.producttable_editdelete_it_2.setHorizontalHeaderItem(12, __qtablewidgetitem42)
        self.producttable_editdelete_it_2.setObjectName(u"producttable_editdelete_it_2")

        self.horizontalLayout_62.addWidget(self.producttable_editdelete_it_2)


        self.verticalLayout_34.addWidget(self.frame_40)


        self.verticalLayout_32.addWidget(self.producttableframe_it)

        self.productframe_it = QFrame(self.frame_35)
        self.productframe_it.setObjectName(u"productframe_it")
        self.productframe_it.setMinimumSize(QSize(0, 0))
        self.productframe_it.setFrameShape(QFrame.StyledPanel)
        self.productframe_it.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.productframe_it)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.newbranchframe_it_8 = QFrame(self.productframe_it)
        self.newbranchframe_it_8.setObjectName(u"newbranchframe_it_8")
        self.newbranchframe_it_8.setMaximumSize(QSize(500, 16777215))
        self.newbranchframe_it_8.setFrameShape(QFrame.StyledPanel)
        self.newbranchframe_it_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.newbranchframe_it_8)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_86 = QLabel(self.newbranchframe_it_8)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setMinimumSize(QSize(125, 0))
        self.label_86.setMaximumSize(QSize(125, 16777215))

        self.horizontalLayout_73.addWidget(self.label_86)

        self.carname = QLineEdit(self.newbranchframe_it_8)
        self.carname.setObjectName(u"carname")

        self.horizontalLayout_73.addWidget(self.carname)


        self.verticalLayout_24.addWidget(self.newbranchframe_it_8)

        self.displaygenderframe_manager_3 = QFrame(self.productframe_it)
        self.displaygenderframe_manager_3.setObjectName(u"displaygenderframe_manager_3")
        self.displaygenderframe_manager_3.setMaximumSize(QSize(500, 16777215))
        self.displaygenderframe_manager_3.setFrameShape(QFrame.StyledPanel)
        self.displaygenderframe_manager_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.displaygenderframe_manager_3)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.label_88 = QLabel(self.displaygenderframe_manager_3)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMinimumSize(QSize(125, 0))
        self.label_88.setMaximumSize(QSize(125, 16777215))

        self.horizontalLayout_75.addWidget(self.label_88)

        self.manufacturerchooseproduct = QComboBox(self.displaygenderframe_manager_3)
        self.manufacturerchooseproduct.addItem("")
        self.manufacturerchooseproduct.addItem("")
        self.manufacturerchooseproduct.setObjectName(u"manufacturerchooseproduct")
        self.manufacturerchooseproduct.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_75.addWidget(self.manufacturerchooseproduct)


        self.verticalLayout_24.addWidget(self.displaygenderframe_manager_3)

        self.displaygenderframe_manager_5 = QFrame(self.productframe_it)
        self.displaygenderframe_manager_5.setObjectName(u"displaygenderframe_manager_5")
        self.displaygenderframe_manager_5.setMaximumSize(QSize(500, 16777215))
        self.displaygenderframe_manager_5.setFrameShape(QFrame.StyledPanel)
        self.displaygenderframe_manager_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.displaygenderframe_manager_5)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.label_96 = QLabel(self.displaygenderframe_manager_5)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setMinimumSize(QSize(125, 0))
        self.label_96.setMaximumSize(QSize(125, 16777215))

        self.horizontalLayout_81.addWidget(self.label_96)

        self.branchchooseproduct = QComboBox(self.displaygenderframe_manager_5)
        self.branchchooseproduct.addItem("")
        self.branchchooseproduct.addItem("")
        self.branchchooseproduct.setObjectName(u"branchchooseproduct")
        self.branchchooseproduct.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_81.addWidget(self.branchchooseproduct)


        self.verticalLayout_24.addWidget(self.displaygenderframe_manager_5)

        self.displaygenderframe_manager_4 = QFrame(self.productframe_it)
        self.displaygenderframe_manager_4.setObjectName(u"displaygenderframe_manager_4")
        self.displaygenderframe_manager_4.setMaximumSize(QSize(500, 16777215))
        self.displaygenderframe_manager_4.setFrameShape(QFrame.StyledPanel)
        self.displaygenderframe_manager_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.displaygenderframe_manager_4)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.label_95 = QLabel(self.displaygenderframe_manager_4)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setMinimumSize(QSize(125, 0))
        self.label_95.setMaximumSize(QSize(125, 16777215))

        self.horizontalLayout_80.addWidget(self.label_95)

        self.cartypechooseproduct = QComboBox(self.displaygenderframe_manager_4)
        self.cartypechooseproduct.addItem("")
        self.cartypechooseproduct.addItem("")
        self.cartypechooseproduct.setObjectName(u"cartypechooseproduct")
        self.cartypechooseproduct.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_80.addWidget(self.cartypechooseproduct)


        self.verticalLayout_24.addWidget(self.displaygenderframe_manager_4)

        self.newbranchframe_it_10 = QFrame(self.productframe_it)
        self.newbranchframe_it_10.setObjectName(u"newbranchframe_it_10")
        self.newbranchframe_it_10.setMinimumSize(QSize(0, 0))
        self.newbranchframe_it_10.setMaximumSize(QSize(500, 16777215))
        self.newbranchframe_it_10.setFrameShape(QFrame.StyledPanel)
        self.newbranchframe_it_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.newbranchframe_it_10)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(9, -1, -1, -1)
        self.frame_50 = QFrame(self.newbranchframe_it_10)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, -1, -1, -1)
        self.label_89 = QLabel(self.frame_50)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setMinimumSize(QSize(125, 0))
        self.label_89.setMaximumSize(QSize(125, 16777215))

        self.horizontalLayout_76.addWidget(self.label_89)

        self.yeareleased = QSpinBox(self.frame_50)
        self.yeareleased.setObjectName(u"yeareleased")
        self.yeareleased.setMaximum(999999999)

        self.horizontalLayout_76.addWidget(self.yeareleased)


        self.verticalLayout_25.addWidget(self.frame_50)

        self.label_90 = QLabel(self.newbranchframe_it_10)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setStyleSheet(u"")

        self.verticalLayout_25.addWidget(self.label_90)


        self.verticalLayout_24.addWidget(self.newbranchframe_it_10)

        self.frame_51 = QFrame(self.productframe_it)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMaximumSize(QSize(500, 16777215))
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(9, -1, -1, -1)
        self.label_92 = QLabel(self.frame_51)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setMinimumSize(QSize(125, 0))
        self.label_92.setMaximumSize(QSize(125, 16777215))

        self.horizontalLayout_78.addWidget(self.label_92)

        self.topspeed = QSpinBox(self.frame_51)
        self.topspeed.setObjectName(u"topspeed")
        self.topspeed.setMaximum(1000000050)

        self.horizontalLayout_78.addWidget(self.topspeed)


        self.verticalLayout_24.addWidget(self.frame_51)

        self.frame_52 = QFrame(self.productframe_it)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMaximumSize(QSize(500, 16777215))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(9, -1, -1, -1)
        self.label_97 = QLabel(self.frame_52)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMinimumSize(QSize(125, 0))
        self.label_97.setMaximumSize(QSize(125, 16777215))

        self.horizontalLayout_82.addWidget(self.label_97)

        self.horsepower = QSpinBox(self.frame_52)
        self.horsepower.setObjectName(u"horsepower")
        self.horsepower.setMaximum(1000000050)

        self.horizontalLayout_82.addWidget(self.horsepower)


        self.verticalLayout_24.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.productframe_it)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMaximumSize(QSize(500, 16777215))
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(9, -1, -1, -1)
        self.label_99 = QLabel(self.frame_53)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setMinimumSize(QSize(125, 0))
        self.label_99.setMaximumSize(QSize(125, 16777215))

        self.horizontalLayout_83.addWidget(self.label_99)

        self.seatcount = QSpinBox(self.frame_53)
        self.seatcount.setObjectName(u"seatcount")
        self.seatcount.setMaximum(1000000050)

        self.horizontalLayout_83.addWidget(self.seatcount)


        self.verticalLayout_24.addWidget(self.frame_53)

        self.frame_54 = QFrame(self.productframe_it)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMaximumSize(QSize(500, 16777215))
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(9, -1, -1, -1)
        self.label_101 = QLabel(self.frame_54)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setMinimumSize(QSize(125, 0))
        self.label_101.setMaximumSize(QSize(125, 16777215))

        self.horizontalLayout_84.addWidget(self.label_101)

        self.length = QDoubleSpinBox(self.frame_54)
        self.length.setObjectName(u"length")
        self.length.setMaximum(10000000000000000000.000000000000000)

        self.horizontalLayout_84.addWidget(self.length)


        self.verticalLayout_24.addWidget(self.frame_54)

        self.frame_55 = QFrame(self.productframe_it)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMaximumSize(QSize(500, 16777215))
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(9, -1, -1, -1)
        self.label_103 = QLabel(self.frame_55)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setMinimumSize(QSize(125, 0))
        self.label_103.setMaximumSize(QSize(125, 16777215))

        self.horizontalLayout_85.addWidget(self.label_103)

        self.width = QDoubleSpinBox(self.frame_55)
        self.width.setObjectName(u"width")
        self.width.setMaximum(10000000000000000000.000000000000000)

        self.horizontalLayout_85.addWidget(self.width)


        self.verticalLayout_24.addWidget(self.frame_55)

        self.frame_56 = QFrame(self.productframe_it)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMaximumSize(QSize(500, 16777215))
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(9, -1, -1, -1)
        self.label_105 = QLabel(self.frame_56)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setMinimumSize(QSize(125, 0))
        self.label_105.setMaximumSize(QSize(125, 16777215))

        self.horizontalLayout_86.addWidget(self.label_105)

        self.price = QDoubleSpinBox(self.frame_56)
        self.price.setObjectName(u"price")
        self.price.setMaximum(10000000000000000000.000000000000000)

        self.horizontalLayout_86.addWidget(self.price)


        self.verticalLayout_24.addWidget(self.frame_56)


        self.verticalLayout_32.addWidget(self.productframe_it)

        self.frame_49 = QFrame(self.frame_35)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.addproduct_it = QPushButton(self.frame_49)
        self.addproduct_it.setObjectName(u"addproduct_it")
        self.addproduct_it.setMinimumSize(QSize(0, 25))
        self.addproduct_it.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_74.addWidget(self.addproduct_it)

        self.editproduct_it = QPushButton(self.frame_49)
        self.editproduct_it.setObjectName(u"editproduct_it")
        self.editproduct_it.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_74.addWidget(self.editproduct_it)

        self.deleteproduct_it = QPushButton(self.frame_49)
        self.deleteproduct_it.setObjectName(u"deleteproduct_it")
        self.deleteproduct_it.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_74.addWidget(self.deleteproduct_it)


        self.verticalLayout_32.addWidget(self.frame_49)


        self.verticalLayout_9.addWidget(self.frame_35)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.it)
        self.profile = QWidget()
        self.profile.setObjectName(u"profile")
        self.verticalLayout_30 = QVBoxLayout(self.profile)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_57 = QFrame(self.profile)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_106 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.label_91 = QLabel(self.frame_57)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setMinimumSize(QSize(0, 50))
        self.label_91.setStyleSheet(u"font: 19pt \"Century Gothic\";\n"
"font: 63 28pt \"Bahnschrift SemiBold Condensed\";")
        self.label_91.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_106.addWidget(self.label_91)


        self.verticalLayout_30.addWidget(self.frame_57)

        self.scrollArea_3 = QScrollArea(self.profile)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 771, 530))
        self.verticalLayout_27 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_97 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setMaximumSize(QSize(16777215, 200))
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_97)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.label_41 = QLabel(self.frame_97)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(180, 180))
        self.label_41.setMaximumSize(QSize(180, 180))
        self.label_41.setPixmap(QPixmap(u"data/img/login_border.png"))

        self.horizontalLayout_77.addWidget(self.label_41)


        self.verticalLayout_27.addWidget(self.frame_97)

        self.employeename_profile = QLabel(self.scrollAreaWidgetContents_3)
        self.employeename_profile.setObjectName(u"employeename_profile")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.employeename_profile.sizePolicy().hasHeightForWidth())
        self.employeename_profile.setSizePolicy(sizePolicy)
        self.employeename_profile.setMaximumSize(QSize(16777215, 60))
        self.employeename_profile.setStyleSheet(u"font: 19pt \"Century Gothic\";\n"
"font: 63 28pt \"Bahnschrift SemiBold Condensed\";")
        self.employeename_profile.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.employeename_profile)

        self.position_profile = QLabel(self.scrollAreaWidgetContents_3)
        self.position_profile.setObjectName(u"position_profile")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.position_profile.sizePolicy().hasHeightForWidth())
        self.position_profile.setSizePolicy(sizePolicy1)
        self.position_profile.setMaximumSize(QSize(16777215, 20))
        self.position_profile.setStyleSheet(u"font: 11pt \"Bahnschrift SemiCondensed\";")
        self.position_profile.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.position_profile)

        self.frame_75 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(0, 0))
        self.frame_75.setMaximumSize(QSize(16777215, 60))
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.managersectionbutton = QPushButton(self.frame_75)
        self.managersectionbutton.setObjectName(u"managersectionbutton")
        self.managersectionbutton.setMinimumSize(QSize(150, 40))
        self.managersectionbutton.setMaximumSize(QSize(150, 40))
        self.managersectionbutton.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.managersectionbutton)

        self.itsectionbutton = QPushButton(self.frame_75)
        self.itsectionbutton.setObjectName(u"itsectionbutton")
        self.itsectionbutton.setMinimumSize(QSize(150, 40))
        self.itsectionbutton.setMaximumSize(QSize(150, 40))
        self.itsectionbutton.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.itsectionbutton)

        self.dbtestbutton_profile = QPushButton(self.frame_75)
        self.dbtestbutton_profile.setObjectName(u"dbtestbutton_profile")
        self.dbtestbutton_profile.setMinimumSize(QSize(150, 40))
        self.dbtestbutton_profile.setMaximumSize(QSize(150, 40))
        self.dbtestbutton_profile.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.dbtestbutton_profile)


        self.verticalLayout_27.addWidget(self.frame_75)

        self.frame_27 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.logoutbutton = QPushButton(self.frame_27)
        self.logoutbutton.setObjectName(u"logoutbutton")
        self.logoutbutton.setMinimumSize(QSize(150, 40))
        self.logoutbutton.setMaximumSize(QSize(150, 40))
        self.logoutbutton.setStyleSheet(u"")

        self.horizontalLayout_29.addWidget(self.logoutbutton)


        self.verticalLayout_27.addWidget(self.frame_27)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 40))
        self.frame_9.setMaximumSize(QSize(16777215, 40))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_87 = QLabel(self.frame_9)
        self.label_87.setObjectName(u"label_87")
        sizePolicy1.setHeightForWidth(self.label_87.sizePolicy().hasHeightForWidth())
        self.label_87.setSizePolicy(sizePolicy1)
        self.label_87.setStyleSheet(u"font: 11pt \"Bahnschrift SemiCondensed\";")
        self.label_87.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_87)


        self.verticalLayout_27.addWidget(self.frame_9)

        self.frame_68 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)

        self.verticalLayout_27.addWidget(self.frame_68)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_30.addWidget(self.scrollArea_3)

        self.stackedWidget.addWidget(self.profile)
        self.databasetest = QWidget()
        self.databasetest.setObjectName(u"databasetest")
        self.verticalLayout_41 = QVBoxLayout(self.databasetest)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_79 = QFrame(self.databasetest)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_101 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.frame_104 = QFrame(self.frame_79)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setMinimumSize(QSize(50, 50))
        self.frame_104.setMaximumSize(QSize(50, 50))
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_101.addWidget(self.frame_104)

        self.label_94 = QLabel(self.frame_79)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setStyleSheet(u"font: 19pt \"Century Gothic\";\n"
"font: 63 28pt \"Bahnschrift SemiBold Condensed\";")
        self.label_94.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_101.addWidget(self.label_94)

        self.profilebuttondbtest = QPushButton(self.frame_79)
        self.profilebuttondbtest.setObjectName(u"profilebuttondbtest")
        self.profilebuttondbtest.setMinimumSize(QSize(50, 50))
        self.profilebuttondbtest.setMaximumSize(QSize(50, 50))
        self.profilebuttondbtest.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"\n"
"")
        self.profilebuttondbtest.setIcon(icon1)
        self.profilebuttondbtest.setIconSize(QSize(40, 40))

        self.horizontalLayout_101.addWidget(self.profilebuttondbtest)


        self.verticalLayout_41.addWidget(self.frame_79)

        self.scrollArea_4 = QScrollArea(self.databasetest)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setStyleSheet(u"")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 754, 683))
        self.verticalLayout_35 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_39 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_47 = QLabel(self.frame_39)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_55.addWidget(self.label_47)


        self.verticalLayout_35.addWidget(self.frame_39)

        self.frame_76 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(0, 50))
        self.frame_76.setMaximumSize(QSize(500, 16777215))
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_55 = QLabel(self.frame_76)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(120, 0))
        self.label_55.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_56.addWidget(self.label_55)

        self.selecttable_dbtest = QComboBox(self.frame_76)
        self.selecttable_dbtest.addItem("")
        self.selecttable_dbtest.addItem("")
        self.selecttable_dbtest.addItem("")
        self.selecttable_dbtest.addItem("")
        self.selecttable_dbtest.addItem("")
        self.selecttable_dbtest.addItem("")
        self.selecttable_dbtest.setObjectName(u"selecttable_dbtest")
        self.selecttable_dbtest.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_56.addWidget(self.selecttable_dbtest)


        self.verticalLayout_35.addWidget(self.frame_76)

        self.frame_80 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_80)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.submitquerybranch = QPushButton(self.frame_80)
        self.submitquerybranch.setObjectName(u"submitquerybranch")
        self.submitquerybranch.setMinimumSize(QSize(0, 25))
        self.submitquerybranch.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_65.addWidget(self.submitquerybranch)

        self.submitpositionquery_2 = QPushButton(self.frame_80)
        self.submitpositionquery_2.setObjectName(u"submitpositionquery_2")
        self.submitpositionquery_2.setMinimumSize(QSize(0, 25))
        self.submitpositionquery_2.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_65.addWidget(self.submitpositionquery_2)

        self.manufacturerquerybt_2 = QPushButton(self.frame_80)
        self.manufacturerquerybt_2.setObjectName(u"manufacturerquerybt_2")
        self.manufacturerquerybt_2.setMinimumSize(QSize(0, 25))
        self.manufacturerquerybt_2.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_65.addWidget(self.manufacturerquerybt_2)

        self.cartypequerybt_2 = QPushButton(self.frame_80)
        self.cartypequerybt_2.setObjectName(u"cartypequerybt_2")
        self.cartypequerybt_2.setMinimumSize(QSize(0, 25))
        self.cartypequerybt_2.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_65.addWidget(self.cartypequerybt_2)

        self.employeequerybt_2 = QPushButton(self.frame_80)
        self.employeequerybt_2.setObjectName(u"employeequerybt_2")
        self.employeequerybt_2.setMinimumSize(QSize(0, 25))
        self.employeequerybt_2.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_65.addWidget(self.employeequerybt_2)

        self.productquerybt_2 = QPushButton(self.frame_80)
        self.productquerybt_2.setObjectName(u"productquerybt_2")
        self.productquerybt_2.setMinimumSize(QSize(0, 25))
        self.productquerybt_2.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_65.addWidget(self.productquerybt_2)


        self.verticalLayout_35.addWidget(self.frame_80)

        self.frame_77 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMinimumSize(QSize(0, 0))
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.itemcount_dbtest = QLabel(self.frame_77)
        self.itemcount_dbtest.setObjectName(u"itemcount_dbtest")

        self.horizontalLayout_66.addWidget(self.itemcount_dbtest)


        self.verticalLayout_35.addWidget(self.frame_77)

        self.employeetableframe_manager_2 = QFrame(self.scrollAreaWidgetContents_4)
        self.employeetableframe_manager_2.setObjectName(u"employeetableframe_manager_2")
        self.employeetableframe_manager_2.setMinimumSize(QSize(0, 0))
        self.employeetableframe_manager_2.setFrameShape(QFrame.StyledPanel)
        self.employeetableframe_manager_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.employeetableframe_manager_2)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.querytable = QTableWidget(self.employeetableframe_manager_2)
        self.querytable.setObjectName(u"querytable")
        self.querytable.setMinimumSize(QSize(0, 450))

        self.horizontalLayout_87.addWidget(self.querytable)


        self.verticalLayout_35.addWidget(self.employeetableframe_manager_2)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_41.addWidget(self.scrollArea_4)

        self.stackedWidget.addWidget(self.databasetest)

        self.verticalLayout_4.addWidget(self.stackedWidget)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(25, 25))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.loading_icon = QLabel(self.frame_6)
        self.loading_icon.setObjectName(u"loading_icon")
        self.loading_icon.setMinimumSize(QSize(20, 20))
        self.loading_icon.setMaximumSize(QSize(20, 20))
        self.loading_icon.setPixmap(QPixmap(u"data/img/loading20.gif"))

        self.horizontalLayout_2.addWidget(self.loading_icon)

        self.status_main = QLabel(self.frame_6)
        self.status_main.setObjectName(u"status_main")
        self.status_main.setStyleSheet(u"font: 25pt \"Century Gothic\";\n"
"font: 63 34pt \"Bahnschrift SemiBold\";\n"
"font: 12pt \"Bahnschrift SemiCondensed\";")

        self.horizontalLayout_2.addWidget(self.status_main)


        self.verticalLayout_4.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CarSel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Expect the unexpected", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sign in", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"Login as", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.signinbutton.setText(QCoreApplication.translate("MainWindow", u"Sign in", None))
        self.refreshbuttonmanager.setText("")
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Manager Section", None))
        self.profilebuttonmanager.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Employee", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Select branch", None))
        self.branchchoose_manager.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.branchchoose_manager.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.branchchoose_manager.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.branchchoose_manager.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.branchchoose_manager.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.branchchoose_manager.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.branchchoose_manager.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))

        self.addresslabel_manager.setText(QCoreApplication.translate("MainWindow", u"Address: ", None))
        self.establishedlabel_manager.setText(QCoreApplication.translate("MainWindow", u"Established: ", None))
        self.employeecount_manager_2.setText(QCoreApplication.translate("MainWindow", u"Employee count in branch:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"What to display in the table?", None))
        self.firstnamecheckboxemployee_manager.setText(QCoreApplication.translate("MainWindow", u"First name", None))
        self.lastnamecheckboxemployee_manager.setText(QCoreApplication.translate("MainWindow", u"Last name", None))
        self.gendercheckboxemployee_manager.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.agecheckboxemployee_manager.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.positioncheckboxemployee_manager.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.addresscheckboxemployee_manager.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.phonenocheckboxemployee_manager.setText(QCoreApplication.translate("MainWindow", u"Phone number", None))
        self.datecheckboxemployee_manager.setText(QCoreApplication.translate("MainWindow", u"Date Joined", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Display gender", None))
        self.genderchoose_manager.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.genderchoose_manager.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.genderchoose_manager.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Display age from", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"years old", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Display position", None))
        self.positionchooser_manager.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.positionchooser_manager.setItemText(1, QCoreApplication.translate("MainWindow", u"Manager", None))
        self.positionchooser_manager.setItemText(2, QCoreApplication.translate("MainWindow", u"Cashier", None))
        self.positionchooser_manager.setItemText(3, QCoreApplication.translate("MainWindow", u"Customer Service", None))
        self.positionchooser_manager.setItemText(4, QCoreApplication.translate("MainWindow", u"Telephone Operator", None))
        self.positionchooser_manager.setItemText(5, QCoreApplication.translate("MainWindow", u"Salesman", None))
        self.positionchooser_manager.setItemText(6, QCoreApplication.translate("MainWindow", u"Janitor", None))
        self.positionchooser_manager.setItemText(7, QCoreApplication.translate("MainWindow", u"IT", None))
        self.positionchooser_manager.setItemText(8, QCoreApplication.translate("MainWindow", u"Accountant", None))

        self.submitbuttonemployee_manager.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.employeecount_manager.setText(QCoreApplication.translate("MainWindow", u"Employee count:", None))
        ___qtablewidgetitem = self.employeetable_manager.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Employee ID", None));
        ___qtablewidgetitem1 = self.employeetable_manager.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Branch", None));
        ___qtablewidgetitem2 = self.employeetable_manager.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem3 = self.employeetable_manager.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem4 = self.employeetable_manager.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem5 = self.employeetable_manager.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem6 = self.employeetable_manager.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None));
        ___qtablewidgetitem7 = self.employeetable_manager.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Date Joined", None));
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Products", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Select branch", None))
        self.branchchoose_manager_2.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.branchchoose_manager_2.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.branchchoose_manager_2.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.branchchoose_manager_2.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.branchchoose_manager_2.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.branchchoose_manager_2.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.branchchoose_manager_2.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))

        self.addresslabel_manager_2.setText(QCoreApplication.translate("MainWindow", u"Address: ", None))
        self.establishedlabel_manager_2.setText(QCoreApplication.translate("MainWindow", u"Established: ", None))
        self.productcount_branch.setText(QCoreApplication.translate("MainWindow", u"Product count in branch:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"What to display in the table?", None))
        self.cartype_manager.setText(QCoreApplication.translate("MainWindow", u"Type ", None))
        self.carname_manager.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.yearreleased_manager.setText(QCoreApplication.translate("MainWindow", u"Year released", None))
        self.topspeed_manager.setText(QCoreApplication.translate("MainWindow", u"Top speed", None))
        self.horsepower_manager.setText(QCoreApplication.translate("MainWindow", u"Horse power", None))
        self.seatcount_manager.setText(QCoreApplication.translate("MainWindow", u"Seat count", None))
        self.length_manager.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.width_manager.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.dateadded_manager.setText(QCoreApplication.translate("MainWindow", u"Date added", None))
        self.price_manager.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Display manufacturer", None))
        self.manuselect_manager.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.manuselect_manager.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.manuselect_manager.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))

        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Display car type", None))
        self.cartypechoose_manager.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.cartypechoose_manager.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.cartypechoose_manager.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))

        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Display year released from", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.label_39.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Display top speed from", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"km/h", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Display horse power from", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"hp", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Display seat count from", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"seats", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Display length from", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"cm", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Display width from", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"cm", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Display price from", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"million rupiahs", None))
        self.submitbuttonproduct_manager.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.productcount_manager.setText(QCoreApplication.translate("MainWindow", u"Product count:", None))
        ___qtablewidgetitem8 = self.producttable_manager.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Car ID", None));
        ___qtablewidgetitem9 = self.producttable_manager.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Manufacturer", None));
        ___qtablewidgetitem10 = self.producttable_manager.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem11 = self.producttable_manager.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem12 = self.producttable_manager.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Year released", None));
        ___qtablewidgetitem13 = self.producttable_manager.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Top speed", None));
        ___qtablewidgetitem14 = self.producttable_manager.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Horse power", None));
        ___qtablewidgetitem15 = self.producttable_manager.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Seat", None));
        ___qtablewidgetitem16 = self.producttable_manager.horizontalHeaderItem(8)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Length", None));
        ___qtablewidgetitem17 = self.producttable_manager.horizontalHeaderItem(9)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Width", None));
        ___qtablewidgetitem18 = self.producttable_manager.horizontalHeaderItem(10)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Date added ", None));
        ___qtablewidgetitem19 = self.producttable_manager.horizontalHeaderItem(11)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Counts", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Select branch", None))
        self.branchchoosecount_counts.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.employeecount_counts.setText(QCoreApplication.translate("MainWindow", u"Employee count:", None))
        self.productcount_counts.setText(QCoreApplication.translate("MainWindow", u"Product count:", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Select position", None))
        self.positionchoose_counts.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.employeenrolled.setText(QCoreApplication.translate("MainWindow", u"Employee enrolled: ", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Select manufacturer", None))
        self.manufacturerchoose_counts.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.manu_onsale_counts.setText(QCoreApplication.translate("MainWindow", u"Product on sale:", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Select car type", None))
        self.cartypechoose_counts.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.cartype_onsale_counts.setText(QCoreApplication.translate("MainWindow", u"Product on sale:", None))
        self.refrehsbuttonit.setText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"IT Section", None))
        self.profilebuttonit.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Branch", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"What are you gonna do?", None))
        self.branchactionchoose_it.setItemText(0, QCoreApplication.translate("MainWindow", u"Add branch", None))
        self.branchactionchoose_it.setItemText(1, QCoreApplication.translate("MainWindow", u"Edit branch", None))
        self.branchactionchoose_it.setItemText(2, QCoreApplication.translate("MainWindow", u"Delete branch", None))

        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Select branch", None))
        self.selectbranch_it.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.selectbranch_it.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.selectbranch_it.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.selectbranch_it.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.selectbranch_it.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.selectbranch_it.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.selectbranch_it.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))

        self.label_42.setText(QCoreApplication.translate("MainWindow", u"New branch name", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Year established", None))
        self.addbranchbt_it.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.editbranchbt_it.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.deletebranchbt_it.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"What are you gonna do?", None))
        self.positionchoose.setItemText(0, QCoreApplication.translate("MainWindow", u"Add position", None))
        self.positionchoose.setItemText(1, QCoreApplication.translate("MainWindow", u"Edit position", None))
        self.positionchoose.setItemText(2, QCoreApplication.translate("MainWindow", u"Delete position", None))

        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Select position", None))
        self.selectposition.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.selectposition.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.selectposition.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.selectposition.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.selectposition.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.selectposition.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.selectposition.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))

        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Position name", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Position description", None))
        self.addpositionbt_it.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.editpositionbt_it.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.deletepositionbt_it.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Employee", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"What are you gonna do?", None))
        self.employeeactionchoose_it.setItemText(0, QCoreApplication.translate("MainWindow", u"Add employee", None))
        self.employeeactionchoose_it.setItemText(1, QCoreApplication.translate("MainWindow", u"Edit employee", None))
        self.employeeactionchoose_it.setItemText(2, QCoreApplication.translate("MainWindow", u"Delete employee", None))

        self.getemployeebt_it.setText(QCoreApplication.translate("MainWindow", u"Get employee list", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.searchbox_it.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name, address, age, position, etc", None))
        self.searchbutton_it.setText("")
        self.employeecount_it.setText(QCoreApplication.translate("MainWindow", u"Employee count: 0", None))
        ___qtablewidgetitem20 = self.employeetable_editdelete_it.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Employee ID", None));
        ___qtablewidgetitem21 = self.employeetable_editdelete_it.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Branch", None));
        ___qtablewidgetitem22 = self.employeetable_editdelete_it.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"First name", None));
        ___qtablewidgetitem23 = self.employeetable_editdelete_it.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Last name", None));
        ___qtablewidgetitem24 = self.employeetable_editdelete_it.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem25 = self.employeetable_editdelete_it.horizontalHeaderItem(5)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Born", None));
        ___qtablewidgetitem26 = self.employeetable_editdelete_it.horizontalHeaderItem(6)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem27 = self.employeetable_editdelete_it.horizontalHeaderItem(7)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem28 = self.employeetable_editdelete_it.horizontalHeaderItem(8)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Phone number", None));
        ___qtablewidgetitem29 = self.employeetable_editdelete_it.horizontalHeaderItem(9)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Date joined", None));
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Select branch", None))
        self.branchchoose_addedit_it.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.branchchoose_addedit_it.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.branchchoose_addedit_it.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.branchchoose_addedit_it.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.branchchoose_addedit_it.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.branchchoose_addedit_it.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.branchchoose_addedit_it.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))

        self.label_50.setText(QCoreApplication.translate("MainWindow", u"First name ", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Last name", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Select gender", None))
        self.gender_addedit_it.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.gender_addedit_it.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Born", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Tip: you can type in the field", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Select position", None))
        self.position_addedit_it.setItemText(0, QCoreApplication.translate("MainWindow", u"Manager", None))
        self.position_addedit_it.setItemText(1, QCoreApplication.translate("MainWindow", u"Cashier", None))
        self.position_addedit_it.setItemText(2, QCoreApplication.translate("MainWindow", u"Customer Service", None))
        self.position_addedit_it.setItemText(3, QCoreApplication.translate("MainWindow", u"Telephone Operator", None))
        self.position_addedit_it.setItemText(4, QCoreApplication.translate("MainWindow", u"Salesman", None))
        self.position_addedit_it.setItemText(5, QCoreApplication.translate("MainWindow", u"Janitor", None))
        self.position_addedit_it.setItemText(6, QCoreApplication.translate("MainWindow", u"IT", None))
        self.position_addedit_it.setItemText(7, QCoreApplication.translate("MainWindow", u"Accountant", None))

        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Login password", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Phone number", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Tip: you can type the numbers in the field", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.addemployeebtt_it.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.editemployeebtt_it.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.deleteemployeebtt_it.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Manufacturer", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"What are you gonna do?", None))
        self.manufacturerchoose.setItemText(0, QCoreApplication.translate("MainWindow", u"Add manufacturer", None))
        self.manufacturerchoose.setItemText(1, QCoreApplication.translate("MainWindow", u"Edit manufacturer", None))
        self.manufacturerchoose.setItemText(2, QCoreApplication.translate("MainWindow", u"Delete manufacturer", None))

        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Select manufacturer", None))
        self.selectmanufacturer.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.selectmanufacturer.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.selectmanufacturer.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.selectmanufacturer.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.selectmanufacturer.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.selectmanufacturer.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.selectmanufacturer.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))

        self.label_74.setText(QCoreApplication.translate("MainWindow", u"New manufacturer name", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Country", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Year established", None))
        self.addmanufacturerbt.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.editmanufacturerbt.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.deletemanufacturerbt.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Car Type", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"What are you gonna do?", None))
        self.cartypechoose.setItemText(0, QCoreApplication.translate("MainWindow", u"Add car type", None))
        self.cartypechoose.setItemText(1, QCoreApplication.translate("MainWindow", u"Edit car type", None))
        self.cartypechoose.setItemText(2, QCoreApplication.translate("MainWindow", u"Delete car type", None))

        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Select car type ", None))
        self.selectcartype.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.selectcartype.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.selectcartype.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.selectcartype.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.selectcartype.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.selectcartype.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.selectcartype.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))

        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Car type name", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Invented", None))
        self.addcartypebt.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.editcartypebt.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.deletecartypebt.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"What are you gonna do?", None))
        self.productchoose.setItemText(0, QCoreApplication.translate("MainWindow", u"Add product", None))
        self.productchoose.setItemText(1, QCoreApplication.translate("MainWindow", u"Edit product", None))
        self.productchoose.setItemText(2, QCoreApplication.translate("MainWindow", u"Delete product", None))

        self.getproductbt_it_2.setText(QCoreApplication.translate("MainWindow", u"Get product list", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.searchproductfield_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name, address, age, position, etc", None))
        self.searchproductbutton_2.setText("")
        self.productcount_it.setText(QCoreApplication.translate("MainWindow", u"Products count:", None))
        ___qtablewidgetitem30 = self.producttable_editdelete_it_2.horizontalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Car ID", None));
        ___qtablewidgetitem31 = self.producttable_editdelete_it_2.horizontalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Manufacturer", None));
        ___qtablewidgetitem32 = self.producttable_editdelete_it_2.horizontalHeaderItem(2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Branch", None));
        ___qtablewidgetitem33 = self.producttable_editdelete_it_2.horizontalHeaderItem(3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem34 = self.producttable_editdelete_it_2.horizontalHeaderItem(4)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem35 = self.producttable_editdelete_it_2.horizontalHeaderItem(5)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Year released", None));
        ___qtablewidgetitem36 = self.producttable_editdelete_it_2.horizontalHeaderItem(6)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Top speed (km/h)", None));
        ___qtablewidgetitem37 = self.producttable_editdelete_it_2.horizontalHeaderItem(7)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Horse power", None));
        ___qtablewidgetitem38 = self.producttable_editdelete_it_2.horizontalHeaderItem(8)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Seat count", None));
        ___qtablewidgetitem39 = self.producttable_editdelete_it_2.horizontalHeaderItem(9)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Length (cm)", None));
        ___qtablewidgetitem40 = self.producttable_editdelete_it_2.horizontalHeaderItem(10)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Width (cm)", None));
        ___qtablewidgetitem41 = self.producttable_editdelete_it_2.horizontalHeaderItem(11)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Date added", None));
        ___qtablewidgetitem42 = self.producttable_editdelete_it_2.horizontalHeaderItem(12)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Price (million Rp)", None));
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Car name", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Manufacturer", None))
        self.manufacturerchooseproduct.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.manufacturerchooseproduct.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Branch", None))
        self.branchchooseproduct.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.branchchooseproduct.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Car Type", None))
        self.cartypechooseproduct.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.cartypechooseproduct.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Year released", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Tip: you can type in the field", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Top speed (km/h)", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Horse power", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Seat count", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Length (cm)", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Width (cm)", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Price (million rupiahs)", None))
        self.addproduct_it.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.editproduct_it.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.deleteproduct_it.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_41.setText("")
        self.employeename_profile.setText(QCoreApplication.translate("MainWindow", u"Debug", None))
        self.position_profile.setText(QCoreApplication.translate("MainWindow", u"Co Founder", None))
        self.managersectionbutton.setText(QCoreApplication.translate("MainWindow", u"Manager Section", None))
        self.itsectionbutton.setText(QCoreApplication.translate("MainWindow", u"IT Section", None))
        self.dbtestbutton_profile.setText(QCoreApplication.translate("MainWindow", u"Database Test", None))
        self.logoutbutton.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"(c) CarSel Co., Ltd. 2021", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Database Test", None))
        self.profilebuttondbtest.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Show tables", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Select table to view", None))
        self.selecttable_dbtest.setItemText(0, QCoreApplication.translate("MainWindow", u"Branch", None))
        self.selecttable_dbtest.setItemText(1, QCoreApplication.translate("MainWindow", u"Position", None))
        self.selecttable_dbtest.setItemText(2, QCoreApplication.translate("MainWindow", u"Manufacturer", None))
        self.selecttable_dbtest.setItemText(3, QCoreApplication.translate("MainWindow", u"Car type", None))
        self.selecttable_dbtest.setItemText(4, QCoreApplication.translate("MainWindow", u"Employee", None))
        self.selecttable_dbtest.setItemText(5, QCoreApplication.translate("MainWindow", u"Products", None))

        self.submitquerybranch.setText(QCoreApplication.translate("MainWindow", u"Show Branch table", None))
        self.submitpositionquery_2.setText(QCoreApplication.translate("MainWindow", u"Show Position table", None))
        self.manufacturerquerybt_2.setText(QCoreApplication.translate("MainWindow", u"Show Manufacturer table", None))
        self.cartypequerybt_2.setText(QCoreApplication.translate("MainWindow", u"Show Car type table", None))
        self.employeequerybt_2.setText(QCoreApplication.translate("MainWindow", u"Show Employee table", None))
        self.productquerybt_2.setText(QCoreApplication.translate("MainWindow", u"Show Products table", None))
        self.itemcount_dbtest.setText(QCoreApplication.translate("MainWindow", u"Item count in table: 0", None))
        self.loading_icon.setText("")
        self.status_main.setText(QCoreApplication.translate("MainWindow", u"Status: OK", None))
    # retranslateUi

