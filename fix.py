# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fix.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(806, 570)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(40, 260, 291, 261))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.groupBox)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(-30, 180, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.commandLinkButton_3.setFont(font)
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.groupBox)
        self.commandLinkButton.setGeometry(QtCore.QRect(-30, 30, 222, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.groupBox)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(-30, 110, 222, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(330, 0, 481, 571))
        self.textEdit.setObjectName("textEdit")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(320, 0, 20, 571))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 40, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "資料庫選項"))
        self.commandLinkButton_3.setText(_translate("Dialog", "登出"))
        self.commandLinkButton.setText(_translate("Dialog", "修改資料庫"))
        self.commandLinkButton_2.setText(_translate("Dialog", "選取資料庫"))
        self.label.setText(_translate("Dialog", "歡迎:"))
        self.label_2.setText(_translate("Dialog", "username"))

