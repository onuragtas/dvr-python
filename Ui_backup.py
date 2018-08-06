# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/onuragtas/Workspace/camera/backup.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(611, 301)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout.addWidget(self.dateTimeEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit_2.setDate(QtCore.QDate(1999, 12, 31))
        self.dateTimeEdit_2.setCalendarPopup(True)
        self.dateTimeEdit_2.setTimeSpec(QtCore.Qt.UTC)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.horizontalLayout_2.addWidget(self.dateTimeEdit_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ara = QtWidgets.QPushButton(Dialog)
        self.ara.setObjectName("ara")
        self.verticalLayout.addWidget(self.ara)
        self.yedekle = QtWidgets.QPushButton(Dialog)
        self.yedekle.setObjectName("yedekle")
        self.verticalLayout.addWidget(self.yedekle)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 2, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.kayitYeriSec = QtWidgets.QPushButton(Dialog)
        self.kayitYeriSec.setObjectName("kayitYeriSec")
        self.horizontalLayout_5.addWidget(self.kayitYeriSec)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 2)
        self.listView = QtWidgets.QListWidget(Dialog)
        self.listView.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 3, 0, 1, 2)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 5, 0, 1, 2)
        self.log = QtWidgets.QLabel(Dialog)
        self.log.setObjectName("log")
        self.gridLayout.addWidget(self.log, 6, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ara.setText(_translate("Dialog", "Ara"))
        self.yedekle.setText(_translate("Dialog", "Yedekle"))
        self.label_3.setText(_translate("Dialog", "Kayıt Yeri:"))
        self.kayitYeriSec.setText(_translate("Dialog", "Seç"))
        self.progressBar.setFormat(_translate("Dialog", "%p"))
        self.log.setText(_translate("Dialog", "Log"))

