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

import argparse
import imutils

class MainDialog(QtWidgets.QDialog, Ui_untitled.Ui_Form):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.min_area = 500
        locale.setlocale(locale.LC_ALL, "tr_TR.UTF-8")
        self.labels = {}
        self.camNoList = {}
        self.captures = {}
        self.hours = {}
        self.out = {}
        self.motion = {}
        self.lastGrayFrame = {}

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
            self.motion[i].release()
        
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
        
        self.motion[i] = cv2.VideoWriter(self.path+"/motion_cam_"+str(i)+"_"+date+".avi", _fourcc, 20.0, (640,480))
        
        self.lastGrayFrame[i] = None
        caps = 0
        while(self.captures[i].isOpened()):
            ret, frame = self.captures[i].read()
            
            caps += 1
            date = "Cam_"+str(i)+"_"+time.strftime("%d.%m.%Y")+"-"+time.strftime("%X")
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,date,(300,20),font,0.55,(0,0,0),2)
            self.out[i].write(frame)

            # rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QtGui.QImage.Format_RGB888).scaled(640/1.5,480/1.5, QtCore.Qt.KeepAspectRatio)
            # self.labels[i].setPixmap(QtGui.QPixmap.fromImage(convertToQtFormat))
            
            newframe = frame
            if newframe is not None:
                gray = cv2.cvtColor(newframe, cv2.COLOR_BGR2GRAY)
                gray = cv2.GaussianBlur(gray, (21, 21), 0)
                
                if self.lastGrayFrame[i] is None:
                    self.lastGrayFrame[i] = gray

                frameDelta = cv2.absdiff(self.lastGrayFrame[i], gray)
                thresh = cv2.threshold(frameDelta, 90, 255, cv2.THRESH_BINARY)[1]
                thresh = cv2.dilate(thresh, None, iterations=4)
                cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE)
                cnts = cnts[0] if imutils.is_cv2() else cnts[1]
                for c in cnts:
                    # if the contour is too small, ignore it
                    if cv2.contourArea(c) < self.min_area:
                        continue
            
                    # compute the bounding box for the contour, draw it on the frame,
                    # and update the text
                    (x, y, w, h) = cv2.boundingRect(c)
                    cv2.rectangle(newframe, (x, y), (x + w, y + h), (0, 0, 0), 2)
                

                    date = "Cam_"+str(i)+"_"+time.strftime("%d.%m.%Y")+"-"+time.strftime("%X")
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(newframe,date,(300,20),font,0.55,(0,0,0),2)
                    self.motion[i].write(newframe)

                    rgbImage = cv2.cvtColor(newframe, cv2.COLOR_BGR2RGB)
                    convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QtGui.QImage.Format_RGB888).scaled(640/1.5,480/1.5, QtCore.Qt.KeepAspectRatio)
                    self.labels[i].setPixmap(QtGui.QPixmap.fromImage(convertToQtFormat))


                    
                    self.lastGrayFrame[i] = gray

            
            
            if(time.strftime("%H") != self.hours[i]):
            # if caps > 120
                self.out[i].release()
                self.motion[i].release()
                date = time.strftime("%d.%m.%Y")+"-"+time.strftime("%X")
                self.hours[i] = time.strftime("%H")
                self.out[i] = cv2.VideoWriter(self.path+"/cam_"+str(i)+"_"+date+".avi", _fourcc, 20.0, (640,480))
                self.motion[i] = cv2.VideoWriter(self.path+"/motion_cam_"+str(i)+"_"+date+".avi", _fourcc, 20.0, (640,480))

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