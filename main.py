#!/usr/bin/env python
#-*- coding:utf8 -*-
import os
import sys
import cv2
import Ui_untitled
import thread
import datetime
import time 
import locale
import numpy
import backupWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class MainDialog(QtWidgets.QDialog, Ui_untitled.Ui_Form):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        locale.setlocale(locale.LC_ALL, "tr_TR.UTF-8")
        self.labels = {}
        self.camNoList = {}
        self.captures = {}
        self.hours = {}
        self.out = {}

        self.setPathButton.clicked.connect(self.setPath)
        self.stop.clicked.connect(self.stopF)
        self.start.clicked.connect(self.startF)
        self.yedek.clicked.connect(self.yedekal)
        
        if self.getPath() != "":
            self.init()
        else:
            self.setPath()

    def yedekal(self):
        self.sc = backupWindow.backupWindow(self)
        self.sc.setPath(self.path)
        self.sc.show()

    def stopF(self):
        for i in self.captures:
            self.captures[i].release()
            self.out[i].release()
        
    def startF(self):
        self.init()   

    def init(self):

        for i in range(0,10):
            self.camNoList[i] = i
            c = cv2.VideoCapture(i)
            if c is None or not c.isOpened():
                del self.camNoList[i]
            c.release()

        for i in self.camNoList:
            self.hours[i] = i
            self.labels[i] = QtWidgets.QLabel('Cam'+str(i))
            self.kameraLayout.addWidget(self.labels[i], int(i/2), i%2)
            thread.start_new_thread(self.cap,(self.camNoList[i],))

    def cap(self, i):
        self.hours[i] = time.strftime("%H")
        self.captures[i] = cv2.VideoCapture(i)
        date = time.strftime("%d.%m.%Y")+"-"+time.strftime("%X")
        _fourcc = cv2.VideoWriter_fourcc(*'MPEG')
        self.out[i] = cv2.VideoWriter(self.path+"/cam_"+str(i)+"_"+date+".avi", _fourcc, 20.0, (640,480))
        
        caps = 0
        while(self.captures[i].isOpened()):
            ret, frame = self.captures[i].read()
            
            date = "Cam_"+str(i)+"_"+time.strftime("%d.%m.%Y")+"-"+time.strftime("%X")
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,date,(300,20),font,0.55,(0,255,0),1)
            self.out[i].write(frame)

            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QtGui.QImage.Format_RGB888).scaled(640/1.5,480/1.5, QtCore.Qt.KeepAspectRatio)
            self.labels[i].setPixmap(QtGui.QPixmap.fromImage(convertToQtFormat))

            caps += 1
            if(time.strftime("%H") != self.hours[i]):
            # if caps > 120
                self.out[i].release()
                date = time.strftime("%d.%m.%Y")+"-"+time.strftime("%X")
                self.hours[i] = time.strftime("%H")
                self.out[i] = cv2.VideoWriter(self.path+"/cam_"+str(i)+"_"+date+".avi", _fourcc, 20.0, (640,480))

    def setPath(self):
        fileDialog = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select USB Drive Location')
        try:
            self.path = fileDialog
            file = open(os.path.dirname(os.path.abspath(__file__))+"/savePath", "w")
            file.write(self.path)
            file.close()
            self.init()
        except IOError:
            print "io error"  
        print self.path

    def getPath(self):
        file = open(os.path.dirname(os.path.abspath(__file__))+"/savePath","r")
        self.path = file.read()
        return self.path
    

app = QtWidgets.QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()