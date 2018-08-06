# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/onuragtas/Workspace/camera/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(603, 122)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.kameraLayout = QtWidgets.QGridLayout()
        self.kameraLayout.setVerticalSpacing(1)
        self.kameraLayout.setObjectName("kameraLayout")
        self.verticalLayout.addLayout(self.kameraLayout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.setPathButton = QtWidgets.QPushButton(Form)
        self.setPathButton.setObjectName("setPathButton")
        self.horizontalLayout_2.addWidget(self.setPathButton)
        self.yedek = QtWidgets.QPushButton(Form)
        self.yedek.setObjectName("yedek")
        self.horizontalLayout_2.addWidget(self.yedek)
        self.stop = QtWidgets.QPushButton(Form)
        self.stop.setObjectName("stop")
        self.horizontalLayout_2.addWidget(self.stop)
        self.start = QtWidgets.QPushButton(Form)
        self.start.setObjectName("start")
        self.horizontalLayout_2.addWidget(self.start)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.setPathButton.setText(_translate("Form", "Kayıt Yeri Seç"))
        self.yedek.setText(_translate("Form", "Yedek Al"))
        self.stop.setText(_translate("Form", "Stop"))
        self.start.setText(_translate("Form", "Start"))

